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


***In this document i will describe how to deploy each of the above helm deployment in minikube kubernetes  cluster . I encourage you to  test both the deployement metonds independently and   test its functionalities***  

Helm deployment packages will contain the **secrets.yaml**  file which contains a set of sensitive data that was encrypted by PGP key .

Also package contains **.sops.yaml**. examines that  file

**encrypted_suffix: SECRET** says that all  variables with SECRET suffix must be encrypted. 


![](https://github.com/parakrama/images/blob/master/mark1.jpg)




# Testing environment

  - Use ubuntu 18.04 
  - Minikube 1.11 Version  https://storage.googleapis.com/minikube/releases/v1.11.0/minikube-linux-amd64
  - I’m using minikube 1.11 version because newer version  of minikube didn’t  work well with **None drive**  and **nginx controller** 
  - Kubernetes version 1.18


## Option ONE - Deployment Expose via NodePort service (Hello-world-2.0.0.tgz )

### Steps to run the  deployment 

<br></br>

   1. Download and install the minikube 

      ```
      Wget https://storage.googleapis.com/minikube/releases/v1.11.0/minikube-linux-amd64  
      sudo cp minikube-linux-amd64 /usr/local/bin/minikube
      sudo chmod 755 /usr/local/bin/minikube
      ```

   2. Run the minikube as ROOT or Sudo
   
      ```
      sudo minikube start --vm-driver=none
      ```
      
      This is a very critical setup of the process , minikube must RUN as **ROOT or SUDO**  in order to  work the persistent volume hostpath feature in minikube     .   Mysql deployment is using the persistent volume feature to store its data and persistent volume uses the **hostPath:/tmp/mysqldata/** to store its data in         running physical machine 

   3. Install the helm secret plugin 
  
      ```
      Sudo helm plugin install https://github.com/futuresimple/helm-secrets
      ```
      This secret plugin is required to encrypt  and decrypt the helm  charts sensitive data such as user name and passwords 
  
  
   4. Running helm setup

      - Once minikube is started create folder called **/tmp/mysqldata/**   this will be used to store the  mysql data directory using persistent volumes
  
      - Clone git repository
         ``` 
         git clone  https://github.com/parakrama/hello-world-app
         ```
  
      - Then go to the clone ***hello-world-app folder*** and then ***public-key folder** . Then copy the pgp public key **secring.gpg**  to **/home/user/.gnupg/**   ( /home/user/**  is the  working user's home directory of a ubuntu machine )  This key will be used to decrypt secrets.yaml file
  
         ```
         cd hello-world-app/public-key/
         cp secring.gpg /home/user/.gnupg/
         ```

        ![](https://github.com/parakrama/images/blob/master/mark2.png)
   
   
      - Go to helm folder inside the clone repository
   
         ```
         cd helm
         ```
   
      - Then extract the hello-world-2.0.0.tgz file
   
         ```
         tar zxvf hello-world-2.0.0.tgz
         cd hello-world 
         ```
   
      - Decrypt the **secrets.yaml**  file in the hello-world folder . this will create the **secret.yaml.dec** file 
   
         ```
         helm  secrets dec secrets.yaml 
         ```
    
         ![](https://github.com/parakrama/images/blob/master/mark3.png)
   

      - Run the helm deployment 

         ```
         sudo helm install     --debug  app  hello-world -f hello-world/secrets.yaml.dec
         ```
         ![](https://github.com/parakrama/images/blob/master/mark4.png)
   
   
   
   
Then you can access the setup using  **http://localhost:30036**  . This allows you to access the setup via **NodePort** service of the Minikube Cluster . 
Then you will see the **Hello World**  output in the browser

![](https://github.com/parakrama/images/blob/master/mark5.png)
   
   
   
   


## Option TWO - Deployment Expose via Nginx Controller service (Hello-world-ingress-2.0.0.tgz)



### Steps to run the deployment 

- First you must enable the ingress feature in minikube 

  ```
  sudo minikube addons enable ingress
  ```

- Similar to **Option ONE steps** , Clone the git repository and run the below commands as shown in the picture

   ```
   Create  folder called  /tmp/mysqldata/   to store the mysql data in persistent volume  ( mkdir /tmp/mysqldata/ )
   git clone https://github.com/parakrama/hello-world-app
   cd hello-world-app      #repository folder 
   cd helm
   tar xvzf hello-world-ingress-2.0.0.tgz 
   cd hello-world-ingress/
   helm secrets dec secrets.yaml  #Decript  helm secret file 
   cd ..
   sudo helm install  application  hello-world-ingress -f hello-world-ingress/secrets.yaml.dec
   ```

   ![](https://github.com/parakrama/images/blob/master/mark6.png)
  
<br></br>


- Nginx ingress hostname defined as  **hello-world.com**   as below  , so make sure to add  **/etc/hosts**  entry to your machine as below

   ![](https://github.com/parakrama/images/blob/master/mark7.png)
  
 
    ```
    /etc/hosts
    127.0.0.1  hello-world.com 
    ```
     ![](https://github.com/parakrama/images/blob/master/mark8.png)
     
  <br></br>
  
  
 - Now you can access the http://hellow-world.com via the browser  
 
  
     ![](https://github.com/parakrama/images/blob/master/mark9.png)
     
 
<br></br>
<br></br>
## Truobleshhting

Incase you get below error when running  helm charts 

```
Internal error occurred: failed calling webhook"validate.nginx.ingress.kubernetes.io": Post https://ingress-nginx-controller-admission.ingress-nginx.svc:443/extensions/v1beta1/ingresses?timeout=30s: context deadline exceeded
```

Run the below command to fix it 

```
kubectl delete -A ValidatingWebhookConfiguration ingress-nginx-admission
```

Issue is described in github URL https://github.com/kubernetes/ingress-nginx/issues/5401

