# Домашнее задание к лекции 2. «Iterators. Generators. Yield»

1. Доработать класс `FlatIterator` в коде ниже. Должен получиться итератор, который принимает список списков и возвращает их плоское представление, т. е. последовательность, состоящую из вложенных элементов. Функция `test` в коде ниже также должна отработать без ошибок.

```python
class FlatIterator:

    def __init__(self, list_of_list):
        ...

    def __iter__(self):
        ...
        return self

    def __next__(self):
        ...
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
```


2. Доработать функцию flat_generator. Должен получиться генератор, который принимает список списков и возвращает их плоское представление.
Функция `test` в коде ниже также должна отработать без ошибок.
```python
import types


def flat_generator(list_of_lists):

    ...
    yield
    ...


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
    
```
### Ответ 

![image](https://github.com/bezymel/py-homeworks-advanced/assets/129361495/3c5bed80-cd7e-4d26-b456-014563fe4666)
![image](https://github.com/bezymel/py-homeworks-advanced/assets/129361495/79a4905b-cef8-4667-a04f-a704d2b974af)


```

---
Домашнее задание сдавайте ссылкой на репозиторий [BitBucket](https://bitbucket.org/) или [GitHub](https://github.com/).

Мы не сможем проверить, если вы пришлёте:

* архивы,
* скриншоты кода,
* теоретический рассказ о возникших проблемах.    


