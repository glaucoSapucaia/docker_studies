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
