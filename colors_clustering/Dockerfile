FROM python:latest

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN mkdir /usr/src/project

COPY requirements.txt /usr/src/project

COPY classes.py /usr/src/project/
COPY constants.py /usr/src/project/
COPY utils.py /usr/src/project/
COPY color_clustering.py /usr/src/project/
COPY main.py /usr/src/project/

WORKDIR /usr/src/project/

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]