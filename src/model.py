import tensorflow as tf
import numpy as np
import os
from datetime import datetime
from callback import PredictionCheckPoint


class Model:
    def __init__(self,
                 name='main',
                 build_core=None,
                 train_set=None, validation_set=None,
                 input_shape=None, output_shape=None, ipu_weight=None,
                 checkpoint=True, check_period=100, save_weights_only=True,
                 tensorboard=True, prediction_check=False,
                 earlystop=False, monitor='loss', min_delta=0.001, patience=100,
                 mode='auto', baseline=None,
                 optimizer=tf.keras.optimizers.Adam(),
                 loss='logcosh',
                 metrics=None,
                 epochs=4,
                 initial_epoch=0,
                 verbose=1,
                 steps_per_epoch=100,
                 batch_size=None,
                 validation_steps=10,
                 init_lr=0.001,
                 lr_drop=0.5,
                 lr_drop_freq=1000.0,
                 lr_step_drop=False):
        self.name = name
        self.build_core = build_core
        self.train_set = train_set
        self.validation_set = validation_set
        self.ipu_weight = ipu_weight

        self.epochs = epochs
        self.initial_epoch = initial_epoch
        self.steps_per_epoch = steps_per_epoch
        self.batch_size = batch_size
        self.validation_steps = validation_steps
        self.verbose = verbose
        self.init_lr = init_lr
        self.lr_drop = lr_drop
        self.lr_drop_freq = lr_drop_freq

        self.core = None
        self.output = None
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.ipu = tf.keras.applications.ResNet50(input_shape=self.input_shape,
                                                  weights=None,
                                                  include_top=False)
        self.ipu.load_weights(self.ipu_weight)
        self.oru = tf.keras.Sequential()
        self.oru.add(tf.keras.layers.Reshape(target_shape=self.output_shape,
                                             input_shape=(
                                             np.prod(self.output_shape),)))
        self.optimizer = optimizer
        self.metrics = metrics
        self.loss = loss

        self.dir_parent = os.path.dirname(os.getcwd())
        self.dir_log = '{}/logs/{}/'.format(self.dir_parent,
                                            self.name) + self.get_now_str()
        self.dir_checkpoint = '{}/logs/{}/'.format(self.dir_parent,
                                                   self.name) + 'checkpoint-{epoch}.h5'
        self.dir_model = '{}/logs/{}/'.format(self.dir_parent,
                                              self.name) + '{}.h5'.format(
            self.name)
        self.check_period = check_period
        self.lr_step_drop = lr_step_drop
        self.checkpoint = checkpoint
        self.tensorboard = tensorboard
        self.checkpoint = checkpoint
        self.earlystop = earlystop
        self.prediction_check = prediction_check
        self.callbacks = []

        self.save_weights_only = save_weights_only

        self.monitor = monitor
        self.min_delta = min_delta
        self.patience = patience
        self.mode = mode
        self.baseline = baseline
        if self.tensorboard:
            self.callbacks.append(
                tf.keras.callbacks.TensorBoard(log_dir=self.dir_log,
                                               write_graph=False))
        if self.lr_step_drop:
            self.callbacks.append(tf.keras.callbacks.LearningRateScheduler(
                schedule=self.step_decay))
        if self.checkpoint:
            self.callbacks.append(
                tf.keras.callbacks.ModelCheckpoint(filepath=self.dir_checkpoint,
                                                   monitor='loss',
                                                   save_weights_only=self.save_weights_only,
                                                   period=self.check_period))
        if self.earlystop:
            self.callbacks.append(
                tf.keras.callbacks.EarlyStopping(monitor=self.monitor,
                                                 min_delta=self.min_delta,
                                                 patience=self.patience,
                                                 verbose=self.verbose,
                                                 mode=self.mode,
                                                 baseline=self.baseline))
        if self.prediction_check:
            self.callbacks.append(
                PredictionCheckPoint(dir_parent=self.dir_parent))

    def compile(self):
        self.core = self.build_core(self.input_shape, self.output_shape,
                                    self.ipu, self.oru)
        self.core.compile(optimizer=tf.keras.optimizers.Adam(), loss=self.loss,
                          metrics=self.metrics)
        self.core.summary()

    def train(self):
        self.core.fit(self.train_set,
                      epochs=self.epochs,
                      initial_epoch=self.initial_epoch,
                      verbose=self.verbose,
                      steps_per_epoch=self.steps_per_epoch,
                      callbacks=self.callbacks,
                      batch_size=self.batch_size,
                      validation_data=self.validation_set,
                      validation_steps=self.validation_steps)

        self.core.save(self.dir_model)

    def step_decay(self, epoch):
        return self.init_lr * np.power(self.lr_drop, np.floor(
            (1 + epoch) / self.lr_drop_freq))

    @staticmethod
    def get_now_str():
        return str(datetime.now()).replace(' ', '-').replace(':', '-').replace(
            '.', '-')
