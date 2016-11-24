sudo /etc/init.d/mysql start

mysql -u root -p -e "CREATE DATABASE mydb;
			GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';
			FLUSH PRIVILEGES;" 

cd /home/box/web/ask
python ./manage.py syncdb

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
