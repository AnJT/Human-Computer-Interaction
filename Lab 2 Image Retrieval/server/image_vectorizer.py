################################################################################################################################
# This file is used to extract features from dataset and save it on disc
# inputs: 
# outputs: 
################################################################################################################################

import random
import tensorflow._api.v2.compat.v1 as tf
import numpy as np
import os
import pickle
from tensorflow.python.platform import gfile
from tqdm import tqdm
import json

BOTTLENECK_TENSOR_NAME = 'pool_3/_reshape:0'
BOTTLENECK_TENSOR_SIZE = 2048
MODEL_INPUT_WIDTH = 299
MODEL_INPUT_HEIGHT = 299
MODEL_INPUT_DEPTH = 3
JPEG_DATA_TENSOR_NAME = 'DecodeJpeg/contents:0'
RESIZED_INPUT_TENSOR_NAME = 'ResizeBilinear:0'
MAX_NUM_IMAGES_PER_CLASS = 2 ** 27 - 1  # ~134M


def create_inception_graph():
    """
    Creates a graph from saved GraphDef file and returns a Graph object.

    Returns:
        Graph holding the trained Inception network, and various tensors we'll be
        manipulating.
    """
    with tf.Session() as sess:
        model_filename = os.path.join('imagenet', 'classify_image_graph_def.pb')
        with gfile.FastGFile(model_filename, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            bottleneck_tensor, jpeg_data_tensor, resized_input_tensor = (
                tf.import_graph_def(graph_def, name='', return_elements=[
                    BOTTLENECK_TENSOR_NAME, JPEG_DATA_TENSOR_NAME,
                    RESIZED_INPUT_TENSOR_NAME]))
    return sess.graph, bottleneck_tensor, jpeg_data_tensor, resized_input_tensor


def run_bottleneck_on_image(sess, image_data, image_data_tensor,
                            bottleneck_tensor):
    bottleneck_values = sess.run(
        bottleneck_tensor,
        {image_data_tensor: image_data})
    bottleneck_values = np.squeeze(bottleneck_values)
    return bottleneck_values


def iter_files(rootDir):
    all_files = []
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            file_name = os.path.join(root, file)
            all_files.append(file_name)
        for dirname in dirs:
            iter_files(dirname)
    return all_files

if __name__ == '__main__':
    all_files = iter_files('database/dataset') # len: 2955
    random.shuffle(all_files)

    num_images = min(10000, len(all_files))
    neighbor_list = all_files[:num_images]

    with open('neighbor_list_recom.pickle', 'wb') as f:
        pickle.dump(neighbor_list, f)
    print("saved neighbour list")

    extracted_features = np.ndarray((num_images, 2048))
    sess = tf.Session()
    graph, bottleneck_tensor, jpeg_data_tensor, resized_image_tensor = (create_inception_graph())

    for i, filename in tqdm(enumerate(neighbor_list), total=num_images, desc='Extract features'):

        image_data = gfile.FastGFile(filename, 'rb').read()
        features = run_bottleneck_on_image(sess, image_data, jpeg_data_tensor, bottleneck_tensor)

        extracted_features[i:i + 1] = features

    np.savetxt("saved_features_recom.txt", extracted_features)
    print("saved exttracted features")

    tag_dict = {}
    for tag_file in os.listdir('database/tags'):
        if tag_file == 'README.txt' or tag_file.endswith('_r1.txt'):
            continue
        tag = tag_file.split('.')[0]
        tag_file_path = os.path.join('database/tags', tag_file)
        with open(tag_file_path, 'r') as f:
            for line in f.readlines():
                tag_dict[f'im{line.strip()}.jpg'] = tag
    with open('tag_dict.json','w') as f:
        json.dump(tag_dict, f, ensure_ascii=False, indent=4, separators=(',', ':'))