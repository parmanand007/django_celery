from celery import shared_task

@shared_task(bind=True)
def test_func(self):
    print("start of delay========>")
    for i in range(10):
        print("pinting=========>",i)
    return "Done"