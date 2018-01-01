import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

dataset = []

dataset.extend(('\\n', '\\t', '\\r', '　'))

for i in range(19968, 40870):  # Unicode中文字範圍為19968~40869
    chinese = chr(i)
    dataset.append(chinese)

for i in range(12032, 12256):  # Unicode康熙部首範圍為12032~12255
    radical = chr(i)
    dataset.append(radical)

for i in range(65281, 65378):  # Unicode常用半形全形字符範圍為65281~65377
    word = chr(i)
    dataset.append(word)

for i in range(12289, 12352):  # Unicode中日韓符號和標點(CJK Symbol)範圍為12289~12351
    word = chr(i)
    dataset.append(word)

encoder = LabelEncoder()
encoder.fit(dataset)

# 保存Model(注:save文件夹要预先建立，否则会报错)
with open('label.pickle', 'wb') as f:
    pickle.dump(encoder, f)

print('目前收錄: ' + str(len(dataset)) + '個字')
