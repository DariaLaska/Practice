from main import *

print(main('--f_name1=vasya@pukin.ru'))
print(main('--customer=John Smith --дата_заказа=27.05.2025'))
print(main('--customer=John Smith --дата_заказа=27.05.2025 --number=+7999 999 98 80'))
print(main('--f_name1=text --f_name2=data'))
print(main('--f_name1=aaa@bbb.ru --f_name2=27.05.2025')) #
print(main('--f_name1=27.05.2025 --f_name2=+7 903 123 45 78'))
print(main('--f_name1=2025-05-25 --f_name2=+7 903 123 45 78'))
print(main('--tumba=27.05.2025 --yumba=+7 903 123 45 78'))
print(main('--order_id=5 --contact=+7 999 999 99 99'))
print(main('--дата_заказа=1990-08-09'))

