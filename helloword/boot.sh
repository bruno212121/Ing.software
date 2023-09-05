#!/bin/bash

GROUP_NAME=umGroupResource

az group create --name $GROUP_NAME --location eastus 

ACR_NAME=stocklister

TAG=v1

APP_IMAGE=helloworld

az acr create --resource-group $GROUP_NAME --name $ACR_NAME --sku Basic 

az acr login --name $ACR_NAME

ACR_REGISTRY_ID=$(az acr show-name $ACR_NAME query "d" --output tsv) 

SERVICE=universidad

USER_NAME=$(az ad sp list --display-name $SERVICE PRINCIPAL NAME --query "[].appId" --output tsv)

PASSWORD=$(az ad sp create-for-rbac --name $SERVICE_PRINCIPAL_NAME --Scopes $ACR_REGISTRY_ID --role acrpull --query password --output tsv)

docker build -t $APP_IMAGE:$TAG .

docker tag $APP_IMAGE:$TAG $ACR_NAME.azurecr.io/$APP_IMAGE:$TAG

az acr repository list --name $ACR_NAME --output table

docker push $ACR_NAME.azureacr.io/$APP_IMAGE:$TAG