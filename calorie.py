# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 17:57:26 2018

@author: Richie
"""

import os
import tabula
from tabula import read_pdf
from tabula import convert_into_by_batch
import pandas as pd

"""Set the working directory"""
os.chdir(r"C:\Users\Richie\OneDrive\Python_Projects\Food_Calorie")

for i in range(1,10):
    print(i)
    df = tabula.read_pdf("Food.pdf",pages = i,multiple_tables = True)
    dataframe = pd.DataFrame()
    dataframe['Category'] = df[0][0][1:]
    dataframe['Portion Size'] = df[0][1][1:]
    dataframe['per 100 gms'] = df[0][2][1:]
    df.to_csv(dataframe, sep='\t', encoding='utf-8')




data=pd.DataFrame(df[0][0],df[0][1],df[0][2])
df[0][0]

# =============================================================================
# """using PyPDF2 reader"""
# =============================================================================
# =============================================================================
# file = open("Food.pdf",'rb')
# pdfreader = PyPDF2.PdfFileReader(file)
# print(pdfreader.getNumPages())
# 
# pageobj = pdfreader.getPage(0)
# print(pageobj.extractText())
# =============================================================================
