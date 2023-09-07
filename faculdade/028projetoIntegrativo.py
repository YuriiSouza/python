import requests
import datetime
import locale

def turn_date_in_str(date, tipe = False):
    if tipe == False:
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
    else:
        date_obj = datetime.datetime.strptime(date, '%d%m%Y')
        
    date_str = date_obj.strftime('%d de %B de %Y')
    
    return date_str
    
    
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8') #definando o local para o idioma ser do local
chave_api = 'V9834MI0TNJA57QB'#chave de acesso a api 


sigla = str(input('Sigla do ativo:'))


url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={sigla}&apikey={chave_api}'#url para acesso as informações
r = requests.get(url)
data = r.json()

inform_data = data['Meta Data']

#configurando a apresentação da data da ultima atualização
date_last_refreshed = inform_data['3. Last Refreshed']
last_refreshed = turn_date_in_str(date_last_refreshed)

print(f'Ativo: {sigla}')

values_data = data['Time Series (Daily)']

required_date = str(input('Data das informações(digite apenas números): '))
required_date_str = turn_date_in_str(required_date, True)

for n in values_data:
    n_date = n
    date = turn_date_in_str(n_date)
    if date == required_date_str:
        results = values_data[n]
        abriu = float(results['1. open'])
        maior_cotacao = float(results['2. high'])
        menor_cotacao = float(results['3. low'])
        fechou = float(results['4. close'])
        volume = float(results['5. volume'])
        print(f'{date}: abriu: R${abriu:.2f}\nMaior cotação: R${maior_cotacao:.2f}\nMenor cotação: R${menor_cotacao:.2f}\nFechou: R${fechou:.2f}\nVolume de transações: R${volume:.2f}')
    