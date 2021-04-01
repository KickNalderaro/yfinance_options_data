import yfinance as yf
import csv
def get_ticker_data(ticker):
    global stock
    stock = yf.Ticker(ticker)
def get_desired_option_data(data):
    global putsToSell
    price = data["ask"]
    putsToSell = stock.option_chain('2021-04-01').puts
    for index, put in putsToSell.iterrows():
        if (put.strike < price) and (put.strike > price - 0.5):
            correct_strikes.append(put.strike)
            putValue.append(put.lastPrice)
            ratio.append(put.lastPrice/put.strike)
    print(ratio)
#ticker_list = ["SNDL", "GNUS", "NBEV", "GNW", "RIG", "MNKD", "NOK", "YPF", "AUY", "SWN", "EXPR", "OPK", "SOLO", "UVXY", "AMRN", "SIRI", "HL", "VXRT", "SOS", "KGC", "CLVS", "TECS", "ET", "KODK"]
ticker_list = ["SNDL", "GNUS", "NBEV", "GNW", "RIG", "MNKD", "NOK", "YPF"]
ratio = []
for ticker in ticker_list:
    correct_strikes = []
    putValue = []
    get_ticker_data(ticker)
    get_desired_option_data(stock.info)

filename = "puts.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(ticker_list)
    csvwriter.writerow(ratio)
#get_ticker_data("SOS")
#priceGetter = stock.info
#get_desired_option_data(priceGetter)

