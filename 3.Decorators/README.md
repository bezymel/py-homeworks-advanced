# Домашнее задание к лекции 3. «Decorators»

1. Доработать декоратор `logger` в коде ниже. Должен получиться декоратор, который записывает в файл 'main.log'  дату и время вызова функции, имя функции, аргументы, с которыми вызвалась, и возвращаемое значение. Функция `test_1` в коде ниже также должна отработать без ошибок.

```python
import os


def logger(old_function):
    ...

    def new_function(*args, **kwargs):
        ...

    return new_function


def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'
    
    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()

```


2. Доработать параметризованный декоратор logger в коде ниже. Должен получиться декоратор, который записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась, и возвращаемое значение. Путь к файлу должен передаваться в аргументах декоратора. Функция `test_2` в коде ниже также должна отработать без ошибок.

```python
import os


def logger(path):
    ...
    
    def __logger(old_function):
        def new_function(*args, **kwargs):
            ...

        return new_function

    return __logger


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()

```

3. Применить написанный логгер к приложению из любого предыдущего д/з.

### Ответ

![image](https://github.com/bezymel/py-homeworks-advanced/assets/129361495/54fe2b2f-0f59-48b6-8d85-e1eb1e8c9188)
![image](https://github.com/bezymel/py-homeworks-advanced/assets/129361495/bf1ee370-8706-4cd3-8208-590eea786bd6)
![image](https://github.com/bezymel/py-homeworks-advanced/assets/129361495/5d1f42f9-5321-40a5-b20a-897d6966e425)
![image](https://github.com/bezymel/py-homeworks-advanced/assets/129361495/8951fa2e-f7b9-4306-b1b4-a8bc05c35dfe)
![image](https://github.com/bezymel/py-homeworks-advanced/assets/129361495/074cdb35-31b2-4732-852a-27faa88fb657)
![image](https://github.com/bezymel/py-homeworks-advanced/assets/129361495/d878c9f7-ee1b-4ac2-a208-c535696e9445)


---
Домашнее задание сдавайте ссылкой на репозиторий [BitBucket](https://bitbucket.org/) или [GitHub](https://github.com/).

МЫ не сможем проверить, если вы пришлёте:

* архивы,
* скриншоты кода,
* теоретический рассказ о возникших проблемах.    


