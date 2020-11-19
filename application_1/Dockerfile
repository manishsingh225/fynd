FROM python:3.7-slim


WORKDIR /opt
COPY . .


RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python", "app.py" ]