# # CSV
# import csv
# with open('1.csv', encoding='utf-8') as f:
#     reader = csv.reader(f) # читает только одну строку, поэтому запускаем цикл
#     count = 0
    # for row in reader:
    #     print(row)
    #     count += 1
#     new_list = list(reader)
# header = new_list.pop(0)
# for news in new_list:
#     print(news[-1])
# # print( count-1)
# print(len(new_list))

# with open('1.csv', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     count = 0
#     for row in reader:
#         row['title']
#         count += 1
#         # print(type(row))
#         print(row)
# print(count)
# # Запись в файл, writerow(s) работает со списками
# with open('new1.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\\')
#     writer.writerow(header)
#     writer.writerows(new_list)
# # Может быть что читать инф-цию нужно с разных файлов, с разными символами/разделителями
# # постоянно параметры задавать/перечислять проблематично. Для этогонабор настроек перенести в переменную
# csv.register_dialect('name', delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\\')
# # Затем в open, write вписываем 'name'
# writer = csv.writer(f, 'name')

# # JSON

# import json

# with open('1.json', encoding='utf-8') as f:
#     json_data = json.load(f)
# news_list = json_data['rss']['channel']['items']
# # print(news_list[0])
# # for news in news_list:
# #     print(news['title'])
# with open('new1.json', 'w', encoding='utf-8') as f:
#     json_data = json.dump(json_data, f, ensure_ascii=False, indent=4)# для записи файла кирилицей ensure_ascii=False, но и без этого кодировка будет читаться кодом
# # # Сохранит всё в одну строку, пайтону нет разницы, если хотим красиво чисто для читаемости
# # # добавляем параметр indent
# # # не поддерживает 'a' обрабатывается целиком

# # XML
from lib2to3.pgen2.token import NEWLINE
from logging import root
from textwrap import indent
import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding='utf-8') 
tree = ET.parse('1.xml', parser)
root = tree.getroot()
# print(root.tag)
# print(root.text)
# print(root.attrib)
# news_list = root.find('channel/item')
# print(type(news_list))
# news_list = root.findall('channel/item')
# print(type(news_list))
# for news in news_list:
#     print(news.find('title').text)

titles_list = root.findall('channel/item/title')
for title in titles_list:
    print(title.text)

tree.write('new1.xml', encoding='utf-8')
from xml.dom import minidom
xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent='   ')
with open('new1.xml', 'w', NEWLINE='', encoding='utf-8') as f:
    f.write(xmlstr)
