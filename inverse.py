import numpy as np

data = np.array([[0,0],[0,0]])
for i in range(2):
    for j in range(2):
        data[i][j] = input(f"plese input {i+1}:{j+1} = ")

mod = int(input("pls input mod = "))

#--- 行列式計算 ---#
det = np.linalg.det(data)
det_inv = int(det % mod) #modかける


#--- ひっくり返す(いい感じじゃない) ---#
tmp = data[0][0]
data[0][0] = data[1][1]
data[1][1] = tmp

tmp = data[0][1]
data[0][1] = data[1][0]*(-1)
data[1][0] = tmp*(-1)

data_inv = np.dot(data, det_inv) % mod

print(data)
print(det_inv)

print(data_inv)