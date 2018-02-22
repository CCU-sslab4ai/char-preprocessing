def gen():
    dataset = []

    dataset.extend(('\\n', '\\t', '\\r', '　', ' ', '0', '1', '2', '3', '4',
                    '5', '6', '7', '8', '9', '…', '︰', '⋯', '□', '○', '\\ue832'))  # 加入特殊符號

    for i in range(33, 256):  # 標點符號範圍為33-255
        word = chr(i)
        dataset.append(word)

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

    for i in range(12549, 12590):  # Unicode標點符號範圍為12549~12589
        word = chr(i)
        dataset.append(word)

    for i in range(8208, 8224):  # Unicode雙引號單引號
        word = chr(i)
        dataset.append(word)

    return dataset
