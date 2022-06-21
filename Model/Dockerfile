FROM tiangolo/uwsgi-nginx-flask:python3.8

# copy over our requirements.txt file
COPY requirements.txt /tmp/

# upgrade pip and install required python packages
RUN pip3 install --upgrade pip
RUN pip3 install -r /tmp/requirements.txt


# copy over our app code
COPY ./app /app

VOLUME /modeldata

# set an environmental variable, MESSAGE,
# which the app will use and display
ENV MODEL_DATA_PATH "/modeldata"

# database environmental variable
ENV MYSQL_DATABASE 'PROJECT_DB'
ENV MYSQL_USER 'user'
ENV MYSQL_PASSWORD 'user'
ENV MYSQL_PORT 3306
ENV PROJECT_BOT_LOG_LEVEL WARNING
#ENV RABBITMQ_ROBOT_METRIC_EXCHANGE metrics_exchange
#ENV RABBITMQ_ROBOT_METRIC_QUEUE metrics_queue
#ENV RABBITMQ_USER guest
#ENV RABBITMQ_PASSWORD guest
#ENV RABBITMQ_HOST urba_rabbitmq
#ENV RABBITMQ_PORT 5672

EXPOSE 80/tcp