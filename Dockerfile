FROM python:latest

WORKDIR /app
RUN apt-get update && apt-get upgrade -y

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

COPY ./ /app

CMD ["python", "main.py"]
