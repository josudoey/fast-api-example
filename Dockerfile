# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . . 

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]
