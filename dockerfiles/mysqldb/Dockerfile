FROM mysql:5.6
ADD dump.sql  /docker-entrypoint-initdb.d/
ENV MYSQL_ROOT_PASSWORD mypass #This password will be resetted during helm deployment process

