from distobjects import RedisBackend, DObject
from distobjects.fields import TextField
import redis
import logging

r = redis.Redis(host='localhost', port=6379, db=5)
redis_backend = RedisBackend(client=r)


class MyStudent(DObject):
    class Meta:
        backend = redis_backend

    first_name = TextField()
    last_name = TextField()

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)

    logging.info("Writing MyStudent 1")
    student1 = MyStudent("1")
    student1.first_name = "Harry"
    student1.last_name = "James"

    logging.info("Deleting from current process memory")
    del student1

    logging.info("Reading")
    student = MyStudent("1")
    logging.info("first_name is {}".format(student.first_name))
    logging.info("full_name is {}".format(student.full_name))

    logging.info("Updating")
    student.last_name = "Potter"

    logging.info("Deleting from current process memory and reading the updated")
    del student
    student_updated = MyStudent("1")
    logging.info("full_name is {}".format(student_updated.full_name))

    logging.info("Clearing object in backend(redis)")
    student_to_be_deleted = MyStudent("1")
    student_to_be_deleted.clear()

    logging.info("Verifying live update after clearing in backend")
    logging.info("full_name is {}".format(student_updated.full_name))
   
