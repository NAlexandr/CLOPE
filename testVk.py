# -*- coding: utf-8 -*-

import copy
import CLOPE
import pickle

with open('data/users.pickle', 'rb') as f:
    dataGroups = pickle.load(f)

# Посредствам задания порога countElements, можно выделить первые countElements транзакция из исходного множества данных
dataNew = {}
index = 0
countElements = -1
for item in dataGroups:
    if countElements > 0 and index > countElements:
        break
    dataNew[item] = dataGroups[item]
    index += 1
dataGroups = copy.deepcopy(dataNew)

# Инициализация параметров алгоритма
repulsion = 1.1
noiseLimit = 0
countTransfer = 1000000
stopLimit = 300

# Выполнение алгоритма
print('Start')
clope = CLOPE.CLOPE()
clope.init_clusters(dataGroups, repulsion, noiseLimit)
print("Инициализация завершена. Число кластеров: ", len(clope.clusters))
while countTransfer > stopLimit:
    countTransfer = clope.next_step(dataGroups, repulsion, noiseLimit)
    print("Число перемещений между кластерами", countTransfer, ". Число кластеров: ", len(clope.clusters))

with open('data/CLOPE_users' + '.r=' + str(repulsion) + '.stopLimit=' + str(stopLimit) + '.pickle', 'wb') as f:
    pickle.dump(clope, f)