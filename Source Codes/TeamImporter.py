import pandas as pd
import requests
import colorama
from colorama import Fore, Back, Style
import os

os.system('cls')

site = input("Enter the site URL here (IE: https://bduadc2020.calicotab.com/):") #Link of the tab site
token = input("Enter the API KEY here (IE: 4f54cbb378ui4yuhbgyu8u0abc78uh7t6y8uu768hu) It can be found on the change password page: ") #API Token
slug = input("Enter the tournament slug here (IE: uadc2020):") #Tournament slug 


print("Getting the institution data...")
r = requests.get(
        f'{site}api/v1/institutions',
        headers={
                'Authorization': 'token '+token
                })
                 
institutions = r.json()

x=0
sheet = pd.read_excel(open('database.xlsx', 'rb'),
                           sheet_name='Teams')

for k in sheet['Team']:
    
    name = sheet['Team'][x]
    code = sheet['Code'][x]    
    for i in institutions:
        if i['code'] == code:
            institution = i['url']
            break
    
    
    
    S1 = sheet['S1'][x]
    E1 = sheet['E1'][x]
    P1 = '' #sheet['P1'][x]
    G1 = sheet['G1'][x]
    if G1 == 'Male':
        G1='M'
    elif G1 == 'Female':
        G1='F'
    else:
        G1='O'
        
    S2 = sheet['S2'][x]
    E2 = sheet['E2'][x]
    P2 = '' #sheet['P2'][x]
    G2 = sheet['G2'][x]
    if G2 == 'Male':
        G2='M'
    elif G2 == 'Female':
        G2='F'
    else:
        G2='O'
        
    S3 = sheet['S3'][x]
    E3 = sheet['E3'][x]
    P3 = '' #sheet['P3'][x]
    G3 = sheet['G3'][x]
    if G3 == 'Male':
        G3='M'
    elif G3 == 'Female':
        G3='F'
    else:
        G3='O'
    
    x = x+1
    
    r = requests.post(
        f'{site}api/v1/tournaments/{slug}/teams',
        json = {
  "reference": name,
  "short_reference": name,
#  "code_name": "",
  "institution": institution,
  "speakers": [
    {
      "name": S1,
      "gender": G1,
      "email": E1,
      "phone": P1,
      "anonymous": False,
      "pronoun": "",
      "categories": [],
      "url_key": ""
    },
    {
      "name": S2,
      "gender": G2,
      "email": E2,
      "phone": P2,
      "anonymous": False,
      "pronoun": "",
      "categories": [],
      "url_key": ""
    },
    {
      "name": S3,
      "gender": G3,
      "email": E3,
      "phone": P3,
      "anonymous": False,
      "pronoun": "",
      "categories": [],
      "url_key": ""
    }
  ],
  "use_institution_prefix": False,
  "break_categories": [],
  "institution_conflicts": []
},
        headers={
                'Authorization': 'token '+token
                })
    print(f"{name}")
    status = r.status_code
    if status != 201:
        print(f"{Fore.RED}Error occured while posting {name}\n Error {status}\n{r.text} {Style.RESET_ALL}")
        
x = input("Importing is done successfully! Press any key to continue...")
