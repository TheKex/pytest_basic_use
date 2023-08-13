Необходимые зависимости указаны в [requirements.txt](requirements.txt)

## Установка зависимостей
```commandline
pip install -r requirements.txt
```

## Запуск тестов
```commandline
pytest -s -v
```

## Настройки среды, для теста Я.Диск API
Необхожимо создать файл .env по примеру [.env.example](.env.example).
В нем указать токен с [яндекс полигона](https://yandex.ru/dev/disk/poligon/) 

#### Тесты
1. Тесты по коллекциям [test_collections.py](test_collections.py)
2. Тесты по API Яндекса [test_ya_disk.py](test_ya_disk.py)