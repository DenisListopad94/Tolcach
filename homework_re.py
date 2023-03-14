import re
# Exercise 1
# pattern = r'\w{0,}cat\w{0,}'
# some_str = 'cat catana procat dog cat song'
# cat_str = re.findall(pattern, some_str)
# print(cat_str)

# Exercise 2
# pattern = r'\w{0,}z\w{3}z\w{0,}'
# some_str = 'cat caztanza procat dzog cat szongz'
# cat_str = re.findall(pattern, some_str)
# print(cat_str)

# Exercise 3
# pattern = r'(\(?8\d{2}\)?-?\d{3}-?\d{2}-?\d{2}|\(?9\d{2}\)?-?\d{3}-?\d{2}-?\d{2})'
# some_str = '8922015356 9563256781 5642312347 7531599632 856-456-23-25 (925)-859-85-92 '
# cat_str = re.findall(pattern, some_str)
# print(cat_str)

# Exercise 4
# pattern = r'\b[aeyuio]\w{0,}'
# some_str = 'cat angry caztanza procat every dzog cat szongz yellow'
# cat_str = re.findall(pattern, some_str)
# print(cat_str)

# Exercise 5
# pattern = r'-?\d{1,}'
# some_str = '1cat angry 5 caztanza procat-9 every 8 dzog cat szongz -123 yellow'
# cat_str = re.findall(pattern, some_str)
# print(cat_str)

# Exercise 6
# pattern = r'computer'
# repl = 'human'
# some_str = 'cat human  caztanza procat every human dzog cat szongz yellow human'
# cat_str = re.sub(repl, pattern, some_str)
# print(cat_str)

# Exercise 7
# pattern = r'\d{2}-\d{2}-\d{4}'
# some_str = '1cat angry 5 caztanza 22-12-2023 procat-9 every 8 dzog cat szongz -123 yellow'
# cat_str = re.findall(pattern, some_str)
# print(cat_str)

# Exercise 8
# pattern = r'\w{0,}b\w{0,}'
# some_str = 'cat angry caztbanza procat every dzobg cat szongz yellowb'
# cat_str = re.findall(pattern, some_str)
# print(cat_str)

# Exercise 9

# pattern = r'q'
# some_str = 'cat human  caztanza procat every human dzog cat szongz yellow human' + ' '
# new_str = ''
# for elem in some_str.split():
#     for ind in range(len(elem)):
#         if elem.isdigit() and elem.isalpha() and elem == '_' and elem.count(elem[ind]) > 1:
#             new_elem = re.sub(elem[ind], pattern, elem)
#             elem = new_elem
#             ind += 1
#     new_str += elem + ' '
# print(new_str.rstrip())

