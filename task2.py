import time
import concurrent.futures


def squaring(nums):
    return list(map(lambda x: x ** 2, nums))


def counting_time(executor_obj, name, nums):
    start_time = time.time()
    executor_obj.submit(squaring, nums)
    time.sleep(2)
    end_time = time.time()
    execution_time = round(end_time - start_time, 5)
    print(f"Выполнение {name} заняло {execution_time} секунд")
    return execution_time


if __name__ == "__main__":
    nums_amount = list(range(1, 1000))

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        threading_time = counting_time(executor, "Thread", nums_amount)

    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        process_time = counting_time(executor, "Process", nums_amount)

    if threading_time < process_time:
        print(f"Thread быстрее на: {str(abs(threading_time - process_time))} секунд")
    else:
        print(f"Process быстрее на: {str(abs(process_time - threading_time))} секунд")
