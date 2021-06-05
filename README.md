# setup

```
sudo apt-get install redis-server
pip install -r requirements.txt
```

vscode extension used to create docker: 
> ms-azuretools.vscode-docker

(optional)
note: to run using docker compose: 
follow **docker_compose_install.md** to install docker compose 


# to Run

```
python -m uvicorn main:app --reload
```

## to run using docker-compose 

to start all the containers
```
docker-compose -f "docker-compose.yml" up -d --build
```

to close all the containers
```
docker-compose -f "docker-compose.yml" down
```

# troubleshooting

```
# error:
File "/home/nithin/anaconda3/envs/py37/lib/python3.7/site-packages/redis/connection.py", line 563, in connect
    raise ConnectionError(self._error_message(e))
redis.exceptions.ConnectionError: Error -2 connecting to 127.0.0.1:6379:6379. Name or service not known.

# solution:
export REDIS_HOST=127.0.0.1
```


start/ stop redis server
```
# stop redis server and
/etc/init.d/redis-server stop

# start redis server 
/etc/init.d/redis-server start
```

to kill application running on a port 8000
```
sudo lsof -i:8000

kill <application-pid>

```


References:
1. [Working with Docker and VSCode](https://www.youtube.com/watch?v=wUUmRbXiIOo)