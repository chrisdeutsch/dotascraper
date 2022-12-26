#!/usr/bin/env bash
timestamp="$(date '+%Y_%m_%d-%H_%M')"

docker run \
       --rm \
       -v /home/chris/dotascraper/data:/data:rw \
       --user "$(id -u):$(id -g)" \
       dotascraper \
       dotascraper.py "/data/${timestamp}.json.gz" -n 10
