import time
import requests
import concurrent.futures


def make_request(url):
    requests.get(url)


def multiple_request(urls):
    start_time = time.time()
    for url in urls:
        make_request(url)
    stop_time = time.time()
    return stop_time - start_time


def thread_requests(urls):
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(5) as executor:
        executor.map(make_request, urls)
    stop_time = time.time()
    return stop_time - start_time


if __name__ == "__main__":
    url = ['https://httpbin.org/delay/4']

    count_requests = 3
    total_execution_time_multiple_requests = 0
    total_execution_time_thread_requests = 0

    for _ in range(count_requests):
        total_execution_time_multiple_requests += multiple_request(url)
        total_execution_time_thread_requests += thread_requests(url)

    if total_execution_time_multiple_requests < total_execution_time_thread_requests:
        time = str(abs((total_execution_time_multiple_requests - total_execution_time_thread_requests)/count_requests))
        print(f"Последовательные запросы быстрее на: {time} секунд в среднем")
    else:
        time = str(abs((total_execution_time_thread_requests - total_execution_time_multiple_requests)/count_requests))
        print(f"Параллельные запросы быстрее на: {time} секунд в среднем")
