"""Data Analyst prerequisite: cleaning, KPI analysis, and EDA practice."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "Datasets" / "sales_data.csv"
OUTPUT_DIR = ROOT / "Source Codes" / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def profile_data(df):
    print(df.info())
    print("\nMissing values:\n", df.isna().sum())
    print("\nDuplicate transaction IDs:", df["transaction_id"].duplicated().sum())
    print("\nNumeric summary:\n", df[["units","unit_price","unit_cost","discount"]].describe())

def clean_data(df):
    clean = df.copy()
    clean["order_date"] = pd.to_datetime(clean["order_date"], errors="coerce")
    clean["discount"] = clean["discount"].fillna(0).clip(0, 1)
    clean = clean.drop_duplicates(subset="transaction_id", keep="first")
    for col in ["region","segment","category","product","returned"]:
        clean[col] = clean[col].astype("string").str.strip()
    clean["gross_sales"] = clean["units"] * clean["unit_price"] * (1 - clean["discount"])
    clean["is_returned"] = clean["returned"].eq("Yes")
    clean["net_sales"] = clean["gross_sales"].where(~clean["is_returned"], 0)
    clean["cost"] = (clean["units"] * clean["unit_cost"]).where(~clean["is_returned"], 0)
    clean["profit"] = clean["net_sales"] - clean["cost"]
    clean["month"] = clean["order_date"].dt.to_period("M").astype(str)
    return clean

def report_kpis(df):
    net_sales = df["net_sales"].sum()
    profit = df["profit"].sum()
    print(f"Net sales: ₹{net_sales:,.2f}")
    print(f"Profit: ₹{profit:,.2f}")
    print(f"Margin: {profit / net_sales * 100:.2f}%")
    print(f"Return rate: {df['is_returned'].mean() * 100:.2f}%")
    print("\nSales by region:\n", df.groupby("region")["net_sales"].sum().sort_values(ascending=False))
    print("\nSales by category:\n", df.groupby("category")["net_sales"].sum().sort_values(ascending=False))

def make_charts(df):
    monthly = df.groupby("month", as_index=False)["net_sales"].sum()
    plt.figure(figsize=(8,4)); plt.plot(monthly["month"], monthly["net_sales"], marker="o")
    plt.title("Monthly Net Sales"); plt.xlabel("Month"); plt.ylabel("Net Sales (₹)")
    plt.tight_layout(); plt.savefig(OUTPUT_DIR / "monthly_net_sales.png", dpi=150); plt.close()

    region = df.groupby("region", as_index=False)["net_sales"].sum().sort_values("net_sales")
    plt.figure(figsize=(8,4)); plt.barh(region["region"], region["net_sales"])
    plt.title("Net Sales by Region"); plt.xlabel("Net Sales (₹)"); plt.ylabel("Region")
    plt.tight_layout(); plt.savefig(OUTPUT_DIR / "net_sales_by_region.png", dpi=150); plt.close()

if __name__ == "__main__":
    raw = pd.read_csv(DATA_PATH)
    profile_data(raw)
    clean = clean_data(raw)
    report_kpis(clean)
    clean.to_csv(OUTPUT_DIR / "cleaned_sales_data.csv", index=False)
    make_charts(clean)
    print("\nOutputs written to Source Codes/outputs/")
