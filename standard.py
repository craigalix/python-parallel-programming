import requests
import time

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
    with requests.Session() as session:
        for i in range(50):
            fetchBoth("HiLow", session, URL)
    end = time.time()
    print("Total time taken = " + str(end-start))

if __name__ == "__main__":
    main()