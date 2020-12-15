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

while True:
    sheet = pd.read_excel(open('database.xlsx', 'rb'),
                sheet_name='Judges')

    short = sheet['Short'][x]
    if short == 'DONE':
        print(f"{Fore.GREEN}SUCCESS! Post completed {Style.RESET_ALL}")
    
    institution = None
    for i in institutions:
        if i['code'] == short:
            institution = i['url']
            print(f"{Fore.YELLOW}{institution}{Style.RESET_ALL}")
            break
        
    
    
    name = sheet['Name'][x]
    score = sheet['Score'][x]
    email = sheet['Email'][x]
    number = sheet['Number'][x]
    gender = sheet['Gender'][x]
    if gender == 'Male':
        gender='M'
    elif gender == 'Female':
        gender='F'
    else:
        gender='O'
    x = x+1
    
    
    r = requests.post(
        f'{site}api/v1/tournaments/{slug}/adjudicators',
        json = {
        "name": name,
        "email": email,
        "anonymous": False,
        "institution": institution,
        "base_score": float(score),
        "breaking": False,
        "trainee": False,
        "independent": True,
        "adj_core": False,
        "institution_conflicts": [],
        "team_conflicts": [],
        "adjudicator_conflicts": [],
        "gender": gender
        },
        headers={
                'Authorization': 'token '+token
                })

    status = r.status_code
    print(f"{status}: {name}, {institution}")
    if status != 201:
        print(f"{Fore.RED}Error occured while posting {name}, {short}\n Error {status}\n{r.text} {Style.RESET_ALL}")
        
x = input()