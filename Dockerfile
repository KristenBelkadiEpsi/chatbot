
FROM rasa/rasa:3.1.0-full


COPY . /app

WORKDIR /app

RUN pip install -r requirements-actions.txt

CMD ["run", "--enable-api", "--cors", "*", "--debug"]
