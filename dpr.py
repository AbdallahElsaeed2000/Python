# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 01:51:16 2019

@author: gcct
"""

import pandas as pd
import pandas_profiling
import time
start = time.process_time()

csv_file = input('Please type the directory of your csv file : ')
with open (csv_file, 'r')as csv_file:
    df=pd.read_csv(csv_file, sep=',', na_values=["?"])
    for col in df.columns:
        df[str(col)]=df[str(col)].astype('category')
    profile = pandas_profiling.ProfileReport(df)
    profile.to_file(output_file="./report.html")
    csv_file.close()

print('Time taken = ' + (str(time.process_time() - start)) + ' s')
input()