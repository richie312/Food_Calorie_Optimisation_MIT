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
from tqdm import tqdm
from lecture1 import *

"""Set the working directory"""
os.chdir(r"C:\Users\Richie\Desktop\Python_Projects\Food_Calorie")

""" Extracting the tables from pdf file and creating multiple csv file to store the 
data in different categories of food."""
# =============================================================================
# for i in tqdm(range(0,9)):
#     print(i)
#     names = ["Breads_Cereals","Breads_Cereals","Meat_Fish","Meat_Fish",
#              "Fruits_Vegetables","Dairy_Products","Fats_Sugars","Fruits","Fruits"]
#     df = read_pdf("Food.pdf",pages = i+1,multiple_tables = True)
#     dataframe = pd.DataFrame()
#     dataframe['Category'] = df[0][0][1:]
#     dataframe['Portion Size'] = df[0][1][1:]
#     dataframe['per 100 gms'] = df[0][2][1:]
#     
#     """ Remove the unwanted characters in each column"""
#     
#     dataframe['Portion Size'] = dataframe['Portion Size'].map(lambda x: str(x)[:3])
#     dataframe['Portion Size'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
#     dataframe['per 100 gms'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
#     
#     """ Write the csv file"""
#     dataframe.to_csv("{}_{}.csv".format(names[i],(i+1)), sep=',')
# 
# =============================================================================
"""Reading the specific dataset"""

names = ["Breads_Cereals","Breads_Cereals","Meat_Fish","Meat_Fish",
              "Fruits_Vegetables","Dairy_Products","Fats_Sugars","Fruits","Fruits"]
i=0
calorie_data = pd.read_csv("{}_{}.csv".format(names[i],(i+1)),index_col=False)
calorie_data.columns

"""Building the food menu along with calorie values in food Class"""

Bread_Cereal = buildMenu(calorie_data['Category'],calorie_data['Portion Size'],calorie_data["per 100 gms"])


"""Optimisation Model_Greedy Algorithm"""
testGreedy(Bread_Cereal, 700,lambda x: 1/Food.getCost(x))
testGreedy(Bread_Cereal, 700,lambda x: 1/Food.getCost(x))
testGreedy(Bread_Cereal, 700,lambda x: Food.getCost(x))