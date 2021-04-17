import time
from uuid import uuid4
from storage import MongodbService

storage = MongodbService.get_instance()

for _ in range(5):
    dto = {
        "_id": str(uuid4()),
        "payload": str(uuid4()),
        "time_stemp": str(int(time.time()))
    }
    storage.set_data(dto)

for data in storage.get_data():
    print(data)