from Tkinter import *
from sklearn import tree

words1 = 1

est1 = 1

words2 = 1

est2 = 1

words3 = 1

est3 = 1

def click():
	entered_text=textentry.get()
	output.delete(0.0, END)
	if words1 == 1:
		word1 = "Close: "
	else:
		word1 = "ERROR!"
	output.insert(END, word1)

	if est1 == 1:
		close = clf1.predict([[entered_text]])
	else:
		close = "ERROR!"
	output.insert(END, close)

	if words2 == 1:
		word2 = "   High: "
	else:
		word2 = "ERROR!"
	output.insert(END, word2)

	if est2 == 1:
		high = clf2.predict([[entered_text]])
	else:
		high = "ERROR!"
	output.insert(END, high)

	if words3 == 1:
		word3 = "   Low: "
	else:
		word3 = "ERROR!"
	output.insert(END, word3)

	if est3 == 1:
		low = clf3.predict([[entered_text]])
	else:
		low = "ERROR!"
	output.insert(END, low)

window = Tk()
window.title("The STAC App")
window.configure(width=600, height=700, bg="blue")

Label (window, text="Stock: PRIM", bg="blue", fg="white", font="plump 44 bold") .grid(row=1, column=0, sticky=W)
Label (window, text="Enter Today's Opening Price:", bg="blue", fg="white", font="plump 20 bold") .grid(row=3, column=0, sticky=W)

textentry = Entry(window, width=30, bg="white")
textentry.grid(row=4, column=0, sticky=W)

Button(window, text="Submit", command=click, font="plump 18") .grid(row=4, column=0, sticky=E)

Label (window, text="Estimates:", bg="blue", fg="white", font="plump 20 bold") .grid(row=6, column=0, sticky=W)

output = Text(window, width=60, height=3, bg="white")
output.grid (row=7, column=0, columnspan=2, sticky=W)

clf1 = tree.DecisionTreeClassifier()

O = [[28.21],	[28.06],   [28.09],	[28.61],	[27.99],	[28.04],
	 [28.02],	[28.17],	[28.29],	[28.03],	[27.46],	
	 [27.26],	[26.73],	[26.59],	[26.46],	[26.28],
	 [26.85],	[26.33],	[26.20], 	[25.86], 	[25.87], 
	 [25.70], 	[25.71],	[25.37], 	[25.18], 	[25.04],
	 [25.00],	[24.87],	[25.02],	[24.72], 	[25.44],
	 [26.52], 	[25.79],	[25.93],	[25.48], 	[25.56],
	 [25.62], 	[25.55],	[25.95],	[25.99], 	[26.31],
	 [26.51], 	[26.74],	[26.31],	[26.52], 	[26.84],
	 [26.89],	[26.80],	[26.50], 	[26.90], 	[26.79],
	 [26.67],	[26.31],	[26.06],	[26.12], 	[25.85],
	 [24.91], 	[25.30],	[24.93],	[24.67], 	[24.97],
	 [25.03],	[24.98], 	[25.17],	[25.95], 	[26.06],
	 [26.36],	[26.76], 	[26.55],	[26.25], 	[26.29],
	 [26.11], 	[26.07], 	[26.00],	[26.32], 	[25.86],
	 [25.85],	[25.96], 	[25.31],	[24.98], 	[26.04],
	 [25.98],	[24.10], 	[24.20],	[24.57], 	[24.27],
	 [24.37],	[24.30], 	[24.54],	[24.00], 	[23.93],
	 [24.27],	[23.95], 	[24.75],	[24.82], 	[24.07],
	 [25.96],	[26.48], 	[25.90],	[26.18], 	[25.95],
	 [26.14],	[26.48], 	[26.42],	[26.58], 	[26.17],
	 [26.27],	[26.14], 	[26.39],	[26.49], 	[27.27],
	 [26.85],	[26.12], 	[26.38],	[27.00], 	[26.85],
	 [27.26],	[27.36], 	[27.38],	[27.22], 	[28.01],
	 [28.05],	[27.77], 	[27.94],	[28.04], 	[27.77],
	 [27.93],	[27.71], 	[27.26],	[27.31], 	[27.88],
	 [27.93],	[28.09], 	[28.16],	[27.98], 	[28.16],
	 [28.04],	[28.40], 	[28.19],	[28.00], 	[27.99],
	 [27.45],	[27.08], 	[26.75],	[26.99], 	[27.25],
	 [26.91],	[26.19], 	[26.07],	[26.01], 	[25.90],
	 [25.84], 	[26.01], 	[26.97],	[26.60], 	[27.71],
	 [28.75], 	[28.03], 	[28.07],	[27.85], 	[28.51],
	 [28.22], 	[28.30], 	[28.09],	[27.58], 	[27.80],
	 [27.90], 	[27.79], 	[27.93],	[28.19], 	[28.40],
	 [29.38], 	[29.54],	[29.15],	[28.96], 	[29.15],
	 [29.06], 	[28.99], 	[28.74],	[28.26], 	[28.56],
	 [29.55], 	[29.40], 	[29.37],	[29.70], 	[29.05],
	 [29.03], 	[29.06], 	[28.65],	[28.39], 	[29.07],
	 [28.71], 	[28.40], 	[28.54],	[28.61], 	[28.55],
	 [28.10], 	[28.02], 	[27.99],	[28.13], 	[28.36],
	 [28.96], 	[28.61], 	[28.50],	[28.47], 	[28.02],
	 [28.18], 	[26.78], 	[26.46],	[26.04], 	[26.18],
	 [26.29], 	[26.19], 	[26.16],	[26.32], 	[27.00],
	 [26.29], 	[25.67], 	[25.79],	[25.93], 	[26.00],
	 [24.59], 	[24.93], 	[25.03],	[25.09], 	[25.00],
	 [24.96], 	[24.89], 	[25.15],	[25.28], 	[24.85],
	 [24.64], 	[25.08], 	[25.12],	[24.82], 	[24.76],
	 [24.90], 	[25.07], 	[25.23],	[24.96], 	[24.62],
	 [24.59], 	[24.46], 	[24.52],	[25.10], 	[25.03],
	 [24.80], 	[25.49], 	[24.85],	[24.65], 	[24.49],
	 [24.00], 	[23.89], 	[24.65],	[24.67], 	[24.69],
	 [24.36], 	[24.38], 	[24.72],	[24.52], 	[24.89],
	 [24.10], 	[23.76], 	[24.02],	[24.11], 	[24.65],
	 [24.60], 	[23.34]]

C = ['28.12',	'27.86',    '28.05',	'28.09',	'28.68',	'28.15',
	 '28.15',	'27.98',	'28.27',	'28.37',	'27.98',
	 '27.44',	'27.27',	'26.69',	'26.62',	'26.25',
	 '26.07', 	'26.83', 	'26.27', 	'26.30', 	'25.97',
	 '25.85', 	'25.95', 	'25.86', 	'25.16', 	'25.075',
	 '25.09', 	'24.94', 	'24.97', 	'24.92', 	'24.77',
	 '25.44',	'26.32',	'25.98',	'25.85',	'25.58',
	 '25.63',	'25.66',	'25.59',	'25.94',	'26.01',
	 '26.28',	'26.50',	'26.68',	'26.29',	'26.65',
	 '26.83',	'26.68',	'26.72',	'26.34',	'26.76',
	 '26.74',	'26.67',	'26.04',	'25.93',	'26.24',
	 '25.77',	'25.24',	'25.31',	'24.98',	'24.61',
	 '24.88',	'25.02',	'24.65',	'25.16',	'26.13',
	 '26.06',	'26.27',	'26.86',	'26.56',	'26.16',
	 '26.23',	'25.95',	'26.00',	'26.00',	'26.19',
	 '26.01',	'25.80',	'26.11',	'25.44',	'24.90',
	 '24.58',	'23.83',	'24.11',	'24.54',	'24.47',
	 '24.22',	'24.40',	'24.42',	'24.28',	'24.13',
	 '24.07',	'24.20',	'23.69',	'24.75',	'24.84',
	 '24.62',	'26.13',	'26.71',	'26.00',	'25.97',
	 '26.20',	'26.28',	'26.30',	'26.25',	'26.48',
	 '26.28',	'26.33',	'26.17',	'26.34',	'26.26',
	 '27.06',	'26.83',	'26.05',	'26.43',	'26.95',
	 '26.91',	'27.25',	'27.20',	'27.48',	'27.19',
	 '28.00',	'27.98',	'27.77',	'27.94',	'27.96',
	 '27.71',	'27.92',	'27.60',	'26.99',	'27.20',
	 '27.88',	'27.88',	'27.95',	'28.17',	'27.89',
	 '28.30',	'28.05',	'28.39',	'27.89',	'27.99',
	 '27.86',	'27.44',	'27.04',	'26.74',	'26.86',
	 '27.24',	'26.77',	'26.12',	'26.22',	'25.86',
	 '26.07',	'26.11',	'26.09',	'27.07',	'26.68',
	 '27.96',	'28.52',	'28.03',	'28.06',	'27.89',
	 '28.27',	'28.18',	'28.40',	'28.09',	'27.58',
	 '27.86',	'27.79',	'27.93',	'27.65',	'28.29',
	 '28.30',	'29.52',	'29.23',	'29.05',	'29.05',
	 '29.03',	'28.90',	'28.99',	'28.72',	'28.25',
	 '28.52',	'29.52',	'29.42',	'29.27',	'29.70',
	 '28.95',	'28.96',	'29.07',	'28.59',	'28.52',
	 '28.95',	'28.78',	'28.40',	'28.51',	'28.62',
	 '28.53',	'28.10',	'28.01',	'28.00',	'28.15',
	 '28.28',	'28.83',	'28.61',	'28.37',	'28.39',
	 '28.16',	'27.95',	'26.40',	'26.45',	'26.18',
	 '26.01',	'26.28',	'26.41',	'26.33',	'26.35',
	 '26.93',	'26.13',	'25.48',	'25.94',	'25.89',
	 '24.92',	'24.70',	'24.88',	'24.95',	'25.08',
	 '24.92',	'24.83',	'24.91',	'25.03',	'25.17',
	 '24.70',	'24.70',	'24.81',	'25.07',	'24.84',
	 '24.87',	'24.89',	'25.12',	'25.24',	'24.86',
	 '24.63',	'24.75',	'24.37',	'24.77',	'25.15',
	 '24.94',	'24.75',	'25.36',	'24.70',	'24.65',
	 '24.46',	'24.17',	'23.84',	'24.61',	'24.66',
	 '24.62',	'24.57',	'24.58',	'24.66',	'24.51',
	 '24.74',	'24.02',	'23.69',	'24.05',	'24.23',
	 '24.74',	'24.53']

clf1 = clf1.fit(O, C)

clf2 = tree.DecisionTreeClassifier()

H = ['28.36',	'28.13',    '28.34',	'28.71',	'28.71',	'28.24',
	 '28.31',	'28.46',	'28.71',	'28.59',	'28.02',
	 '27.59',	'27.31',	'26.93',	'26.76',
	 '27.07',	'26.85',	'27.09',	'26.59',	'26.43',
	 '26.11',	'25.87',	'26.42',	'25.91',	'25.46',
	 '25.61',	'25.38',	'25.04',	'25.12',
	 '25.13',	'25.44',	'26.52',	'26.50',	'26.04',
	 '25.955',	'25.77',	'25.93',	'26.01',	'25.99',
	 '26.08',	'26.36',	'26.82',	'27.02',	'26.74',
	 '26.67',	'26.94',	'27.14',	'26.98',	'26.84',
	 '26.90',	'27.07',	'26.80',	'26.73',	'26.38',
	 '26.33',	'26.30',	'25.83',	'26.00',	'25.37',
	 '25.97',	'25.23',	'25.30',	'25.09',	'25.24',
	 '26.05',	'26.55',	'26.57',	'26.76',	'27.04',
	 '26.62',	'26.55',	'26.57',	'26.30',	'26.19',
	 '26.42',	'26.28',	'26.23',	'26.51',	'26.77',
	 '25.49',	'26.29',	'26.40',	'24.20',	'24.51',
	 '24.79',	'24.77',	'24.57',	'24.78',	'24.54',
	 '24.82',	'24.26',	'24.29',	'24.44',	'24.75',
	 '25.12',	'25.09',	'26.00',	'26.62',	'26.76',
	 '26.38',	'26.18',	'26.46',	'26.58',	'26.53',
	 '26.73',	'26.52',	'26.34',	'26.52',	'26.48',
	 '26.56',	'27.35',	'27.12',	'26.97',	'26.41',
	 '27.00',	'27.07',	'27.26',	'27.69',	'27.83',
	 '27.73',	'28.01',	'28.67',	'28.13',	'28.07',
	 '28.21',	'28.08',	'28.11',	'28.12',	'27.69',
	 '27.51',	'27.99',	'28.20',	'28.17',	'28.27',
	 '28.23',	'28.40',	'28.46',	'28.40',	'28.96',
	 '28.23',	'28.25',	'28.04',	'27.48',	'27.28',
	 '27.10',	'27.40',	'27.41',	'26.80',	'26.34',
	 '26.37',	'26.17',	'26.25',	'26.24',	'27.09',
	 '27.54',	'27.71',	'28.75',	'28.62',	'28.25',
	 '28.26',	'28.51',	'28.58',	'28.41',	'28.54',
	 '28.14',	'27.80',	'28.07',	'27.94',	'28.05',
	 '28.24',	'28.51',	'29.63',	'29.82',	'29.36',
	 '29.36',	'29.28',	'29.21',	'29.22',	'29.07',
	 '28.84',	'28.67',	'29.55',	'29.54',	'29.67',
	 '29.90',	'29.89',	'29.47',	'29.24',	'29.21',
	 '28.79',	'29.26',	'29.19',	'28.93',	'28.67',
	 '28.84',	'28.75',	'28.70',	'28.24',	'28.10',
	 '28.19',	'28.45',	'29.05',	'28.99',	'28.75',
	 '28.60',	'28.51',	'30.00',	'28.00',	'26.72',
	 '26.75',	'26.44',	'26.38',	'26.51',	'26.63',
	 '26.59',	'27.36',	'27.16',	'26.48',	'26.07',
	 '27.98',	'26.22',	'24.99',	'25.27',	'25.24',
	 '25.34',	'25.25',	'25.17',	'25.21',	'25.33',
	 '25.28',	'25.59',	'24.86',	'25.08',	'25.12',
	 '25.25',	'25.06',	'25.11',	'25.31',	'25.47',
	 '25.62',	'25.00',	'24.90',	'24.79',	'24.79',
	 '25.10',	'25.37',	'25.11',	'25.49',	'25.74',
	 '24.96',	'24.88',	'24.52',	'24.43',	'24.68',
	 '24.72',	'24.86',	'24.68',	'24.61',	'24.72',
	 '24.85',	'25.00',	'24.76',	'24.28',	'24.03',
	 '24.42',	'24.79',	'25.10',	'24.54']

clf2 = clf2.fit(O, H)

clf3 = tree.DecisionTreeClassifier()

L = ['27.81',	'27.73',   '27.53',	'28.04',	'27.98',	'27.86',
	 '27.48',	'27.92',	'28.03',	'27.57',	'27.38',
	 '27.18',	'26.69',	'26.38',
	 '26.33',	'26.16',	'26.06',	'26.33',	'26.06',
	 '25.86',	'25.49',	'25.44',	'25.57',	'25.36',
	 '24.98',	'25.02',	'24.99',	'24.78',	'24.80',
	 '24.68',	'24.64',	'25.41',	'25.79',	'25.52',
	 '25.00',	'25.18',	'25.44',	'25.29',	'25.55',
	 '25.69',	'25.79',	'26.22',	'26.35',	'26.25',
	 '26.13',	'26.53',	'26.71',	'26.61',	'26.42',
	 '26.24',	'26.73',	'26.41',	'26.19',	'25.96',
	 '25.75',	'25.85',	'24.80',	'24.57',	'24.58',
	 '24.67',	'24.59',	'24.62',	'24.58',	'24.65',
	 '25.16',	'26.03',	'25.84',	'25.91',	'26.19',
	 '26.18',	'26.03',	'26.11',	'25.83',	'25.89',
	 '25.74',	'25.33',	'25.67',	'25.62',	'25.31',
	 '24.63',	'24.88',	'23.73',	'23.65',	'23.93',
	 '24.31',	'24.27',	'24.14',	'24.30',	'24.03',
	 '23.61',	'23.87',	'23.87',	'23.61',	'23.69',
	 '24.66',	'23.96',	'24.59',	'26.12',	'25.67',
	 '25.91',	'25.80',	'26.06',	'26.06',	'26.08',
	 '26.05',	'26.07',	'25.91',	'25.97',	'26.12',
	 '26.11',	'26.25',	'26.77',	'25.90',	'25.91',
	 '26.41',	'26.55',	'26.51',	'27.02',	'27.12',
	 '27.22',	'27.18',	'27.81',	'27.73',	'27.73',
	 '27.88',	'27.69',	'27.65',	'27.42',	'27.26',
	 '26.93',	'27.08',	'27.42',	'27.49',	'27.30',
	 '27.88',	'27.83',	'27.97',	'27.89',	'28.07',
	 '26.92',	'27.86',	'27.22',	'27.07',	'26.56',
	 '26.60',	'26.79',	'26.62',	'26.19',	'25.94',
	 '25.94',	'25.45',	'25.75',	'25.54',	'26.07',
	 '26.49',	'26.10',	'26.80',	'28.01',	'27.81',
	 '27.65',	'27.32',	'28.22',	'27.94',	'27.87',
	 '27.53',	'27.21',	'27.83',	'27.61',	'27.53',
	 '27.49',	'28.16',	'28.16',	'29.39',	'29.05',
	 '28.86',	'28.76',	'28.85',	'28.85',	'28.56',
	 '28.26',	'28.20',	'28.41',	'29.09',	'29.31',
	 '29.02',	'29.00',	'28.94',	'28.76',	'28.43',
	 '28.32',	'28.49',	'28.71',	'28.35',	'28.19',
	 '28.40',	'28.41',	'28.10',	'27.91',	'27.88',
	 '27.70',	'28.02',	'28.07',	'28.45',	'28.26',
	 '28.13',	'27.85',	'27.76',	'26.78',	'26.25',
	 '26.04',	'25.85',	'25.94',	'26.05',	'26.00',
	 '26.23',	'25.36',	'26.00',	'25.47',	'25.44',
	 '25.48',	'24.94',	'24.54',	'24.48',	'24.66',
	 '24.75',	'24.98',	'24.73',	'24.62',	'24.72',
	 '24.84',	'24.85',	'24.22',	'24.57',	'24.73',
	 '24.56',	'24.75',	'24.75',	'24.79',	'24.74',
	 '24.82',	'24.29',	'24.44',	'23.73',	'23.81',
	 '24.48',	'24.50',	'24.68',	'24.39',	'24.85',
	 '24.51',	'24.44',	'23.91',	'23.60',	'23.71',
	 '24.20',	'24.44',	'24.20',	'24.14',	'24.19',
	 '24.36',	'24.33',	'24.06',	'23.70',	'23.64',
	 '23.78',	'24.19',	'24.45',	'23.20']

clf3 = clf3.fit(O, L)

window.mainloop()