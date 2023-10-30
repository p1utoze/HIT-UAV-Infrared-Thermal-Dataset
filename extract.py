import json
import csv
import os
import pandas
import pathlib

target_dir = pathlib.Path('normal_json')
extracted_dir = pathlib.Path('extracted')
annotation_dir = target_dir / 'annotations'
data_split = ['train', 'val', 'test']

with open(extracted_dir / data_split[0] / 'smtg.txt', 'w') as f:
    s = 'aditya'
    f.write(s)
with open(annotation_dir / 'train.json', 'r') as f:
    annotation_dir = json.loads(f.read())
    assert isinstance(annotation_dir['images'], list)
    print(json.dumps(annotation_dir['annotation'][1], indent=4))
    print(json.dumps(annotation_dir['images'][1], indent=4))

    for i, (image, annote) in enumerate(zip(annotation_dir['images'], annotation_dir['annotation'])):
        assert image['id'] == annote['id']
        assert (i == image['id'] and i == annote['id'])

    print('DONE')

