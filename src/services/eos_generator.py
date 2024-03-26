import json 

def run(payload):
    print("Entering 'eos_generator.run'")
    print("payload:" + str(payload))

    # eos_data = payload["payload"]
    # print("eos_data.type:" + str(payload["type"]))

    return  {
        "payload": payload,
        "eos": [
            [1, 1],
            [2, 2],
            [3, 3],
        ]
    }

