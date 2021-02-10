import tensorflow as tf
import numpy as np
import random




x_=np.array([1,2,3],dtype=np.float32)
y_=np.array([2.5,5.0,7.5],dtype=np.float32)
w=tf.Variable(tf.random_normal([1],dtype=tf.float32))
x=tf.placeholder(tf.float32)
y=tf.placeholder(tf.float32)



predict=tf.multiply(x,w)

cost=tf.reduce_mean(tf.square(predict-y))
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.01)
train=optimizer.minimize(cost)



with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(5000):
        sess.run(train,feed_dict={x:x_,y:y_+random.randint(1,10)/100})
        if i%500==0:
            print(sess.run(w))
print(111)
