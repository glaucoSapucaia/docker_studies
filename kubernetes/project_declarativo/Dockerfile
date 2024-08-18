# image
FROM python:3

# commands
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# diretorio container
WORKDIR /app

# commands
RUN pip install Flask

# copiando arquivos para container
COPY . .

# ports
EXPOSE 5000

# executando app
CMD [ "python3", "./app.py" ]