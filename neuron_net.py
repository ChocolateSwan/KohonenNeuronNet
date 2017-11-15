from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

FLAGS = None
inputCount = 28 * 28
neuronCount = 10


class Link:
    """связь"""
    neuron = None
    weight = None

    def __init__(self, neuron, weight):
        self.neuron = neuron
        self.weight = weight


class Neuron:
    """нейрон"""
    name = "Neuron "
    digit = None
    power = None

    def __init__(self, number):
        self.incomingLinks = []
        self.digit = number
        self.name += str(number)
        self.power = 0


class Input:
    """Входные нейроны"""
    def __init__(self):
        self.OutgoingLinks = []


class KohonenNetWork:
    _inputs = []
    _neurons = []

    def __init__(self):
        print("Init")
        for i in range(inputCount):
            self._inputs.append(Input())

        for i in range(neuronCount):
            self._neurons.append(Neuron(i))

        for index_link in range(len(self._inputs)):
            for index_neuron in range(len(self._neurons)):
                link = Link(self._neurons[index_neuron], 0.0)
                self._inputs[index_link].OutgoingLinks.append(link)
                self._neurons[index_neuron].incomingLinks.append(link)

    def recognize(self, image):

        for i in range(len(self._inputs)):
            input_neuron = self._inputs[i]
            for outgoingLink in input_neuron.OutgoingLinks:
                outgoingLink.neuron.power += outgoingLink.weight * image[i]

        max_neuron = max(self._neurons, key=lambda n: n.power)

        print(*list(map(lambda n: n.name + " = " + str(round(n.power, 3)),
                        self._neurons)), sep="\n")

        self.reset_neurons()

        return max_neuron.digit

    def study(self, image, answer):
        neuron = self._neurons[answer.index(1)]
        for i in range(len(neuron.incomingLinks)):
            neuron.incomingLinks[i].weight += 0.5 * (image[i] - neuron.incomingLinks[i].weight)

    def reset_neurons(self):
        for neuron in self._neurons:
            neuron.power = 0


def main(_):
    pass
