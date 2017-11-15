from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from tkinter.filedialog import *
from paint import Paint
from neuron_net import KohonenNetWork
import argparse
import sys

from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf

FLAGS = None
WINDOW_SIZE = "504x504"
STUDY_SET = 40000


def main(_):
    mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)
    kn = KohonenNetWork()
    for _ in range(STUDY_SET):
        batch_xs, batch_ys = mnist.train.next_batch(1)
        kn.study(list(batch_xs[0]), list(batch_ys[0]))

    root = Tk()
    root.geometry(WINDOW_SIZE)
    app = Paint(root, kn)
    root.mainloop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/input_data',
                        help='Directory for storing input data')
    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)