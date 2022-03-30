FROM python:3.9
ENV PYTHONNUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt-get update
RUN apt-get install -y gcc libavdevice-dev libavfilter-dev libopus-dev libvpx-dev pkg-config
RUN apt-get install -y locales
RUN sed -i -e 's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen \
ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU:ru
ENV LC_ALL ru_RU.UTF-8
COPY req.txt /code/
RUN pip install --upgrade pip
RUN pip install -r req.txt