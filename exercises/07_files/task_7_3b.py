# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac_template = """
{0:<10}{1:<20}{2}
"""
user_vlan = int(input("Enter VLAN number: "))

with open('CAM_table.txt') as cam_table:
    for line in cam_table:
        mac_line = line.split()
        if mac_line and mac_line[0].isdigit() and user_vlan == int(mac_line[0]):
            print(mac_template.format(mac_line[0], mac_line[1], mac_line[3]).lstrip().rstrip())
