
import time
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import pytz
from pprint import pprint
from google_sheet import clean_up, update_google_sheet,update_cell


def  btstLogicBankend(condition,row_to_start,row_to_clean,sheetname,conditionName,conditionNameLocation):
   
    try:
     
        update_cell(conditionNameLocation,conditionName,sheetname="DashBoard") 
      
        if condition.empty:
                # print("No data Found - check")
                time.sleep(10)
                clean_up(range_to_clear=row_to_clean,sheetname=sheetname)
                update_cell("AL4","No data Found ",sheetname="Hello World")
                return
        else:      
            stock_list_sorted = condition.sort_values(by='LTP_difference_percent', ascending=False)
            print(stock_list_sorted)
            update_google_sheet(row_to_start,stock_list_sorted[['symbol','ltp_df1','ltp_df2','LTP_difference_percent']],range_to_clear=row_to_clean,sheetname=sheetname)
            return{'message': 'Google sheet update success'}
                
    except Exception as e:
            print(f"chartinkLogicBankend -------------->>>>{e}")

            
def morningclean(row_to_clean,sheetname):
      clean_up(range_to_clear=row_to_clean,sheetname=sheetname)