FROM harbor.syslab.org/library/python3web:1.0

#RUN mkdir  -p /app/ACMTOOLS/
#ADD ACMTOOLS /app/ACMTOOLS/
WORKDIR /app/ACMTOOLS/

COPY ACMTOOLS  /app/ACMTOOLS/ACMTOOLS/
COPY API       /app/ACMTOOLS/API/
COPY HUSTOJ    /app/ACMTOOLS/HUSTOJ/
COPY MAIN      /app/ACMTOOLS/MAIN/
COPY docker    /app/ACMTOOLS/docker/
COPY requirements.txt /app/ACMTOOLS/requirements.txt

COPY media/export         /app/ACMTOOLS/media/export/
COPY media/login/build    /app/ACMTOOLS/media/login/build/
COPY media/manager/build  /app/ACMTOOLS/media/manager/build/

COPY manage.py /app/ACMTOOLS/

RUN apt-get update  && apt-get install -y  python-mysqldb && apt-get clean
RUN pip3 install -r /app/ACMTOOLS/requirements.txt  -i https://pypi.douban.com/simple


# Service config files
#COPY docker/mysql/mysqld.cnf           /etc/mysql/mysql.conf.d/mysqld.cnf
COPY docker/nginx/default               /etc/nginx/sites-available/default
COPY docker/supervisord/acmtools.conf   /etc/supervisor/conf.d/


ENTRYPOINT ["supervisord","-n"]



