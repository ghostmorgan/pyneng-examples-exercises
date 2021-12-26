# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент
вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое
файла в строку, а затем передать строку как аргумент функции (как передать вывод
команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем.
То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция должна
работать и на других файлах (тест проверяет работу функции на выводе
из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
    вместо имени файла, мы делаем функцию более универсальной: она может работать
    и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """    
    list_config = list(filter(None, command_output.strip().split('\n'))) #формирование списка строк из строки вывода команды show cdp neighbors (удаляет переносы и пустые строки) 
    
    list_devices = cdp_list(list_config)
    dict_devices = cdp_dict(list_devices)
    
    return dict_devices


def cdp_list(list_config):
    """
    Функция формирующая два списка для словаря из списка строк:

    На вход принимает строку - вывод команды show cdp neighbors

    На выходе возвращает список кортежей (device, interface)
        * нечетный элемент - локальное устройство с соответствующим интерфейсом
        * четный элемент - соседнее устройство с соответствующим интерфейсом
    """

    l_keys = []
    l_values = []

    for line in list_config:
        if "show" in line:
            local_device = line.split('>')[0]
        elif num_check(line):
            neighbor = line.strip().split()
            l_keys.append(local_device)
            l_values.append(neighbor[1] + neighbor[2])
            l_keys.append(neighbor[0])
            l_values.append(neighbor[-2] + neighbor[-1])
    
    result_list = list(zip(l_keys, l_values))

    return result_list


def num_check(line):
    """
    Функция проверяющая есть ли в строке хотя бы одна цифра

    На вход принимает строку line:
        * возращает True - если в строке есть хотя бы одна цифра 
        * возращает False - если в строке нет цифр
    """
    return any(char.isdigit() for char in line)


def cdp_dict(list_neighbors):
    """
    Функция формирующая итоговый словарь соседей

    На вход принимает строку список кортежей, в котором:
        * нечетный элемент - локальное устройство с соответствующим интерфейсом
        * четный элемент - соседнее устройство с соответствующим интерфейсом
        
    Возращает словарь кортежей в формате: 
        {("R4", "Fa0/1"): ("R5", "Fa0/1"),
        ("R4", "Fa0/2"): ("R6", "Fa0/0")}
    """
    result_dict = {}

    for position, string in enumerate(list_neighbors):
        if position % 2 == 0:
            key = string
            result_dict[string] = None
        else:
            result_dict[key] = string

    return result_dict


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))
