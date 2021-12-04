FROM python:3.8.5-alpine

RUN pip install --upgrade pip
RUN pip install -U pipenv
COPY ./Pipfile ./Pipfile.lock ./
RUN pipenv install --system

COPY . ./app
WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]