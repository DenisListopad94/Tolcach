# Exercise 1

# class Exercise1:
#     VALUE_1 = 1
#     VALUE_2 = 10
#
#     def info(self):
#         print(self.VALUE_1, self.VALUE_2)
#
#     def change(self):
#         self.VALUE_1 += 5
#         self.VALUE_2 += 15
#         print(self.VALUE_1, self.VALUE_2)
#
#     def summ(self):
#         summ = self.VALUE_1 + self.VALUE_2
#         print(summ)
#
#     def max(self):
#         print(max(self.VALUE_1, self.VALUE_2))
#
#
# value = Exercise1()
# value.info()
# value.change()
# value.summ()
# value.max()

# Exercise

# class Counter:
#     def __init__(self, count):
#         self.count = count
#
#     def decrease(self):
#         if self.count > 0:
#             self.count -= 1
#
#     def increase(self):
#         if self.count < 9:
#             self.count += 1
#
#     def info(self):
#         print(self.count)
#
#
# value = Counter(count=5)
# value.info()
# value.increase()
# value.info()
# value.decrease()
# value.info()

# Exercise 3

# class Shop:
#     SHOP = dict()
#
#     def __init__(self, name, quality, price):
#         self.name = name
#         self.quality = quality
#         self.price = price
#
#     def add_product(self):
#         Shop.SHOP.update([(self.name, {'quality': self.quality, 'price': self.price})])
#
#     def del_product(self):
#         Shop.SHOP.pop(self.name)
#
#     def search(self):
#         print(f'Product {self.name}: {Shop.SHOP.get(self.name)}')
#
#
# hoodie = Shop('hoodie', 8, 120)
# trousers = Shop('trousers', 10, 80)
# hoodie.add_product()
# trousers.add_product()
# trousers.search()
# hoodie.search()
# trousers.del_product()
# print(Shop.SHOP)

# Exercise 4
# class MoneyBox:
#     CAPACITY = 100
#
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#     def info_money(self):
#         print(f'монет в копилке {self.capacity}')
#
#     def money_add(self, value):
#         if (self.capacity + value) < MoneyBox.CAPACITY:
#             self.capacity += value
#         else:
#             add = MoneyBox.CAPACITY - self.capacity
#             print(f'В копилку можно добавить {add} монет')
#
#     def info_money_add(self):
#         add = MoneyBox.CAPACITY - self.capacity
#         print(f'В копилку можно добавить {add} монет')
#
#
# piggy = MoneyBox(20)
# piggy.info_money()
# piggy.money_add(81)
# piggy.money_add(35)
# piggy.info_money_add()
# piggy.info_money()

# Дополнительные задачи
# Exercise 1
# class Shop:
#     SHOP = {
#         'hoodie': {'quality': 4, 'price': 100},
#         'trousers': {'quality': 8, 'price': 80},
#         'jacket': {'quality': 4, 'price': 195}
#     }
#
#     def __init__(self, name, quality, price):
#         self.name = name
#         self.quality = quality
#         self.price = price
#
#
# class Client:
#     def application(self, name):
#         self.name = name
#         Shop.SHOP.get(self.name)
#         if Shop.SHOP.get(self.name):
#             print(f'Customer pays for goods {self.name}')
#         else:
#             print('The merchandiser makes a request to the warehouse')
#
#
# class Merchandiser(Shop, Client):
#     def add_product(self):
#         Shop.SHOP.update([(self.name, {'quality': self.quality, 'price': self.price})])
#         print(f'Product {self.name} added ')
#
#
# slippers = Merchandiser('slippers', 20, 10)
# slippers.add_product()
# anna = Client()
# anna.application('jacket')
# anna.application('singlet')

# Exercise 2
# class Faculty:
#     def __init__(self, name, physics, chemistry, biology):
#         self.name = name
#         self.physics = physics
#         self.chemistry = chemistry
#         self.biology = biology
#
#     def system_faculty(self):
#         average_mark = (self.physics + self.chemistry + self.biology)/3
#         if average_mark < 8:
#             print(f'{self.name} ваш средний бал равен {average_mark} и поэтому вы не поступили на факультет, сожалеем')
#         else:
#             print(f'{self.name} ваш средний бал равен {average_mark} и поэтому вы поступили на факультет, поздравляем')
#
#
# Vova = Faculty('Vova', 8, 7, 10)
# Vova.system_faculty()

