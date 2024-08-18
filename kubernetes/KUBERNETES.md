# Kubernetes

![alt text](asset/image.png)
![alt text](asset/image-1.png)
![alt text](asset/image-2.png)
![alt text](asset/image-14.png)

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

### Build e push Dokcker file (docker hub)

- build e push para docker hub  
nomeie já para utilizar o Docker Hub
![alt text](asset/image-7.png)
![alt text](asset/image-8.png)
![alt text](asset/image-9.png)

### Deployments

- deployment | kubectl create deployment "nome" --image="image"  
criando deploy do projeto via kubernetes
![alt text](asset/image-10.png)

- get deployents | describe deployments
retorna deployments e seus detalhes
![alt text](asset/image-11.png)

- scale deployments/"nome" --replicas="numero"
escalando aplicanção com pods  
podemos também indicar um numero menor de replicas do que há, assim,  
realizamos o SCALE DOWN da aplicação
![alt text](asset/image-18.png)

- delete deployment "nome"  
exclui um deployment e interrompe todos os PODs
![alt text](asset/image-29.png)

#### Atualizando imagens

É necessário incluir uma tag na build para diferenciar as versões  
Faça o push (docker hub) da nova imagem:tag  
Pegue o nome do container/pod no dashboard  
![alt text](asset/image-20.png)

- set image deployment/"nome_deployment" "nome_container"="imagem"  
![alt text](asset/image-21.png)

#### Desfazendo ações erradas

Atualizando imagem como nome errado  
![alt text](asset/image-22.png)
![alt text](asset/image-23.png)
![alt text](asset/image-25.png)

- rollout status deployment/"nome"  
verifica alterações
![alt text](asset/image-24.png)

- rollout undo deployment/"nome"  
desfaz alterações
![alt text](asset/image-26.png)
![alt text](asset/image-27.png)

### Pods

- get pods | describe pods  
retorna pods e seus detalhes
![alt text](asset/image-12.png)

### Kubernetes Config

- config view  
retorna informações da infraestrutura (kubernetes/minikube)
![alt text](asset/image-13.png)

### Services

#### --type

LoadBalancer -> aplica o servilço para TODOS os PODS  

- expose deployment "nome" --type="tipo" --port="port"  
cria serviço expondo container ao mundo externo
![alt text](asset/image-15.png)

- minikube service "nome"  
gera IP Address para acessar service dos pods  
o nome do serviço criado é igual ao do deployment  
existem várias formas, dependendo do serviço utilizado (minikube, AWS, Azure, etc)  
![alt text](asset/image-16.png)

- get services | describe services/"nome"
retornas services e seus detalhes
![alt text](asset/image-17.png)

- delete service "nome"  
encerra serviço
![alt text](asset/image-28.png)

## Modo Declarativo

![alt text](asset/image-30.png)
![alt text](asset/image-31.png)
![alt text](asset/image-41.png)

### Deployment

- apply -f "file.yaml"  
executa o arqvuio declarativo
![alt text](asset/image-32.png)
![alt text](asset/image-33.png)
![alt text](asset/image-34.png)
![alt text](asset/image-35.png)

- delete -f "file.yaml"  
encerra o deployment
![alt text](asset/image-36.png)

### Service

- apply -f "file-service.yaml"  
Execute o serviço de modo declarativo  
obtenha o ip address para acesso (minikube)
![alt text](asset/image-37.png)

- delete -f "file-service.yaml"  
encerra serviço
![alt text](asset/image-38.png)

### Atualizando imagem

Após alterações, faça o build novamente  
Faça o push para o docker hub  
Atualize o arquivo de deployment .yaml  
Faça p apply -f com o arquivo .yaml de deploy alterado  
![alt text](asset/image-39.png)
![alt text](asset/image-40.png)

### Unindo arquivos yaml

Separe o conteudo do arquivo .yaml com "---"

- apply -f "file.yaml"  
Executa o arquivo global
![alt text](asset/image-42.png)
