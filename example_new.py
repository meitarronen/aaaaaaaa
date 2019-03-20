#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
from mtcnn.mtcnn import MTCNN

detector = MTCNN()

image = cv2.imread("ivan.jpg")
result = detector.detect_faces(image)
print(len(result))
for i in range(0,len(result)):
    # Result is an array with all the bounding boxes detected. We know that for 'ivan.jpg' there is only one.
    bounding_box = result[i]['box']
    keypoints = result[i]['keypoints']

    cv2.rectangle(image,
                  (bounding_box[0], bounding_box[1]),
                  (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                  (0,155,255),
                  2)

    cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)

cv2.imwrite("ivan_drawn.jpg", image)

print(result)
