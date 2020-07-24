FROM python:3.8

ENV PYTHONUNBUFFERED 1
ADD . /app/

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ADD poetry.lock /app/
ADD pyproject.toml /app/


WORKDIR /app
RUN $HOME/.poetry/bin/poetry export -f requirements.txt > requirements.txt
RUN pip install -r requirements.txt