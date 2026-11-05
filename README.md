# Hands-On Data Lab Implementation

A working data analysis environment plus practical exercises in **data manipulation**, **visualization** and **basic analysis** using Python and Jupyter.

## What is inside
```
data/               sales.csv, products.csv (generated, seeded)
notebooks/data_lab.ipynb   executed notebook with all exercises and outputs
src/generate_data.py       recreates the datasets
src/build_notebook.py      rebuilds the notebook
outputs/            saved charts (PNG) and an HTML export of the notebook
requirements.txt, environment.yml
```

## 1. Environment setup
**Option A - venv + pip**
```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m ipykernel install --user --name data-lab
jupyter lab
```
**Option B - conda**
```bash
conda env create -f environment.yml
conda activate data-lab
jupyter lab
```
Open `notebooks/data_lab.ipynb` and choose **Run > Run All Cells**. The first section prints library versions to verify the setup.

## 2. Exercises
| Part | Skills practised |
|------|------------------|
| Data manipulation | load CSV, inspect, remove duplicates, handle missing values, fix dtypes, merge, feature engineering, filter/sort, groupby, pivot tables, NumPy statistics |
| Visualization | line, bar, histogram + KDE, box plot, heatmaps, pie, scatter, multi-panel dashboard |
| Basic analysis | descriptive stats, correlation, Welch t-tests, linear regression, customer segmentation |

## 3. Key findings
- 25 duplicate rows removed and all missing values handled (2,025 raw rows -> 2,000 clean orders).
- Electronics = about 85% of revenue; the Laptop is the top product.
- Nov-Dec average daily revenue is about 105% higher than Jan-Oct (p < 0.001).
- Unit price correlates strongly with revenue (r = 0.86); discounts do not significantly change quantity (p = 0.89).
- The top third of customers generates about 62% of total spend.

The data is synthetic, so the project runs with no downloads.
