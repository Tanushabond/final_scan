
import pandas as pd
from google_sheet import clean_up, update_cell, update_google_sheet
from back_end_btst import btstLogicBankend
from jugaad_data.nse import NSELive

data = None
n = NSELive()
def dataFetch():
    try:
        n = NSELive()
        q = n.live_index("NIFTY 200")
        datas = (q['data'])

        list = []
        for data in datas:
            toLoad = {
                    "symbol": data["symbol"],
                    "ltp": data['lastPrice'],
                    "pChange": data['pChange'],
                    }
            list.append(toLoad)
            df = pd.DataFrame(list)
        return df
    except Exception as e:
        print(e)

def sendtoWrite(data): 
    try:
        conditionName = "BTST" # change name Here
        if data.empty:
            row_to_start ='AJ3'
            row_to_clean = "AJ3:AN"
            conditionNameLocation = "AC4"
            btstLogicBankend(condition=data,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
        else:    
            # Condtion 2
                        # CONDITION2 = CONDITION2
            # print("inside sendtoWrite")s
            # print(f"{data}")
            row_to_start ='AJ3'
            row_to_clean = "AJ3:AN"
            conditionNameLocation = "AC4"
            btstLogicBankend(condition=data,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
            return {"message": "Second Run Sucessful"}
    except Exception as e:
        print(e)
        
def firstRun():
    df1 = dataFetch()
    df1_filtered = df1[(df1['pChange'] >= 3) & (df1['pChange'] <= 5)]
    global data
    data = df1_filtered
    # print(data)
    return {"message": "First Run sucessful"}
    # print(df) 
def secondRun():
    global data
    df1_filtered = data
    df2 = dataFetch()
    df2_filtered = df2[df2['symbol'].isin(df1_filtered['symbol'])]
    df_merged = pd.merge(df1_filtered[['symbol', 'ltp']], df2_filtered[['symbol', 'ltp']], on='symbol', suffixes=('_df1', '_df2'))
    # print(df_merged)
    df_merged['LTP_difference_percent'] = ((df_merged['ltp_df2'] - df_merged['ltp_df1']) / df_merged['ltp_df2']) * 100
    filtered_df = df_merged[(df_merged['LTP_difference_percent'] >= 1.5 ) & (df_merged['LTP_difference_percent'] <= 3)]
    # print(filtered_df)
    if filtered_df.empty:
        # print("No data found")
        sendtoWrite(filtered_df)  
    else:
        print(filtered_df[['symbol','LTP_difference_percent']]) # Stock list with yes)
        sendtoWrite(filtered_df) 


def btstgsclean():
    clean_up(range_to_clear="AJ3:AN",sheetname="Hello World")   
    return {'message': 'Clean up completed'}

