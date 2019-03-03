import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

verbruikdetails = pd.read_csv('verbruikdetailsminuten.csv')

#Distributieplot maken van kolom Duur/aantal
#sns.distplot(verbruikdetails['Seconden'], kde=False)
#sns.rugplot(verbruikdetails['Seconden'])
sns.pairplot(verbruikdetails)
plt.show()
