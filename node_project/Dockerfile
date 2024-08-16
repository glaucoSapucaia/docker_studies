# imagem de referencia
# :14 -> versão indicada
FROM node:14

# diretorio da aplicação no container
WORKDIR /app

# copiando arquivos para o container
# * -> indica os dois arquivos .json da aplicação
# . -> a cópia sera feita no diretorio principal -> /app
COPY package*.json .

# rodando comandos de instalação no container
RUN npm install

# copiando demais arquivos da aplicação para o container
COPY app.js .

# expondo porta do container
EXPOSE 3000

# executando a aplicação no container | terminal
CMD [ "node", "app.js" ]