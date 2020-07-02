import json
import xml.etree.ElementTree as ET


def input_file_name():
        file_name = input('Введите имя файла:\n')
        return file_name
  
def file_load():
    input_file_type = input("Выберите формат обрабатываемого файла:"
                        "Обработать json-файл - нажмите 'j',"
                        "обработать xml-файл - нажмите 'x':\n")
   
    if input_file_type == 'j':
        with open(input_file_name(), encoding = "utf-8") as f:
            data = json.load(f)
            news_list = data["rss"]["channel"]["items"]
        return news_list
    
    elif input_file_type == 'x':
        parser = ET.XMLParser(encoding="utf-8")
        tree = ET.parse(input_file_name(), parser)
        root = tree.getroot()
        news_list = root.findall("channel/item/")#description
        print(news_list.text)
##        text_list = []
##        for news in news_list:
##            text_list.extend(news.text.split(" ")) 
        return text_list
        

##def convet_text_to_list(): 
##    description_list = []    
##    for d in file_load():
##        description_list.extend(d["description"].split(" "))
##    return description_list
##
##
##def word_sort():
##    word_len = int(input('Введите минимальную длину слов в итоговом списке\n'))
##    final_list_lenght = int(input('Введите количество слов в итговом списке в итоговом списке\n'))
##    dict_of_lenght = {0:[]}                 
##    for element in convet_text_to_list():
##        if len(element) in dict_of_lenght.keys():
##            dict_of_lenght[len(element)].append(element)
##        else:
##            dict_of_lenght.update({len(element):[element]})
##    for key in range(word_len):                
##        del dict_of_lenght[key]
##
##    print(f'{final_list_lenght} самых часто встречающихся в новостях слов длиннее {word_len-1} символов:')
##    return dict_of_lenght
##
##
##
##def values_extract():
##    word_list_more_than = []                
##    for value in word_sort().values():
##        word_list_more_than.extend(value)            
##    word_list_more_than_lower = list((word_list_more_than.count(i), i.lower()) for i in word_list_more_than)
##    j = sorted(list(set(word_list_more_than_lower)),
##        key=lambda x: (x[0], [-ord(c) for c in x[1]]), reverse = True)    
##    for m in range(10):
##        print(j[m])
##    return
##
##    


print(file_load())





    

    
