#####copied from https://github.com/eldor4do/TensorFlow-Examples/blob/master/retraining-example.py  and then changed by ME ########

import redness as rd
import numpy as np
import tensorflow as tf

imagePath = './ear_OME/OME12.jpg'
modelFullPath = './cnn_graphs/output_graph.pb'
labelsFullPath = './cnn_graphs/output_labels.txt'

def create_graph():
    """Creates a graph from saved GraphDef file and returns a saver."""
    # Creates graph from saved graph_def.pb.
    with tf.gfile.FastGFile(modelFullPath, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')


def run_inference_on_image(img):
    imagePath=img
    answer = None

    if not tf.gfile.Exists(imagePath):
        tf.logging.fatal('File does not exist %s', imagePath)
        return answer
    image_data = tf.gfile.FastGFile(imagePath, 'rb').read()
    create_graph()

    with tf.Session() as sess:

        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor,{'DecodeJpeg/contents:0': image_data})
        predictions = np.squeeze(predictions)

        top_k = predictions.argsort()[-5:][::-1]  # Getting top 5 predictions
        f = open(labelsFullPath, 'r')
        lines = f.readlines()
        labels = [str(w).replace("\n", "") for w in lines]
        for node_id in top_k:
            human_string = labels[node_id]
            score = predictions[node_id]
            #print('Probability of %s = %.5f' % (human_string, score))
            if 'NORMAL' in human_string:
                answer1=score

        answer = labels[top_k[0]]
        return answer1


if __name__ == '__main__':
    prob_AOM=[]
    red=[]
    for i in range (35):
        imagePath='./ear_AOM/AOM{}.jpg'.format(i+1)

    print(red)
    print(prob_AOM)
