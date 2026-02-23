import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import os
from src.data_processing import load_and_clean_data, get_kpis
from src.forecasting import generate_30_day_forecast
from src.report_generator import generate_executive_pdf

# Page Config
st.set_page_config(page_title="Sales Intelligence System", layout="wide")
st.title("📈 Executive Sales Intelligence Platform")

# --- DEBUG MODE: Let's see what Python sees ---
with st.expander("🛠️ Debug Folder Paths (Click to expand)"):
    st.write(f"**Current Working Directory:** `{os.getcwd()}`")
    st.write(f"**Does the 'data' folder exist?** `{os.path.exists('data')}`")
    st.write(f"**Does 'data/sales.csv' exist?** `{os.path.exists('data/sales.csv')}`")
    if os.path.exists('data'):
        st.write("**Files inside 'data' folder:**", os.listdir('data'))
# ----------------------------------------------

# Load Data
df = load_and_clean_data("data/sales.csv")

if df is not None:
    # --- KPI LAYER ---
    st.header("1. Real-Time KPIs")
    kpis = get_kpis(df)
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", f"₹{kpis['Total_Revenue']:,.2f}")
    col2.metric("Total Units Sold", f"{kpis['Total_Units_Sold']:,}")
    col3.metric("Avg Daily Revenue", f"₹{kpis['Average_Daily_Revenue']:,.2f}")
    
    st.markdown("---")
    
    # --- VISUAL DECISION LAYER ---
    st.header("2. Revenue & Regional Performance")
    col1, col2 = st.columns(2)
    
    with col1:
        # Category Performance
        category_rev = df.groupby('Category')['Revenue'].sum().reset_index()
        fig_cat = px.bar(category_rev, x='Category', y='Revenue', title="Revenue by Category", color='Category')
        st.plotly_chart(fig_cat, use_container_width=True)
        
    with col2:
        # Outlier Detection (Boxplot)
        fig_out = px.box(df, x='Region', y='Revenue', title="Revenue Distribution by Region", color='Region')
        st.plotly_chart(fig_out, use_container_width=True)

    st.markdown("---")
    
    # --- PREDICTIVE LAYER ---
    st.header("3. 30-Day Revenue Forecast")
    historical, forecast = generate_30_day_forecast(df)
    
    fig_forecast = go.Figure()
    fig_forecast.add_trace(go.Scatter(x=historical.index, y=historical['Revenue'], name='Historical Revenue', mode='lines+markers'))
    fig_forecast.add_trace(go.Scatter(x=forecast['Date'], y=forecast['Predicted_Revenue'], name='30-Day Forecast', mode='lines', line=dict(dash='dash', color='orange')))
    fig_forecast.update_layout(title="Revenue Trends & Projection", xaxis_title="Date", yaxis_title="Revenue (INR)")
    st.plotly_chart(fig_forecast, use_container_width=True)

    st.markdown("---")
    
    # --- AUTOMATED REPORTING LAYER ---
    st.header("4. Executive Reporting")
    st.write("Generate a boardroom-ready PDF summary of current KPIs and insights.")
    
    # Generate the PDF in the background first
    report_path = generate_executive_pdf(kpis)
    
    # Read the generated PDF as binary data (bytes)
    with open(report_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        
    # Create the Streamlit download button
    st.download_button(
        label="⬇️ Download Executive Report (PDF)",
        data=pdf_bytes,
        file_name="Executive_Sales_Report.pdf",
        mime="application/pdf"
    )
        
else:
    st.error("Data not found. Please check the Debug menu above to see what is missing.")