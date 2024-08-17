# Volumes

![alt text](asset/image-48.png)
![alt text](asset/image-49.png)

## Volumes anonimos

![alt text](asset/image-50.png)

- docker run -v /data
criando volume anonimo
![alt text](asset/image-51.png)

- volume ls
lista volumes
![alt text](asset/image-52.png)
volume listado no docker inspect
![alt text](asset/image-53.png)

## Volumes nomeados

![alt text](asset/image-54.png)

- docker run -v nome_volumes:/dir_volume
o diretorio deve respeita o indicado na camada WORKDIR do Dockerfile
![alt text](asset/image-55.png)
![alt text](asset/image-56.png)

## Bind mount

Possibilita persistir dados em tempo real
![alt text](asset/image-57.png)

- docker run -v diretorio_local:diretorio_container
![alt text](asset/image-58.png)

- erro com permissões
![alt text](asset/image-59.png)
execute o /bin/bash do container
![alt text](asset/image-60.png)
verifique e altere as permissoes
![alt text](asset/image-61.png)
![alt text](asset/image-62.png)
outra opção é utilizar o caminho absoluto da pasta local
![alt text](asset/image-63.png)

## Bind mount | atualizando projreto em tempo real

para isso, copie todo o projeto
![alt text](asset/image-64.png)

## volume create "nome"

criando volumes nomeados manualmente
![alt text](asset/image-65.png)
![alt text](asset/image-66.png)

## volume inspect "nome"

inspecionando volumes
![alt text](asset/image-67.png)
![alt text](asset/image-68.png)

## volume rm "nome"

removendo volumes
![alt text](asset/image-69.png)
