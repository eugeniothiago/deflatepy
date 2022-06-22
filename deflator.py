import pandas as pd
import sys
from datetime import datetime
from api_call import api_call

def deflate(data_frame:pd.DataFrame,date_column,deflate_year=None, deflate_month=None):
    series=""
    target_date = None
    if not deflate_year:
        print("At least the deflate_year argument must be specified")
        sys.exit(1)
    if not deflate_month:
        series='yearly'
        target_date = pd.to_datetime(datetime(deflate_year,1,1)).strftime("%Y")
    else:
        series='monthly'
        target_date = pd.to_datetime(datetime(deflate_year,deflate_month,1)).strftime("%Y-%m")
    ipca_values = api_call(series=series)
    
    if series =='yearly':
        date_format="%Y"
    else:
        date_format="%Y-%m"
    
    ipca_values['date'] = ipca_values['date'].dt.strftime(date_format)
    
    temp_df = pd.merge(left=data_frame, right=ipca_values, left_on=date_column, right_on='date', how='left')
    temp_df['temp_date_column'] = temp_df[date_column].dt.strftime(date_format)
    
    
    deflator = ipca_values.loc[ipca_values.date == target_date]['value'].squeeze()
    
    data_frame[date_column] = pd.to_datetime(data_frame[date_column])