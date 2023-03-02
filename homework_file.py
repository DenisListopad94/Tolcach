import json
from datetime import date
import datetime

# Exercise 1
with open('test_file.txt', 'r+', encoding='UTF-8') as file:
    text = ''
    for line in file:
        text += line.replace(' \n', '!') + '\n'

print(text)

# Exercise 2
with open('input.txt', 'w', encoding='UTF-8') as file:
    numbers = input('enter numbers:')
    file.write(str(numbers))

product_of_numbers = 1
with open('input.txt', 'r', encoding='UTF-8') as file:
    numbers = (file.read()).split()
    for numb in numbers:
        product_of_numbers *= int(numb)
print(product_of_numbers)

with open('output.txt', 'w', encoding='UTF-8') as file:
    file.write(str(product_of_numbers))

# Exercise 3

shop = [
    {'name': 'perforator', 'quantity': 2, 'price': 200, 'receipt_date': (2023, 2, 15)},
    {'name': 'tron', 'quantity': 1, 'price': 1003500, 'receipt_date': (2023, 2, 20)},
    {'name': 'gsp', 'quantity': 28, 'price': 15, 'receipt_date': (2022, 12, 10)}
]


with open('shop.json', 'w', encoding='UTF-8') as file_json:
    json.dump(shop, file_json)

with open('shop.json', 'r', encoding='UTF-8') as file_json:
    file_shop = json.load(file_json)
    for elem in file_shop:
        year, month, day = elem.get('receipt_date')
        admission = datetime.date(year, month, day)
        if elem.get('price') >= 1000000 or date.today() - admission > datetime.timedelta(60):
            print(elem)

# Exercise 4
count = 0
ind = 0
with open('answers.txt', 'r', encoding='UTF-8') as file_answers:
    answers = (file_answers.read()).split('\n')

with open('questions.txt', 'r', encoding='UTF-8') as file_questions:
    for question in file_questions:
        answer_user = input(question).capitalize()
        if answer_user == answers[ind]:
            count += 1
        ind += 1
print(f'Количество верных ответов {count}')

# Exercise 5
dict1 = {
    12345: ('Alex', 31),
    23456: ('Noy', 40),
    34567: ('Shon', 20),
    45678: ('Jon', 15),
    56789: ('Parker', 35)
}

with open('dict.json', 'w', encoding='UTF-8') as file_dict:
    json.dump(dict1, file_dict)

# Exercise 6
with open('dict.json', 'r', encoding='UTF-8') as file_json:
    dict1 = json.load(file_json)

with open('file_csv.csv', 'w', encoding='UTF-8') as file_csv:
    for elem in dict1:
        name, age = dict1.get(elem)
        file_csv.write('person' + '; ' + str(elem) + '; ' + name + '; ' + str(age) + '; ' + '\n')

