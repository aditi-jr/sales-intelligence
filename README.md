
📈 Executive Sales Intelligence Platform

**Live Demo:** [View the Interactive Dashboard Here](https://sales-intelligence-mffv9zggaiydgreseausru.streamlit.app/)

## 📌 Project Overview
The **Executive Sales Intelligence Platform** is a centralized, automated analytics dashboard designed to transform raw retail transaction data into actionable business insights. Built for executive decision-making, it bridges the gap between raw data engineering, descriptive analytics, and predictive forecasting.

This tool eliminates the need for manual Excel reporting by providing real-time KPI tracking, anomaly detection, and automated, boardroom-ready PDF report generation.

# 🚀 Key Features
* **Data Engineering & Cleaning:** Automatically ingests raw CSV data, standardizes formats, and engineers business-critical metrics (Revenue, Avg Daily Revenue).
* **Real-Time KPI Tracking:** Instant visibility into Total Revenue, Units Sold, and Daily Averages.
* **Visual Decision Layer:** Interactive Plotly charts highlighting category performance and regional revenue distribution (outlier detection).
* **Predictive Forecasting:** Utilizes Exponential Smoothing (Statsmodels) to generate a baseline 30-day forward-looking revenue projection.
* **Automated Executive Reporting:** One-click PDF generation (using FPDF) that compiles KPIs and insights into a downloadable document directly from the browser.

🛠️ Technology Stack
* **Frontend/Framework:** Streamlit
* **Data Manipulation:** Python, Pandas, NumPy
* **Data Visualization:** Plotly Express, Plotly Graph Objects
* **Predictive Modeling:** Statsmodels (Exponential Smoothing)
* **Report Generation:** FPDF

📂 Project Structure
```text
sales-intelligence/
│
├── data/
│   └── sales.csv                 # Raw transaction data
│
├── src/
│   ├── data_processing.py        # Data cleaning and feature engineering
│   ├── forecasting.py            # Time-series predictive modeling
│   └── report_generator.py       # PDF layout and generation logic
│
├── app.py                        # Main Streamlit dashboard application
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation

```

## 💻 Local Installation & Setup

To run this project locally on your machine:

1. **Clone the repository:**
```bash
git clone [https://github.com/aditi-jr/sales-intelligence.git](https://github.com/aditi-jr/sales-intelligence.git)
cd sales-intelligence

```


2. **Install the required dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the Streamlit app:**
```bash
streamlit run app.py

```

## 👤 Author

*Aditi J*
* [GitHub](https://www.google.com/search?q=https://github.com/aditi-jr)

