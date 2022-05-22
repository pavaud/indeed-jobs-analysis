# -*- coding: utf-8 -*-
"""
Created on Thu May 20 12:54:07 2022
@author: phili
--
Function:
Collect Jobs from "fr.Indeed.com" for insights with location, salary...
"""
import pandas as pd
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_jobs(keyword, num_jobs, verbose=False, slp_time=5):
    '''
    Scrape Jobs from Indeed and return it as a dataframe

    Parameters
    ----------
    keyword : STRING
        JOB NAME TO SEARCH.
    num_jobs : INT
        NUMBER OF JOBS TO SEARCH.
    verbose : BOOL
        VARIABLE TO PRINT WHEN DEBUGGING.
    slp_time : INT
        TIME TO WAIT TO LOAD AND REFRESH PAGES.

    Returns
    -------
    dataframe.
    '''
    
    # initializing webdriver
    # options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_size(800, 700)
    
    #keyword = '"data%20engineer"'
    url = 'https://fr.indeed.com/jobs?q='+keyword+'&l=France&sort=date'
    driver.get(url)
    
    # accept cookies
    driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
    
    # loop until num_jobs collected reached
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
        
        # collect all jobs in the page
        job_buttons = driver.find_elements(By.CLASS_NAME,"job_seen_beacon")
        
        # collect for each job important infos
        for job_button in job_buttons:
            
            job_button.click()  #You might 
            time.sleep(2)
            
            # get data
            title = job_button.find_element(By.CLASS_NAME,"jcs-JobTitle").text
            company = job_button.find_element(By.CLASS_NAME,"companyName").text
            location = job_button.find_element(By.CLASS_NAME,"companyLocation").text
                
            try:
                salary = job_button.find_element(By.CLASS_NAME,"attribute_snippet").text
            except:
                salary = -1
                
            date = job_button.find_element(By.CLASS_NAME,"date").text
            snippet = job_button.find_element(By.CLASS_NAME,"job-snippet").text
            
            # debug
            if verbose:
                print('Job : '+title)
                print('Company : '+company)
                print('Location : ' + location)
                print('Salary : ' + str(salary))
                print('Date : ' + date)
                print('***')
            
            # add line in dictionary for jobs
            jobs.append({"Job Title" : title,
                    "Company Name" : company,
                    "Location" : location,
                    "Salary" : salary,
                    "Date" : date,
                    "Snippet " : snippet})
            
    
    
        # "Next page" button click            
        try:
            driver.find_element(By.XPATH,'.//a[@aria-label="Suivant"]').click()
        except NoSuchElementException:
            print("Next not found")
        
        time.sleep(slp_time)
            
    
    # convert dict to df
    df = pd.DataFrame(jobs)
    print(df)
    
    #driver.quit()