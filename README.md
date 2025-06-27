# 🚖 Cab Booking System Data Analysis (SQL + Python + Excel)

Analyze NYC taxi ride data using **Microsoft SQL Server**, **Python**, and **Excel** to uncover key business insights such as demand peaks, trip distances, and revenue trends.

---

## 📌 Objective

Load and analyze real-world cab trip data in SQL Server, automate loading with Python, and visualize insights using Excel.

---

## 🛠 Tech Stack

- **SQL Server 2022 Express** – Data storage & querying
- **Python (pandas, pyodbc)** – Data automation
- **VS Code** – Project setup
- **Excel** – Visualization charts

---

## 📂 Folder Structure
cab-booking-analysis-mssql/
├── data/ # Contains yellow_tripdata.csv
├── notebooks/ # (Optional) Jupyter notebooks
├── sql/
│ ├── schema.sql # DB schema
│ └── queries.sql # SQL queries
├── load_data.py # Python script to load CSV
├── requirements.txt # Python packages
└── README.md # Project overview


---

## 📊 Key Insights

- 🚕 **Peak Hours:** 5 PM to 9 PM
- 📅 **Longest Rides:** On weekends
- 💸 **Revenue Boost:** Evening rides generate most income
- 💡 **Visualization:** Done using MS Excel charts

---

## 🧠 SQL Example

sql
SELECT DATENAME(WEEKDAY, pickup_datetime) AS DayOfWeek,
       AVG(trip_distance) AS AvgDistance
FROM CabTrips
GROUP BY DATENAME(WEEKDAY, pickup_datetime);

## 📎 Dataset

NYC Yellow Cab Trip Data (sample of 100,000+ rows)  
Source: [NYC TLC Trip Records](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)


## 📷 Sample Output

Here are some outputs from the project:

### ✅ SQL Server Table Setup
![CabTrips Table Created in SSMS](screenshot1.png)

> The `CabTrips` table was successfully created in Microsoft SQL Server Management Studio.

### ✅ Sample Query Output & Charts
![Top 5 CabTrips + Bar Charts](screenshot2.png)

> Preview of top 5 records from the `CabTrips` table and visual charts created in Excel for analysis.
