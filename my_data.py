tinkof = 'https://www.tinkoff.ru/invest/currencies/USDRUB/'
binance = 'https://p2p.binance.com/ru/trade/sell/USDT?fiat=RUB&payment=Tinkoff'
API_KEY = 'API KEY'

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "123",
    "content-type": "application/json",
    "Host": "p2p.binance.com",
    "Origin": "https://p2p.binance.com",
    "Pragma": "no-cache",
    "TE": "Trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
    }
    
data = {
    "asset": "USDT",
    "fiat": "RUB",
    "merchantCheck": True,
    "page": 1,
    "payTypes": ["Tinkoff"],
    "publisherType": None,
    "rows": 10,
    "tradeType": "Sell",
}
