#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:23:04 2023

@author: xsulda
"""
import matplotlib.pyplot as plt
from matplotlib import pyplot
import pandas as pd
import numpy as np
plt.style.use('seaborn-deep')
import seaborn as sns
import matplotlib.ticker as plticker
import matplotlib.ticker as ticker


#First column are heights
df=pd.read_excel('Heigth.xlsx')


x1 = df['A']


print(df)



plt.hist([x1], bins=15)
plt.yticks([0, 5, 10])

#Check if ticks matches dimensions
ax2 = plt.twinx()
sns.kdeplot(x1, ax=ax2, bw_method=0.5, legend="true")
plt.yticks([0, 0.5, 1])


plt.savefig('Distribution.png', dpi=300)
plt.savefig('Distribution.pdf')

plt.show()