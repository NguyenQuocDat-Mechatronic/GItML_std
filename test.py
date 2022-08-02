# import numpy as np
# # a =np.array([-5,3])
# b =np.array([[1,1],[2,2]])
# # print(b)
# # A_inv = np.linalg.pinv(b)
# # print(A_inv)
# # print(b.dot(A_inv))
# # print(np.linalg.det(b))
# e = np.array([[0,-1],[1,0]])
# # print(e)
# c = b.dot(e)
# print(c)
# # # print(c)
# # # d = np.flip(a,axis=)
# # # d1 = a.dot(e)
# # # print(d)
# # # print(d1)
# # import torch
# import numpy as np
# #
# A = np.array([[1, 2, 3],
#               [3, 2, 1],
#               [4, 2, 2]])
# A = np.array([[1,1,1],[3,2,1],[2,1,2]])
# B = np.array([15,28,23])
# #
# A_inv = np.linalg.inv(A)
# print(A_inv.dot(B))
# # print(np.linalg.det(A)*np.linalg.det(A_inv))
# # print(A_inv)
# #
# #
# # import torch
# #
# # A = torch.tensor([[1, 2, 3],
# #               [3, 2, 1],
# #               [4, 2, 2]], dtype=torch.float32)
# #
# # A_inv = torch.linalg.pinv(A)
# # print(A_inv)
# # import tensorflow as ts
# import numpy as np
# A = np.array([1,1])
# B = np.array([[-1,0],[0,1]])
# C = A.dot(B)
# # print(C)

x = 'A'

# if(ord(x) >= 48 and ord(x) <= 57):
#     print("It is a Number")
# else:
#     print("It is Not a Number")

if(ord(x) < 48 or ord(x) > 57):
    print("It is a not Number")
else:
    print("It is  a Number")