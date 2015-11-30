#!/usr/bin/env python3.4
import sys, time
import pymongo as mongo
import redis

# connect to redis & mongodb
redis = redis.Redis()
mongodb = mongo.MongoClient()
collection = mongodb.test_database['test-collection']
collection.ensure_index('key', unique=True)

def mongo_set(data):
    for k in data:
        collection.insert_one({"key": k, "value": data[k]})

def mongo_get(data):
    for k in data:
        val = collection.find_one({"key": k})

def redis_set(data):
    for k in data:
        redis.set(k, data[k])

def redis_get(data):
    for k in data:
        val = redis.get(k)

def do_tests(num, tests):
    # setup dict with key/values to retrieve
    data = {'key' + str(i): 'val' + str(i)*100 for i in range(num)}
    # run tests
    for test in tests:
        start = time.time()
        test(data)
        elapsed = time.time() - start
        print ("Completed %s: %d ops in %.2f seconds : %.1f ops/sec" %\
              (test.__name__, num, elapsed, num / elapsed))

if __name__ == '__main__':
    num = 1000 if len(sys.argv) == 1 else int(sys.argv[1])
    tests = [mongo_set, mongo_get,redis_set, redis_get]
    do_tests(num, tests)