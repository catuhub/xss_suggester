FROM python:2.7-buster

RUN apt update && apt upgrade -y

COPY . /wapt_suggester

WORKDIR /wapt_suggester

EXPOSE 5000

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
