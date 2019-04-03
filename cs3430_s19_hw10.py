#!/usr/bin/python

import math
from PIL import Image

#######################################################
# module: cs3430_s19_hw10.py
# Krista Gurney
# A01671888
########################################################

##################### Problem 1 (4 points) ####################

## a function to convert an rgb 3-tuple to a grayscale value.
def luminosity(rgb, rcoeff=0.2126, gcoeff=0.7152, bcoeff=0.0722):
    return rcoeff*rgb[0]+gcoeff*rgb[1]+bcoeff*rgb[2]

def save_gd_edges(input_fp, output_fp, magn_thresh=20):
    input_image  = Image.open(input_fp)
    output_image = gd_detect_edges(input_image, magn_thresh=magn_thresh)
    output_image.save(output_fp)
    del input_image
    del output_image

def gd_detect_edges(rgb_img, magn_thresh=20):
    ## gray scale image
    greyed = rgb_img.convert('L')
    img = Image.new('L', greyed.size)

    for row in range(img.size[0]):
        if row > 0:
            for col in range(img.size[1]):
                if col > 1 and col < greyed.size[1]-1 and row > 1 and row < greyed.size[0]-1:
                    # pixel = greyed.getpixel((row, col))
                    above = greyed.getpixel((row-1, col))
                    below = greyed.getpixel((row+1, col))
                    right = greyed.getpixel((row, col+1))
                    left = greyed.getpixel((row, col-1))
                    dy = above - below
                    dx = right - left
                    if dx == 0:
                        dx = 1
                    G = math.sqrt(dy**2 + dx**2)
                    if G > magn_thresh:
                        img.putpixel((row, col), 255)
                    else:
                        img.putpixel((row, col), 0)

    return img


###################### Problem 2 (1 point) #####################

def cosine_sim(img1, img2):
    assert img1.size == img2.size
    greyed_img1 = img1.convert('L')
    greyed_img2 = img2.convert('L')

    top_sum = 0
    bottom_left_sum = 0
    bottom_right_sum = 0

    for row in range(img1.size[0]):
        for col in range(img1.size[1]):
            temp = greyed_img1.getpixel((row,col))
            top_sum += greyed_img1.getpixel((row,col)) * greyed_img2.getpixel((row,col))

            bottom_left_sum += greyed_img1.getpixel((row,col))**2
            bottom_right_sum += greyed_img2.getpixel((row,col))**2

    return top_sum / (math.sqrt(bottom_left_sum)* (math.sqrt(bottom_right_sum)))


'''
>>> test_cosine_sim('img/2b_nb_09_ed.png', 'img/2b_nb_09_ed.png')
('img/2b_nb_09_ed.png', 'img/2b_nb_09_ed.png')
1.0
>>> test_cosine_sim('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
0.512202985103
>>> test_cosine_sim('img/output11884_ed.jpg', 'img/output11885_ed.jpg')
('img/output11884_ed.jpg', 'img/output11885_ed.jpg')
0.352152693884
>>> test_cosine_sim('img/output11885_ed.jpg', 'img/output11884_ed.jpg')
('img/output11885_ed.jpg', 'img/output11884_ed.jpg')
0.352152693884
'''
def test_cosine_sim(img_fp1, img_fp2):
    img1 = Image.open(img_fp1)
    img2 = Image.open(img_fp2)
    sim = cosine_sim(img1, img2)
    del img1
    del img2
    print(img_fp1, img_fp2)
    print(sim)

def euclid_sim(img1, img2):
    assert img1.size == img2.size
    ## your code here
    pass

'''
>>> test_euclid_sim('img/2b_nb_10_ed.png', 'img/2b_nb_10_ed.png')
('img/2b_nb_10_ed.png', 'img/2b_nb_10_ed.png')
0.0
>>> test_euclid_sim('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
16981.9278941
>>> test_euclid_sim('img/2b_nb_10_ed.png', 'img/2b_nb_09_ed.png')
('img/2b_nb_10_ed.png', 'img/2b_nb_09_ed.png')
16981.9278941
'''
def test_euclid_sim(img_fp1, img_fp2):
    img1 = Image.open(img_fp1)
    img2 = Image.open(img_fp2)
    sim = euclid_sim(img1, img2)
    del img1
    del img2
    print(img_fp1, img_fp2)
    print(sim)

def jaccard_sim(img1, img2):
    assert img1.size == img2.size
    ## your code here
    pass

'''
>>> test_jaccard_sim('img/2b_nb_10_ed.png', 'img/2b_nb_10_ed.png')
('img/2b_nb_10_ed.png', 'img/2b_nb_10_ed.png')
1.0
>>> test_jaccard_sim('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
1.0
>>> test_jaccard_sim('img/2b_nb_10_ed.png', 'img/2b_nb_09_ed.png')
('img/2b_nb_10_ed.png', 'img/2b_nb_09_ed.png')
1.0
>>> test_jaccard_sim('img/output11885_ed.jpg', 'img/output11884_ed.jpg')
('img/output11885_ed.jpg', 'img/output11884_ed.jpg')
0.934065934066
>>> test_jaccard_sim('img/output11884_ed.jpg', 'img/output11885_ed.jpg')
('img/output11884_ed.jpg', 'img/output11885_ed.jpg')
0.934065934066
'''
def test_jaccard_sim(img_fp1, img_fp2):
    img1 = Image.open(img_fp1)
    img2 = Image.open(img_fp2)
    sim = jaccard_sim(img1, img2)
    del img1
    del img2
    print(img_fp1, img_fp2)
    print(sim)

def test_01():
    save_gd_edges('img/1b_bee_01.png', 'img/1b_bee_01_ed.png', magn_thresh=20)
    # save_gd_edges('img/1b_bee_10.png', 'img/1b_bee_10_ed.png', magn_thresh=20)
    # save_gd_edges('img/2b_nb_10.png', 'img/2b_nb_10_ed.png', magn_thresh=20)
    # save_gd_edges('img/2b_nb_21.png', 'img/2b_nb_21_ed.png', magn_thresh=20)
    # save_gd_edges('img/elephant.jpg', 'img/elephant_ed.jpg', magn_thresh=20)
    # save_gd_edges('img/output11885.jpg', 'img/output11885_ed.jpg', magn_thresh=20)
    # save_gd_edges('img/2b_nb_09.png', 'img/2b_nb_09_ed.png', magn_thresh=20)
    # save_gd_edges('img/output11884.jpg', 'img/output11884_ed.jpg', magn_thresh=20)

## testing the PIL/PILLOW installation
def test_02():
    img = Image.open('img/1b_bee_01.png').convert('LA')
    img2 = img.save('img/1b_bee_01_gray.png')
    del img
    del img2

def test_03():
    test_cosine_sim('img/2b_nb_09_ed.png', 'img/2b_nb_09_ed.png')
    # ('img/2b_nb_09_ed.png', 'img/2b_nb_09_ed.png')
    # 1.0
    test_cosine_sim('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
    # ('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
    # 0.512202985103
    test_cosine_sim('img/output11884_ed.jpg', 'img/output11885_ed.jpg')
    # ('img/output11884_ed.jpg', 'img/output11885_ed.jpg')
    # 0.352152693884
    test_cosine_sim('img/output11885_ed.jpg', 'img/output11884_ed.jpg')
    # ('img/output11885_ed.jpg', 'img/output11884_ed.jpg')
    # 0.352152693884
    #
if __name__ == '__main__':
    test_03()


