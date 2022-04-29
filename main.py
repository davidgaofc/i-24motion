import logging
#import ecs_logging
import time
from random import randint
import sys
from logstash_async.handler import AsynchronousLogstashHandler
import logstash
from src.logger import Logger

myLogger = Logger('myLogger', 'DB')

print("Generating log entries...")

messages = [
    "Message1",#
    "Message2",
    "Message3",
    "Message4",
    "Message5",
    "Message6",
    "Message7",
    "Message8",
    "Message9",
    "Message10",
    "Message11",
    "Message12",
    "Message13",
    "Message14",
    "Message15"
    ]
extra = {
    'test_string': 'post processing',
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 4, 'c': 6},
    'test_float': 1.23,
    'test_integer': 123,
    'test_list': [1, 2, 7],
}

extra1 = {
    'test_string': 'computer vision',
    'test_boolean': False,
    'test_dict': {'a': 1, 'b': 3, 'c': 4},
    'test_float': 4.23,
    'test_integer': 23,
    'test_list': [1, 4, 3],
}

extra2 = {
    'test_string': 'camera 1',
    'test_boolean': False,
    'test_dict': {'a': 5, 'b': 2, 'c': 3},
    'test_float': 4.75,
    'test_integer': 89,
    'test_list': [7, 3, 7],
}

extra3 = {
    'test_string': 'camera 2',
    'test_boolean': True,
    'test_dict': {'a': 7, 'b': 3, 'c': 1},
    'test_float': 8.23,
    'test_integer': 3,
    'test_list': [21, 25, 1],
}

while True:
    random1 = randint(0,15)
    random2 = randint(1,10)
    if random1 > 11:
        random1 = 0
    if(random1<=4):
        myLogger.info(messages[random1], extra=extra)
    elif(random1>=5 and random1<=8):
        myLogger.warning(messages[random1], extra=extra1)
    elif(random1>=9 and random1<=10):
        myLogger.error(messages[random1], extra=extra2)
    else:
        myLogger.critical(messages[random1], extra=extra3)
    time.sleep(3)

