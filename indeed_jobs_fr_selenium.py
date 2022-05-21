# -*- coding: utf-8 -*-
"""
Created on Thu May 20 12:54:07 2022

@author: phili
"""
import pandas as pd
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


# Initializing webdriver
# options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_size(800, 700)

# constants
num_jobs = 60
slp_time = 3
keyword = '"data%20engineer"'
url = 'https://fr.indeed.com/jobs?q='+keyword+'&l=France&sort=date'

driver.get(url)

# accept cookies
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

jobs = []
while len(jobs) < num_jobs:
    
    # let some time to load the page
    time.sleep(slp_time)
    
    # close sign up if prompt
    try:
        driver.find_element(By.ID,"popover-x").click()
        print("sign up prompt close")
        time.sleep(slp_time)
    except:
        print("no sign up prompt")
        pass
    
    job_buttons = driver.find_elements(By.CLASS_NAME,"job_seen_beacon")
    
    for job in job_buttons:
        
        # get data
        title = job.find_element(By.CLASS_NAME,"jcs-JobTitle").text
        company = job.find_element(By.CLASS_NAME,"companyName").text
        location = job.find_element(By.CLASS_NAME,"companyLocation").text
            
        try:
            salary = job.find_element(By.CLASS_NAME,"attribute_snippet").text
        except:
            salary = -1
            
        date = job.find_element(By.CLASS_NAME,"date").text
        snippet = job.find_element(By.CLASS_NAME,"job-snippet").text
        
        # print data to console
        print('Job : '+title)
        print('Company : '+company)
        print('Location : ' + location)
        print('Salary : ' + str(salary))
        print('Date : ' + date)
        print('***')
        
        # add line for jobs
        jobs.append({"Job Title" : title,
                "Company Name" : company,
                "Location" : location,
                "Salary" : salary,
                "Date" : date,
                "Snippet " : snippet})
        


    # Next page button click            
    try:
        driver.find_element(By.XPATH,'.//a[@aria-label="Suivant"]').click()
    except NoSuchElementException:
        print("Next not found")
    
    time.sleep(slp_time)
        

# convert dict to df
df = pd.DataFrame(jobs)
print(df)