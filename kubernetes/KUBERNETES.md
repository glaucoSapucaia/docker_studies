# Kubernetes

![alt text](asset/image.png)
![alt text](asset/image-1.png)
![alt text](asset/image-2.png)

## Tools

- [chocolatey | Windows](https://chocolatey.org/)
- [kubernetes tools](https://kubernetes.io/docs/tasks/tools/)
- [minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download)

## Minikube

- start --driver="driver"  
inicia minikube

- status  
checa status do minikube  

![alt text](asset/image-3.png)

- stop  
encerra minikube
![alt text](asset/image-4.png)

- dashboard | --url  
obtendo informações gerais do projeto | kubernetes painel
![alt text](asset/image-5.png)
![alt text](asset/image-6.png)

## Project

- build e push para docker hub  
nomeie já para utilizar o Docker Hub
![alt text](asset/image-7.png)
![alt text](asset/image-8.png)
![alt text](asset/image-9.png)

- deployment | kubectl create deployment "nome" --image="image"  
criando deploy do projeto via kubernetes
![alt text](asset/image-10.png)

- get deployents | describe deployments
retorna deployments e seus detalhes
![alt text](asset/image-11.png)
