FROM jupyter/tensorflow-notebook

COPY app /app

USER root

RUN sudo apt-get update && apt-get install -y protobuf-compiler python-pil python-tk

USER $NB_UID

RUN pip install --user Cython contextlib2 matplotlib Flask opencv-python tqdm lxml mpld3

RUN pip install --upgrade numpy

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"