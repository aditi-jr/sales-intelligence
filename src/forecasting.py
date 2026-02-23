import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def generate_30_day_forecast(df):
    """Forecasts revenue for the next 30 days based on historical daily data."""
    # Aggregate revenue by day
    daily_revenue = df.groupby('Date')['Revenue'].sum().reset_index()
    daily_revenue = daily_revenue.set_index('Date').asfreq('D').fillna(0)
    
    # Fit the model (Using simple smoothing for small sample sizes)
    model = ExponentialSmoothing(daily_revenue['Revenue'], trend=None, seasonal=None, initialization_method="estimated")
    fit_model = model.fit()
    
    # Forecast next 30 days
    forecast = fit_model.forecast(30)
    
    # Format output
    forecast_df = pd.DataFrame({
        'Date': pd.date_range(start=daily_revenue.index[-1] + pd.Timedelta(days=1), periods=30),
        'Predicted_Revenue': forecast.values
    })
    
    return daily_revenue, forecast_df