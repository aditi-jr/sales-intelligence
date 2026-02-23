import pandas as pd
import numpy as np

def load_and_clean_data(filepath):
    """Loads raw data, cleans it, and engineers business metrics."""
    try:
        df = pd.read_csv(filepath)
        
        # Standardize column names to match dashboard logic
        df.rename(columns={
            'date': 'Date',
            'region': 'Region',
            'product': 'Product',
            'category': 'Category',
            'units_sold': 'Quantity',
            'unit_price': 'Unit_Price'
        }, inplace=True)
        
        # Standardize date formats
        df['Date'] = pd.to_datetime(df['Date'])
        
        # Engineer the Revenue metric
        df['Revenue'] = df['Quantity'] * df['Unit_Price']
            
        return df
    except Exception as e:
        print(f"Error processing data: {e}")
        return None

def get_kpis(df):
    """Calculates top-level KPIs for the dashboard."""
    kpis = {
        'Total_Revenue': df['Revenue'].sum(),
        'Total_Units_Sold': df['Quantity'].sum(),
        'Average_Daily_Revenue': df.groupby('Date')['Revenue'].sum().mean(),
    }
    return kpis