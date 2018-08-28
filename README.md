python-ws
===

# インストール

```
# download repository
$ cd /path/to/ws
ws$ git clone git@github.com:rog-works/python-ws.git

# start docker container
ws$ cd python-ws
python-ws$ docker-compose build
python-ws$ docker-compose up -d
```

# テスト

```
$ cd /path/to/python-ws

python-ws$ docker-compose exec app python -m unittest discover ./tests
```
