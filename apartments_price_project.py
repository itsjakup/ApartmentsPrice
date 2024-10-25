
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


df =  pd.read_excel(r"C:\Users\Perdorues\Downloads\Apartments_Data.xlsx")

print(df.head())

print(df.describe())

df.info()

cmimi_mesatar = df['cmimi'].mean()

cmimi_mesatar_i_perafert = round(cmimi_mesatar, 2)
print("Cmimi mesatar i nje apartamenti ne Tirane eshte", cmimi_mesatar_i_perafert)

moda = df['cmimi'].mode()[0]
print("Moda eshte cmimi", moda)

devijimi_standard =  df['cmimi'].std()
print("Devijimi standard", devijimi_standard)

varianca =  df['cmimi'].var()
print("Varianca eshte", varianca)

percentilet =  df['cmimi'].quantile([0.25, 0.5, 0.75, 0.00])
print("Percentilet e cmimit te apartamentit jane", percentilet)

shperndarja =    df['cmimi'].skew()
print("Shperndarja eshte", shperndarja)

shperndarja_uniforme =   df['cmimi'].kurtosis()
print("Shperndarja uniforme eshte", shperndarja_uniforme)
















