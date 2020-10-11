import time
def job_scheduler(f, n):
    time.sleep(n / 1000)
    return f


def add_two_numbers(a, b):
    return a + b

#Driver code
print(job_scheduler(add_two_numbers(1, 2), 5000))