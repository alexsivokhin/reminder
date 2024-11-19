## Установка библиотек
```
sudo apt install -y python3-venv
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```
## Создание виртуального окружения
```
python3 -m venv .venv
```

## Переключение в контекст venv
```
source .venv/bin/activate
```

## Выход из venv
```
deactivate
```

## Обновляем pip
```
pip install --upgrade pip
```

## Устанавлииваем библиотеки в venv
```
pip install -r requirements.txt
```

## Создаем файл .env и добавляем туда переменные

1) Создаем файл
touch .env

2) Создаем в нем переменные
TOKEN=[ВАШ ТОКЕН]
SQLALCHEMY_URL=[URL БАЗЫ ДАННЫХ]

