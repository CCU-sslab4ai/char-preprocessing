import pickle
import data
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
# define example
dataset = data.gen()

# for i in range(0, 195102):
#     try:
#         word = chr(i)
#         dataset.append(word)
#     except:
#         pass

# integer encode
label_encoder = None
with open('label.pickle', 'rb') as f:
    label_encoder = pickle.load(f)
integer_encoded = label_encoder.fit_transform(dataset)
print(integer_encoded)
# binary encode
onehot_encoder = OneHotEncoder()
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoder.fit(integer_encoded)

with open('onehot.pickle', 'wb') as f:
    pickle.dump(onehot_encoder, f)

print('目前收錄: ' + str(len(dataset)) + '個字')
