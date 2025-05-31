
FROM python:3.11

ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

WORKDIR /app

# Zainstalowanie netcat (nc)
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    postgresql-client \
 && apt-get clean



COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY ./init_db /app/init_db


COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh


EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
