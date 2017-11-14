# нейросеть конохена
# определить размер изображения, например 50 на 50,то есть входов в нашу нейронную сеть будет 50 * 50
#цифр всего 10, то есть нейронов будет 10 - по одному на аждый ответ
# https://habrahabr.ru/post/143668/
# Каждая связь входа сети с нейроном имеет свой вес. Импульс, проходя через связь, меняется: импульс = импульс * вес_связи.
# Нейрон получает импульсы от всех входов и просто суммирует их. Нейрон набравший больший суммарный импульс побеждает. Все просто, реализуем!


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf

FLAGS = None
inputCount = 28 * 28
neuronCount = 10

class Link:
    # Нейрон
    neuron = None
    #     вес связи
    weight = None
    def __init__(self, neuron, weight):
        self.neuron = neuron
        self.weight = weight


class Neuron:
    # имя нейрона
    name = "Neuron "
    digit = None
    # все входы нейрона
    # incomingLinks = []
    power = None

    def __init__(self, number):
        self.incomingLinks = []
        self.digit = number
        self.name += str(number)
        self.power = 0


# Входы в нейроны
class Input:
    def __init__ (self):
        self.OutgoingLinks = []


class KohonenNetWork:
    _inputs = []
    _neurons = []

    def __init__(self):
        print ("Инит сетки")
        for i in range(inputCount):
            self._inputs.append(Input())

        for i in range(neuronCount):
            self._neurons.append(Neuron(i))

        for index_link in range(len(self._inputs)):
            for index_neuron in range(len(self._neurons)):
                link = Link(self._neurons[index_neuron], 0.0)
                self._inputs[index_link].OutgoingLinks.append(link)
                self._neurons[index_neuron].incomingLinks.append(link)


    def Handle(self, image):
        q = 0
        for i in image:
            print(round(i,2), end = " ")
            q += 1
            if q%28 == 0:
                print ()



        for i in range(len(self._inputs)):
            input_neuron = self._inputs[i]
            for outgoingLink in input_neuron.OutgoingLinks:
                outgoingLink.neuron.power += outgoingLink.weight * image[i]

        # for n in self._neurons:
        #     print(n.power)

        max_index = 0
        max_power = 0

        for neuron in self._neurons:
            if neuron.power > max_power:
                max_power = neuron.power
                max_index = neuron.digit

        # Снять импульс со всех нейронов
        for neuron in self._neurons:
            print (neuron.power)
            neuron.power = 0

        return max_index

    # обучение = изменение весов связей
    def study(self, image, answer):
        neuron = self._neurons[answer.index(1)]
        for i in range(len(neuron.incomingLinks)):
            neuron.incomingLinks[i].weight += 0.5 * (image[i] - neuron.incomingLinks[i].weight)



def main(_):
    pass

    # mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)
    # kn = KohonenNetWork()
    # for _ in range(10000):
    #     batch_xs, batch_ys = mnist.train.next_batch(1)
    #     kn.study(list(batch_xs[0]), list(batch_ys[0]))
    # print ("Я обучилась")
    # # проверка
    # batch_xs, batch_ys = mnist.train.next_batch(1)
    # qq = kn.Handle(list(*batch_xs))
    # print (batch_ys, qq)


# if __name__ == '__main__':
  # parser = argparse.ArgumentParser()
  # parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/input_data',
  #                     help='Directory for storing input data')
  # FLAGS, unparsed = parser.parse_known_args()
  # tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
