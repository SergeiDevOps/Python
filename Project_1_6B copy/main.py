import os
import shutil
import time
#Информация о для создания лог-файла
def file_metadata(file_name):
    stat_info = os.stat(file_name)
    t = time.ctime(stat_info.st_ctime)
    return t
#Создание директории копирования
os.mkdir('sales')
k = '_sales'
k1 = file_metadata('sales') + k
os.mkdir(k1)
os.rename('sales', k1)
#Список файлов для копирования
list_of_the_file = ["1.Brand_sale_Russia.csv",
                    "2.Model_sale_Russia.csv",
                    "3.Brand_sale_USA.csv",
                    "4.Model_sale_USA.csv",
                    "5.Brand_sale_Japan.csv"]
l = list_of_the_file
l1 = []
#Модуль копирования файлов списка и обработки исключений
def get_copy():
    for i in l:
        try:
            e = shutil.copy2(i, k1)
        except Exception as g:
            g = "FileNotExist"
            if g not in l1:
                l1.append(g)
            pass
        if e not in l1:
            l1.append(e)
    return (l1)
s = get_copy()
#Модуль копирования файлов списка и обработки исключений
l3 = "\n".join(l1)
with open("Jornal.csv", "w", encoding="utf-8") as file:
    file.write(l3)