# Vendor Performance & Inventory Analytics

## 📁 Project Structure
```
.
├── ingestion_db.py
├── vendor_summary.py
├── EDA.ipynb
├── Vendor_Performance_analysis.ipynb
├── data/
├── logs/
└── README.md

```

## 🧩 Data Pipeline Overview

1. Raw CSV → PostgreSQL ingestion
  `ingestion_db.py` loads every CSV in /data into database tables.
  Uses SQLAlchemy + pandas.

2. Vendor Summary Generation

  `vendor_summary.py` merges:

  * purchases

  * sales

  * price/volume

  * freight

And computes:

  * Gross Profit

  * Profit Margin

  * Stock Turnover

  * Sales-to-Purchase Ratio

3. Exploratory & Vendor Analysis

   Two notebooks provide structured analysis of the final dataset.

## 📊 Exploratory Data Analysis (EDA)

***✔ Dataset Preview***

The EDA notebook loads:

  * purchase data

  * sales data

  * vendor data

  * freight data

  * price/volume metadata

***✔ Key Observations From Tables***

1. Missing or inconsistent values

  Some records have zeros in purchase or sales columns

  A few text fields (VendorName, Brand) contain leading/trailing whitespace

2. Outliers

  * PurchaseQuantity and SalesQuantity contain large outliers (bulk orders)

  * PurchasePrice varies widely 

  * Premium categories have significantly higher price points

## 🧠 Vendor Performance Analysis

### 1. 🔍 Brands Needing Promotion or Price Adjustment

  `Scatterplot` comparing:
  
  Total Sales
  
  Profit Margin
  
The plot segments brands into four quadrants:

• High margin + low sales (top-left)

➡ These brands need promotion, visibility, or better positioning.

• High sales + low margin (bottom-right)

➡ These brands need price optimization or cost control.

*✔ Visualization*

  <img width="650" height="400" alt="download" src="https://github.com/user-attachments/assets/21209e25-8ec9-4e27-8391-b78df4c5211f" />


### 2. 🏆 Highest Sales Performance

From bar charts:

Top brands include major names from the beverage category.

Vendors such as DIAGEO NORTH AMERICA INC, BACARDI USA INC, and MAST-JAEGERMEISTER US appear consistently in the top slots.

These are your high-revenue, high-volume vendors.

*✔ Visualization*

  <img width="1491" height="490" alt="download" src="https://github.com/user-attachments/assets/e5b46ade-c634-4672-a859-52da4ec3e89d" />


### 3. 💰 Top Vendors by Purchase Dollars

Tables show:

Vendors with the highest purchase dollars

<img width="924" height="525" alt="image" src="https://github.com/user-attachments/assets/b7c7ab3d-b044-4b7a-ad70-a4e64d7b0b16" /> <img width="1161" height="455" alt="image" src="https://github.com/user-attachments/assets/19aa861c-8c89-41d6-a204-056b9649d953" />

Several vendors dominate procurement spending

This indicates concentration of supplier relationships

This leads directly to the Pareto analysis.

### 4. 📈 Pareto Chart – Vendor Dependency

The Pareto chart shows:

Top 10 vendors account for ~65.59% of total purchasing

The rest (~34%) come from many small vendors

This means:

  Procurement is highly vendor-dependent
  
  Contract negotiations with top vendors significantly affect cost
  
  Performance of top vendors has outsized impact on business

*✔ Visualization*

  <img width="897" height="755" alt="download" src="https://github.com/user-attachments/assets/bc8fda88-a821-4798-89ea-af731641d7d2" />

### 5. 🍩 Vendor Contribution Donut Chart

The donut chart shows the % contribution breakdown:


DIAGEO NORTH AMERICA INC — 14.3%

BACARDI USA INC — 10.2%

PERNOD RICARD USA — 8.4%

*✔ Visualization*

  <img width="984" height="656" alt="download" src="https://github.com/user-attachments/assets/0c79ee2f-2f86-4e16-b682-3c68839e2f38" />


### 6. 📉 Bulk Purchase Effect on Unit Cost

The grouped summary and table :

Shows how unit cost varies across:

Small

Medium

Large

Insight:

Bulk purchases have lower unit price

Prices decrease as purchase volume increases

This suggests:

Bulk buying should be prioritized for high-turnover products

Vendor negotiations can include volume-based pricing agreements

*✔ Visualization*

  <img width="859" height="545" alt="download" src="https://github.com/user-attachments/assets/699821a3-0da4-49c0-a9c7-35de8e6029d4" />

### 7. Confidence Interval Analysis: Profit Margins of Top vs Low Performing Vendors

  To understand the stability and expected range of vendor profit margins, 95% confidence intervals were computed for:
  
  Top vendors → highest 75% of Total Sales Dollars
  
  Low vendors → lowest 25% of Total Sales Dollars

*✔ Method*

A custom function calculates:

  Mean

  Standard Error
  
  Margin of Error
  
  95% Confidence Interval

*✔ Results*

  Top Vendors 95% CI: (30.74%, 31.61%), Mean: 31.18%

  Low Vendors 95% CI: (40.50%, 42.64%), Mean: 41.57%

*✔ Visualization*
  <img width="1005" height="545" alt="download" src="https://github.com/user-attachments/assets/768918e4-24df-4510-b3b1-4976e9acd6e7" />

### 8. Hypothesis Testing: Are Profit Margins Significantly Different?

  To statistically validate the difference between top and low vendor profit margins, a Welch’s Two-Sample T-Test was conducted.

Hypotheses

  H₀ (Null):
  There is no significant difference in mean profit margins.

  H₁ (Alternative):
  The mean profit margins are significantly different.

```
t_stat, p_value = ttest_ind(top_vendors, low_vendors, equal_var=False)
print(f"T-Statistic: {t_stat:.4f}, P-Value: {p_value:.4f}")
```

*✔ Results*

  T-Statistic: -17.6669
  
  P-Value: 0.0000
  
  Reject H₀: There is a significant difference in profit margins.

✔ Interpretation

  The probability that the difference occurred by chance is essentially zero.
  
  Profit margins of the two groups are statistically and materially different.
  
  Top vendors → lower but stable margins
  
  Low vendors → higher but inconsistent margins
  
  This split indicates value in vendor segmentation and targeted strategy.











