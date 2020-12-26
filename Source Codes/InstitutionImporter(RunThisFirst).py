import pandas as pd
import requests
import colorama
from colorama import Fore, Back, Style
import os

os.system('cls')

site = input("Enter the site URL here (IE: https://bduadc2020.calicotab.com/):") #Link of the tab site
token = input("Enter the API KEY here (IE: 4f54cbb378ui4yuhbgyu8u0abc78uh7t6y8uu768hu) It can be found on the change password page: ") #API Token
x=0

sheet = pd.read_excel(open('database.xlsx', 'rb'),
                      sheet_name='Institutions')

for k in sheet['Long']:

    a = sheet['Long'][x]
    b = sheet['Short'][x]
    x = x+1
    
    r = requests.post(
        f'{site}api/v1/institutions',
        json = {                
                    "name": a,
                    "code": b,
                },
        headers={
                'Authorization': 'token '+token
                })
    status = r.status_code
    if status != 201:
        print(Fore.RED, f"Error occured while posting {a}, {b}\n Error {status}\n{r.text} {Style.RESET_ALL}")
        
print(f"{Fore.GREEN}SUCCESS! Post completed {Style.RESET_ALL}")


    
