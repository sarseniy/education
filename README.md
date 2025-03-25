# Education app

This repository represents small educational application for learning foreign languages

## How to start

1) Install requirements 
```shell
pip install -r requirements.txt
```
2) Create `.env` file and put there `SECRET_KEY` value
```shell
cp .env.local .env
```
3) Run migrations
```shell
./manage.py migrate
```
4) Run application
```shell
./manage.py runserver
```