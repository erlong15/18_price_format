# Форматирование цены
Модуль форматирования цены для корректного отображения.
Модуль предполагается как подключаемый.
Имеется возможность консольного запуска

# Как подключить
В функцию передается цена и значение, которое выведется в случае ошибки

пример импорта и вызова модуля
```python

from format_price import format_price

print(format_price(123456.12345, "Цена уточняется"))
```

Результат будет в виде
```bash
123 456.12
```

# Консольный запуск

```bash
python3 format_price.py 12345678.123450
12 345 678.12
```

# Запуск тестов

```bash
python3 tests.py 
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

# Цели проекта

тестовый код для проекта - [DEVMAN.org](https://devman.org)
