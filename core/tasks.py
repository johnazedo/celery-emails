from celery.decorators import task
import time

@task(name="sleep")
def to_sleep(period: int):
    for i in range(period):
        time.sleep(1)
        print(i)
    
    return None