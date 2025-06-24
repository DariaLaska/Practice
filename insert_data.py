from tinydb import TinyDB, Query


db = TinyDB('db.txt')
Data = Query()

db.truncate()
db.insert({"name": "Name", "customer":"text", "дата_заказа":"data"})
db.insert({
  "name": "Проба",
  "f_name1": "email",
  "f_name2": "data"
})
db.insert({
  "name": "Форма заказа",
  "customer": "text",
  "order_id": "text",
  "дата_заказа": "date",
  "contact": "phone"
})

