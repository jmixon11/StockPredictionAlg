from Tkinter import *
from sklearn import tree

def click():
	entered_text=textentry.get()
	output.delete(0.0, END)
	word1 = "Close: "
	output.insert(END, word1)
	close = clf1.predict([[entered_text]])
	output.insert(END, close)
	word2 = "   High: "
	output.insert(END, word2)
	high = clf2.predict([[entered_text]])
	output.insert(END, high)
	word3 = "   Low: "
	output.insert(END, word3)
	low = clf3.predict([[entered_text]])
	output.insert(END, low)

window = Tk()
window.title("The STAC App")
window.configure(width=600, height=700, bg="blue")

Label (window, text="Stock: MPC", bg="blue", fg="white", font="plump 44 bold") .grid(row=1, column=0, sticky=W)
Label (window, text="Enter Today's Opening Price:", bg="blue", fg="white", font="plump 20 bold") .grid(row=3, column=0, sticky=W)

textentry = Entry(window, width=30, bg="white")
textentry.grid(row=4, column=0, sticky=W)

Button(window, text="Submit", command=click, font="plump 18") .grid(row=4, column=0, sticky=E)

Label (window, text="Estimates:", bg="blue", fg="white", font="plump 20 bold") .grid(row=6, column=0, sticky=W)

output = Text(window, width=60, height=3, bg="white")
output.grid (row=7, column=0, columnspan=2, sticky=W)

clf1 = tree.DecisionTreeClassifier()

O = [[73.86],	[73.46],   [74.50],	[74.01],	[73.64],
	 [74.71],	[75.61],	[75.61],	[77.89],	[78.94],
	 [78.84],	[79.52],	[80.00],	[81.76],	[82.27],
	 [79.78],	[79.40],	[78.77],	[77.01],	[77.90],
	 [78.17],	[77.77],	[79.16],	[79.98],	[80.58],
	 [77.60],	[77.10],	[77.85],	[77.84],	[77.72],
	 [77.94],	[76.17],	[76.43],	[77.23],	[76.90],
	 [76.28],	[73.28],	[74.28],	[75.47],	[82.56],
	 [80.70],	[79.19],	[80.32],	[79.98],	[79.40],
	 [78.80],	[79.07],	[77.79],	[74.98],	[74.46],
	 [74.30],	[73.71],	[72.94],	[72.47],	[72.71],
	 [73.24],	[71.59],	[72.70],	[72.95],	[72.23],
	 [73.13],	[73.88],	[72.10],	[73.40],	[72.37],
	 [71.81],	[69.70],	[69.40],	[68.51],	[69.56],
	 [69.65],	[69.38],	[70.24],	[69.73],	[68.12],
	 [66.96],	[66.62],	[64.88],	[64.38],	[64.27],
	 [65.96],	[66.16],	[66.92],	[66.88],	[66.53],
	 [66.29],	[67.45],	[67.60],	[68.16],	[65.46],
	 [64.67],	[64.48],	[63.45],	[64.91],	[66.96],
	 [62.93],	[66.08],	[68.33],	[69.77],	[69.24],
	 [69.05],	[71.51],	[71.29],	[72.08],	[73.37],
	 [73.31],	[72.04],	[71.66],	[71.78],	[71.11],
	 [71.60],	[70.47],	[69.72],	[68.79],	[69.39],
	 [69.07],	[68.87],	[68.66],	[67.46],	[66.11],
	 [66.47],	[66.43],	[66.72],	[66.55],	[66.70],
	 [65.70],	[65.06],	[66.03],	[65.87],	[64.95],
	 [64.16],	[64.30],	[64.82],	[64.65],	[64.19],
	 [63.10],	[64.32],	[63.42],	[62.92],	[62.82],
	 [61.69],	[62.01],	[62.29],	[61.95],	[62.16],
	 [62.35],	[62.19],	[62.11],	[61.85],	[61.51],
	 [60.45],	[62.32],	[61.79],	[61.98],	[62.62],
	 [63.29],	[62.58],	[62.34],	[62.26],	[61.06],
	 [60.24],	[59.78],	[58.50],	[57.68],	[57.52],
	 [56.96],	[56.54],	[57.48],	[57.30],	[56.42],
	 [56.52],	[55.74],	[56.42],	[56.89],	[56.00],
	 [56.31],	[56.72],	[56.13],	[55.80],	[56.48],
	 [56.16],	[55.53],	[55.94],	[55.46],	[55.26],
	 [54.61],	[55.36],	[55.00],	[54.24],	[54.43],
	 [54.38],	[53.75],	[53.06],	[52.36],	[53.27],
	 [54.00],	[53.95],	[53.48],	[52.66],	[52.63],
	 [51.64],	[53.58],	[52.55],	[52.55],	[51.53],
	 [52.17],	[52.33],	[51.47],	[50.26],	[49.43],
	 [49.71],	[50.07],	[49.62],	[50.72],	[52.00],
	 [52.25],	[52.08],	[52.03],	[53.04],	[54.43],
	 [54.90],	[55.59],	[55.98],	[56.05],	[56.15],
	 [56.11],	[55.16],	[55.92],	[54.27],	[56.39],
	 [56.14],	[55.57],	[55.34],	[55.76],	[54.90],
	 [54.62],	[53.86],	[53.81],	[53.68],	[54.74],
	 [53.92],	[53.95],	[52.87],	[53.14],	[52.83],
	 [52.63],	[52.14],	[52.89],	[52.12],	[51.40],
	 [51.64],	[51.19],	[52.12],	[52.93],	[53.66],
	 [53.81],	[53.31],	[53.10],	[54.87],	[54.48],
	 [54.90],	[53.55],	[52.89],	[52.84],	[52.58],
	 [52.57],	[52.86],	[52.43]]

C = ['72.62',	'72.48',    '73.82',	'74.52',	'74.79',
	 '73.56',	'75.19',	'74.88',	'75.46',	'77.77',
	 '78.99',	'79.15',	'78.76',	'80.33',	'81.93',
	 '81.92',	'79.03',	'79.55',	'77.61',	'77.00',
	 '79.11',	'78.87',	'78.49',	'78.85',	'79.53',
	 '80.71',	'76.73',	'77.29',	'78.34',	'77.33',
	 '77.54',	'77.11',	'75.31',	'76.50',	'76.94',
	 '77.46',	'75.84',	'72.90',	'74.91',	'81.43',
	 '82.93',	'80.23',	'79.78',	'79.85',	'79.76',
	 '79.40',	'78.78',	'78.55',	'77.52',	'74.59',
	 '74.25',	'74.02',	'73.70',	'71.67',	'72.45',
	 '73.41',	'72.57',	'72.60',	'71.80',	'73.11',
	 '71.82',	'72.88',	'73.68',	'71.28',	'72.97',
	 '73.21',	'71.46',	'69.21',	'69.68',	'68.63',
	 '69.36',	'69.24',	'69.27',	'70.22',	'69.03',
	 '67.68',	'67.39',	'66.16',	'65.19',	'64.79',
	 '64.06',	'65.60',	'66.29',	'66.81',	'66.46',
	 '66.27',	'66.25',	'67.93',	'67.80',	'68.16',
	 '66.08',	'64.77',	'63.84',	'62.79',	'65.09',
	 '65.69',	'64.58',	'67.41',	'68.69',	'69.27',
	 '69.13',	'70.15',	'71.74',	'71.08',	'71.59',
	 '73.12',	'73.16',	'71.89',	'71.49',	'71.98',
	 '70.78',	'71.42',	'70.25',	'69.51',	'69.00',
	 '69.39',	'69.34',	'68.68',	'68.61',	'67.18',
	 '65.98',	'66.40',	'66.42',	'66.84',	'66.36',
	 '66.33',	'65.66',	'64.75',	'66.01',	'65.75',
	 '64.66',	'64.15',	'64.49',	'64.46',	'64.75',
	 '64.00',	'63.46',	'64.54',	'63.30',	'62.84',
	 '62.63',	'61.40',	'62.22',	'61.88',	'62.03',
	 '62.01',	'62.29',	'61.94',	'62.27',	'62.01',
	 '61.50',	'62.87',	'62.20',	'61.72',	'61.66',
	 '63.22',	'63.11',	'62.35',	'62.20',	'62.17',
	 '60.89',	'59.74',	'59.06',	'58.47',	'57.27',
 	 '56.44',	'56.99',	'56.34',	'57.49',	'57.10',
	 '56.75',	'56.51',	'55.72',	'56.37',	'56.55',
	 '56.22',	'56.25',	'56.14',	'56.02',	'56.25',
	 '56.31',	'56.14',	'55.89',	'56.08',	'55.47',
	 '55.24',	'55.38',	'55.53',	'54.73',	'54.37',
	 '54.43',	'54.20',	'53.58',	'52.96',	'52.34',
	 '53.21',	'53.77',	'53.75',	'53.42',	'52.63',
	 '52.37',	'51.79',	'54.28',	'52.45',	'52.33',
	 '51.43',	'52.52',	'51.72',	'51.13',	'50.17',
	 '49.67',	'49.45',	'50.11',	'49.70',	'51.06',
	 '51.89',	'52.31',	'52.16',	'52.21',	'52.99',
	 '54.44',	'54.90',	'55.79',	'55.89',	'56.20',
	 '56.53',	'55.99',	'54.98',	'56.15',	'55.66',
	 '56.02',	'55.56',	'55.34',	'55.40',	'55.55',
	 '54.83',	'54.31',	'53.81',	'53.84',	'53.76',
 	 '54.20',	'54.08',	'54.07',	'52.85',	'52.90',
	 '53.10',	'52.33',	'51.81',	'52.62',	'51.85',
	 '51.33',	'51.50',	'51.17',	'51.73',	'52.85',
	 '54.29',	'53.77',	'52.99',	'53.35',	'55.03',
	 '54.47',	'54.71',	'53.43',	'52.97',	'53.09',
	 '52.80',	'52.70',	'53.13']

clf1 = clf1.fit(O, C)

clf2 = tree.DecisionTreeClassifier()

H = ['74.18',	'73.80',    '74.91',	'75.15',	'75.23',
	 '75.46',	'76.19',	'75.79',	'78.31',	'78.94',
	 '79.34',	'79.61',	'80.15',	'82.20',	'83.33',
	 '82.03',	'82.69',	'80.47',	'78.84',	'77.97',
	 '79.26',	'78.93',	'80.36',	'80.11',	'80.72',
	 '80.92',	'77.27',	'78.64',	'78.60',	'77.97',
	 '78.25',	'78.11',	'76.92',	'78.97',	'77.51',
	 '77.72',	'77.63',	'74.43',	'79.01',	'82.63',
	 '83.27',	'80.28',	'81.63',	'80.22',	'80.04',
	 '79.81',	'79.98',	'78.82',	'77.92',	'75.00',
	 '74.62',	'74.47',	'74.13',	'72.99',	'73.46',
	 '73.95',	'72.82',	'72.78',	'73.38',	'73.64',
	 '73.43',	'74.92',	'74.06',	'74.48',	'73.89',
	 '73.88',	'71.82',	'69.57',	'69.98',	'69.77',
	 '70.02',	'70.29',	'70.48',	'70.68',	'69.07',
	 '68.11',	'67.87',	'66.49',	'65.42',	'65.58',
	 '65.96',	'67.08',	'67.05',	'67.17',	'67.65',
	 '67.48',	'67.88',	'68.43',	'68.82',	'68.42',
	 '66.40',	'65.70',	'64.58',	'65.34',	'67.64',
	 '65.94',	'67.43',	'69.45',	'70.49',	'69.64',
	 '69.58',	'71.74',	'72.02',	'72.23',	'73.53',
	 '73.50',	'73.20',	'72.03',	'72.52',	'72.48',
	 '71.83',	'71.50',	'70.43',	'69.63',	'69.55',
	 '69.68',	'69.45',	'69.05',	'68.96',	'67.25',
	 '66.74',	'66.56',	'66.88',	'67.07',	'66.85',
	 '66.79',	'65.86',	'66.12',	'66.38',	'66.19',
 	 '65.04',	'64.41',	'65.29',	'65.08',	'64.94',
	 '64.07',	'64.46',	'65.41',	'64.32',	'63.06',
	 '62.78',	'62.24',	'62.38',	'62.45',	'62.25',
	 '62.40',	'62.36',	'62.53',	'62.45',	'62.57',
	 '61.81',	'63.08',	'62.55',	'62.28',	'62.73',
	 '63.41',	'63.12',	'62.53',	'62.78',	'62.34',
	 '61.90',	'60.16',	'59.57',	'58.93',	'57.92',
	 '57.14',	'57.27',	'57.49',	'57.74',	'57.14',
	 '56.86',	'56.52',	'56.57',	'56.92',	'56.90',
	 '56.54',	'57.02',	'56.49',	'56.40',	'56.90',
	 '56.69',	'56.31',	'56.27',	'56.54',	'55.77',
	 '55.78',	'55.65',	'55.81',	'55.01',	'54.89',
	 '54.70',	'54.33',	'53.73',	'53.12',	'53.33',
	 '54.08',	'54.48',	'53.84',	'53.70',	'53.10',
	 '52.56',	'53.65',	'54.32',	'52.86',	'52.54',
	 '52.52',	'52.97',	'52.20',	'51.54',	'50.38',
	 '49.96',	'50.10',	'50.54',	'50.89',	'52.06',
	 '52.36',	'52.69',	'52.34',	'53.04',	'54.69',
	 '55.06',	'55.70',	'56.45',	'56.26',	'56.69',
	 '56.81',	'56.20',	'56.20',	'56.46',	'56.61',
	 '56.64',	'55.87',	'55.57',	'55.83',	'55.71',
	 '54.84',	'54.49',	'54.05',	'53.88',	'54.80',
	 '54.57',	'54.51',	'54.15',	'53.52',	'53.07',
	 '53.36',	'52.61',	'53.02',	'52.86',	'52.35',
	 '52.06',	'51.65',	'52.12',	'52.995',	'53.81',
	 '54.37',	'53.77',	'53.33',	'54.90',	'55.05',
	 '55.20',	'54.97',	'53.96',	'53.17',	'53.16',
	 '53.16',	'53.13',	'53.57']

clf2 = clf2.fit(O, H)

clf3 = tree.DecisionTreeClassifier()

L = ['72.56',	'72.23',    '73.30',	'73.71',	'73.25',
	 '73.27',	'75.08',	'74.44',	'75.22',	'76.84',
	 '78.03',	'78.35',	'78.76',	'79.73',	'81.55',
	 '79.00',	'79.03',	'77.96',	'76.53',	'75.93',
	 '77.55',	'77.21',	'78.25',	'78.59',	'79.10',
	 '77.24',	'75.93',	'76.72',	'77.52',	'76.99',
	 '76.62',	'75.84',	'74.28',	'76.46',	'76.09',
	 '74.52',	'72.94',	'70.46',	'74.10',	'81.31',
	 '79.96',	'78.18',	'79.12',	'78.88',	'79.14',
	 '78.21',	'78.51',	'76.60',	'74.78',	'73.97',
	 '73.42',	'73.41',	'72.86',	'71.65',	'71.53',
	 '72.73',	'70.31',	'71.38',	'70.84',	'72.13',
	 '71.59',	'72.40',	'72.08',	'71.17',	'72.11',
	 '71.71',	'69.44',	'68.72',	'68.50',	'67.45',
	 '69.15',	'68.76',	'69.17',	'69.43',	'67.39',
	 '66.68',	'66.23',	'64.60',	'64.10',	'64.14',
	 '64.05',	'65.59',	'66.06',	'65.76',	'66.41',
	 '66.13',	'65.83',	'66.98',	'66.88',	'65.18',
	 '64.29',	'64.02',	'61.46',	'62.77',	'64.94',
	 '62.26',	'63.23',	'66.81',	'67.12',	'68.21',
	 '67.81',	'69.97',	'71.19',	'71.01',	'71.29',
	 '72.64',	'71.72',	'71.09',	'71.16',	'70.92',
	 '70.61',	'70.47',	'69.35',	'68.45',	'68.91',
	 '69.01',	'68.51',	'68.40',	'67.41',	'65.98',
	 '65.96',	'66.16',	'66.36',	'66.41',	'66.22',
	 '65.42',	'64.76',	'64.68',	'65.73',	'64.70',
	 '64.06',	'63.80',	'64.27',	'64.33',	'63.95',
	 '63.00',	'63.27',	'63.15',	'62.61',	'61.59',
	 '61.44',	'60.95',	'61.65',	'61.60',	'61.58',
	 '61.26',	'61.80',	'61.75',	'61.64',	'61.15',
	 '60.10',	'61.95',	'61.71',	'61.61',	'60.90',
	 '62.56',	'62.14',	'62.10',	'61.90',	'60.87',
	 '60.07',	'58.83',	'58.25',	'57.40',	'55.87',
	 '55.89',	'56.54',	'56.26',	'57.15',	'56.17',
	 '56.40',	'55.73',	'55.68',	'56.29',	'55.80',
	 '56.14',	'56.18',	'56.04',	'55.71',	'56.14',
	 '55.90',	'55.25',	'55.53',	'55.28',	'55.15',
	 '54.61',	'55.07',	'54.98',	'54.13',	'54.26',
	 '54.03',	'53.38',	'52.93',	'52.26',	'52.31',
	 '52.70',	'53.58',	'52.59',	'52.52',	'52.34',
	 '51.49',	'50.52',	'52.50',	'52.00',	'51.37',
	 '51.12',	'52.03',	'51.36',	'50.19',	'49.33',
	 '49.30',	'49.45',	'49.43',	'49.68',	'50.91',
	 '51.76',	'52.06',	'51.69',	'52.13',	'52.83',
	 '54.31',	'54.85',	'55.66',	'55.75',	'56.06',
	 '55.90',	'55.02',	'54.93',	'53.51',	'55.64',
	 '55.95',	'55.33',	'54.84',	'54.81',	'54.74',
	 '54.22',	'53.61',	'53.60',	'53.22',	'53.72',
	 '53.83',	'53.91',	'52.68',	'52.62',	'52.23',
	 '52.62',	'51.70',	'51.72',	'51.85',	'51.08',
	 '51.25',	'50.74',	'51.09',	'51.18',	'52.47',
	 '53.81',	'53.01',	'52.75',	'53.29',	'54.34',
	 '53.85',	'53.46',	'52.86',	'52.47',	'52.42',
	 '52.44',	'52.44',	'52.38']

clf3 = clf3.fit(O, L)

window.mainloop()
