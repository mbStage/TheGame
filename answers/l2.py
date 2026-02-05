import numpy as np

ini_li = [0,1]

np_arr = np.array(ini_li)

result = 0
while np_arr[len(np_arr)-1] + np_arr[len(np_arr)-2] < 4000000 :
    if float(np_arr[len(np_arr)-1] + np_arr[len(np_arr)-2]) % 2 == 0:
        result += np_arr[len(np_arr)-1] + np_arr[len(np_arr)-2]
    np_arr = np.append(np_arr,np_arr[len(np_arr)-1] + np_arr[len(np_arr)-2])

print(result)

