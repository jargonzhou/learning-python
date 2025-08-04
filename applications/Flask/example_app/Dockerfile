FROM python:3.12-alpine

ENV FLASK_APP main.py
ENV FLASK_CONFIG docker

RUN adduser -D example_app
USER example_app

WORKDIR /home/example_app

COPY requirements requirements
RUN python -m venv venv
RUN venv/bin/pip install --no-cache-dir -r requirements/docker.txt
# RUN venv/bin/pip install six

COPY app app
COPY migrations migrations
COPY main.py ./
COPY config.py ./
COPY boot.sh ./

# runtime configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]