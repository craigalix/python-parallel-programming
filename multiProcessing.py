import requests
import time
from multiprocessing.pool import Pool

URL = 'https://httpbin.org/uuid'

def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])

def fetch1(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])

def fetchBoth(str, session, URL):
    print(str)
    fetch(session, URL)
    fetch1(session, URL)

def main():
    start = time.time()
    ##
    with Pool() as pool:
        with requests.Session() as session:
            pool.starmap(fetchBoth, [("HiLow",session, URL) for i in range(100)])
    ##
    end = time.time()
    print("Total time taken = " + str(end-start))

if __name__ == "__main__":
    main()