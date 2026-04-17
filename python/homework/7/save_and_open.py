import numpy as np

a=np.arange(0,10,0.5).reshape(4,-1)
np.savetxt("out.txt",a,fmt="%d",delimiter=",")
b=np.loadtxt("out.txt",delimiter=",")
print(b)


#csv文件
a=np.array(range(20)).reshape((4,5))
print(a)

filename = 'a.csv'

np.savetxt(filename,a,fmt="%d",delimiter=',')

b = np.loadtxt(filename,dtype=np.int32,delimiter=',')
print(b)

#npy二进制文件
a=np.array(range(20)).reshape((2,2,5))
print(a)

filename='b.npy'

np.save(filename,a)

b=np.load(filename)
print(b)
print(b.shape)



#npz文件
a=np.array(range(20)).reshape((2,2,5))
b=np.array(range(20,44)).reshape(2,3,4)
print('a',a)
print('b',b)

filename='c.npz'

np.savez(filename,a,b=b)

c=np.load(filename)
print(c.keys())
print(c['arr_0'])
print(c['b'])