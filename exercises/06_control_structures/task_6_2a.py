# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_address = input("Введите IP-адрес в формате 10.0.1.1: ")

# проверка корректности адреса

ip_list = ip_address.split('.')

if len(ip_list) == 4:
   for oct in ip_list:
      if oct.isdigit() and int(oct) in range(256):
         continue
      else:
         print("Неправильный IP-адрес")
         break
   else:
      if ip_address == '255.255.255.255':
         print("local broadcast")
      elif ip_address == '0.0.0.0':
         print("unassigned")
      elif int(ip_address.split('.')[0]) in range(1, 224):
         print("unicast")
      elif int(ip_address.split('.')[0]) in range(224, 240):
         print("multicast")
      else:
         print("unused")
else:
   print("Неправильный IP-адрес")

