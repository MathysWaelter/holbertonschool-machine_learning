#!/usr/bin/env python3
"""train"""


import tensorflow.compat.v1 as tf

calculate_accuracy = __import__('3-calculate_accuracy').calculate_accuracy
calculate_loss = __import__('4-calculate_loss').calculate_loss
create_placeholders = __import__('0-create_placeholders').create_placeholders
create_train_op = __import__('5-create_train_op').create_train_op
forward_prop = __import__('2-forward_prop').forward_prop


def train(X_train,
          Y_train,
          X_valid,
          Y_valid,
          layer_sizes,
          activations,
          alpha,
          iterations,
          save_path="/tmp/model.ckpt"):
    """
    Train a tensforflow graph
    :param X_train: The training dataset
    :param Y_train: The training thruth
    :param X_valid: The validation dataset
    :param Y_valid: The validation thruth
    :param layer_sizes: A list contain number of node for
                        each layers
    :param activations: A list contain the activation
                        function for each layer
    :param alpha: The learning rate
    :param iterations: The number of iteration
    :param save_path: The path to save the file
    :return: The path where the model was saved
    """
    x, y = create_placeholders(X_train.shape[1],
                               Y_train.shape[1])
    tf.add_to_collection("x", x)
    tf.add_to_collection("y", y)
    y_pred = forward_prop(x, layer_sizes, activations)
    tf.add_to_collection("y_pred", y_pred)
    loss = calculate_loss(y, y_pred)
    tf.add_to_collection("loss", loss)
    accuracy = calculate_accuracy(y, y_pred)
    tf.add_to_collection("accuracy", accuracy)
    train_op = create_train_op(loss, alpha)
    tf.add_to_collection("train_op", train_op)
    init = tf.global_variables_initializer()
    saver = tf.train.Saver()
    with tf.Session() as session:
        session.run(init)
        for iteration in range(iterations + 1):
            loss_train = session.run(loss,
                                     feed_dict={x: X_train,
                                                y: Y_train})
            acc_train = session.run(accuracy,
                                    feed_dict={x: X_train,
                                               y: Y_train})
            loss_valid = session.run(loss,
                                     feed_dict={x: X_valid,
                                                y: Y_valid})
            acc_valid = session.run(accuracy,
                                    feed_dict={x: X_valid,
                                               y: Y_valid})
            if iteration % 100 == 0 or iteration == iterations:
                print("After {} iterations:".format(iteration))
                print("\tTraining Cost: {}".format(loss_train))
                print("\tTraining Accuracy: {}".format(acc_train))
                print("\tValidation Cost: {}".format(loss_valid))
                print("\tValidation Accuracy: {}".format(acc_valid))
            if iteration < iterations:
                session.run(train_op, feed_dict={x: X_train,
                                                 y: Y_train})
        save_path = saver.save(session, save_path)
    return save_path