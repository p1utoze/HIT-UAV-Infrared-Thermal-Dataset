import json
import csv
import os
import pandas as pd
import pathlib

'''
TO create dir:
paste this in terminal:
> cd extracted; for i in train test val; do echo $i; mkdir $i; done; cd ..;
'''
target_dir = pathlib.Path('normal_json')
extracted_dir = pathlib.Path('extracted')
annotation_dir = target_dir / 'annotations'
data_split = ['train', 'val', 'test']

for folder in data_split:
    path = annotation_dir / f'{folder}.json'
    with open(path, 'r') as f:
        annotation_dict = json.loads(f.read())
    assert isinstance(annotation_dict['images'], list)
    print(annotation_dict['images'].__len__(), annotation_dict['annotation'].__len__())
    # print(json.dumps(annotation_dict['annotation'][0], indent=4))
    # print(json.dumps(annotation_dict['images'][0], indent=4))
    annote = pd.read_csv(f'{folder}_annote.csv')
    img = pd.read_csv(f'{folder}.csv')
    print(annote.head(3), img.head(3), sep='\n')
    df = pd.merge(annote, img, left_on='image_id', right_on='id')
    df.to_csv(f'{folder}_merged.csv', index=False)
    # pd.DataFrame(annotation_dict['images']).to_csv(f'{folder}.csv', index=False)
    # pd.DataFrame(annotation_dict['annotation']).to_csv(f'{folder}_annote.csv', index=False)
    # with open(extracted_dir / folder / fname, 'w') as f:
    #     f.write()
    # for i, (image, annote) in enumerate(zip(annotation_dict['images'], annotation_dict['annotation'])):
    #     s = f'ID: {image['id']} didnt match Annote ID: {annote['image_id']}'
    #     assert image['id'] == annote['image_id'], s
    #     assert (i == image['id'] and i == annote['image_id']), s


