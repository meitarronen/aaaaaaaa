#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import os
from mtcnn.mtcnn import MTCNN
input_folder = './images/'
output_folder = '.NewFrameImage/TSP'
detector = MTCNN()

for filename in os.listdir(input_folder):
	if filename.endswith(".png") or filename.endswith(".jpg"):
		image = cv2.imread(filename)
		result = detector.detect_faces(image)

	# Result is an array with all the bounding boxes detected. We know that for 'ivan.jpg' there is only one.
	bounding_box = result[0]['box']
	keypoints = result[0]['keypoints']

	cv2.rectangle(image,
              (bounding_box[0], bounding_box[1]),
              (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
              (0,255,0),
              2, thickness = 8)

#cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
#cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
#cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
#cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
#cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)

	cv2.imwrite(str(output_folder)+str(filename), image)

#print(result)
