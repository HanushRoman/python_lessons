# with open('lhello.txt') as file:
#     first_5_symbols = file.read(5)
#     print(first_5_symbols)
    # file.seek(0, 0)
    # line = file.readline()
    # print(line)
    # lines = file.readlines()
    # print(lines)
    # for line in file:
    #     print(line, end='')

#
# with open('lhello2.txt', 'r') as file:
#     lines = file.readlines()


# lines[0] = 'some new line\n'
# with open('lhello2.txt', 'w') as file:
#     file.writelines(lines)

# string = 'привет'
# encode_string = string.encode(encoding='utf-8')
# print(encode_string)

# with open('lhello3.txt') as file:
#     file_text = file.read()
#     print(file_text)
#
# cp1251_string = file_text.encode(encoding='cp1251')
#
# with open('not_utf.txt', 'wb') as file:
#     file.write(cp1251_string)

# import json
#
# with open('hw8.json') as json_file:
#     json_date = json.load(json_file)
#     print(json_date)
#
#
# json_date["12345678"] = "Anna"
#
#
# with open('new_json.json', 'w') as json_file:
#     json.dump(json_date, json_file, indent=4)

import  csv
import json
#
# with open('exemple.csv') as file:
#     csv_reader = csv.reader(file)
#     index = 0
#     date = []
#     json_date = []
#     for index, line in enumerate(csv_reader):
#         if index == 0:
#             column_names = line
#             continue
#
#         line_objects = {}
#         for column_name, value in zip(column_names,line):
#             line_objects[column_name] = value
#             json_date.append((line_objects))
#
#
#
#
# print(json_date)
#
#
# with open ('csv_to_json.json', 'w') as json_file:
# #     json.dump(json_date, json_file
# text_ = """ Вечерело
# жужали мухи
# как дела дед мороз
# что ты сделал в своей жизни"""
# # with open('article.txt', 'w') as file:
# #     file.write(text_)
#
# def read(file_name: str) -> list:
#     with open(file_name, 'r') as file:
#         words = file.read().split()
#         # print(words)
#         max_word_len = len(words[0])
#         for word in words[1:]:
#             if max_word_len < len(word):
#                 max_word = len(word)
#         result_filter = list(filter(lambda slovo: len(slovo) == max_word_len, words))
#
#
#         return result_filter
#
# print(read('article.txt'))

import  openpyxl



