##1.Run the app in docker

###1.1 First build the docker image

build image
```
git clone https://github.com/heyuantao/ACMTOOLS.git
cd ACMTOOLS
docker built -t acmtools:3.0 .
```
###1.2 Start the mysql docker
create the app dir
```
sudo mkdir -p /app
sudo chown -R ${USER}:${USER} /app/
```
start the mysql container
```
sudo mkdir -p /app/data/db
docker run -d --name=mysql --restart=always --network=host -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -e MYSQL_DATABASE=acmtools -v /app/data/db:/var/lib/mysql -v $PWD/docker/mysqld/mysqld.cnf:/etc/mysql/mysql.conf.d/mysqld.cnf mysql:5.6
```
start the redis container
```
docker run -d --name=redis --restart=always --network=host redis:5.0
```
###1.3 Start the app docker
```
sudo mkdir -p /app/data/logs
docker run -d --name=acmtools --restart=always --network=host -e ACM_HOST=x.x.x.x -e ACM_USER=xxx -e ACM_PASSWORD=xxxx -v /app/data/logs/:/var/log/supervisor/ acmtools:3.0
```
###1.4 Exec into web container and do init
```
docker exec -it <web_container_id> /bin/bash   
make initsystem
```
