"""Data Analyst prerequisite: cleaning, KPI analysis, and EDA practice.

Run from the repository root:
    python data-analyst-prerequisite/python/eda_and_cleaning.py

The input dataset is synthetic and contains intentionally introduced quality issues
such as a missing discount and a duplicate transaction ID.
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data-analyst-prerequisite" / "data" / "sales_data.csv"
OUTPUT_DIR = ROOT / "data-analyst-prerequisite" / "python" / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def profile_data(df: pd.DataFrame) -> None:
    print("\n=== DATA PROFILE ===")
    print(f"Rows: {len(df):,}")
    print(f"Columns: {df.shape[1]:,}")
    print("\nData types:")
    print(df.dtypes)
    print("\nMissing values:")
    print(df.isna().sum().sort_values(ascending=False))
    print(f"\nDuplicate transaction IDs: {df['transaction_id'].duplicated().sum()}")
    print("\nNumeric summary:")
    print(df[["units", "unit_price", "unit_cost", "discount"]].describe())


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    clean = df.copy()
    clean["order_date"] = pd.to_datetime(clean["order_date"], errors="coerce")

    # Discount is a business field bounded between 0 and 1.
    # For this training dataset, missing discounts are conservatively filled with 0
    # and the treatment is documented rather than silently ignored.
    clean["discount"] = clean["discount"].fillna(0).clip(lower=0, upper=1)

    # A transaction ID should be unique at the transaction grain.
    before = len(clean)
    clean = clean.drop_duplicates(subset="transaction_id", keep="first")
    print(f"\nRemoved duplicate transaction rows: {before - len(clean)}")

    # Standardise categorical text.
    text_columns = ["region", "segment", "category", "product", "returned"]
    for column in text_columns:
        clean[column] = clean[column].astype("string").str.strip()

    # Derived fields. Returned orders contribute no net sales/profit.
    clean["gross_sales"] = clean["units"] * clean["unit_price"] * (1 - clean["discount"])
    clean["is_returned"] = clean["returned"].eq("Yes")
    clean["net_sales"] = clean["gross_sales"].where(~clean["is_returned"], 0)
    clean["cost"] = (clean["units"] * clean["unit_cost"]).where(~clean["is_returned"], 0)
    clean["profit"] = clean["net_sales"] - clean["cost"]
    clean["margin_pct"] = clean["profit"].div(clean["net_sales"].replace(0, pd.NA)) * 100
    clean["month"] = clean["order_date"].dt.to_period("M").astype(str)

    return clean


def report_kpis(df: pd.DataFrame) -> None:
    gross_sales = df["gross_sales"].sum()
    net_sales = df["net_sales"].sum()
    profit = df["profit"].sum()
    margin = profit / net_sales * 100 if net_sales else 0
    return_rate = df["is_returned"].mean() * 100

    print("\n=== CORE KPIs ===")
    print(f"Gross sales: ₹{gross_sales:,.2f}")
    print(f"Net sales:   ₹{net_sales:,.2f}")
    print(f"Profit:      ₹{profit:,.2f}")
    print(f"Margin:      {margin:.2f}%")
    print(f"Return rate: {return_rate:.2f}%")

    print("\n=== NET SALES BY REGION ===")
    print(df.groupby("region", as_index=False)["net_sales"].sum().sort_values("net_sales", ascending=False))

    print("\n=== NET SALES BY CATEGORY ===")
    print(df.groupby("category", as_index=False)["net_sales"].sum().sort_values("net_sales", ascending=False))

    print("\n=== MONTHLY NET SALES ===")
    print(df.groupby("month", as_index=False)["net_sales"].sum())


def detect_outliers(df: pd.DataFrame, column: str) -> None:
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    mask = (df[column] < lower) | (df[column] > upper)
    print(f"\n{column} IQR outliers: {int(mask.sum())} (lower={lower:.2f}, upper={upper:.2f})")


def make_charts(df: pd.DataFrame) -> None:
    monthly = df.groupby("month", as_index=False)["net_sales"].sum()
    region = df.groupby("region", as_index=False)["net_sales"].sum().sort_values("net_sales")

    plt.figure(figsize=(8, 4))
    plt.plot(monthly["month"], monthly["net_sales"], marker="o")
    plt.title("Monthly Net Sales")
    plt.xlabel("Month")
    plt.ylabel("Net Sales (₹)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "monthly_net_sales.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 4))
    plt.barh(region["region"], region["net_sales"])
    plt.title("Net Sales by Region")
    plt.xlabel("Net Sales (₹)")
    plt.ylabel("Region")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "net_sales_by_region.png", dpi=150)
    plt.close()


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    raw = pd.read_csv(DATA_PATH)
    profile_data(raw)

    clean = clean_data(raw)
    detect_outliers(clean, "net_sales")
    report_kpis(clean)

    output_csv = OUTPUT_DIR / "cleaned_sales_data.csv"
    clean.to_csv(output_csv, index=False)
    make_charts(clean)

    print(f"\nCleaned dataset saved to: {output_csv}")
    print(f"Charts saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
