# fynd
for this use case created 2 flask application naming Application_1 and Application_2

Aplication contanrization 
step 1: 
    created image for the flask application using Dockerfile present in application_1 and appication _2 folders respectivley. Having images names as fynd_app1 and fynd_app2.

    comannds to create images are 

    docker build -t manish225/fynd_app1:f1 .

    for testing images locally used below command to run docker container:

    Docker run -d -p 8000:8000 manish225/fynd_app1

Step 2 : 

    Once testing of Docker images is Done Pushed the image to dokcer hub repo.Using below commands:

    Docker login (for authenticating docker repo)

    Docker push manish225/fynd_app1:f1

Application Deployment

Step 3 : 

    Created GKE cluster in GCP platform.having name "fynd-test" and k8s version "1.16.13"

Step 4 : 
    used Manifest files to deploy the application in gke cluster using below command

    kubectl apply -f deployment/

Step 5 :
    Once deployment is complete we can check for the service using below comand:

    kubectl get svc -n app1namespace

    from svc we can get external ip and use this to access the application host.

    http://<external-ip>/myPodInfo
