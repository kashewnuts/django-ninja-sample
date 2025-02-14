# README

[django-ninja](https://django-ninja.dev/) でcache_pageとthrottleがどのように動くのかを確認するためのリポジトリ

## requirements
* Python3.11+: ローカル環境で動作
* Docker/docker-compose: Redisが起動する

## init & run

```bash
$ python3 -m venv .venv
$ . .venv/bin/activate
$ (venv) pip install -r requirements.txt
$ (venv) python manage.py migrate
$ (venv) python manage.py runserver
```

別のターミナルを立ち上げて以下で動作確認

```bash
$ (venv) python main.py
```
