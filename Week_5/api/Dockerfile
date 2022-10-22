FROM python
RUN pip install flask
RUN pip install psycopg2
ENV API_PORT=${API_PORT}
VOLUME [ "/app" ]
WORKDIR /app
EXPOSE ${API_PORT}