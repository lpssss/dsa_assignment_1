# code to generate a dataset from UTMCS000 to UTMCS999

import random
import json
import os

def generate_dataset():
    NUM_ELEMENTS = [100, 500, 1000]

    dataset = []
    for i in range(max(NUM_ELEMENTS)):
        dataset.append('UTMCS' + str(i).zfill(3))
    
    # first dataset: nearly ordered dataset, swap 019 and 020
    dataset[19], dataset[20] = dataset[20], dataset[19]

    # save the dataset to json
    folder_name = "near_ordered_dataset"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for num_elements in NUM_ELEMENTS:
        dataset_filename = os.path.join(folder_name, 'dataset_' + str(num_elements) + '.json')
        with open(dataset_filename, 'w') as f:
            json.dump(dataset[:num_elements], f)

    # second dataset: random dataset
    seed = 42
    random.seed(seed)

    # shuffle the dataset
    random.shuffle(dataset)

    # save the dataset to json
    folder_name = "random_dataset"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for num_elements in NUM_ELEMENTS:
        dataset_filename = os.path.join(folder_name, 'dataset_' + str(num_elements) + '.json')
        with open(dataset_filename, 'w') as f:
            json.dump(dataset[:num_elements], f)

if __name__ == '__main__':
    generate_dataset()
    print('dataset generated')