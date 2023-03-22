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
#Task 3
import json
import csv


my_dict = {
    12345678: ('Sam', 38),
    72345628: ('Roma', 18),
    12395678: ('Dima', 48),
    32345678: ('Din', 33),

}

with open('hw8.json', 'w') as file:
    json.dump(my_dict, file)


#Task_4
import json
import csv
import random


with open('hw8.json', 'r') as json_file:
    data = json.load(json_file)

with open('data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['id', 'name', 'age', 'phone'])
for item in data:
    writer.writerow([item, data[item][0], data[item][1], random.randint(1, 10)])

# Решит проблемму со словарем, код не работает
#