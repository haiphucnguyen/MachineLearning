FROM jupyter/tensorflow-notebook

COPY app /app

USER root

RUN sudo apt-get update && apt-get install -y protobuf-compiler python-pil python-lxml python-tk

USER $NB_UID

RUN pip install --user Cython contextlib2 matplotlib Flask mpld3 opencv-python

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"