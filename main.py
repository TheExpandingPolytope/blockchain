from hashlib import sha256
import json
import time


class block:
    def __init__(self, index, data, time, prev_hash):
        self.index = index
        self.data = data
        self.time = time
        self.prev_hash = prev_hash

    def hash(data):
        block_string = json.dumps(self.__dict__, sort_keys=True) # The string equivalent also considers the previous_hash field now
        return sha256(block_string.encode()).hexdigest()