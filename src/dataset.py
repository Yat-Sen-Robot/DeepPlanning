import tensorflow as tf
import numpy as np
import os


class DatasetHolder:
    def __init__(self, food_type='gpld', file_type='tfrecords', menu=None):
        self.dir_parent = os.path.dirname(os.getcwd())
        self.file_type = file_type
        self.food_type = food_type
        self.menu = menu
        self.gridmap_shape = (500, 500, 3)
        if self.food_type == 'gpld':
            self.label_shape = (4, 3)
        elif self.food_type == 'gcld':
            self.label_shape = (5, 3)
        else:
            raise NameError('wrong food name')
        self.header = {'gridmap': tf.FixedLenFeature(shape=(), dtype=tf.string),
                       'condition': tf.FixedLenFeature(shape=(), dtype=tf.string),
                       'label': tf.FixedLenFeature(shape=(), dtype=tf.string),
                       'delta': tf.FixedLenFeature(shape=(), dtype=tf.string)}

    def _parse_features(self, proto):
        header = self.header
        parsed_features = tf.parse_single_example(proto, header)
        features = []
        for key in self.menu:
            x = tf.decode_raw(parsed_features[key], tf.float32)
            if key == 'gridmap':
                x = tf.reshape(x, self.gridmap_shape) / 255
            else:
                x = tf.reshape(x, self.label_shape)
            features.append(x)
        return tuple(features)

    def create_dataset(self, use_for='train', batch_size=1, shuffle_buffer=100, num_parallel_calls=4):
        dir_raw = '{}/food/{}_{}.{}'.format(self.dir_parent, self.food_type, use_for, self.file_type)
        dataset = tf.data.TFRecordDataset(dir_raw)
        dataset = dataset.map(self._parse_features, num_parallel_calls=num_parallel_calls)

        # This dataset will go on forever
        dataset = dataset.repeat()

        # Set the number of datapoints you want to load and shuffle
        dataset = dataset.shuffle(shuffle_buffer)

        # Set the batchsize
        dataset = dataset.batch(batch_size)

        # # Create an iterator
        # iterator = dataset.make_one_shot_iterator()
        # # Create your tf representation of the iterator
        # gridmap, delta = iterator.get_next()

        return dataset

    def my_accuracy(self, y_true, y_pred, **kwargs):
        threshold = [0.5, 0.5, np.radians(3)]
        limit = self.label_shape[0] * self.label_shape[1]

        y_pred = tf.convert_to_tensor(y_pred)
        y_true = tf.cast(y_true, y_pred.dtype)
        threshold = tf.cast(threshold, y_pred.dtype)
        limit = tf.cast(limit, y_pred.dtype)

        x = tf.abs(y_pred - y_true)
        x = tf.cast(x < threshold, y_pred.dtype)
        x = tf.reduce_sum(x, axis=-1)
        x = tf.reduce_sum(x, axis=-1)
        x = tf.cast(x >= limit, tf.float32)
        x = tf.keras.backend.mean(x, axis=-1)
        return x
