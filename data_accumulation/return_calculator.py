import pandas as pd 
import numpy as np
data=pd.read_csv(r"C:\Users\Admin\Desktop\FBSDE PROJECT\data_accumulation\aapl_data.csv")
#calculating daily log returns 
data['returns']=np.log((data['Close'])/(data['Close'].shift(1)))
total_number_of_days_in_a_year=252
log_return=data['returns'].mean()
"""we have to find annualized log return"""
mu=log_return*total_number_of_days_in_a_year