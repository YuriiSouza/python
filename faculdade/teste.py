
import datetime

def turn_date_in_str(date, tipe = False):
    if tipe == False:
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
    else:
        date_obj = datetime.datetime.strptime(date, '%d%m%Y')
        
    date_str = date_obj.strftime('%d de %B de %Y')
    
    return date_str