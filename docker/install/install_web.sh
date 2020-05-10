#echo "Install Apt Package !"
#apt-get update  && apt-get install -y python-mysqldb && apt-get clean


echo "Install virtualenv and requirements !"
cd /app/ACMTOOLS && make installenv


echo "Install node yarn and node modules !"
cd /app/ACMTOOLS && make installnodeenv


echo "Build node modules !"
cd /app/ACMTOOLS && make buildnodemodules


echo "Clear useless node modules !"
cd /app/ACMTOOLS && make cleannodemodules


echo "Copy Nginx and Supervisor Config Fle !"
cp /app/ACMTOOLS/docker/nginx/default               /etc/nginx/sites-available/default
cp /app/ACMTOOLS/docker/supervisord/acmtools.conf   /etc/supervisor/conf.d/


echo "Install Finished !" 
