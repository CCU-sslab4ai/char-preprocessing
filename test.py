import pickle

test = ['我', '愛', '高', '\\n']

with open('label.pickle', 'rb') as f:
    label = pickle.load(f)
    print(label.transform(test))
