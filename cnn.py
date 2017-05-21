import cv2                 # working with, mainly resizing, images
import numpy as np         # dealing with arrays
import os                  # dealing with directories
from random import shuffle # mixing up or currently ordered data that might lead our network astray in training.
from tqdm import tqdm      # a nice pretty percentage bar for tasks. Thanks to viewer Daniel BA1/4hler for this suggestion
import tflearn
from tflearn.data_preprocessing import ImagePreprocessing
from tflearn.data_augmentation import ImageAugmentation

TRAIN_DIR1 = './ear_normal'
TRAIN_DIR2 = './ear_AOM'
TEST_DIR = '/home/madhielango/test'
IMG_SIZE = 100
LR = 1e-5
VAL_SIZE=20

MODEL_NAME = 'normalvsAOM-{}-{}.model'.format(LR, '2conv-basic') # just so we remember which saved model is which, sizes must match

def label_img(img):
	if (img[0]=='N'):
		return [1,0]
	else:
		return [0,1]

def create_train_data():
	training_data = []
	for img in tqdm(os.listdir(TRAIN_DIR1)):
		label = label_img(img)
		path = os.path.join(TRAIN_DIR1,img)
		try: 
			img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
			img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
		except:
			continue
		training_data.append([np.array(img),np.array(label)])
	for img in tqdm(os.listdir(TRAIN_DIR2)):
		label = label_img(img)
		path = os.path.join(TRAIN_DIR2,img)
		img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
		img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
		training_data.append([np.array(img),np.array(label)])
	shuffle(training_data)
	#np.save('train_data.npy', training_data)
	return training_data

def process_test_data():
	testing_data = []
	for img in tqdm(os.listdir(TEST_DIR)):
		path = os.path.join(TEST_DIR,img)
		img_num = img.split('.')[0]
		img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
		img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
		testing_data.append([np.array(img), img_num])
	shuffle(testing_data)
	np.save('test_data.npy', testing_data)
	return testing_data

train_data = create_train_data()




from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression

img_aug = ImageAugmentation()
img_aug.add_random_flip_leftright()
img_aug.add_random_rotation(max_angle = 89.)
img_aug.add_random_blur(sigma_max=3.)
img_aug.add_random_flip_updown()
img_aug.add_random_90degrees_rotation(rotations = [0, 1, 2, 3])
	

convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 1], name='input', data_augmentation=img_aug)


convnet = conv_2d(convnet, 32, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = conv_2d(convnet, 64, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = fully_connected(convnet, 1024, activation='relu')
convnet = dropout(convnet, 0.8)
convnet = fully_connected(convnet, 2, activation='softmax')
convnet = fully_connected(convnet, 2, activation='softmax')
convnet = fully_connected(convnet, 2, activation='softmax')
convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

model = tflearn.DNN(convnet, tensorboard_dir='log')

train = train_data[:-VAL_SIZE]
test = train_data[-VAL_SIZE:]

X = np.array([i[0] for i in train]).reshape(-1,IMG_SIZE,IMG_SIZE,1)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1,IMG_SIZE,IMG_SIZE,1)
test_y = [i[1] for i in test]

model.fit({'input': X}, {'targets': Y}, n_epoch=3, validation_set=({'input': test_x}, {'targets': test_y}), 
	snapshot_step=500, show_metric=True, run_id=MODEL_NAME)


#tensorboard --logdir=home/madhielango/log

