import cv2, os
import tensorflow as tf
from tensorflow.python.ops import math_ops, array_ops, gen_math_ops
import numpy as np
import pathlib
from base_model import BlazePose
from config import epoch_to_test, eval_mode, dataset, use_existing_model_weights, pck_metric, batch_size, img_idxs
from data import x_test, y_test
from utils.draw import draw_images, draw_heatmaps
import utils.logger as logger
import utils.metrics as metrics
import mlflow

def Eclidian2(a, b):
# Calculate the square of Eclidian distance
    assert len(a)==len(b)
    summer = 0
    for i in range(len(a)):
        summer += (a[i] - b[i]) ** 2
    return summer

checkpoint_path_regression = "checkpoints_regression"
loss_func_mse = tf.keras.losses.MeanSquaredError()
loss_func_bce = tf.keras.losses.BinaryCrossentropy()
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

if use_existing_model_weights:
    weight_filepath = "model.weights.h5"
else:
    weight_filepath = os.path.join(checkpoint_path_regression, "models/model_ep{}_val_loss_{val_loss:.2f}.weights.h5".format(epoch_to_test))

model = BlazePose().call()
model.compile(optimizer, loss=[loss_func_bce, loss_func_mse, loss_func_bce], metrics=[None, metrics.PCKMetric(), None])

print("Load regression weights", weight_filepath)
model.load_weights(weight_filepath)

res = model.evaluate(x=x_test, y=y_test, batch_size=batch_size, callbacks=[logger.keras_custom_callback])       
print("Test PCK score:", res[-1])
mlflow.log_metrics({"test_coordinates_pck": res[-1]})

# model.summary(print_fn=logger.print_and_log, show_trainable=True)
tmp_dir = os.path.join(os.getcwd(), "tmp")
os.makedirs(tmp_dir, exist_ok=True)
output_file = os.path.join(tmp_dir, "model_architecture.png")
tf.keras.utils.plot_model(model, to_file=output_file, show_shapes=True, show_layer_activations=True, show_trainable=True)
mlflow.log_artifact(output_file)

image_files = draw_images(model, img_idxs=img_idxs)
for image_file in image_files:
    mlflow.log_artifact(image_file)  

image_files = draw_heatmaps(model, img_idxs=img_idxs)
for image_file in image_files:
    mlflow.log_artifact(image_file)                            
