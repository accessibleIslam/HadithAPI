import json
import os
from collections import namedtuple

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

f = open(os.path.join("./JSONFiles", "eng-bukhari.json"), "r", encoding="utf-8")
hadithData = f.read()
f.close()

x = json2obj(hadithData)
print(x.metadata)
