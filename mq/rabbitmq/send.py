# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-7-3 上午10:13
@Desc :
'''
import time
import names
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

i = 0
while True:
    time.sleep(3)
    name = names.get_full_name()
    channel.basic_publish(exchange='', routing_key='hello', body=name)
    i = i + 1
    print(" {} Sent {}".format(i, name))
    # connection.close()
