# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
correct_ip = False

while not correct_ip:
    ip_address = input("Введите IP-адрес в формате 10.0.1.1: ") # получаем адрес от пользователя
    ip_list = ip_address.split('.') # получаем список октетов по разделителю "точка"
    correct_ip = True

    if len(ip_list) == 4: # проверка на кол-во октетов
        for oct in ip_list: # цикл для проверки каждого октета условия того, что октет содержит только числа в диапазоне 0-255
            if oct.isdigit() and int(oct) in range(256):
                continue
            else: # иначе выкидываем ошибку на предмет того, что октет содержит не только числа или находится не в диапазоне 0-255 и запрашиваем снова адрес
                print("Неправильный IP-адрес")
                correct_ip = False
                break
    else: # выкидываем ошибку в случае если кол-во октетов больше 4 и запрашиваем снова адрес
        print("Неправильный IP-адрес")
        correct_ip = False
    
# блок на определение типа адреса, выполняется только после получения корректного адреса
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
