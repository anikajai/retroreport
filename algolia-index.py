from algoliasearch import algoliasearch
import json
import yaml


client = algoliasearch.Client("SIZJY7AJ5K", "ae8c3d9edcd1dd5ae5a6f5db0a69c668")
index = client.init_index("Oct29_index")

# fileHandle = open("source.json")
#
# items = yaml.load(fileHandle)
# index.add_objects(items)

index.setSettings({
  'attributesToHighlight': [
    'content'
  ]
});

res = index.search(
    "Court area assembly",
    {"attributesToRetrieve": "content, tag ", "hitsPerPage": 20}
)

print(res)