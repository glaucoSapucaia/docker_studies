# imagem de referencia
FROM php:8-apache

# diretprio da aplicacao
WORKDIR /var/www/html/

# copiando arquivos para o container
COPY . .

# porta de execução
EXPOSE 80

# comando de execução
# chown -> comando para permissões aos arquivos
# necessario para o apache no linux
RUN chown -R www-data:www-data /var/www
