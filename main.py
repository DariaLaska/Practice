import re
from tinydb import TinyDB, Query

types = {'phone': r'(\+?7 ?)(\d{3})([ ])(\d{3})([ ])(\d{2})([ ])(\d{2})',
         'email': r'\w+@\w+.(ru|com)',
         'data': r'^(([0-2][1-9])|3[0-1]).((0[1-9])|1[1-2]).\d{4}',
         'data ': r'^\d{4}-(0[1-9]|1[1-2])-(([0-2][1-9])|3[0-1])'
         } #also 'text'

db = TinyDB('db.txt')
Data = Query()


def identify_type(info):
    for i in list(types.items()):
        if re.fullmatch(i[1], info):
            return i[0].rstrip()
    return 'text'


def existence(diction):
    exist_list=[]
    for i in list(diction.items()):
        exist_list.extend(db.search(Data[i[0]] == i[1]) )

    string_list = list(map(str, exist_list))

    uniq = list(set(string_list))
    if len(uniq)==1 and len(exist_list)==len(diction):
        first = list(diction.items())[0]
        return db.search(Data[first[0]] == first[1])[0]['name']
    else:
        for j in uniq:
            if string_list.count(j) == len(diction):
                first = list(diction.items())[0]
                return db.search(Data[first[0]] == first[1])[0]['name']

        return diction


def main(input_):
    input_ = input_[2:].split('--') #--customer=John Smith --дата_заказа=27.05.2025

    diction = {}
    for string in input_:
        key, info = string.split('=')
        spicies = identify_type(info.rstrip())
        diction[key]= spicies
    return existence(diction)

print(main(input()))

