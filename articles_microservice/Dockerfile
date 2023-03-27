FROM python:3.8-buster

WORKDIR /app

COPY . /app

EXPOSE 7000

RUN pip install -r requirements.txt

CMD ["python", "-u", "./app.py"]