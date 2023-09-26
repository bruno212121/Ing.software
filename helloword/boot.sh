#!/bin/bash

GROUP_NAME=umGroupResource
ACR_NAME=registerhelloworld
TAG=v1
APP_IMAGE=helloworld
SERVICE_PRINCIPAL_NAME=universidad
ACR_REGISTRY_ID=$(az acr show --name $ACR_NAME --query "id" --output tsv)

az group create --name $GROUP_NAME --location eastus 

# Verificar si el ACR ya existe en el grupo de recursos
if az acr show --name $ACR_NAME; then
    echo "El Azure Container Registry '$ACR_NAME' ya existe en el grupo de recursos '$GROUP_NAME'."
else
    # Si no existe, crear el ACR
    echo "Creando el Azure Container Registry '$ACR_NAME' en el grupo de recursos '$GROUP_NAME'..."
    az acr create --resource-group $GROUP_NAME --name $ACR_NAME --sku Basic
fi

# Verificar si la etiqueta de la imagen ya existe en el ACR
if az acr repository show-tags --name $ACR_NAME --repository $APP_IMAGE --output tsv | grep -q $TAG; then
    echo "La etiqueta '$TAG' de la imagen '$APP_IMAGE' ya existe en el ACR '$ACR_NAME'. No es necesario volver a empujar la imagen."

    USER_NAME=$(az ad sp list --display-name $SERVICE_PRINCIPAL_NAME --query "[].appId" --output tsv)
    PASSWORD=$(az ad sp create-for-rbac --name $SERVICE_PRINCIPAL_NAME --scopes $ACR_REGISTRY_ID --role acrpull --query password --output tsv)

    az acr repository list --name $ACR_NAME --output table
    az container create --resource-group $GROUP_NAME --name $APP_IMAGE --image $ACR_NAME.azureacr.io/$APP_IMAGE:$TAG --cpu 1 --memory 1 --registry-login-server $ACR_NAME.azureacr.io --registry-username $USER_NAME --registry-password $PASSWORD --ip-address Public --dns-name-label dns-um-$RANDOM --ports 5000

    az group list -output tsv

else
    Si la etiqueta no existe, construir y empujar la imagen
    az acr login --name $ACR_NAME
    ACR_REGISTRY_ID=$(az acr show-name $ACR_NAME --query "id" --output tsv)

    docker build -t $APP_IMAGE:$TAG .
    docker tag $APP_IMAGE:$TAG $ACR_NAME.azurecr.io/$APP_IMAGE:$TAG
    az acr repository list --name $ACR_NAME --output table
    docker push $ACR_NAME.azureacr.io/$APP_IMAGE:$TAG

fi
