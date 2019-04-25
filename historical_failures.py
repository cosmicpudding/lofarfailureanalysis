# LOFAR failure analysis: historical failures
# V.A. Moss (vmoss.astro@gmail.com)
__author__ = "V.A. Moss"
__date__ = "$25-apr-2019 17:00:00$"
__version__ = "1.0"

import os
import sys
<<<<<<< HEAD
import datetime
from astropy.io import ascii
import numpy as np
from pylab import *

# Plotting imports
import pandas as pd

def plot_historical_failures(files,save_loc,cyc):
=======
from astropy.io import ascii
import datetime

# Plotting imports
from numpy import *
from math import *
import matplotlib
matplotlib.rcParams["interactive"] = True
from pylab import *
from matplotlib import rc
rc('text', usetex=True)
rc('font',**{'family':'serif','serif':['serif'],'size':10})
import pandas as pd

def plot_historical_failures(files):
>>>>>>> 716f2bcdf093229e40b16cb7ec73660d42d44bdf

	dates = []
	hours = []

	for f in files:

		print (f)

		d = ascii.read(f,guess=False,delimiter=',')
		print (d.keys())
		dates = dates + list(d['DATE'])
		hours = hours + list(d['OBSERVING HOURS LOST'])


	# Turn the dates into proper dates
	dates = np.array([datetime.datetime.strptime(x,'%Y-%m-%d') for x in dates])
	hours = np.array(hours)

	# Turn into something that can be plotted (?) need to sum the hours if on the same day...
	truedates = []
	truehours = []

	# Plot by month
	print (min(dates).month,min(dates).year)
	print (max(dates).month,max(dates).year)

	# Make an array for appropriate dates
	startmonth = datetime.datetime.strptime(str(min(dates).year)+str(min(dates).month),'%Y%m')
	endmonth = datetime.datetime.strptime(str(max(dates).year)+str(max(dates).month+1),'%Y%m')
	daterange = pd.date_range(str(startmonth),str(endmonth) , freq='1M') 

	for i in range(0,len(daterange)):

		print (daterange[i])


		if i > 0:
			mask = (dates <= daterange[i]) & (dates > daterange[i-1])
		else:
			mask = (dates <= daterange[i])
		dsub = dates[mask]
		hsub = hours[mask]

		truedates.append(daterange[i]-datetime.timedelta(days=29.5))
		truehours.append(sum(hsub))

	# # Plot
	figure(figsize=(12,3))
	grid(True,alpha=0.3)
	bar(truedates,truehours,width=20,edgecolor='k',facecolor='k',alpha=0.5,zorder=100)
	ylabel('Observing hours lost')

	# Current date saving
	today = str(datetime.datetime.utcnow().date())
<<<<<<< HEAD
	savefig('%s/%s_historicalfailures_%s.png' % (save_loc,''.join(cyc.split()),today),bbox_inches='tight',dpi=200)
=======
	savefig('historicalfailures_%s.png' % today,bbox_inches='tight',dpi=200)
>>>>>>> 716f2bcdf093229e40b16cb7ec73660d42d44bdf

