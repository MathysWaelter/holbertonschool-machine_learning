#!/usr/bin/env python3
"""forward_prop"""


import tensorflow.compat.v1 as tf

calculate_accuracy = __import__('3-calculate_accuracy').calculate_accuracy
calculate_loss = __import__('4-calculate_loss').calculate_loss
create_placeholders = __import__('0-create_placeholders').create_placeholders
forward_prop = __import__('2-forward_prop').forward_prop


def evaluate(X, Y, save_path):
    """
    Evaluates the output of a neural network.
    """
    tf.reset_default_graph()
    x, y = create_placeholders(X.shape[1], Y.shape[1])
    y_pred = forward_prop(x, [], [])
    loss = calculate_loss(y, y_pred)
    accuracy = calculate_accuracy(y, y_pred)

    saver = tf.train.Saver()

    with tf.Session() as sess:
        saver.restore(sess, save_path)

        prediction = sess.run(y_pred, feed_dict={x: X, y: Y})
        acc = sess.run(accuracy, feed_dict={x: X, y: Y})
        cost = sess.run(loss, feed_dict={x: X, y: Y})

    return prediction, acc, cost
