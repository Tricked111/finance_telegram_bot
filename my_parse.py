from bs4 import BeautifulSoup as BS
import requests
import my_data as DATA

def parse_tinkoff():
    r = requests.get(DATA.tinkof)
    soup = BS(r.text,'html.parser')
    string_data = soup.find_all("span", class_="Money-module__money_UZBbh")
    value = [c.text for c in string_data]
    return(value[1][0:2]+'.'+value[1][3:4])
    
def parse_binance():
    r = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=DATA.headers, json=DATA.data).json()

    #with open("data.json", "w") as write_file:
    #    json.dump(r, write_file,indent = 6)
  
    #with open('data.json', 'r') as f:
    #data = json.loads(r.read())
    #data = r
    clear_list = []
    for i in r['data']:
        list = i['adv']
        clear_list.append(list['price'])
    
    
    result = [float(item) for item in clear_list] 
    res = sum(result)/10
    return ("%.3f" % res)