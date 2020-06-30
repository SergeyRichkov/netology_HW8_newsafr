import json


with open("newsafr.json", encoding = "utf-8") as f:
    data = json.load(f)
    news_list = data["rss"]["channel"]["items"]
    
word_list = []    
for description in news_list:
    word_list.extend(description["description"].split(" "))


dict_of_lenght = {0:[]}                 #{словарь длина: слова такой длины}
for element in word_list:
    if len(element) in dict_of_lenght.keys():
        dict_of_lenght[len(element)].append(element)
    else:
        dict_of_lenght.update({len(element):[element]})



for key in range(7):                #удалить слова короче 6 символов
    del dict_of_lenght[key]


word_list_more6 = []                # один список со словами, длиннее 6 символов
for value in dict_of_lenght.values():
    word_list_more6.extend(value)


##with open('word_list_more6.txt', 'w') as f:
##    json.dump(word_list_more6, f, ensure_ascii=False, indent=4)   





for nn in range(10):
    count = 0
    final =[]
    for each in word_list_more6:
        if word_list_more6.count(each) > count:
            count = word_list_more6.count(each)
            a = each      
    final.append(a)
    for k in range(count):
        word_list_more6.remove(a)
    print(a, count)

with open('word_list_more6-туристов.txt', 'w') as f:
    json.dump(word_list_more6, f, ensure_ascii=False, indent=4)  


##print("final", final)
##print("word_list_more6.count(each)", word_list_more6.count(a[-1]))

##for k in range(word_list_more6.count(each)):
##    word_list_more6.remove(each)
##print("осталось:", word_list_more6.count(each))
##print(a)


##
##with open('word_list_more6-туристов.txt', 'w') as f:
##    json.dump(word_list_more6, f, ensure_ascii=False, indent=4)     
##
##    
##


     
      



    

    
