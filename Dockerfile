FROM python:3.13-alpine

ENV USER=card_app
ENV UID=50000

COPY . /app
RUN adduser -D ${USER} --uid ${UID}
RUN chown -R ${USER}:root /app
WORKDIR "/app"
USER ${USER}

ENTRYPOINT ["python3", "main.py"]