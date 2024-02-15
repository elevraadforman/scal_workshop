#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 13:49:26 2022

@author: lotheboletdfdf
"""

import numpy as np
import matplotlib.pyplot as plt

# create random data
xdata = np.random.random([2, 10])

x = np.linspace(0, 10, 30)

#define LETy

Lo = 2
Eo = 3
To = 4

Lw = Lo
Ew = Eo
Tw = To



#define paraeters

Swir = 0.1
Sorw = 0.3
kOro = 1
kOrw = 0.6

Sw = np.linspace(Swir, 1-Sorw, 50)

S_w = (Sw - Swir)/(1- Sorw - Swir)

#water rel_perm


krw = kOrw*((S_w**Lw)/((S_w**Lw)+Ew*((1-S_w)**Tw)))
#krw = kOrw*((S_w[1:]**Lw)/((S_w[1:]**Lw)+Ew*((1-S_w[1:])**Tw)))

#oil rel_perm

kro = kOro*(((1-S_w)**Lo)/(((1-S_w)**Lo)+Eo*(S_w**To)))





# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(Sw, krw, color='b')
ax.plot(Sw, kro, color='r')

plt.show()
