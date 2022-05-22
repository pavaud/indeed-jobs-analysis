# -*- coding: utf-8 -*-
"""
Created on Thu May 20 12:54:07 2022
@author: phili
--
Function:
Collect Jobs from "fr.Indeed.com" for insights with location, salary...
"""
import indeed_scraper as sp 
#import pandas as pd 

df = sp.get_jobs('data%20engineer',500, True, 5)

df.to_csv('glassdoor_jobs.csv', index = False)