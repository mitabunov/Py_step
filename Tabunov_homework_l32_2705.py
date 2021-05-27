"""
По ссылке дан json файл:
https://drive.google.com/file/d/1cPuIyOusuPryzeY1PjEpynbiSABxgpez/view?usp=sharing

Задача:
Сформировать аналогичный по структуре xml документ. Структура и реализация остаётся
за программистом.

В качестве ответа в личном кабинете выложить файл с кодом, который делает необходимые
преобразования.
"""


import xml.etree.ElementTree as ET

def main():
    root = ET.Element('items')
    
    item_0 = ET.SubElement(root,'id')
    item_1 = ET.SubElement(root,'login')
    item_2 = ET.SubElement(root,'password_hash')
    item_3 = ET.SubElement(root,'token')
#     print(ET.dump(root))
    id_0 = ET.SubElement(item_0,'id')
    id_0.text = '0'
    
    login_0 = ET.SubElement(item_1,'login')
    login_0.text ='matyrka.margarit@rambler.ru'
    
    pass_0 = ET.SubElement(item_2,'password_hash')
    pass_0.text = '3cc849279ba298b587a34cabaeffc5ecb3a044bbf97c516fab7ede9d1af77cfa'
    
    token_0 = ET.SubElement(item_3,'token')
    token_0.text = '12001bdeae6745a699c5b0a234c66d98'
    
    ET.dump(root)

if __name__=='__main__':
    main()
