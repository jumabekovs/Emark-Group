# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get install gcc
RUN pip install -r requirements.txt
COPY . /code/
# RUN python3 manage.py makemigrations && python3 manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]