# Docker Swarm

![alt text](asset/image.png)
![alt text](asset/image-1.png)
![alt text](asset/image-12.png)

## Tools

- [lab docker](https://labs.play-with-docker.com/)
- [swarm commands](https://medium.com/docker-um-canivete-su%C3%ADco/docker-principais-comandos-%C3%BAteis-a37639a432d5)

## Inicie instancias

![alt text](asset/image-2.png)

## comandos

- start  
Indique o ip addres do node manager
![alt text](asset/image-3.png)

- leave -f  
força saida de um swarm
![alt text](asset/image-4.png)

- node ls
lista nodes
![alt text](asset/image-5.png)

## node como worker

Use a chave token do node manager
![alt text](asset/image-6.png)
![alt text](asset/image-7.png)

- join-token manager  
recupera token do manager
![alt text](asset/image-15.png)

## Adicionando e manipulando serviços e containers

![alt text](asset/image-8.png)

- docker service ls  
listando serviços  
![alt text](asset/image-9.png)

- docker service rm "servico"  
encerra serviços
![alt text](asset/image-10.png)

- --replicas | tasks  
Indica qtd de replicas para nodes
![alt text](asset/image-11.png)

- derrubando container worker (Manager o reinicia)  
![alt text](asset/image-13.png)
![alt text](asset/image-14.png)
