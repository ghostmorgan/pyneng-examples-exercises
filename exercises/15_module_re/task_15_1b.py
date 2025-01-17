# -*- coding: utf-8 -*-
"""
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a
на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них.

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким
образом, чтобы в значении словаря она возвращала список кортежей
для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет
несколько кортежей. Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность
IP-адреса, диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""


import re

def get_ip_from_cfg(filename):
    
    #dict_intf = {}

    with open(filename) as f:
        regex = (r"^interface +(?P<intf>\S+)$"
        r"| ip address " 
        r"+(?P<ip>\d+\.\d+\.\d+\.\d+) "
        r"+(?P<mask>\d+\.\d+\.\d+\.\d+)")

        match = regex.finditer(f.read())

        for m in match:
            result = m.group("intf", "ip", "mask")
            print(result)

    #with open(filename) as f:
    #    for line in f:
    #      m = re.search(regex, line)
    #      if m and not m.group(1) == None:
    #        intf = m.group(1)
    #      elif m:
    #        dict_intf[intf] = m.group(2, 3)
#
    #print(dict_intf)


if __name__ == "__main__":
    get_ip_from_cfg("config_r2.txt")
