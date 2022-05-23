FROM python:latest

RUN mkdir /usr/src/project
RUN mkdir /root/.kaggle

COPY kaggle.json /root/.kaggle
COPY requirements.txt ./usr/src/project

COPY ./constants.py /usr/src/project/
COPY ./utils.py /usr/src/project/
COPY ./remote_operations.py /usr/src/project/
COPY ./main.py /usr/src/project/

WORKDIR /usr/src/project/

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]