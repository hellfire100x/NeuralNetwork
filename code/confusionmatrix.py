import numpy as np
import matplotlib.pyplot as plt

conf_arr = [[1466,9,13,5,5,12,6,39,33,9], 
            [31,1486,36,47,11,10,3,10,12,14], 
            [45,36,2648,14,40,40,8,28,10,13], 
            [13,19,16,1828,17,29,1,13,20,21], 
            [7,18,28,16,4861,12,40,27,46,44], 
            [15,9,66,29,14,2217,5,20,5,4], 
            [7,3,19,2,65,4,1873,31,9,6],
            [18,14,45,11,34,17,25,3956,5,24], 
            [18,9,10,18,13,6,4,14,1647,5], 
            [19,6,18,11,32,9,13,16,14,2385]]

norm_conf = []
for i in conf_arr:
    a = 0
    tmp_arr = []
    a = sum(i, 0)
    for j in i:
        tmp_arr.append(float(j)/float(a))
    norm_conf.append(tmp_arr)

fig = plt.figure()
plt.clf()
ax = fig.add_subplot(111)
ax.set_aspect(1)
res = ax.imshow(np.array(norm_conf), cmap=plt.cm.jet, 
                interpolation='nearest')

width = len(conf_arr)
height = len(conf_arr[0])

for x in xrange(width):
    for y in xrange(height):
        ax.annotate(str(conf_arr[x][y]), xy=(y, x), 
                    horizontalalignment='center',
                    verticalalignment='center')

cb = fig.colorbar(res)
alphabet = '0123456789'
plt.xticks(range(width), alphabet[:width])
plt.yticks(range(height), alphabet[:height])
plt.savefig('confusion_matrix.png', format='png')
