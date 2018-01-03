import numpy as np
import pickle
import data
from sklearn.preprocessing import LabelEncoder

dataset = data.gen()

# for i in range(0, 195102):
#     try:
#         word = chr(i)
#         dataset.append(word)
#     except:
#         pass

encoder = LabelEncoder()
encoder.fit(dataset)

# 保存Model(注:save文件夹要预先建立，否则会报错)
with open('label.pickle', 'wb') as f:
    pickle.dump(encoder, f)

print('目前收錄: ' + str(len(dataset)) + '個字')
