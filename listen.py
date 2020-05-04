import json

import sseclient


if __name__ == '__main__':

    messages = sseclient.SSEClient('http://localhost:5000/listen')

    for msg in messages:
        print(msg)  # call print(dir(msg)) to see the available attributes
