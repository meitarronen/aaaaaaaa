#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import os
from mtcnn.mtcnn import MTCNN
input_folder = ('images/')
directory = os.fsencode(input_folder)
output_folder = 'NewFrameImages/TSP/'
detector = MTCNN()

for file in os.listdir(input_folder):
	filename = os.fsdecode(file)
	if filename.endswith(".png"):
		image = cv2.imread(input_folder+filename)
		result = detector.detect_faces(image)

	# Result is an array with all the bounding boxes detected. We know that for 'ivan.jpg' there is only one.
		if (len(result) > 0 ):
			bounding_box = result[0]['box']
			keypoints = result[0]['keypoints']

			cv2.rectangle(image,
              		(bounding_box[0], bounding_box[1]),
              		(bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
              		(0,255,0),
              		thickness = 8)

#cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
#cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
#cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
#cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
#cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)

			print(output_folder+filename)
		cv2.imwrite(output_folder+filename, image)

#print(result)
