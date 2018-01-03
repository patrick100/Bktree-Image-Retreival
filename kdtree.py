#from scipy import spatial
#import numpy as np

#x, y = np.mgrid[0:4, 0:4]
#points = zip(x.ravel(), y.ravel())
#tree = spatial.KDTree(points)
#tree.query_ball_point([2, 0], 1)


import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial import KDTree
import cv2
import os
                                                                             
limite = 10


folder = "NewData/"
lista = [];
lista_label = [];

#print(os.listdir("C:/Users/patrickdz96/Desktop/EDA PROYECTO FINAL/image/dataset"))


for name in os.listdir(folder):
	print(name)
	im = cv2.imread(folder+name)
	# calculate mean value from RGB channels and flatten to 1D array
	vals = im.mean(axis=2).flatten()
	counts, bins = np.histogram(vals, range(257))

	lista.append(counts)
	lista_label.append(name)
    #os.rename(name,folder+str(i))
    

#for i in range(1):
#    lista.append([0] * 257)


#print(lista)

#print(len(bins))
#print(bins)

# plot histogram centered on values 0..255
#plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
#plt.xlim([-0.5, 255.5])
#plt.show()

#print(lista)

#pts = np.array([(1, 1, 1,1), (1,2, 4,2), (2,1,3,0), (3,4, 4,0), (4,1, 4,0)])

pts = np.array(lista)

T = KDTree(pts)


im = cv2.imread('prueba3.png')
# calculate mean value from RGB channels and flatten to 1D array
vals = im.mean(axis=2).flatten()
counts, bins = np.histogram(vals, range(257))


idx = T.query_ball_point(counts,r=10000)
print (idx)



#for name in os.listdir(folder):
#	print(name)
x=0

for name in idx:
	if(x<limite):
		result = cv2.imread(folder+lista_label[name])

		cv2.imshow("Result", result )
		cv2.waitKey(0)
		#img = Image.open(str(name))
		#img.show() 
		x+=1
	else:
		break	


#print(T.query(counts))


#print("IMPRIMIENDO LA DATA")
#print(T.data)

#distance, index = T.query(counts)

#print("LA DISTANCIA ES:")

#print(distance)

#print("LA POSICION ES:")

#print(index)

#print(T)
#idx = T.query_ball_point([1,1,0,0],r=4)
#print (pts[idx])
