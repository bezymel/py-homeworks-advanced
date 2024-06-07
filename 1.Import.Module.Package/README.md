# Домашнее задание к лекции 1. «Import. Module. Package»

1. Разработать **структуру** программы «Бухгалтерия»:
- main.py;  
- application/salary.py;  
- application/db/people.py.

Main.py — основной модуль для запуска программы.  
В модуле salary.py функция calculate_salary.  
В модуле people.py функция get_employees.  

2. Импортировать функции в модуль main.py и вызывать эти функции в конструкции.
```
if __name__ == '__main__':
```
**Сами функции реализовывать не нужно**. Достаточно добавить туда какой-либо вывод.

3. Познакомиться с модулем [datetime](https://pythonworld.ru/moduli/modul-datetime.html). 
При вызове функций модуля main.py выводить текущую дату.

4. Найти интересный для себя пакет на [pypi](https://pypi.org/) и в файле requirements.txt указать его с актуальной версией. При желании можно написать программу с этим пакетом.

\*5. Создать рядом с файлом main.py модуль dirty_main.py и импортировать все функции с помощью
конструкции (необязательное задание).
```
from package.module import *
```

### Ответ 

![image](https://github.com/bezymel/py-homeworks-advanced/assets/129361495/fcbfed83-2e4d-4ef6-a428-d0079304a045)
![image](https://github.com/bezymel/py-homeworks-advanced/assets/129361495/395d14fa-65b0-4cab-ba5f-e2776bb109b1)
![image](https://github.com/bezymel/py-homeworks-advanced/assets/129361495/56efb2f8-2fa1-4ac0-8624-3aee432444e7)
![image](https://github.com/bezymel/py-homeworks-advanced/assets/129361495/e1d2dff6-0623-474f-b364-450eb91217b6)
![image](https://github.com/bezymel/py-homeworks-advanced/assets/129361495/f93e67c8-a792-48b2-9b7e-279281ecff0b)
![image](https://github.com/bezymel/py-homeworks-advanced/assets/129361495/a115d9f9-f7a4-4804-a616-7480d45ff13a)
![image](https://github.com/bezymel/py-homeworks-advanced/assets/129361495/bd1e8e35-fd28-442a-a233-f2c69d9b2385)
![image](https://github.com/bezymel/py-homeworks-advanced/assets/129361495/15d4904f-7989-4ea6-924c-a2373467eac2)



---
Сдайте домашнее задание ссылкой на репозиторий [BitBucket](https://bitbucket.org/) или [GitHub](https://github.com/).

Мы не сможем проверить задание, если вы пришлёте:

* архивы,
* скриншоты кода,
* теоретический рассказ о возникших проблемах.    


