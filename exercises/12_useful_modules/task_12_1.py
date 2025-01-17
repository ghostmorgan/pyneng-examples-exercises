# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess

ip_list = ['8.8.8.8', '4.4.4.4']

def ping_ip_addresses(ip_list):
    reachable = []
    unreachable = []
    for ip in ip_list:
        result = subprocess.run(['ping', '-n', '1', ip], stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)
    return (reachable, unreachable)


if __name__ == "__main__":
    print(ping_ip_addresses(ip_list))
