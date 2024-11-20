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

## Устанавливаем библиотеки в venv
```
pip install -r requirements.txt
```

## Создаем файл .env и добавляем туда переменные

1) Создаем файл\
touch .env

2) Создаем в нем переменные\
TOKEN=[ВАШ ТОКЕН]\
SQLALCHEMY_URL=[URL БАЗЫ ДАННЫХ]

## Сделать сервис

1) Создать файл для systemd
```
cd /lib/systemd/system/
sudo nano НазваниеСервиса.service
```

2) Конфиг файла .service
```
[Unit]
Description=Описание сервиса
After=network.target

[Service]
Type=idle
Restart=always
RestartSec=5
KillMode=process
WorkingDirectory=РабочаяДиректория
ExecStart=РабочаяДиректориия/.venv/bin/python3 bot.py

[Install]
WantedBy=multi-user.target
```

3) Добавление в автозагрузку и старт
```
sudo systemctl enable НазваниеСервиса
sudo systemctl start НазваниеСервиса
```
