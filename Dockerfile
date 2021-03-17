# build: docker build --force-rm -t test/daisyapi .
# run: docker run --rm -it --name daisyapi -p 5000:5000 test/daisyapi
FROM python:3

WORKDIR /app

COPY . .

RUN make deps

ENV FLASK_APP apps

ENV FLASK_ENV development

CMD ["flask", "run" , "--host=0.0.0.0", "--port=5000"]
