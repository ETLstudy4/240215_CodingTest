import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 실행 시간: {end - start}초")
        return result
    return wrapper

@timer
def example_function():
    time.sleep(1)
    print("함수 실행 완료")

example_function()