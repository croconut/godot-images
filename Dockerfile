FROM ubuntu:20.04

RUN apt-get update && apt-get install -y wget curl python3 python3-pip unzip
RUN pip3 install beautifulsoup4 requests

COPY ./download_single.sh /download_single.sh
COPY ./download_all.py /download_all.py

RUN chmod u+x /download_single.sh
RUN chmod u+x /download_all.py

RUN python3 /download_all.py

RUN rm -rf /download_all.py /download_single.sh
