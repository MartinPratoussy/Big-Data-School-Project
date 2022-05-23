FROM python:latest

RUN mkdir /usr/src/project

COPY requirements.txt /usr/src/project

COPY constants.py /usr/src/project/
COPY favorites.py /usr/src/project/
COPY main.py /usr/src/project/

WORKDIR /usr/src/project/

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]