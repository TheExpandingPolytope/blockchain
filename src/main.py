from hashlib import sha256
import json
import time


class block:
    def __init__(self, index, data, time, prev_hash):
        self.index = index
        self.data = data
        self.time = time
        self.prev_hash = prev_hash

    def get_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True) # The string equivalent also considers the previous_hash field now
        return sha256(block_string.encode()).hexdigest()

class chain:
    def __init__(self):
        self.chain = []
        self.genesis_block()

    def genesis_block(self):
        gen_block = block(0, [], time.time(), "0")
        gen_block.hash = gen_block.get_hash()
    