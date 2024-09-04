FROM python:3.11.0-slim
ARG APP_PATH= /app/Resume-Matcher
ARG PORT=8011

ENV APP_PATH=$APP_PATH

WORKDIR $APP_PATH
RUN apt-get update
RUN apt-get install -y build-essential python-dev git
COPY ./app/requirements.txt ./requirements.txt
RUN pip install -U pip setuptools wheel
RUN pip install -r requirements.txt

COPY ./.env /tmp/env
RUN cat /tmp/env >> /etc/environment
RUN rm /tmp/env

COPY ./app $APP_PATH

RUN python run_first.py
ENTRYPOINT [ "streamlit", "run", "streamlit_app.py"]

EXPOSE 8501
