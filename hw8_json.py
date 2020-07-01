import json

def json_load(file_name):
    with open(file_name, encoding = "utf-8") as f:
        data = json.load(f)
        news_list = data["rss"]["channel"]["items"]
    return news_list 


def convet_text_to_list():
    file_name= input('Введите имя файла:\n')
    word_list = []    
    for description in json_load(file_name):
        word_list.extend(description["description"].split(" "))
    return word_list 

    
#создать из списка словарь {длина: слова такой длины}
#и удалить все пары, которые описываь слова короче word_len символов

def word_sort(word_len):
    dict_of_lenght = {0:[]}                 
    for element in convet_text_to_list():
        if len(element) in dict_of_lenght.keys():
            dict_of_lenght[len(element)].append(element)
        else:
            dict_of_lenght.update({len(element):[element]})
    for key in range(word_len):                
        del dict_of_lenght[key]
    return dict_of_lenght



# создать один список со словами, длиннее 6 символов и
# отсортировать его по алфавиту чтобы при равном количестве вхождений в список
# слова выдавались в алфавитном порядке
# а также привести все слова к одному регистру

def values_extract():
    word_len = int(input('Введите минимальную длину слов в списке\n'))
    word_list_more_than = []                
    for value in word_sort(word_len).values():
        word_list_more_than.extend(value)            
    word_list_more_than_lower = list((word_list_more_than.count(i), i.lower()) for i in word_list_more_than)
    return word_list_more_than_lower

 

j = sorted(list(set(values_extract())),
           key=lambda x: (x[0], [-ord(c) for c in x[1]]), reverse = True)
print('10 самых часто встречающихся в новостях слов длиннее 6 символов:')
for m in range(10):
    print(j[m])

    
    
with open('word_list_moreTUPLE.txt', 'w') as f:
    json.dump(j, f, ensure_ascii=False, indent=4)

######
########with open('word_list_moreSORTED.txt', 'w') as f:
########    json.dump(word_list_more_than_lower, f, ensure_ascii=False, indent=4)
######
######def choose_most_used(how_many_words):
######    final =[]
######    for numbers in range(how_many_words):
######        count = 0
######        for each in values_extract():
######            if values_extract().count(each) > count:
######                count = values_extract().count(each)
######                a = each
######        final.append((a, count))
######        for k in range(count):
######            values_extract().remove(a)
######    print(final)
######    return

##choose_most_used(2)




     
      



    

    
