cd /app/ACMTOOLS/
/app/venv/bin/python3 manage.py migrate
/app/venv/bin/python3 manage.py createuser -u admin@example.com -p example.com  -t admin
