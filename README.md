
⸻

⚽ FIFA Players Data Analysis with PySpark

A complete PySpark-based project for cleaning, transforming, analyzing, and visualizing FIFA football player data. This project demonstrates practical data engineering workflows and exploratory data analysis using Spark and Python visualization libraries.

⸻

📂 Project Structure

football-pyspark/
├── data/                           # Raw and cleaned data (CSV & Parquet)
├── 01_clean_and_store.py          # Script for cleaning raw CSV and saving as Parquet
├── 02_transform_query.py          # Notebook for data transformation, UDFs, and analysis
├── 03_visualize_or_insight.ipynb  # Notebook for generating visual insights using Pandas + Seaborn
├── README.md                      # Project overview and instructions


⸻

🚀 Getting Started

✅ Requirements
	•	Python 3.10+
	•	Apache Spark
	•	PySpark
	•	Pandas
	•	Matplotlib
	•	Seaborn
	•	Jupyter Notebook (optional but recommended)

💻 Set Up Environment

# Recommended: Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install pyspark pandas matplotlib seaborn notebook


⸻

🧠 Project Goals
	•	Clean and preprocess FIFA player dataset using PySpark
	•	Apply user-defined functions (UDFs) for currency conversion
	•	Perform statistical analysis and transformations
	•	Generate insights and visualizations using Pandas + Seaborn

⸻

📊 Features & Highlights

1. Data Cleaning (01_clean_and_store.py)
	•	Dropped nulls in essential fields: long_name, age, club_name, etc.
	•	Replaced missing numeric values (value_eur, wage_eur) with 0
	•	Saved cleaned data to Parquet for efficient I/O

2. Transformation & Querying (02_transform_query.py)
	•	Wrote a PySpark UDF to convert currency fields from “€105M” to float
	•	Added new columns:
	•	is_top_player: Players with Overall >= 85
	•	age_bucket: Categorized players into Teen, 20s, 30s, 40+
	•	Performed aggregations and grouping:
	•	Average stats by nationality
	•	Correlation between Age and Wage_EUR
	•	Used Spark SQL for player nationality distribution

3. Visualization (03_visualize_or_insight.ipynb)
	•	Converted Spark DataFrame to Pandas
	•	Used Matplotlib & Seaborn to plot:
	•	Top 10 countries by player count
	•	Average rating by age bucket
	•	Age vs Wage scatter plot (highlighting top players)
	•	Top 10 most valuable players

⸻

🔍 Example Visuals

Player Distribution by Country	Age vs Wage
	

(Optional: Add visual plots if you export and save them to /images/)

⸻

🧰 Tools & Libraries Used

Tool	    Purpose
PySpark	    Distributed data processing & analysis
Pandas	    Data manipulation for plotting
Matplotlib	Data visualization
Seaborn     Statistical visualizations
Jupyter     Lab	Interactive notebook interface


⸻

✅ Skills Demonstrated
	•	PySpark (DataFrames, SQL, UDFs)
	•	Data Cleaning and Transformation
	•	Writing clean, modular Python code
	•	Performing EDA and generating insights
	•	Building scalable, reproducible workflows

⸻

📎 Credits
	•	FIFA 21 Player dataset from Kaggle

⸻