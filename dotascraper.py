#!/usr/bin/env python
import argparse
import gzip
import json
import sys
import time

import requests


def scrape(num=1):
    matches = []

    for i in range(num):
        params = None
        if len(matches):
            min_match_id = min(match["match_id"] for match in matches)
            params = {"less_than_match_id": min_match_id}

        r = requests.get("https://api.opendota.com/api/publicMatches",
                         params=params)
        if not r.ok:
            raise RuntimeError(f"Could not access API endpoint. Returned {r.status_code}.")

        matches += r.json()
        time.sleep(1)

    return matches


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("outfile")
    parser.add_argument("-n", "--num", default=1, type=int)
    args = parser.parse_args(args)

    matches = scrape(args.num)

    with gzip.open(args.outfile, "wt", encoding="utf-8") as fout:
        json.dump(matches, fout)

    return 0


if __name__ == "__main__":
    sys.exit(main())
