# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

main_config = argv[1]
result_config = argv[2]

ignore = ["duplex", "alias", "configuration"]

with open(main_config) as src, open(result_config, 'w') as dst:
    for line in src:
        words = line.split()
        intersection = set(ignore).intersection(words)
        if not line.startswith('!') and not intersection:
            dst.write(line)
