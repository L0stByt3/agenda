
FROM python:3.10-slim

WORKDIR /gsalinas

RUN apt-get update && apt-get install -y \
    libmariadb-dev gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=gruposalinas.settings
ENV DJANGO_CONFIGURATION=BaseConfig
ENV PYTHONUNBUFFERED=1

EXPOSE 6666

CMD ["gunicorn", "--bind", "0.0.0.0:6666", "gruposalinas.wsgi:application"]
