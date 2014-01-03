# import glob
# #http://matplotlib.org/downloads.html
import matplotlib.pyplot as plt
# from sklearn import manifold
# from sklearn.metrics import euclidean_distances


file1 = open("ds_features/ds1_features.txt", "r")

result_arr = []
for line in file1:
    current_arr = []
    for val in line.split("  "):
        val = val.replace("\r", "")
        val = val.replace("\n", "")
        current_arr.append(val)
    result_arr.append(current_arr)

z=[]

for arr in result_arr:
    for x in arr:
        try:
            plt.scatter( float(x), 10 )
        except ValueError:
            x = x


plt.show()