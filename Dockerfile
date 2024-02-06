FROM ubuntu:22.04

RUN apt update && \
    apt install mysql-server -y && \
    apt install mysql-client -y && \
    apt install python3 python3-pip -y && \
    pip3 install mysql-connector-python && \
    service mysql start

ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=app

COPY --chown=mysql:mysql src/ /home/mysql/
RUN chmod 555 /home/mysql/
RUN chown -R mysql:mysql /home/mysql

WORKDIR /home/mysql

USER mysql

# Встановлення app.py як точки входу для контейнера
ENTRYPOINT ["python3", "/home/mysql/app.py"]
