import pickle

test = ['我', '愛', '高']
integer_encode = None

with open('label.pickle', 'rb') as f:
    label = pickle.load(f)
    print(label.transform(test))
    integer_encode = label.transform(test)

with open('onehot.pickle', 'rb') as f:
    label = pickle.load(f)
    output=label.transform(integer_encode.reshape(len(integer_encode), 1))
    print(output)
    print('WORD DIM: '+str(output.shape))
