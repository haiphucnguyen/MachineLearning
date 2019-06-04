FROM jupyter/tensorflow-notebook

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]