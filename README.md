# Proyecto Agendita

Este repositorio proporciona instrucciones para ejecutar la imagen Docker `l0stbyt3/agendita:1.0.0`, que contiene una aplicación Django preconfigurada para la gestión de una agenda.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu máquina:

- [Docker](https://www.docker.com/get-started)

## Iniciar la Aplicación

Para iniciar la aplicación utilizando Docker, sigue los siguientes pasos:

1. **Ejecuta el siguiente comando:**

   ```bash
   docker run -d -p 8000:8000 l0stbyt3/agendita:1.0.0