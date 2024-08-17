# img base
FROM mysql:5.7

# copiando e executando mysql script
# docker-entrypoint-inidb.d/ -> path para scripts mysql do container
COPY schema.sql /docker-entrypoint-initdb.d/

# porta padrao MySql
EXPOSE 3306
