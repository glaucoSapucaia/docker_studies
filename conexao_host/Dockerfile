# image base
FROM python:3

# atualizando sistema e instalando pacotes
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# diretorio do container
WORKDIR /app

# instalando mais dependencias
RUN pip install Flask requests flask_mysqldb

# copiando dados locais para container
COPY . .

# porta do container
EXPOSE 5000

# executando palicação
CMD [ "python3", "./app.py" ]
