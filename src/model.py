from __future__ import print_function
import tensorflow as tf
import numpy as np
import os
import sys
from callback import WarmUpLRSchedule


class Model:
    def __init__(self, core, config, pipeline):
        self.core = core
        self.pipeline = pipeline
        self.root = os.getcwd()
        self.config = config
        self.callbacks = []
        self.startup()

    @property
    def optimizer(self):
        if self.config['Optimizer']['type'] == 'adam':
            return tf.keras.optimizers.Adam(
                lr=self.config['Optimizer']['lr'],
                beta_1=self.config['Optimizer']['beta_1'],
                beta_2=self.config['Optimizer']['beta_2'])

    def loss(self, y_true, y_pred):
        print ('hello')
        a_ = self.config['Model']['A']
        b_ = self.config['Model']['B']
        c_ = self.config['Model']['C']
        s_ = self.config['Model']['S']
        batch = self.config['Model']['batch']
        lam0 = self.config['Loss']['lam0']
        loss_crd, loss_cla, loss_obj = 0, 0, 0
        for j in range(batch):
            for i in range(b_):
                y_p = y_pred[j, :, :, i*(c_+a_):(i+1)*(c_+a_)]
                y_t = y_true[j, :, :, i*(c_+a_):(i+1)*(c_+a_)]
                mask = y_t[:, :, a_-1]
                crd_p = y_p[:, :, :a_-1] * tf.stack([mask]*(a_-1), axis=-1)
                crd_t = y_t[:, :, :a_-1]
                loss_crd += lam0 * tf.reduce_sum(tf.abs(crd_t - crd_p))

                cla_p = y_p[:, :, a_] * mask
                cla_t = y_t[:, :, a_]
                loss_cla += tf.keras.backend.binary_crossentropy(
                    target=tf.keras.backend.flatten(cla_t),
                    output=tf.keras.backend.flatten(cla_p))

                obj_p = y_p[:, :, a_ - 1]
                obj_t = y_t[:, :, a_ - 1]
                loss_obj += tf.keras.backend.binary_crossentropy(
                    target=tf.keras.backend.flatten(obj_t),
                    output=tf.keras.backend.flatten(obj_p))
        loss = loss_cla
        return loss

    def startup(self):
        self.set_callbacks()

    def compile(self):
        self.core.compile(optimizer=self.optimizer, loss=self.loss)
        self.core.summary()

    def train(self):
        self.core.fit_generator(
            generator=self.pipeline.train,
            steps_per_epoch=self.config['Model']['ts_step'],
            epochs=self.config['Model']['epoch'],
            initial_epoch=self.config['Model']['ini_epoch'],
            verbose=self.config['Model']['verbose'],
            callbacks=self.callbacks,
            validation_data=self.pipeline.valid,
            validation_steps=self.config['Model']['vs_step'])

        self.core.save(self.log_dir + os.sep + 'model.h5')

    def set_callbacks(self):
        if self.config['TensorBoard']['enable']:
            self.callbacks.append(tf.keras.callbacks.TensorBoard(
                log_dir=self.log_dir,
                write_graph=self.config['TensorBoard']['write_graph']))
        if self.config['LRSchedule']['enable']:
            self.callbacks.append(WarmUpLRSchedule(
                warm_up=self.warm_up,
                schedule=self.schedule))
        if self.config['CheckPoint']['enable']:
            self.callbacks.append(tf.keras.callbacks.ModelCheckpoint(
                filepath=self.log_dir + os.sep + 'checkpoint-{epoch}.h5',
                monitor=self.config['CheckPoint']['monitor'],
                save_weights_only=self.config['CheckPoint']['only_weights'],
                period=self.config['CheckPoint']['period']))
        if self.config['EarlyStop']['enable']:
            self.callbacks.append(tf.keras.callbacks.EarlyStopping(
                monitor=self.config['EarlyStop']['monitor'],
                min_delta=self.config['EarlyStop']['min_delta'],
                patience=self.config['EarlyStop']['min_delta'],
                verbose=self.config['EarlyStop']['verbose'],
                mode=self.config['EarlyStop']['mode']))

    def warm_up(self, batch):
        lr = self.config['Optimizer']['lr']
        wp_lr = self.config['LRSchedule']['wp_lr']
        wp_step = self.config['LRSchedule']['wp_step']
        if batch < wp_step:
            return wp_lr + (lr - wp_lr) * batch / (wp_step - 1)
        else:
            return lr

    def schedule(self, epoch):
        lr = self.config['Optimizer']['lr']
        epochs = self.config['Model']['epoch']
        if self.config['LRSchedule']['type'] == 'cosine':
            return 0.5 * (1 + np.cos(epoch / epochs * np.pi)) * lr

    @property
    def log_dir(self):
        return (self.root + os.sep + 'logs' +
                os.sep + self.config['Model']['name'])
