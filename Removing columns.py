import pandas as pd

Australian_Vehicle_Prices_df = pd.read_csv('Australian Vehicle Prices.csv')

Australian_Vehicle_Prices_df = Australian_Vehicle_Prices_df.loc[:,['Brand']]

Australian_Vehicle_Prices_df.to_csv('Australian Vehicle Prices UPDATED.csv', index=False)