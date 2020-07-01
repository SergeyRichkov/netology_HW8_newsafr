import json

def json_load():
    file_name= input('Введите имя файла:\n')
    with open(file_name, encoding = "utf-8") as f:
        data = json.load(f)
        news_list = data["rss"]["channel"]["items"]
    def print_news():
        print(news_list)
        return
    input_dict = {'n': print_news, 'c': convet_text_to_list}
    choose = input("Вывести все новости c заголовками и ссылками - нажмите 'n',"
                   "продолжить работу с данными - нажмите 'c':\n")
    input_dict[choose]()
    return news_list
    
def xml_load():
    pass


def convet_text_to_list(): 
    word_list = []    
    for description in json_load():
        word_list.extend(description["description"].split(" "))
    return word_list


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
    j = sorted(list(set(word_list_more_than_lower)),
        key=lambda x: (x[0], [-ord(c) for c in x[1]]), reverse = True)
    print('10 самых часто встречающихся в новостях слов длиннее 6 символов:')
    for m in range(10):
        print(j[m])
    return

    
####    
####with open('word_list_moreTUPLE.txt', 'w') as f:
####    json.dump(j, f, ensure_ascii=False, indent=4)
####


def choose_most_used():
    input_dict = {'j': json_load, 'x': xml_load }
    file_type = input('Выберите тип обрабатываемого файла. j - .json, x - .xml:\n')
    return input_dict[file_type]()

choose_most_used()


print(convet_text_to_list())

     
      



    

    
