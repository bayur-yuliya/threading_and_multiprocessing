import concurrent.futures


def even_numbers(nums):
    for even_num in range(1, nums + 1):
        if even_num % 2 == 0:
            print(f"Четное число - {even_num}")


def odd_numbers(nums):
    for odd_num in range(1, nums + 1):
        if odd_num % 2 != 0:
            print(f"Нечетное число - {odd_num}")


if __name__ == "__main__":
    nums_amount = 20

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(even_numbers, nums_amount)
        executor.submit(odd_numbers, nums_amount)
