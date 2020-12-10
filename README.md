# Overview

Please refer the Git hub repository https://github.com/parakrama/hello-world-app   Where you can find below details in the Folders

| Requirement      	| Folder      	|
|------------------	|-------------	|
| Application Code 	| code        	|
| Helm Chart       	| helm        	|
| Docker files     	| dockerfiles 	|

Helm folder contain two  helm packages 

- Hello-world-2.0.0.tgz  :   This contains helm package which exposes the deployment via NodePort service 

- Hello-world-ingress-2.0.0.tgz  : This package contains the deployment . which will expose the application via  Nginx ingress controller 


In this section i will describe how to deploy each helm deployment in minikube kubernetes  cluster 


Helm deployment packages will contain the **secrets.yaml**  file which contains a set of sensitive data that was encrypted by PGP key .

Also package contains **.sops.yaml**. Examins that file file

**encrypted_suffix: SECRET** says that all  variables with SECRET suffix must be encrypted. 

Image:

![](https://github.com/parakrama/images/blob/master/mark1.jpg)




# Testing environment

- Use ubuntu 18.04 
- Minikube 1.11 Version  https://storage.googleapis.com/minikube/releases/v1.11.0/minikube-linux-amd64
- I’m using minikube 1.11 version because newer version  of minikube didn’t  work well with **None drive**  and **nginx controller** 
- Kubernetes version 1.18


## Option ONE - Deployment Expose via NodePort service

### Steps to run the  deployment 

  1. Download and install the minikube 

 ```
    Wget https://storage.googleapis.com/minikube/releases/v1.11.0/minikube-linux-amd64  
    sudo cp minikube-linux-amd64 /usr/local/bin/minikube
    sudo chmod 755 /usr/local/bin/minikube
```



