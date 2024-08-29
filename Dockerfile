
FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libmariadb-dev gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN chmod +x /app/entrypoint.sh

ENV DJANGO_SETTINGS_MODULE=gruposalinas.settings
ENV DJANGO_CONFIGURATION=BaseConfig
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]

