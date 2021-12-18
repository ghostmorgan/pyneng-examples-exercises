# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

template = """
    Prefix                {0:<15}
    AD/Metric             {1:<15}
    Next-Hop              {2:<15}
    Last update           {3:<15}
    Outbound Interface    {4:<15}
"""

with open('ospf.txt', 'r') as f:
    for line in f:
        ospf = line.split()
        prefix, ad, next_hop, update, out_intf = ospf[1], ospf[2].strip('[]'), ospf[4].strip(','), ospf[5].strip(','), ospf[6]
        print(template.format(prefix, ad, next_hop, update, out_intf))
