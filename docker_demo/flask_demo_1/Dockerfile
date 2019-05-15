FROM python:3.6-alpine
ENV VERSION=1.0 FLASK_APP="app.py" \
    NAME="Happy Feet" FLASK_DEBUG=1 \
    FLASK_RUN_HOST="0.0.0.0" FLASK_RUN_PORT=80
ADD . /code
WORKDIR /code
RUN pip install redis flask
CMD ["flask", "run"]