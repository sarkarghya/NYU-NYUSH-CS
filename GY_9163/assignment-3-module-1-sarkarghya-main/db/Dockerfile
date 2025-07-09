FROM mysql:8.0.29

COPY ./products.csv /products.csv
COPY ./users.csv /users.csv
COPY ./setup.sql /docker-entrypoint-initdb.d/setup.sql

ENTRYPOINT ["/entrypoint.sh"]
CMD ["mysqld", "--secure-file-priv=/"]
#CMD ["--secure-file-priv=/"]
