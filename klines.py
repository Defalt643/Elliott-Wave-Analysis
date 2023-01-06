from binance.client import Client
from binance.client import Client
from datetime import datetime, timezone
import csv

def add_detail(data):
    res = [{
        "Kline open time": datetime.utcfromtimestamp(data[0][0]/1000).strftime('%Y-%m-%d %H:%M:%S'),
        "Open price": data[0][1],
        "High price": data[0][2],
        "Low price": data[0][3],
        "Close price": data[0][4],
        "Volume": data[0][5],
        "Kline close time": datetime.utcfromtimestamp(data[0][6]/1000).strftime('%Y-%m-%d %H:%M:%S'),
        "Quote asset volume": data[0][7],
        "Number of trade": data[0][8],
        "Taker buy base asset volume": data[0][9],
        "Taker buy quote asset volume": data[0][10],
        "Unused field. Ignore.": data[0][11],
    }]
    return res

def getCSV(sysmbol,interval,since):
    print("Getting csv data...")
    client = Client()
    if interval == '1m':
        interval = Client.KLINE_INTERVAL_1MINUTE
    elif interval == '3m':
        interval = Client.KLINE_INTERVAL_3MINUTE
    elif interval == '15m':
        interval = Client.KLINE_INTERVAL_15MINUTE
    elif interval == '30m':
        interval = Client.KLINE_INTERVAL_30MINUTE
    elif interval == '1h':
        interval = Client.KLINE_INTERVAL_3MINUTE
    elif interval == '2h':
        interval = Client.KLINE_INTERVAL_2HOUR
    elif interval == '4h':
        interval = Client.KLINE_INTERVAL_4HOUR
    elif interval == '6h':
        interval = Client.KLINE_INTERVAL_6HOUR
    elif interval == '8h':
        interval = Client.KLINE_INTERVAL_8HOUR
    elif interval == '12h':
        interval = Client.KLINE_INTERVAL_12HOUR
    elif interval == '1d':
        interval = Client.KLINE_INTERVAL_1DAY
    elif interval == '3d':
        interval = Client.KLINE_INTERVAL_3DAY
    elif interval == '1w':
        interval = Client.KLINE_INTERVAL_1WEEK
    else :
        interval = Client.KLINE_INTERVAL_1MONTH
    klines = client.get_historical_klines(symbol=sysmbol, interval=interval,start_str=since)

    with open('testCSV.csv','w') as file :
        writer = csv.writer(file)
        header = ['Date','Open','High','Low','Close']
        writer.writerow(header)

        for i in range (0,len(klines)):
            date = str(datetime.utcfromtimestamp(klines[i][0]/1000).strftime('%Y-%m-%d'))
            # print(type(date))
            open_price = klines[i][1]
            high = klines[i][2]
            low = klines[i][3]
            close_price = klines[i][4]
            data = [date, open_price,high,low,close_price]
            writer.writerow(data)

# result = add_detail(klines)

# print(result)



