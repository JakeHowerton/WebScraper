#!/usr/bin/env python3

import concurrent.futures
import re
import time
import requests 


def scrape(url):
  try:
    response = requests.get(url, timeout=10)  #sends request and times out after 10s
    response.raise_for_status()  #for http error

    headings = re.findall(  #finds heading patterns
        r"<h[1-3][^>]*>(.*)</h[1-3]>", response.text, re.DOTALL
    )

    return list( 
        map(lambda x: re.sub(r"<[^>]+>", "", x).strip(), headings)
    )

  except requests.RequestException as error:
    print(f"Error fetching {url}: {error}")
    return []


def main():
  base = ("https://pnutz.h4x0r.space/courses/cse.20589.fa26") #CSE 20589 course page
  urls = [f"{base}/reading{i:02}.html" for i in range(1, 6)] #Scrapes only the first 5 reading assignments

  for workers in [1, 5]:
    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
      results = list(executor.map(scrape, urls))  #Scrapes all urls

    elapsed = time.perf_counter() - start  #Total time passed

    print(f"\n{workers} worker(s): {elapsed:.3f} seconds")

    for url, headings in zip(urls, results):  #Pairs url to its result
      print(f"\nURL: {url}")
      for heading in headings[:3]:
        print(f"  - {heading}")


if __name__ == "__main__":
  main()