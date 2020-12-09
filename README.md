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



Also package contains .sops.yaml ,

**encrypted_suffix: SECRET** says that all  variables with SECRET suffix must be encrypted. 


