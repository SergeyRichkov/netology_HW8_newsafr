import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
print(root.tag)


news_list = root.findall("channel/item/description")
text_list = []
for news in news_list:
    text_list.extend(news.text.split(" "))



dict_of_lenght = {0:[]}                 #{словарь длина: слова такой длины}
for element in text_list:
    if len(element) in dict_of_lenght.keys():
        dict_of_lenght[len(element)].append(element)
    else:
        dict_of_lenght.update({len(element):[element]})



for key in range(7):                #удалить слова короче 6 символов
    del dict_of_lenght[key]


word_list_more_than = []                # один список со словами, длиннее 6 символов
for value in dict_of_lenght.values():
    word_list_more_than.extend(value)
word_list_more_than.sort()              # сортирует список по алфавиту
                                        #чтобы при равном количестве вхождений в список
                                        #слова выдавались в алфавитном порядке


#привести слова к нижнему регистру
word_list_more_than_lower = list(i.lower() for i in word_list_more_than)




for nn in range(10):
    count = 0
    final =[]
    for each in word_list_more_than_lower:
        each
        if word_list_more_than_lower.count(each) > count:
            count = word_list_more_than_lower.count(each)
            a = each      
    final.append(a)
    for k in range(count):
        word_list_more_than_lower.remove(a)
    print(a, count)


    
################
################with open("newsafr.json", encoding = "utf-8") as f:
################    data = json.load(f)
################    news_list = data["rss"]["channel"]["items"]
################    
################word_list = []    
################for description in news_list:
################    word_list.extend(description["description"].split(" "))
################
################
################dict_of_lenght = {0:[]}                 #{словарь длина: слова такой длины}
################for element in word_list:
################    if len(element) in dict_of_lenght.keys():
################        dict_of_lenght[len(element)].append(element)
################    else:
################        dict_of_lenght.update({len(element):[element]})
################
################
################
################for key in range(7):                #удалить слова короче 6 символов
################    del dict_of_lenght[key]
################
################
################word_list_more_than = []                # один список со словами, длиннее 6 символов
################for value in dict_of_lenght.values():
################    word_list_more_than.extend(value)
################word_list_more_than.sort()              # сортирует список по алфавиту
################                                        #чтобы при равном количестве вхождений в список
################                                        #слова выдавались в алфавитном порядке
################
################
#################привести слова к нижнему регистру
################word_list_more_than_lower = list(i.lower() for i in word_list_more_than)
################
################
################
################
################
################
################with open('word_list_moreSORTED.txt', 'w') as f:
################    json.dump(word_list_more_than_lower, f, ensure_ascii=False, indent=4)
################for nn in range(10):
################    count = 0
################    final =[]
################    for each in word_list_more_than_lower:
################        each
################        if word_list_more_than_lower.count(each) > count:
################            count = word_list_more_than_lower.count(each)
################            a = each      
################    final.append(a)
################    for k in range(count):
################        word_list_more_than_lower.remove(a)
################    print(a, count)
################
################with open('word_list_more6-туристов.txt', 'w') as f:
################    json.dump(word_list_more_than_lower, f, ensure_ascii=False, indent=4)  
################

      



    

    
