FROM python:latest

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -ys

RUN mkdir /usr/src/project

COPY requirements.txt ./usr/src/project

COPY ./constants.py /usr/src/project/
COPY ./recommendation.py /usr/src/project/
COPY ./main.py /usr/src/project/

WORKDIR /usr/src/project/

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]