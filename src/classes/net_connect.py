import json
import http.client
from matplotlib import pyplot as plt

#get latest stock price for the symbol
#returns -1 for invalid symbol
def get_quote(symbol):
    try:
        conn = http.client.HTTPSConnection("stock-data-yahoo-finance-alternative.p.rapidapi.com")
        headers = {
            'x-rapidapi-host': "stock-data-yahoo-finance-alternative.p.rapidapi.com",
            'x-rapidapi-key': "0b9c3bb71cmsha990fbcbca0e8e6p1a5894jsnc0101b1bb302"
        }
        conn.request("GET", "/v6/finance/quote?symbols="+symbol, headers=headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        info = json.loads(data)
        return (info['quoteResponse']['result'][0]['regularMarketPrice'])
    except:
        return -1

#get chart for given symbol
def get_chart(symbol):
    try:
        conn = http.client.HTTPSConnection("stock-data-yahoo-finance-alternative.p.rapidapi.com")
        headers = {
            'x-rapidapi-host': "stock-data-yahoo-finance-alternative.p.rapidapi.com",
            'x-rapidapi-key': "0b9c3bb71cmsha990fbcbca0e8e6p1a5894jsnc0101b1bb302"
        }
        conn.request("GET", "/v8/finance/chart/"+symbol+"?comparisons=AMZN&events=div%2Csplit", headers=headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        info = json.loads(data)
        plotlist = info['chart']['result'][0]['indicators']['quote'][0]['high']
        plotlist = plotlist[:325]
        for i in range(0,len(plotlist)):
            if plotlist[i] is None:
                plotlist[i]=plotlist[i-1]
        # print(plotlist)
        max_plotlist = max(plotlist)
        min_plotlist = min(plotlist)
        width = 0.2
        plt.title(symbol)
        plt.plot(plotlist,color='b',linestyle='dotted',marker='.')
        plt.grid(True)
        plt.ylabel("price(USD)")
        plt.xlabel("Timestamp")
        plt.style.use('classic')
        plt.tight_layout()
        plt.savefig("plot.png")
        temp = plt.show()
        return 1
    except:
        return -1


#returns a list containing top gainers and top losers
def popular_stocks():
    conn = http.client.HTTPSConnection("stock-data-yahoo-finance-alternative.p.rapidapi.com")
    headers = {
        'x-rapidapi-host': "stock-data-yahoo-finance-alternative.p.rapidapi.com",
        'x-rapidapi-key': "0b9c3bb71cmsha990fbcbca0e8e6p1a5894jsnc0101b1bb302"
        }
    conn.request("GET", "/ws/screeners/v1/finance/screener/predefined/saved?scrIds=day_gainers&count=2", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    info = json.loads(data)
    gainers_list = list()
    received_list = info['finance']['result'][0]['quotes']
    for i in received_list:
        gainers_list.append(('⇑ '+i['symbol']+':'+str(i['regularMarketChangePercent'])+'%'))
    conn = http.client.HTTPSConnection("stock-data-yahoo-finance-alternative.p.rapidapi.com")
    headers = {
        'x-rapidapi-host': "stock-data-yahoo-finance-alternative.p.rapidapi.com",
        'x-rapidapi-key': "0b9c3bb71cmsha990fbcbca0e8e6p1a5894jsnc0101b1bb302"
        }
    conn.request("GET", "/ws/screeners/v1/finance/screener/predefined/saved?scrIds=day_losers&count=2", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    info = json.loads(data)
    losers_list = list()
    received_list = info['finance']['result'][0]['quotes']
    for i in received_list:
        losers_list.append(('⇓ '+i['symbol']+':'+str(i['regularMarketChangePercent'])+'%'))
    return gainers_list + losers_list

# print(popular_stocks())
