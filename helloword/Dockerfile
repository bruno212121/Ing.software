FROM python:3.10-buster

WORKDIR /app

COPY ./app.py .

EXPOSE 5000

ADD requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./app.py" ]