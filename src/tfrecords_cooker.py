import os
import toolbox
import numpy as np
import tensorflow as tf
from PIL import Image


def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


dir_parent = os.path.dirname(os.getcwd())
dir_food = dir_parent + '/food'
if not os.path.exists(dir_food):
    os.mkdir(dir_food)
    print('dir food is not exist, made it')

paths = []
cdts = []
labels5 = []
labels4 = []
deltas5 = []
deltas4 = []
wastes = []
originals = []
name_food_cd = '{}/food/cd.tfrecords'.format(dir_parent)
name_food_pd = '{}/food/pd.tfrecords'.format(dir_parent)

writer_cd = tf.python_io.TFRecordWriter(name_food_cd)
writer_pd = tf.python_io.TFRecordWriter(name_food_pd)

here = 0
end = 633
while here <= end:
    name_gridmap = '{}/dataset/{}gridmap.png'.format(dir_parent, here)
    name_cdt = '{}/dataset/{}condition.csv'.format(dir_parent, here)
    name_label = '{}/dataset/{}label.csv'.format(dir_parent, here)
    print(here)
    here += 1
    if not os.path.exists(name_label):
        wastes.append(name_label)
        # print(name_label + ' is not exist')
        continue

    gridmap = np.array(Image.open(name_gridmap).convert(mode='RGB'), dtype=np.float32) / 255
    label = np.array(toolbox.read_csv(name_label), dtype=np.float32)
    cdt = np.array(toolbox.read_csv(name_cdt, delimiter=' '), dtype=np.float32)
    if cdt.shape[0] > 5:
        print(name_cdt + 'is over size')
    if cdt.shape[0] < 5:
        print(name_cdt + 'is below size')
        while cdt.shape[0] < 5:
            cdt = np.append(cdt, [cdt[-1, :]], 0)
            label = np.append(label, [label[-1, :]], 0)
    if cdt.shape[0] < 5:
        print('is not enough')
    delta5 = label - cdt
    delta4 = delta5[1:, :]

    example_cd = tf.train.Example(features=tf.train.Features(feature={
        'data': _bytes_feature(gridmap.tostring()),
        'label': _bytes_feature(delta5.tostring())}))

    writer_cd.write(example_cd.SerializeToString())

    example_pd = tf.train.Example(features=tf.train.Features(feature={
        'data': _bytes_feature(gridmap.tostring()),
        'label': _bytes_feature(delta4.tostring())}))

    writer_pd.write(example_pd.SerializeToString())

writer_cd.close()
writer_pd.close()

# reconstructed_images = []
# record_iterator = tf.python_io.tf_record_iterator(path=name_food_cld)
# for string_record in record_iterator:
#     example = tf.train.Example()
#     example.ParseFromString(string_record)
#
#     data_string = (example.features.feature['data'].bytes_list.value[0])
#
#     delta_string = (example.features.feature['mask_raw'].bytes_list.value[0])
#
#     img_1d = np.fromstring(data_string, dtype=np.float32)
#     reconstructed_img = img_1d.reshape((500, 500, -1))
#
#     delta_1d = np.fromstring(delta_string, dtype=np.float32)
#
#     # Annotations don't have depth (3rd dimension)
#     reconstructed_annotation = delta_1d.reshape((5, 3))
#
#     print(reconstructed_img[200, 300, 0])
#     print(reconstructed_annotation)
#
#     reconstructed_images.append((reconstructed_img, reconstructed_annotation))
