FROM ubuntu:20.04

RUN apt-get update && apt-get install -y wget curl python3 python3-pip unzip
RUN pip3 install beautifulsoup4 requests

COPY ./download_single.sh /download_single.sh
COPY ./setup_single_version.py /setup_single_version.py

RUN chmod u+x /download_single.sh
RUN chmod u+x /setup_single_version.py

ARG VERSION

RUN python3 /setup_single_version.py ${VERSION}

RUN rm -rf /setup_single_version.py /download_single.sh
