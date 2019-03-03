import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#inlezen van CSV verbruikdetails.csv in PANDAS dataframe verbruikdetails
#bestand staat op laptop Denise c:\user\piete
#In het orginele Excel bestaand moet het formaat 00:00:00 omgezet worden naar seconden
#Dit kan door de kolom met duur in het formaat hh:mm te zetten en de seconden kolom naar decimaal (integer) 
#In de seconden kolom zet je dan de formule (hh:mm * 1440) * 60
# zie https://cybertext.wordpress.com/2017/08/02/excel-convert-hours-and-minutes-to-minutes/

verbruikdetails = pd.read_csv('verbruikdetailsminuten.csv')

#de functie head geeft info over het dataframe
print(verbruikdetails.head())
print()

#Distributieplot maken van kolom Duur/aantal
sns.distplot(verbruikdetails['Seconden'])

plt.show()