FROM ubuntu:jammy

ARG DEBIAN_FRONTEND=noninteractive

RUN : \
    && apt-get update \
    && apt-get install --no-install-recommends -y \
    python3-requests \
    python-is-python3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY dotascraper.py /usr/bin/

CMD ["dotascraper.py"]
