"""Generate the practice datasets (sales + products) used in the lab. Seeded for reproducibility."""
from pathlib import Path
import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"
DATA.mkdir(exist_ok=True)
rng = np.random.default_rng(7)

products = pd.DataFrame({
    "product_id": [f"P{i:03d}" for i in range(1, 21)],
    "product_name": ["Laptop", "Phone", "Tablet", "Headphones", "Smartwatch", "Monitor", "Keyboard", "Mouse",
                     "Desk", "Chair", "Lamp", "Bookshelf", "Notebook", "Pen Set", "Backpack", "Water Bottle",
                     "Yoga Mat", "Dumbbells", "Sneakers", "Jacket"],
    "category": ["Electronics"] * 8 + ["Furniture"] * 4 + ["Stationery"] * 2 + ["Lifestyle"] * 6,
    "unit_price": [900, 650, 400, 120, 220, 300, 45, 25, 250, 180, 35, 140, 4, 12, 55, 15, 30, 60, 85, 110],
})
products.to_csv(DATA / "products.csv", index=False)

n = 2000
weights = np.r_[np.full(8, 0.07), np.full(4, 0.04), np.full(2, 0.06), np.full(6, 0.0)]
weights[14:] = (1 - weights.sum()) / 6
dates = pd.to_datetime("2025-01-01") + pd.to_timedelta(rng.integers(0, 365, n), unit="D")
sales = pd.DataFrame({
    "order_id": np.arange(10001, 10001 + n),
    "order_date": dates.strftime("%Y-%m-%d"),
    "customer_id": [f"C{c:04d}" for c in rng.integers(1, 401, n)],
    "product_id": rng.choice(products.product_id, n, p=weights),
    "quantity": rng.integers(1, 6, n),
    "region": rng.choice(["North", "South", "East", "West"], n, p=[.28, .24, .26, .22]),
    "payment_method": rng.choice(["Card", "UPI", "Cash", "NetBanking"], n, p=[.4, .3, .15, .15]),
    "discount_pct": rng.choice([0, 5, 10, 15, 20], n, p=[.5, .2, .15, .1, .05]).astype(float),
})
# seasonality: move 300 orders into Nov-Dec (holiday season)
holiday = rng.choice(n, 300, replace=False)
sales.loc[holiday, "order_date"] = (pd.to_datetime("2025-11-01")
        + pd.to_timedelta(rng.integers(0, 60, 300), unit="D")).strftime("%Y-%m-%d")
# inject data-quality issues for the cleaning exercise
sales.loc[rng.choice(n, 40, replace=False), "region"] = np.nan
sales.loc[rng.choice(n, 30, replace=False), "discount_pct"] = np.nan
sales = pd.concat([sales, sales.sample(25, random_state=1)], ignore_index=True)  # 25 duplicate rows
sales.to_csv(DATA / "sales.csv", index=False)
print("Saved", len(sales), "sales rows and", len(products), "products")
