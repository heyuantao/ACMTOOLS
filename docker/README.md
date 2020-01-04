1.Create the test network thenStart The MySQL and Redis

$docker network create django
$docker run -p 80:80 -d --net=django --name=acmtools-db  -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -e MYSQL_DATABASE=acmtools  -v $PWD/etc/mysql/mysql.conf.d/mysqld.cnf:/etc/mysql/mysql.conf.d/mysqld.cnf  mysql:5.6
$docker run -d --net=container:acmtools-db --name=acmtools-redis redis:3.0.6

2  Build And RunThe Docker image
2.1 User docker build image

$cd ..
$docker build -t harbor.syslab.org/library/acmtools-web .

2.2 Run the docker image

$docker run -it --net=container:acmtools-db --name=acmtools-web -e ACM_HOST="172.16.3.19" -e ACM_USER="readonly" -e ACM_PASSWORD="60632180"  harbor.syslab.org/library/acmtools-web:latest

The Env IS:
################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.getenv('HOST', '127.0.0.1'),
        'PORT': os.getenv('PORT', '3306'),
        'NAME': os.getenv('NAME', 'acmtools'),
        'USER': os.getenv('USER', 'root'),
        'PASSWORD': os.getenv('PASSWORD',''),
    },
    'hustoj': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.getenv('ACM_HOST', ''),
        'PORT': os.getenv('ACM_PORT', '3306')
        'NAME': os.getenv('ACM_NAME', 'jol'),
        'USER': os.getenv('ACM_USER', 'readonly'),
        'PASSWORD': os.getenv('ACM_PASSWORD','60632108'),
    }
}
##############

2.3 Exec into docker and execute the init.sh to initalized the database

$docker exec acmtools-web bash
