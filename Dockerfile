FROM python:3.8.5-alpine


# gcc stuff
RUN apk update
RUN apk add build-base
RUN apk add python3-dev \
                gcc \
                libc-dev \
                libffi-dev

# install psycopg2 dependencies
RUN apk add postgresql-dev musl-dev

# Pillow stuff
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

# pipenv lock -r > requirements.txt
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . ./app
WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]