import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial import KDTree
import cv2
import os
import csv
from colordescriptor import ColorDescriptor
import time






limite = 10


folder = "dataset/"
lista = [];
lista_label = [];

with open('index.csv','r') as f:
	reader = csv.reader(f)
	for row in reader:
		print(row[0])
		features = [float(x) for x in row[1:]]
		lista.append(features)
		lista_label.append(row[0])
		

f.close()


pts = np.array(lista)

T = KDTree(pts)


# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))




X = []
Y = []

folder_consultas = 'consultas/'

lista_consultas = ['103100.png','103300.png','108100.png','115100.png','123600.png','127502.png']


for consulta in lista_consultas:
	X.append(consulta)
	query = cv2.imread(folder_consultas+consulta)
	features = cd.describe(query)	
	
	start_time = time.time()
	idx = T.query_ball_point(features,r=1000)

	
	Y.append(time.time() - start_time)



x=0

for name in idx:
	if(x<limite):
		result = cv2.imread(folder+lista_label[name])

		cv2.imshow("Resultado", result )
		cv2.waitKey(0)
		#img = Image.open(str(name))
		#img.show() 
		x+=1
	else:
		break	



# plot
plt.plot(X,Y)
# beautify the x-labels
plt.gcf().autofmt_xdate()

plt.show()



