from matplotlib import pyplot as plt
import cv2
import numpy as np
def read_img(img_path):
    img = cv2.imread(img_path)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

style_img = read_img('D:\\MachineLearning\\Neural-Style-Transfer\\Training\\train_image\\style_3.jpg')
# style_img = style_img.astype('float64')
cv2.imshow('Style Image', style_img)

content_img =read_img('D:\\MachineLearning\\Neural-Style-Transfer\\Training\\train_image\\origin_2.jpg')
# content_img = content_img.astype('float64')
cv2.imshow('Content Image', content_img)
# cv2.waitKey(0)



result = read_img("D:\\MachineLearning\\Neural-Style-Transfer\\output_image\\output_at_iteration_9.png")
# result = result.astype('float64')
cv2.imshow('Result Image', result)
cv2.waitKey(0)