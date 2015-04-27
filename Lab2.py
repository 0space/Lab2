from spyre import server

import pandas as pd
import urllib2
import json
from numpy import *
import matplotlib.pyplot as plt
import math
import pylab
from matplotlib import mlab
import matplotlib.pyplot as plt

class Lab2(server.App):
	title = "Project 2.\n Created by Andrey Khimich, student FB-31"
	
	inputs = [{	"input_type":'dropdown',
				"label": 'Province', 
				"options" : [ 	{"label": "Cherkasy", "value":"01"},
								{"label": "Chernihiv", "value":"02"},
								{"label": "Chernivtsi", "value":"03"},
								{"label": "Crimea", "value":"04"},
								{"label": "Dnipropetrovs'k", "value":"05"},
								{"label": "Donets'k", "value":"06"},
								{"label": "Ivano-Frankivs'k", "value":"07"},
								{"label": "Kharkiv", "value":"08"},
								{"label": "Kherson", "value":"09"},
								{"label": "Khmel'nyts'kyy", "value":"10"},
								{"label": "Kiev", "value":"11"},
								{"label": "Kiev City", "value":"12"},
								{"label": "Kirovohrad", "value":"13"},
								{"label": "Luhans'k", "value":"14"},
								{"label": "L'viv", "value":"15"},
								{"label": "Mykolayiv", "value":"16"},
								{"label": "Odessa", "value":"17"},
								{"label": "Poltava", "value":"18"},
								{"label": "Rivne", "value":"19"},
								{"label": "Sevastopol'", "value":"20"},
								{"label": "Sumy", "value":"21"},
								{"label": "Ternopil'", "value":"22"},
								{"label": "Transcarpathia", "value":"23"},
								{"label": "Vinnytsya", "value":"24"},
								{"label": "Volyn", "value":"25"},
								{"label": "Zaporizhzhya", "value":"26"},
								{"label": "Zhytomyr", "value":"27"}],
				"variable_name": 'ticker1', 
				"action_id": "update_data" },
			{ "input_type":'slider',
				"label": 'Year', 
				"min" : 1981,
				"max" : 2015,
				"value" : 1981,
				"variable_name": 'year', 
				"action_id": 'plot'},
			{ "input_type":'slider',
				"label": 'Week1', 
				"min" : 1,
				"max" : 52,
				"value" : 1,
				"variable_name": 'week1', 
				"action_id": 'plot'},
			{ "input_type":'slider',
				"label": 'Week2', 
				"min" : 1,
				"max" : 52,
				"value" : 1,
				"variable_name": 'week2', 
				"action_id": 'plot'},
			{ "input_type":'dropdown',
				"label": 'Index', 
				"options" : [ {"label": "VCI", "value":"VCI"},
							{"label": "TCI", "value":"TCI"},
							{"label": "VHI", "value":"VHI"}],
				"variable_name": 'ticker2', 
				"action_id": "update_data" }
			]	
	
	tabs = ["Plot", "Table"]
	
	outputs = [{	"output_type" : "plot",
					"output_id" : "plot",
					"control_id" : "update_data",
					"tab" : "Plot",
					"on_page_load" : True },
				{	"output_type" : "table",
					"output_id" : "table_id",
					"control_id" : "update_data",
					"tab" : "Table",
					"on_page_load" : True }]
			


	data_params = None
	data = pd.DataFrame()
	
	def getData(self, params):
		ticker1 = str(params['ticker1'])
		ticker2 = str(params['ticker2'])
		year = float(params['year'])
		week1 = float(params['week1'])
		week2 = float(params['week2'])
		if week1<=week2:
			min = week1
			max = week2
		else:
			min = week2
			max = week1
		df = pd.read_csv('data/vhi_id_%s.csv'%ticker1,index_col=False, header=1)
		a = df[df["week"]<=max ]
		b=a[df["week"]>=min]
		c = b[df['year']!=0]
		z=c[df['VHI']!=-1]
		z
		return z
		
	def getPlot(self, params):
		year = 0
		ticker1 = str(params['ticker1'])
		ticker2 = str(params['ticker2'])
		year = float(params['year'])
		week1 = float(params['week1'])
		week2 = float(params['week2'])
		if week1<=week2:
			min = week1
			max = week2
		else:
			min = week2
			max = week1
		df = pd.read_csv('data/vhi_id_%s.csv'%ticker1,index_col=False, header=1)
		if year!=0:
			w=df[df['year']==year]
		else:
			w=df
		x=w[[ticker2]]
		y =w['week']
		plt = x.plot(y)
		fig = plt.get_figure()
		return fig

app = Lab2()
app.launch(port=9090)
