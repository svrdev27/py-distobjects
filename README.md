# py-distobjects

**py-distobjects** (Python Distributed Objects) is a Python ORM/ODM library to easily map Objects to Caching Systems like Redis.
### Install
py-distobjects is available on PyPI:
```console
$ pip install distobjects
```
if you don't have pip command use -m pip
```console
$ python -m pip install distobjects
```

### Usage
- Simply define classes with minimum schema and connect to a backend
- Create objects from those classes and use them as if they are regualer objects
- Even Concurrent Access from multiple hosts will work as long as conntected to same backend
- You can update the object from any Host/Process, you can access the updated values instently from other Hosts/Processes by just reading attribute without explicit refresh/reading

### Why? when i can use redis directly
- Same reson as why we use ORMs for Database access when we can use SQL directly
- No need to worry about keys, values, Serialization, and Deserialization etc. all over the code.
- It just makes it easily organize/maintain the code by abstracting some functions

### Creating object in host1
```python
>>> from distobjects import RedisBackend, DObject
>>> from distobjects.fields import TextField
>>> import redis
>>>
>>> r = redis.Redis(host='redis-server1', port=6379, db=5)
>>> redis_backend = RedisBackend(client=r)
>>> class MyStudent(DObject):
...    class Meta:
...        backend = redis_backend
...    first_name = TextField()
...    last_name = TextField()
...
>>> student1 = MyStudent("1")
>>> student1.first_name = "Harry"
>>> student1.last_name = "James"
```

### Reading object in host2
```python
>>> from distobjects import RedisBackend, DObject
>>> from distobjects.fields import TextField
>>> import redis
>>>
>>> r = redis.Redis(host='redis-server1', port=6379, db=5)
>>> redis_backend = RedisBackend(client=r)
>>> class MyStudent(DObject):
...    class Meta:
...        backend = redis_backend
...    first_name = TextField()
...    last_name = TextField()
...
>>> student = MyStudent("1")
>>> student
<__main__.MyStudent object at 0x105bc29d0>
>>> student.first_name
'Harry'
>>> student.last_name
'James'
```
