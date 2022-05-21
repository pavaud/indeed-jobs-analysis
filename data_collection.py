# -*- coding: utf-8 -*-
"""
Created on Thu May 20 12:54:07 2022
@author: phili
--
Function:
Collect Jobs from "fr.Indeed.com" for insights with location, salary...
"""
import indeed_scraper 
import pandas as pd 

df = indeed_scraper.get_jobs('data engineer',500, False, 5)

df.to_csv('glassdoor_jobs.csv', index = False)