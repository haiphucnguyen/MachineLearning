import os
import numpy as np

import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import time


class Model:
    def __init__(self):
        print("Init Globals")

    @staticmethod
    def loadModel():
        print('START LOADING MODEL>>>>>>>>>>.........')
        start_time = time.time()

        sys.path.append("./models-1.13.0/research")
        from object_detection.utils import label_map_util
        # What model to download.
        MODEL_NAME = 'ssd_mobilenet_v2_coco_2018_03_29'
        MODEL_FILE = MODEL_NAME + '.tar.gz'
        DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'

        # Path to frozen detection graph. This is the actual model that is used for the object detection.
        PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

        # List of the strings that is used to add correct label for each box.
        PATH_TO_LABELS = os.path.join(os.getcwd(),
                                      'models-1.13.0/research/object_detection/data/mscoco_label_map.pbtxt')

        NUM_CLASSES = 90
        IMAGE_SIZE = (20, 16)

        opener = urllib.request.URLopener()
        opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
        tar_file = tarfile.open(MODEL_FILE)
        for file in tar_file.getmembers():
            file_name = os.path.basename(file.name)
            if 'frozen_inference_graph.pb' in file_name:
                tar_file.extract(file, os.getcwd())

        detection_graph = tf.Graph()
        with detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

        label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
        categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, \
                                                                    use_display_name=True)
        category_index = label_map_util.create_category_index(categories)

        Model.category_index = category_index
        Model.detection_graph = detection_graph
        print('STOP LOADING MODEL>>>>>>>>>>.........')
        print("--- %s seconds ---" % (time.time() - start_time))


Model.loadModel()