import numpy as np

sample_3d =np.array([
    #j=0 j=2
    [[1,2,3],[5,6,7]], #i = 0
    [[11,12,13],[15,16,17]],# i=1
    [[21,22,23],[25,26,27]] #i=2
    #k=0 , 1, 2
])

print(sample_3d)
# print(sample_3d[0,:,:])
# print(sample_3d[:,1,:])
# print(sample_3d[:,:,-1])
# print(sample_3d[0,0,0:2])
print(sample_3d[1:3,1:3,1:3])