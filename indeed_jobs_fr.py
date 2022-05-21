# -*- coding: utf-8 -*-
"""
Created on Thu May 19 12:54:07 2022

@author: phili
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd

keyword = '"data%20engineer"'
url = 'https://fr.indeed.com/jobs?q='+keyword+'&l=France&sort=date'
page = requests.get(url) 
data = page.text
soup = BeautifulSoup(data, 'html.parser')
jobs = soup.find_all('div',class_='job_seen_beacon')

print('Nombre d\'offres : '+ str(len(jobs)))
print('########################')

jobs_dict = []

for job in jobs:
    title = job.find('a',class_="jcs-JobTitle").text
    company = job.find('span',class_='companyName').text
    location = job.find('div',class_='companyLocation').text
        
    try:
        salary = job.find('div',class_='attribute_snippet').text
    except:
        salary = -1
        
    date = job.find('span',class_='date').text
    snippet = job.find('div',class_='job-snippet').text
    
    
    print('Job : '+title)
    print('Company : '+company)
    print('Location : ' + location)
    print('Salary : ' + str(salary))
    print('Date : ' + date)
    print('***')
    
    jobs_dict.append({"Job Title" : title,
            "Company Name" : company,
            "Location" : location,
            "Salary" : salary,
            "Date" : date,
            "Snippet " : snippet})
 
print(jobs_dict)

df = pd.DataFrame(jobs_dict)
print(df)