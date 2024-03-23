import services.eos_merge as eos_merge
import services.eos_generator as eos_generator

class TaskManager:

    def __init__(self, request_type, payload):
        self.request_type = request_type
        self.payload = payload
        self.__choice_table = {
            "eos_merge": eos_merge.run,
            "eos_generator": eos_generator.run,
        }

    def invoke(self):
        return self.__choice_table[self.request_type](self.payload)
