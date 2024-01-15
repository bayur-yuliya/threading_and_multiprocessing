import requests
from multiprocessing import Pool


def make_request(url):
    response = requests.get(url)
    return f"{url} - status: {response.status_code}"


if __name__ == "__main__":
    urls = [
        'https://httpbin.org/delay/4',
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/3',
        'https://httpbin.org/delay/3',
        'https://httpbin.org/delay/4',
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/3',
        'https://httpbin.org/delay/3',
        'https://httpbin.org/delay/4',
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/3',
        'https://httpbin.org/delay/3'
    ]

    with Pool(processes=5) as pool:
        results = pool.map(make_request, urls)

    for result in results:
        print(result)
