import json
# Пример вывода для одной операции:
#14.10.2018 Перевод организации
#Visa Platinum 7000 79** **** 6361 -> Счет **9638
#82771.72 руб.

def json_to_list(json_file):
    with open(json_file, encoding='UTF-8') as file:
        operations_list = json.load(file)
    return operations_list
json_to_list('operations.json')



