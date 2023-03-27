import requests
import time
from concurrent.futures import ThreadPoolExecutor

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
    with ThreadPoolExecutor(max_workers=100) as executor:
        with requests.Session() as session:
            executor.map(fetchBoth, ["Hello"]*100, [session]*100, [URL]*100)
    ##
    end = time.time()
    print("Total time taken = " + str(end-start))

if __name__ == "__main__":
    main()