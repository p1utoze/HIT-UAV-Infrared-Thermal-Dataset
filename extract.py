import json
import csv
import os
import pandas as pd
import pathlib
import ast

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
    # for file in os.listdir(extracted_dir / folder):
    #     with open(extracted_dir / folder / file, 'w+') as f:
    #         lines = f.readlines()
    #         lines = '\n'.join([line.strip() for line in lines])
    #         f.write(lines)

    df = pd.read_csv(f'{folder}_merged.csv')
    df = df.loc[df['category_id'] == 0]
    df['bbox'] = df['bbox'].map(ast.literal_eval).map(lambda x: " ".join(map(str, x)))
    print(df.head())
    assert df['image_id'].nunique() == df['filename'].nunique(), "FILENAME AND IMAGE ID DONT MATCH"
    for id, file in zip(df['image_id'].unique(), df['filename'].unique()):
        file = file.replace('jpg', 'txt')
        path = extracted_dir / folder / file
        with open(path, 'w') as f:
            s = df.loc[df['image_id'] == id, 'bbox'].map(lambda x: x.strip()).to_string(f, index=False, header=False)

    # pd.DataFrame(annotation_dict['images']).to_csv(f'{folder}.csv', index=False)
    # pd.DataFrame(annotation_dict['annotation']).to_csv(f'{folder}_annote.csv', index=False)
    # with open(extracted_dir / folder / fname, 'w') as f:
    #     f.write()
    # for i, (image, annote) in enumerate(zip(annotation_dict['images'], annotation_dict['annotation'])):
    #     s = f'ID: {image['id']} didnt match Annote ID: {annote['image_id']}'
    #     assert image['id'] == annote['image_id'], s
    #     assert (i == image['id'] and i == annote['image_id']), s


