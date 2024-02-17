import json
import requests
import threading


def make_request(url, data):
    request = requests.get(url)
    data.append(request.json())


if __name__ == "__main__":
    urls = [
        'https://httpbin.org/delay/4',
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/3',
        'https://httpbin.org/delay/3',
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/4',
        'https://httpbin.org/delay/5',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/2'
    ]

    data = []
    threads = []

    for url in urls:
        thread_by_url = threading.Thread(target=make_request, args=(url, data))
        threads.append(thread_by_url)
        thread_by_url.start()
    for thread_by_url in threads:
        thread_by_url.join()

    with open('requests_file.json', 'w') as file:
        json.dump(data, file)
