FROM harbor.syslab.org/library/python3web:1.0


#WORKDIR /app/ACMTOOLS/
#COPY ACMTOOLS  /app/ACMTOOLS/ACMTOOLS/
#COPY API       /app/ACMTOOLS/API/
#COPY HUSTOJ    /app/ACMTOOLS/HUSTOJ/
#COPY MAIN      /app/ACMTOOLS/MAIN/
#COPY docker    /app/ACMTOOLS/docker/
#COPY requirements.txt /app/ACMTOOLS/requirements.txt
#COPY media/export         /app/ACMTOOLS/media/export/
#COPY media/login/build    /app/ACMTOOLS/media/login/build/
#COPY media/manager/build  /app/ACMTOOLS/media/manager/build/
#COPY manage.py /app/ACMTOOLS/


# Service config files
#COPY docker/mysql/mysqld.cnf           /etc/mysql/mysql.conf.d/mysqld.cnf
#COPY docker/nginx/default               /etc/nginx/sites-available/default
#COPY docker/supervisord/acmtools.conf   /etc/supervisor/conf.d/

WORKDIR /app/ACMTOOLS
COPY . /app/ACMTOOLS/
RUN bash /app/ACMTOOLS/docker/install/install_web.sh

VOLUME ['/var/log/supervisor/']

ENTRYPOINT ["supervisord","-n"]



