FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN pip install --upgrade pip
RUN pip install pipenv && pipenv install --skip-lock --system

COPY . /code/

CMD ["python3", "./run.py"]
