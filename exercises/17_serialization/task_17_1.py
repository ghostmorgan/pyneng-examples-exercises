# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""

import csv
from fileinput import filename
from pprint import pprint
import re

list_of_filenames = ["sw1_dhcp_snooping.txt", "sw2_dhcp_snooping.txt", "sw3_dhcp_snooping.txt"]

def write_dhcp_snooping_to_csv(filenames, output):
    
    regex_filename = (r"^[^_]*")                # регулярка для получения имени устройства из имени файла
    regex_output = (r"^([0-9a-fA-F]:?){12}")    # регулярка для получения необходимых данных из вывода команд

    list_filenames = []
    headers = ["switch", "mac", "ip","vlan", "interface"]
    
    # получение списка имён устройств из имён исходных файлов
    for filename in filenames:
        m = re.search(regex_filename, filename)
        if m:
            list_filenames.append(m.group(0))

    #получение данных из исходных данных
    for file in filenames:
        with open(file) as f:
            for line in f:
                res = re.search(regex_output, line)

                if res:
                    print(file + "   ---   " + res.group(0))
    
    # запись полученных данных в файл csv
    with open(output, "w") as f:
        print()
        ###

if __name__ == "__main__":
    write_dhcp_snooping_to_csv(list_of_filenames, "result_dhcp_snooping.csv")
