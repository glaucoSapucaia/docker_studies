# Networks

![alt text](asset/image-73.png)
![alt text](asset/image-74.png)
![alt text](asset/image-75.png)

- ls
lista as networks
![alt text](asset/image-76.png)

- create "nome"
cria uma rede | use -d para indicar o driver
![alt text](asset/image-77.png)
![alt text](asset/image-78.png)

- network connect "rede" "container"
Conecta manualmente um container a uma rede
![alt text](asset/image-99.png)

- rm "nome"
remove uma rede
![alt text](asset/image-79.png)

## Conexão Externa

![alt text](asset/image-81.png)

- container conectando a API
simulando app python
![alt text](asset/image-82.png)

## Conexão host

![alt text](asset/image-83.png)
![alt text](asset/image-91.png)
![alt text](asset/image-92.png)
![alt text](asset/image-93.png)

- mysql container
![alt text](asset/image-84.png)
![alt text](asset/image-85.png)
![alt text](asset/image-86.png)
![alt text](asset/image-87.png)  
Entre com a senha indicada no docker run  
[comandos mysql](https://www.diegobrocanelli.com.br/mysql/comandos-basicos-mysql-no-terminal/)  
CREATE DATABASE "nome_db"  
![alt text](asset/image-88.png)
![alt text](asset/image-89.png)
![alt text](asset/image-90.png)  
exit -> sai do terminal mysql

## Conexão entre containers

Crie um container mysql  
Crie um container de aplicação  
Crie uma network
![alt text](asset/image-94.png)

- rodando containers  
Mysql container  
-e MYSQL_ALLOW_EMPTY_PASSWORD=True -> variavel de ambiente que permite senhas vazias  
![alt text](asset/image-95.png)
flask container  
![alt text](asset/image-96.png)
Execução da conexão
![alt text](asset/image-97.png)
![alt text](asset/image-98.png)
