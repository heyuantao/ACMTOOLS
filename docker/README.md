1.Create the test network thenStart The MySQL and Redis

$docker network create django
$docker run -p 80:80 -d --net=django --name=acmtools-db  -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -e MYSQL_DATABASE=acmtools  -v $PWD/etc/mysql/mysql.conf.d/mysqld.cnf:/etc/mysql/mysql.conf.d/mysqld.cnf  mysql:5.6
$docker run -d --net=container:acmtools-db --name=acmtools-redis redis:3.0.6

2  Build And RunThe Docker image
2.1 User docker build image

$cd ..
$docker build -t harbor.syslab.org/library/acmtools-web .

2.2 Run the docker image

$docker run -it --net=container:acmtools-db --name=acmtools-web  harbor.syslab.org/library/acmtools-web:latest

2.3 Exec into docker and execute the init.sh to initalized the database

$docker exec acmtools-web bash
