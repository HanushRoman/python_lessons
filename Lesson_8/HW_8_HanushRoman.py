# Task1
# bytes_value = b'r\xc3\xa9sum\xc3\xa9'
# decoding_string = bytes_value.decode(encoding='utf-8')
# print(decoding_string)
# encoding_string = decoding_string.encode(encoding='Latin1')
# print(encoding_string)
# string_decode = encoding_string.decode(encoding='Latin1')
# print(string_decode)

# Task2
# string1 = 'hello'
# string2 = 'world'
# string3 = 'cod'
# string4 = 'time'
# with open('hw8task2.txt', 'w') as file:
#     file.write(string1)
#     file.write(f'\n{string2}')
#     file.close()
# with open('hw8task2.txt', 'a') as file:
#     file.seek(0, 0)
#     file.write(f'\n{string3}')
#     file.write(f'\n{string4}')


#Task_4
import json
import csv
import random


with open('hw8.json', 'r') as json_file:
    data = json.load(json_file) # загрузил данные из json файла
print(data)

with open('data.csv', 'w', newline='') as csv_file:
    writter = csv.writer(csv_file)
    writter.writerow(['id', 'name', 'age', 'phone'])
for item in data:
            writter.writerow([item, data[item][0], data[item][1], random.randint(1,10)])

# Решит проблемму со словарем, код не работает