FROM jupyter/pyspark-notebook

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN conda install -c conda-forge scikit-surprise

USER root

RUN apt-get -y update && apt-get -y install vim