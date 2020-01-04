FROM harbor.syslab.org/library/ubuntu:18.04

#RUN mkdir  -p /app/ACMTOOLS/
#ADD ACMTOOLS /app/ACMTOOLS/
WORKDIR /app/ACMTOOLS/

COPY ACMTOOLS  /app/ACMTOOLS/ACMTOOLS/
COPY API       /app/ACMTOOLS/API/
COPY HUSTOJ    /app/ACMTOOLS/HUSTOJ/
COPY MAIN      /app/ACMTOOLS/MAIN/
COPY requirements.txt /app/ACMTOOLS/requirements.txt

COPY media/export         /app/ACMTOOLS/media/export/
COPY media/login/build    /app/ACMTOOLS/media/login/build/
COPY media/manager/build  /app/ACMTOOLS/media/manager/build/

COPY manage.py /app/ACMTOOLS/


RUN apt-get update 
RUN apt-get install -y python3 python3-pip python3-dev libmysqlclient-dev python-mysqldb libssl-dev nginx supervisor
RUN pip3 install -r /app/ACMTOOLS/requirements.txt  -i https://pypi.douban.com/simple
#RUN pip3 install  gunicorn -i https://pypi.douban.com/simple


# Service config files
#COPY docker/mysql/mysqld.cnf           /etc/mysql/mysql.conf.d/mysqld.cnf
COPY docker/nginx/default               /etc/nginx/sites-available/default
COPY docker/supervisord/acmtools.conf   /etc/supervisor/conf.d/


ENTRYPOINT ["supervisord","-n"]



