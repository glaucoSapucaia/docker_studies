# Imagens

![alt text](asset/image-18.png)

## build . -> monta imagem Dockerfile no diretório atual

- build "diretorio da imagem"
Monta imagem indicada
![alt text](asset/image-19.png)

- -t
Monta imagem com nome e tag | nome:tag
![alt text](asset/image-30.png)
![alt text](asset/image-31.png)

## image

- ls
Lista imagens disponiveis
![alt text](asset/image-20.png)

## Rodando minha imagem/container

![alt text](asset/image-21.png)
![alt text](asset/image-22.png)

## Alterando aplicação

Ao alterar a aplicação, é necessário remontar a imagem para efetivar as alterações
![alt text](asset/image-23.png)
![alt text](asset/image-24.png)
![alt text](asset/image-25.png)

## tag "id" - nomeando imagens e tags

TAG -> indica a "versão" da imagem podendo ser usada assim: docker pull nome_imagem:tag_imagem

![alt text](asset/image-28.png)
![alt text](asset/image-29.png)

## rmi "nome ou id"

Remove imagem  
Caso a imagem tenha sido usada em um container, precisamos forçar a remoção

![alt text](asset/image-33.png)

- -f
Força a remoção de uma imagem
![alt text](asset/image-34.png)

## upload de imagens

- docker login | logout
Faça o login em sua conta
![alt text](asset/image-42.png)
![alt text](asset/image-43.png)

- repositorio
crie um repositorio no docker hub
![alt text](asset/image-44.png)

- build
a imagem deve ter o mesmo nome do repositorio
![alt text](asset/image-45.png)

- push "imagem"
Faz o upload de uma imagem
![alt text](asset/image-46.png)
![alt text](asset/image-47.png)
