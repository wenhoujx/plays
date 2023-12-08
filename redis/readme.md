# try out redis

## start redis in docker

```
docker run -p 6379:6379 -it --rm redis/redis-stack-server
```

## install redis-cli

```
brew install redis
# then 
redis-cli 
# enters redis console 
```

```
# create sensor1 timeseries 
ts.create sensor1
ts.add sensor1 1626434637914 26
ts.add sensor1 * 26

```
