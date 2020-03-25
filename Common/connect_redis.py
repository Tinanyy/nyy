import redis

class Task(object):
    def __init__(self,phone):
        self.rc = redis.ConnectionPool(host='',password='',port=6379,decode_responses=True,db = 1)
        self.r = redis.Redis(connection_pool=self.rc)

        self.queue = 'CAPTCHA:USER'+ ':' + str(phone)

    def listen_task(self):
        while True:
            queue = self.r.get(self.queue)

            break
        return queue


if __name__ == '__main__':
    print(Task(15526236892).listen_task())

