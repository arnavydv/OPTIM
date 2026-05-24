import pandas as pd 
import numpy as np
data=pd.read_csv(r"C:\Users\Admin\Desktop\FBSDE PROJECT\data_accumulation\aapl_data.csv")

"""NOW WE HAVE TO FIND THE VALUE OF SIGMA WHICH 
IS CALCULATED THROUGH THE RETURNS AND THEN THEIR STANDARD DEVIATION 
THAT IS SIGMA"""
data=data.dropna()
data['returns']=np.log(data['Close']/data['Close'].shift(1))
sigma=data['returns'].std()
print(sigma)