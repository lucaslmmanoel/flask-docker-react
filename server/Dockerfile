FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python3.7 python3.7-dev python3-pip

WORKDIR /app
COPY ./ /app

RUN python3.7 -m pip install -r requirements.txt
CMD ["python3.7", "app.py"]