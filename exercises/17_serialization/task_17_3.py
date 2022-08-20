# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""

import re

def parse_sh_cdp_neighbors(output):

    # получаем с помощью регулярки имя устройства из вывода команды show cdp neighbor
    regex_local_device = (r"(?P<device_name>.*)[>#]show")
    device_name = re.search(regex_local_device, output).group("device_name")
    
    # получаем с помощью регулярки имя удаленных устройств, локальные интерфейсы и интерфейсы на удаленных устройствах 
    output_dict= {}
    regex_parse = (r"^(?P<remote_device>\S+)\s+(?P<local_intf>\S+ \d+\/\d+).* (?P<remote_intf>\S+ \S+\/\d+)$")
    output_dict[device_name] = {}

    matches = re.finditer(regex_parse, output, re.MULTILINE)
    for match in matches:
        output_dict[device_name].update({match.group('local_intf'): {match.group('remote_device'): match.group('remote_intf')}})
        
    return(output_dict)


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as input_file:
        output = input_file.read()
        parse_sh_cdp_neighbors(output)
