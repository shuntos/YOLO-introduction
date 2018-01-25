#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 22:33:59 2018

@author: shunt
"""

import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt


#%config InlineBackend.figure_format = 'svg'

# define the model options and run

options = {
    'model': 'cfg/yolo.cfg',
    'load': 'bin/yolo.weights',
    'threshold': 0.3,
    #'gpu': 1.0
}

tfnet = TFNet(options)

# read the color image and covert to RGB

img = cv2.imread('car.JPG', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# use YOLO to predict the image
result = tfnet.return_predict(img)

print (len(result))

img.shape


# pull out some info from the results
for i in range(len(result)):
    tl = (result[i]['topleft']['x'], result[i]['topleft']['y'])
    br = (result[i]['bottomright']['x'], result[i]['bottomright']['y'])
    label = result[i]['label']
    img = cv2.rectangle(img, tl, br, (0, 255, 0), 7)



img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
plt.imshow(img)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imwrite("output.jpg",img)
plt.show()
