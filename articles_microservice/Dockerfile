FROM python:3.10

# Crear usuario
RUN useradd -ms /bin/bash articles_ms
# RUN adduser -S -D -H articles_ms
# RUN mkdir /home/articles_ms
# RUN chown -R articles_ms /home/articles_ms

# Dar permisos al usuario a cierto directorio
RUN chown -R articles_ms:articles_ms /home/articles_ms
RUN chmod 755 /home/articles_ms


# Selecionar directorio
WORKDIR /home/articles_ms

# Crear directorio main
RUN mkdir main

# Copiar archivos
COPY ./main ./main
COPY ./app.py .

# Instalar dependencias de mysql

RUN apt-get update && apt-get install -y libmcrypt-dev default-mysql-client




# install requirements
COPY requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 7000

CMD ["python3", "./app.py"]