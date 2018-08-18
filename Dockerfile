FROM alpine:latest
MAINTAINER Jacob Elias
COPY . /app
WORKDIR /app
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install --upgrade pip \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/* \
  && pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r ./requirements.txt
EXPOSE 8050
CMD [ "python", "app2.py" ]
