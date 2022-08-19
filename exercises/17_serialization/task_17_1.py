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
import re

def write_dhcp_snooping_to_csv(filenames, output):
    
    regex_filename = (r"^[^_]*")                                                                   # регулярка для получения имени устройства из имени файла
    regex_command = (r"(?P<mac>\S+) +(?P<ip>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<interface>\S+)")    # регулярка для получения необходимых данных из команды show dhcp snooping binding
    
    device_dict = {}
    result_list = []

    for file in filenames: 
        # находим с помощью регулярки имя устройства в имени входного файла
        name_of_device = re.search(regex_filename, file)
        if name_of_device:
            device_dict['switch'] = name_of_device.group(0)

        # открываем файл с данными и обновляем список с помощью полученных данных
        with open(file) as dhcp_output:
            for line in dhcp_output:              
                result = re.search(regex_command, line)
                if result:
                    device_dict.update(result.groupdict())
                    result_list.append(device_dict.copy())

    # запись полученных данных в файл csv
    with open(output, "w", newline='') as csv_file:
        fieldnames = list(result_list[0].keys())
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in result_list:
            writer.writerow(row)

if __name__ == "__main__":
    list_of_filenames = ["sw1_dhcp_snooping.txt", "sw2_dhcp_snooping.txt", "sw3_dhcp_snooping.txt"]
    write_dhcp_snooping_to_csv(list_of_filenames, "result_dhcp_snooping.csv")
