FROM python:3.8.5-alpine

# RUN pip install --upgrade pip
# RUN pip install -U pipenv
RUN pip3 install --upgrade pip
RUN pip3 install -U pipenv
COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN python3 -m pipenv install --deploy --ignore-pipfile

COPY . ./app
WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]