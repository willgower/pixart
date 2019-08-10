# LED Matrix

import pygame
import time
import pyautogui as pag
from datetime import datetime
from datetime import timedelta
import math
import random
import urllib.request
import json
from noise import pnoise2
from noise import pnoise1

pygame.init()

MATRIX_W = 17
MATRIX_H = 17

scaling = 2 if pygame.display.Info().current_w > 3000 else 1
border = 4 * scaling
pixel_s = 26 * scaling

display_width = MATRIX_W * pixel_s + (MATRIX_W + 1) * border
display_height = MATRIX_H * pixel_s + (MATRIX_H + 1) * border + 100
top = display_height - (border * MATRIX_H) - (pixel_s * MATRIX_H)

screen = pygame.display.set_mode((display_width, display_height))

# maxsize = pygame.display.list_modes()[0]
# screen = pygame.display.set_mode(maxsize, pygame.FULLSCREEN)

pygame.display.set_caption('LED Matrix')

# Define some basic colours
black = [0, 0, 0]
grey = [100, 100, 100]
white = [255, 255, 255]

saved = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 255], [0, 0, 0], [150, 150, 150]]
saved_clock = [[255, 255, 255], [0, 0, 0]]

hsv = [[255, 0, 0], [255, 1, 0], [255, 3, 0], [255, 4, 0], [255, 6, 0], [255, 7, 0], [255, 9, 0], [255, 10, 0],
       [255, 12, 0], [255, 13, 0], [255, 15, 0], [255, 16, 0], [255, 18, 0], [255, 19, 0], [255, 21, 0], [255, 23, 0],
       [255, 24, 0], [255, 26, 0], [255, 27, 0], [255, 29, 0], [255, 30, 0], [255, 32, 0], [255, 33, 0], [255, 35, 0],
       [255, 36, 0], [255, 38, 0], [255, 39, 0], [255, 41, 0], [255, 43, 0], [255, 44, 0], [255, 46, 0], [255, 47, 0],
       [255, 49, 0], [255, 50, 0], [255, 52, 0], [255, 53, 0], [255, 55, 0], [255, 56, 0], [255, 58, 0], [255, 59, 0],
       [255, 61, 0], [255, 62, 0], [255, 64, 0], [255, 66, 0], [255, 67, 0], [255, 69, 0], [255, 70, 0], [255, 72, 0],
       [255, 73, 0], [255, 75, 0], [255, 76, 0], [255, 78, 0], [255, 79, 0], [255, 81, 0], [255, 82, 0], [255, 84, 0],
       [255, 86, 0], [255, 87, 0], [255, 89, 0], [255, 90, 0], [255, 92, 0], [255, 93, 0], [255, 95, 0], [255, 96, 0],
       [255, 98, 0], [255, 99, 0], [255, 101, 0], [255, 102, 0], [255, 104, 0], [255, 105, 0], [255, 107, 0],
       [255, 109, 0], [255, 110, 0], [255, 112, 0], [255, 113, 0], [255, 115, 0], [255, 116, 0], [255, 118, 0],
       [255, 119, 0], [255, 121, 0], [255, 122, 0], [255, 124, 0], [255, 125, 0], [255, 127, 0], [255, 129, 0],
       [255, 130, 0], [255, 132, 0], [255, 133, 0], [255, 135, 0], [255, 136, 0], [255, 138, 0], [255, 139, 0],
       [255, 141, 0], [255, 142, 0], [255, 144, 0], [255, 145, 0], [255, 147, 0], [255, 149, 0], [255, 150, 0],
       [255, 152, 0], [255, 153, 0], [255, 155, 0], [255, 156, 0], [255, 158, 0], [255, 159, 0], [255, 161, 0],
       [255, 162, 0], [255, 164, 0], [255, 165, 0], [255, 167, 0], [255, 168, 0], [255, 170, 0], [255, 172, 0],
       [255, 173, 0], [255, 175, 0], [255, 176, 0], [255, 178, 0], [255, 179, 0], [255, 181, 0], [255, 182, 0],
       [255, 184, 0], [255, 185, 0], [255, 187, 0], [255, 188, 0], [255, 190, 0], [255, 192, 0], [255, 193, 0],
       [255, 195, 0], [255, 196, 0], [255, 198, 0], [255, 199, 0], [255, 201, 0], [255, 202, 0], [255, 204, 0],
       [255, 205, 0], [255, 207, 0], [255, 208, 0], [255, 210, 0], [255, 211, 0], [255, 213, 0], [255, 215, 0],
       [255, 216, 0], [255, 218, 0], [255, 219, 0], [255, 221, 0], [255, 222, 0], [255, 224, 0], [255, 225, 0],
       [255, 227, 0], [255, 228, 0], [255, 230, 0], [255, 231, 0], [255, 233, 0], [255, 235, 0], [255, 236, 0],
       [255, 238, 0], [255, 239, 0], [255, 241, 0], [255, 242, 0], [255, 244, 0], [255, 245, 0], [255, 247, 0],
       [255, 248, 0], [255, 250, 0], [255, 251, 0], [255, 253, 0], [255, 255, 0], [253, 255, 0], [251, 255, 0],
       [250, 255, 0], [248, 255, 0], [247, 255, 0], [245, 255, 0], [244, 255, 0], [242, 255, 0], [241, 255, 0],
       [239, 255, 0], [238, 255, 0], [236, 255, 0], [235, 255, 0], [233, 255, 0], [231, 255, 0], [230, 255, 0],
       [228, 255, 0], [227, 255, 0], [225, 255, 0], [224, 255, 0], [222, 255, 0], [221, 255, 0], [219, 255, 0],
       [218, 255, 0], [216, 255, 0], [215, 255, 0], [213, 255, 0], [211, 255, 0], [210, 255, 0], [208, 255, 0],
       [207, 255, 0], [205, 255, 0], [204, 255, 0], [202, 255, 0], [201, 255, 0], [199, 255, 0], [198, 255, 0],
       [196, 255, 0], [195, 255, 0], [193, 255, 0], [192, 255, 0], [190, 255, 0], [188, 255, 0], [187, 255, 0],
       [185, 255, 0], [184, 255, 0], [182, 255, 0], [181, 255, 0], [179, 255, 0], [178, 255, 0], [176, 255, 0],
       [175, 255, 0], [173, 255, 0], [172, 255, 0], [170, 255, 0], [168, 255, 0], [167, 255, 0], [165, 255, 0],
       [164, 255, 0], [162, 255, 0], [161, 255, 0], [159, 255, 0], [158, 255, 0], [156, 255, 0], [155, 255, 0],
       [153, 255, 0], [152, 255, 0], [150, 255, 0], [149, 255, 0], [147, 255, 0], [145, 255, 0], [144, 255, 0],
       [142, 255, 0], [141, 255, 0], [139, 255, 0], [138, 255, 0], [136, 255, 0], [135, 255, 0], [133, 255, 0],
       [132, 255, 0], [130, 255, 0], [129, 255, 0], [127, 255, 0], [125, 255, 0], [124, 255, 0], [122, 255, 0],
       [121, 255, 0], [119, 255, 0], [118, 255, 0], [116, 255, 0], [115, 255, 0], [113, 255, 0], [112, 255, 0],
       [110, 255, 0], [109, 255, 0], [107, 255, 0], [105, 255, 0], [104, 255, 0], [102, 255, 0], [101, 255, 0],
       [99, 255, 0], [98, 255, 0], [96, 255, 0], [95, 255, 0], [93, 255, 0], [92, 255, 0], [90, 255, 0], [89, 255, 0],
       [87, 255, 0], [86, 255, 0], [84, 255, 0], [82, 255, 0], [81, 255, 0], [79, 255, 0], [78, 255, 0], [76, 255, 0],
       [75, 255, 0], [73, 255, 0], [72, 255, 0], [70, 255, 0], [69, 255, 0], [67, 255, 0], [66, 255, 0], [64, 255, 0],
       [62, 255, 0], [61, 255, 0], [59, 255, 0], [58, 255, 0], [56, 255, 0], [55, 255, 0], [53, 255, 0], [52, 255, 0],
       [50, 255, 0], [49, 255, 0], [47, 255, 0], [46, 255, 0], [44, 255, 0], [43, 255, 0], [41, 255, 0], [39, 255, 0],
       [38, 255, 0], [36, 255, 0], [35, 255, 0], [33, 255, 0], [32, 255, 0], [30, 255, 0], [29, 255, 0], [27, 255, 0],
       [26, 255, 0], [24, 255, 0], [23, 255, 0], [21, 255, 0], [19, 255, 0], [18, 255, 0], [16, 255, 0], [15, 255, 0],
       [13, 255, 0], [12, 255, 0], [10, 255, 0], [9, 255, 0], [7, 255, 0], [6, 255, 0], [4, 255, 0], [3, 255, 0],
       [1, 255, 0], [0, 255, 0], [0, 255, 1], [0, 255, 3], [0, 255, 4], [0, 255, 6], [0, 255, 7], [0, 255, 9],
       [0, 255, 10], [0, 255, 12], [0, 255, 13], [0, 255, 15], [0, 255, 16], [0, 255, 18], [0, 255, 19], [0, 255, 21],
       [0, 255, 23], [0, 255, 24], [0, 255, 26], [0, 255, 27], [0, 255, 29], [0, 255, 30], [0, 255, 32], [0, 255, 33],
       [0, 255, 35], [0, 255, 36], [0, 255, 38], [0, 255, 39], [0, 255, 41], [0, 255, 43], [0, 255, 44], [0, 255, 46],
       [0, 255, 47], [0, 255, 49], [0, 255, 50], [0, 255, 52], [0, 255, 53], [0, 255, 55], [0, 255, 56], [0, 255, 58],
       [0, 255, 59], [0, 255, 61], [0, 255, 62], [0, 255, 64], [0, 255, 66], [0, 255, 67], [0, 255, 69], [0, 255, 70],
       [0, 255, 72], [0, 255, 73], [0, 255, 75], [0, 255, 76], [0, 255, 78], [0, 255, 79], [0, 255, 81], [0, 255, 82],
       [0, 255, 84], [0, 255, 86], [0, 255, 87], [0, 255, 89], [0, 255, 90], [0, 255, 92], [0, 255, 93], [0, 255, 95],
       [0, 255, 96], [0, 255, 98], [0, 255, 99], [0, 255, 101], [0, 255, 102], [0, 255, 104], [0, 255, 105],
       [0, 255, 107], [0, 255, 109], [0, 255, 110], [0, 255, 112], [0, 255, 113], [0, 255, 115], [0, 255, 116],
       [0, 255, 118], [0, 255, 119], [0, 255, 121], [0, 255, 122], [0, 255, 124], [0, 255, 125], [0, 255, 127],
       [0, 255, 129], [0, 255, 130], [0, 255, 132], [0, 255, 133], [0, 255, 135], [0, 255, 136], [0, 255, 138],
       [0, 255, 139], [0, 255, 141], [0, 255, 142], [0, 255, 144], [0, 255, 145], [0, 255, 147], [0, 255, 149],
       [0, 255, 150], [0, 255, 152], [0, 255, 153], [0, 255, 155], [0, 255, 156], [0, 255, 158], [0, 255, 159],
       [0, 255, 161], [0, 255, 162], [0, 255, 164], [0, 255, 165], [0, 255, 167], [0, 255, 168], [0, 255, 170],
       [0, 255, 172], [0, 255, 173], [0, 255, 175], [0, 255, 176], [0, 255, 178], [0, 255, 179], [0, 255, 181],
       [0, 255, 182], [0, 255, 184], [0, 255, 185], [0, 255, 187], [0, 255, 188], [0, 255, 190], [0, 255, 192],
       [0, 255, 193], [0, 255, 195], [0, 255, 196], [0, 255, 198], [0, 255, 199], [0, 255, 201], [0, 255, 202],
       [0, 255, 204], [0, 255, 205], [0, 255, 207], [0, 255, 208], [0, 255, 210], [0, 255, 211], [0, 255, 213],
       [0, 255, 215], [0, 255, 216], [0, 255, 218], [0, 255, 219], [0, 255, 221], [0, 255, 222], [0, 255, 224],
       [0, 255, 225], [0, 255, 227], [0, 255, 228], [0, 255, 230], [0, 255, 231], [0, 255, 233], [0, 255, 235],
       [0, 255, 236], [0, 255, 238], [0, 255, 239], [0, 255, 241], [0, 255, 242], [0, 255, 244], [0, 255, 245],
       [0, 255, 247], [0, 255, 248], [0, 255, 250], [0, 255, 251], [0, 255, 253], [0, 255, 255], [0, 253, 255],
       [0, 251, 255], [0, 250, 255], [0, 248, 255], [0, 247, 255], [0, 245, 255], [0, 244, 255], [0, 242, 255],
       [0, 241, 255], [0, 239, 255], [0, 238, 255], [0, 236, 255], [0, 235, 255], [0, 233, 255], [0, 231, 255],
       [0, 230, 255], [0, 228, 255], [0, 227, 255], [0, 225, 255], [0, 224, 255], [0, 222, 255], [0, 221, 255],
       [0, 219, 255], [0, 218, 255], [0, 216, 255], [0, 215, 255], [0, 213, 255], [0, 211, 255], [0, 210, 255],
       [0, 208, 255], [0, 207, 255], [0, 205, 255], [0, 204, 255], [0, 202, 255], [0, 201, 255], [0, 199, 255],
       [0, 198, 255], [0, 196, 255], [0, 195, 255], [0, 193, 255], [0, 192, 255], [0, 190, 255], [0, 188, 255],
       [0, 187, 255], [0, 185, 255], [0, 184, 255], [0, 182, 255], [0, 181, 255], [0, 179, 255], [0, 178, 255],
       [0, 176, 255], [0, 175, 255], [0, 173, 255], [0, 172, 255], [0, 170, 255], [0, 168, 255], [0, 167, 255],
       [0, 165, 255], [0, 164, 255], [0, 162, 255], [0, 161, 255], [0, 159, 255], [0, 158, 255], [0, 156, 255],
       [0, 155, 255], [0, 153, 255], [0, 152, 255], [0, 150, 255], [0, 149, 255], [0, 147, 255], [0, 145, 255],
       [0, 144, 255], [0, 142, 255], [0, 141, 255], [0, 139, 255], [0, 138, 255], [0, 136, 255], [0, 135, 255],
       [0, 133, 255], [0, 132, 255], [0, 130, 255], [0, 129, 255], [0, 127, 255], [0, 125, 255], [0, 124, 255],
       [0, 122, 255], [0, 121, 255], [0, 119, 255], [0, 118, 255], [0, 116, 255], [0, 115, 255], [0, 113, 255],
       [0, 112, 255], [0, 110, 255], [0, 109, 255], [0, 107, 255], [0, 105, 255], [0, 104, 255], [0, 102, 255],
       [0, 101, 255], [0, 99, 255], [0, 98, 255], [0, 96, 255], [0, 95, 255], [0, 93, 255], [0, 92, 255], [0, 90, 255],
       [0, 89, 255], [0, 87, 255], [0, 86, 255], [0, 84, 255], [0, 82, 255], [0, 81, 255], [0, 79, 255], [0, 78, 255],
       [0, 76, 255], [0, 75, 255], [0, 73, 255], [0, 72, 255], [0, 70, 255], [0, 69, 255], [0, 67, 255], [0, 66, 255],
       [0, 64, 255], [0, 62, 255], [0, 61, 255], [0, 59, 255], [0, 58, 255], [0, 56, 255], [0, 55, 255], [0, 53, 255],
       [0, 52, 255], [0, 50, 255], [0, 49, 255], [0, 47, 255], [0, 46, 255], [0, 44, 255], [0, 43, 255], [0, 41, 255],
       [0, 39, 255], [0, 38, 255], [0, 36, 255], [0, 35, 255], [0, 33, 255], [0, 32, 255], [0, 30, 255], [0, 29, 255],
       [0, 27, 255], [0, 26, 255], [0, 24, 255], [0, 23, 255], [0, 21, 255], [0, 19, 255], [0, 18, 255], [0, 16, 255],
       [0, 15, 255], [0, 13, 255], [0, 12, 255], [0, 10, 255], [0, 9, 255], [0, 7, 255], [0, 6, 255], [0, 4, 255],
       [0, 3, 255], [0, 1, 255], [0, 0, 255], [1, 0, 255], [3, 0, 255], [4, 0, 255], [6, 0, 255], [7, 0, 255],
       [9, 0, 255], [10, 0, 255], [12, 0, 255], [13, 0, 255], [15, 0, 255], [16, 0, 255], [18, 0, 255], [19, 0, 255],
       [21, 0, 255], [23, 0, 255], [24, 0, 255], [26, 0, 255], [27, 0, 255], [29, 0, 255], [30, 0, 255], [32, 0, 255],
       [33, 0, 255], [35, 0, 255], [36, 0, 255], [38, 0, 255], [39, 0, 255], [41, 0, 255], [43, 0, 255], [44, 0, 255],
       [46, 0, 255], [47, 0, 255], [49, 0, 255], [50, 0, 255], [52, 0, 255], [53, 0, 255], [55, 0, 255], [56, 0, 255],
       [58, 0, 255], [59, 0, 255], [61, 0, 255], [62, 0, 255], [64, 0, 255], [66, 0, 255], [67, 0, 255], [69, 0, 255],
       [70, 0, 255], [72, 0, 255], [73, 0, 255], [75, 0, 255], [76, 0, 255], [78, 0, 255], [79, 0, 255], [81, 0, 255],
       [82, 0, 255], [84, 0, 255], [86, 0, 255], [87, 0, 255], [89, 0, 255], [90, 0, 255], [92, 0, 255], [93, 0, 255],
       [95, 0, 255], [96, 0, 255], [98, 0, 255], [99, 0, 255], [101, 0, 255], [102, 0, 255], [104, 0, 255],
       [105, 0, 255], [107, 0, 255], [109, 0, 255], [110, 0, 255], [112, 0, 255], [113, 0, 255], [115, 0, 255],
       [116, 0, 255], [118, 0, 255], [119, 0, 255], [121, 0, 255], [122, 0, 255], [124, 0, 255], [125, 0, 255],
       [127, 0, 255], [129, 0, 255], [130, 0, 255], [132, 0, 255], [133, 0, 255], [135, 0, 255], [136, 0, 255],
       [138, 0, 255], [139, 0, 255], [141, 0, 255], [142, 0, 255], [144, 0, 255], [145, 0, 255], [147, 0, 255],
       [149, 0, 255], [150, 0, 255], [152, 0, 255], [153, 0, 255], [155, 0, 255], [156, 0, 255], [158, 0, 255],
       [159, 0, 255], [161, 0, 255], [162, 0, 255], [164, 0, 255], [165, 0, 255], [167, 0, 255], [168, 0, 255],
       [170, 0, 255], [172, 0, 255], [173, 0, 255], [175, 0, 255], [176, 0, 255], [178, 0, 255], [179, 0, 255],
       [181, 0, 255], [182, 0, 255], [184, 0, 255], [185, 0, 255], [187, 0, 255], [188, 0, 255], [190, 0, 255],
       [192, 0, 255], [193, 0, 255], [195, 0, 255], [196, 0, 255], [198, 0, 255], [199, 0, 255], [201, 0, 255],
       [202, 0, 255], [204, 0, 255], [205, 0, 255], [207, 0, 255], [208, 0, 255], [210, 0, 255], [211, 0, 255],
       [213, 0, 255], [215, 0, 255], [216, 0, 255], [218, 0, 255], [219, 0, 255], [221, 0, 255], [222, 0, 255],
       [224, 0, 255], [225, 0, 255], [227, 0, 255], [228, 0, 255], [230, 0, 255], [231, 0, 255], [233, 0, 255],
       [235, 0, 255], [236, 0, 255], [238, 0, 255], [239, 0, 255], [241, 0, 255], [242, 0, 255], [244, 0, 255],
       [245, 0, 255], [247, 0, 255], [248, 0, 255], [250, 0, 255], [251, 0, 255], [253, 0, 255], [255, 0, 255],
       [255, 0, 253], [255, 0, 251], [255, 0, 250], [255, 0, 248], [255, 0, 247], [255, 0, 245], [255, 0, 244],
       [255, 0, 242], [255, 0, 241], [255, 0, 239], [255, 0, 238], [255, 0, 236], [255, 0, 235], [255, 0, 233],
       [255, 0, 231], [255, 0, 230], [255, 0, 228], [255, 0, 227], [255, 0, 225], [255, 0, 224], [255, 0, 222],
       [255, 0, 221], [255, 0, 219], [255, 0, 218], [255, 0, 216], [255, 0, 215], [255, 0, 213], [255, 0, 211],
       [255, 0, 210], [255, 0, 208], [255, 0, 207], [255, 0, 205], [255, 0, 204], [255, 0, 202], [255, 0, 201],
       [255, 0, 199], [255, 0, 198], [255, 0, 196], [255, 0, 195], [255, 0, 193], [255, 0, 192], [255, 0, 190],
       [255, 0, 188], [255, 0, 187], [255, 0, 185], [255, 0, 184], [255, 0, 182], [255, 0, 181], [255, 0, 179],
       [255, 0, 178], [255, 0, 176], [255, 0, 175], [255, 0, 173], [255, 0, 172], [255, 0, 170], [255, 0, 168],
       [255, 0, 167], [255, 0, 165], [255, 0, 164], [255, 0, 162], [255, 0, 161], [255, 0, 159], [255, 0, 158],
       [255, 0, 156], [255, 0, 155], [255, 0, 153], [255, 0, 152], [255, 0, 150], [255, 0, 149], [255, 0, 147],
       [255, 0, 145], [255, 0, 144], [255, 0, 142], [255, 0, 141], [255, 0, 139], [255, 0, 138], [255, 0, 136],
       [255, 0, 135], [255, 0, 133], [255, 0, 132], [255, 0, 130], [255, 0, 129], [255, 0, 127], [255, 0, 125],
       [255, 0, 124], [255, 0, 122], [255, 0, 121], [255, 0, 119], [255, 0, 118], [255, 0, 116], [255, 0, 115],
       [255, 0, 113], [255, 0, 112], [255, 0, 110], [255, 0, 109], [255, 0, 107], [255, 0, 105], [255, 0, 104],
       [255, 0, 102], [255, 0, 101], [255, 0, 99], [255, 0, 98], [255, 0, 96], [255, 0, 95], [255, 0, 93], [255, 0, 92],
       [255, 0, 90], [255, 0, 89], [255, 0, 87], [255, 0, 86], [255, 0, 84], [255, 0, 82], [255, 0, 81], [255, 0, 79],
       [255, 0, 78], [255, 0, 76], [255, 0, 75], [255, 0, 73], [255, 0, 72], [255, 0, 70], [255, 0, 69], [255, 0, 67],
       [255, 0, 66], [255, 0, 64], [255, 0, 62], [255, 0, 61], [255, 0, 59], [255, 0, 58], [255, 0, 56], [255, 0, 55],
       [255, 0, 53], [255, 0, 52], [255, 0, 50], [255, 0, 49], [255, 0, 47], [255, 0, 46], [255, 0, 44], [255, 0, 43],
       [255, 0, 41], [255, 0, 39], [255, 0, 38], [255, 0, 36], [255, 0, 35], [255, 0, 33], [255, 0, 32], [255, 0, 30],
       [255, 0, 29], [255, 0, 27], [255, 0, 26], [255, 0, 24], [255, 0, 23], [255, 0, 21], [255, 0, 19], [255, 0, 18],
       [255, 0, 16], [255, 0, 15], [255, 0, 13], [255, 0, 12], [255, 0, 10], [255, 0, 9], [255, 0, 7], [255, 0, 6],
       [255, 0, 4], [255, 0, 3], [255, 0, 1]]
hsv_i = 0

current_image = ""

# Start off with selected colour as white
primaryColour = saved[3]
secondaryColour = saved[4]

number_array = {
    "0": [True, True, True, True, False, True, True, False, True, True, False, True, True, True, True],
    "1": [False, False, True, False, False, True, False, False, True, False, False, True, False, False, True],
    "2": [True, True, True, False, False, True, True, True, True, True, False, False, True, True, True],
    "3": [True, True, True, False, False, True, True, True, True, False, False, True, True, True, True],
    "4": [True, False, True, True, False, True, True, True, True, False, False, True, False, False, True],
    "5": [True, True, True, True, False, False, True, True, True, False, False, True, True, True, True],
    "6": [True, True, True, True, False, False, True, True, True, True, False, True, True, True, True],
    "7": [True, True, True, False, False, True, False, False, True, False, False, True, False, False, True],
    "8": [True, True, True, True, False, True, True, True, True, True, False, True, True, True, True],
    "9": [True, True, True, True, False, True, True, True, True, False, False, True, False, False, True],
    ":": [False, False, False, False, True, False, False, False, False, False, True, False, False, False, False],
    "%": [True, False, True, False, False, True, False, True, False, True, False, False, True, False, True],
    "+": [False, False, False, False, True, False, True, True, True, False, True, False, False, False, False]}

char_array = {
    "A": [False, False, True, False, False, False, True, False, True, False, True, False, False, False, True, True,
          False, False, False, True, True, True, True, True, True, True, False, False, False, True, True, False, False,
          False, True],
    "B": [True, True, True, True, False, False, True, False, False, True, False, True, False, False, True, False, True,
          True, True, False, False, True, False, False, True, False, True, False, False, True, True, True, True, True,
          False],
    "C": [False, True, True, True, False, True, False, False, False, True, True, False, False, False, False, True,
          False, False, False, False, True, False, False, False, False, True, False, False, False, True, False, True,
          True, True, False],
    "D": [True, True, True, True, False, False, True, False, False, True, False, True, False, False, True, False, True,
          False, False, True, False, True, False, False, True, False, True, False, False, True, True, True, True, True,
          False],
    "E": [True, True, True, True, True, True, False, False, False, False, True, False, False, False, False, True, True,
          True, True, False, True, False, False, False, False, True, False, False, False, False, True, True, True, True,
          True],
    "F": [True, True, True, True, True, True, False, False, False, False, True, False, False, False, False, True, True,
          True, True, False, True, False, False, False, False, True, False, False, False, False, True, False, False,
          False, False],
    "G": [False, True, True, True, False, True, False, False, False, True, True, False, False, False, False, True,
          False, False, True, True, True, False, False, False, True, True, False, False, False, True, False, True, True,
          True, True],
    "H": [True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, True, True,
          True, True, True, True, False, False, False, True, True, False, False, False, True, True, False, False, False,
          True],
    "I": [False, True, True, True, False, False, False, True, False, False, False, False, True, False, False, False,
          False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, True,
          True, True, False],
    "J": [False, False, True, True, True, False, False, False, True, False, False, False, False, True, False, False,
          False, False, True, False, False, False, False, True, False, True, False, False, True, False, False, True,
          True, False, False],
    "K": [True, False, False, False, True, True, False, False, True, False, True, False, True, False, False, True, True,
          False, False, False, True, False, True, False, False, True, False, False, True, False, True, False, False,
          False, True],
    "L": [True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True,
          False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, True,
          True, True, True],
    "M": [True, False, False, False, True, True, True, False, True, True, True, False, True, False, True, True, False,
          True, False, True, True, False, False, False, True, True, False, False, False, True, True, False, False,
          False, True],
    "N": [True, False, False, False, True, True, False, False, False, True, True, True, False, False, True, True, False,
          True, False, True, True, False, False, True, True, True, False, False, False, True, True, False, False, False,
          True],
    "O": [False, True, True, True, False, True, False, False, False, True, True, False, False, False, True, True, False,
          False, False, True, True, False, False, False, True, True, False, False, False, True, False, True, True, True,
          False],
    "P": [True, True, True, True, False, True, False, False, False, True, True, False, False, False, True, True, True,
          True, True, False, True, False, False, False, False, True, False, False, False, False, True, False, False,
          False, False],
    "Q": [False, True, True, True, False, True, False, False, False, True, True, False, False, False, True, True, False,
          False, False, True, True, False, True, False, True, True, False, False, True, False, False, True, True, False,
          True],
    "R": [True, True, True, True, False, True, False, False, False, True, True, False, False, False, True, True, True,
          True, True, False, True, False, True, False, False, True, False, False, True, False, True, False, False,
          False, True],
    "S": [False, True, True, True, False, True, False, False, False, True, True, False, False, False, False, False,
          True, True, True, False, False, False, False, False, True, True, False, False, False, True, False, True, True,
          True, False],
    "T": [True, True, True, True, True, False, False, True, False, False, False, False, True, False, False, False,
          False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False,
          True, False, False],
    "U": [True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, True,
          False, False, False, True, True, False, False, False, True, True, False, False, False, True, False, True,
          True, True, False],
    "V": [True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, True,
          False, False, False, True, True, False, False, False, True, False, True, False, True, False, False, False,
          True, False, False],
    "W": [True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, True,
          False, True, False, True, True, False, True, False, True, True, False, True, False, True, False, True, False,
          True, False],
    "X": [True, False, False, False, True, True, False, False, False, True, False, True, False, True, False, False,
          False, True, False, False, False, True, False, True, False, True, False, False, False, True, True, False,
          False, False, True],
    "Y": [True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, False,
          True, False, True, False, False, False, True, False, False, False, False, True, False, False, False, False,
          True, False, False],
    "Z": [True, True, True, True, True, False, False, False, False, True, False, False, False, True, False, False,
          False, True, False, False, False, True, False, False, False, True, False, False, False, False, True, True,
          True, True, True],
    "a": [False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False,
          False, False, False, True, False, True, True, True, True, True, False, False, False, True, False, True, True,
          True, True],
    "b": [True, False, False, False, False, True, False, False, False, False, True, False, True, True, False, True,
          True, False, False, True, True, False, False, False, True, True, False, False, False, True, True, True, True,
          True, False],
    "c": [False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, True,
          False, False, False, False, True, False, False, False, False, True, False, False, False, True, False, True,
          True, True, False],
    "d": [False, False, False, False, True, False, False, False, False, True, False, True, True, False, True, True,
          False, False, True, True, True, False, False, False, True, True, False, False, False, True, False, True, True,
          True, True],
    "e": [False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, True,
          False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, True, True,
          True, False],
    "f": [False, False, True, True, False, False, True, False, False, True, False, True, False, False, False, True,
          True, True, False, False, False, True, False, False, False, False, True, False, False, False, False, True,
          False, False, False],
    "g": [False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True,
          False, False, False, True, False, True, True, True, True, False, False, False, False, True, False, True, True,
          True, False],
    "h": [True, False, False, False, False, True, False, False, False, False, True, False, True, True, False, True,
          True, False, False, True, True, False, False, False, True, True, False, False, False, True, True, False,
          False, False, True],
    "i": [False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False,
          True, True, False, False, False, False, True, False, False, False, False, True, False, False, False, True,
          True, True, False],
    "j": [False, False, False, True, False, False, False, False, False, False, False, False, True, True, False, False,
          False, False, True, False, False, False, False, True, False, True, False, False, True, False, False, True,
          True, False, False],
    "k": [True, False, False, False, False, True, False, False, False, False, True, False, False, True, False, True,
          False, True, False, False, True, True, False, False, False, True, False, True, False, False, True, False,
          False, True, False],
    "l": [False, True, True, False, False, False, False, True, False, False, False, False, True, False, False, False,
          False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, True,
          True, True, False],
    "m": [False, False, False, False, False, False, False, False, False, False, True, True, False, True, False, True,
          False, True, False, True, True, False, True, False, True, True, False, True, False, True, True, False, True,
          False, True],
    "n": [False, False, False, False, False, False, False, False, False, False, True, False, True, True, False, True,
          True, False, False, True, True, False, False, False, True, True, False, False, False, True, True, False,
          False, False, True],
    "o": [False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, True,
          False, False, False, True, True, False, False, False, True, True, False, False, False, True, False, True,
          True, True, False],
    "p": [False, False, False, False, False, False, False, False, False, False, True, True, True, True, False, True,
          False, False, False, True, True, True, True, True, False, True, False, False, False, False, True, False,
          False, False, False],
    "q": [False, False, False, False, False, False, False, False, False, False, False, True, True, False, True, True,
          False, False, True, True, False, True, True, True, True, False, False, False, False, True, False, False,
          False, False, True],
    "r": [False, False, False, False, False, False, False, False, False, False, True, False, True, True, False, True,
          True, False, False, True, True, False, False, False, False, True, False, False, False, False, True, False,
          False, False, False],
    "s": [False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, True,
          False, False, False, False, False, True, True, True, False, False, False, False, False, True, True, True,
          True, True, False],
    "t": [False, True, False, False, False, False, True, False, False, False, True, True, True, False, False, False,
          True, False, False, False, False, True, False, False, False, False, True, False, False, True, False, False,
          True, True, False],
    "u": [False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, True,
          False, False, False, True, True, False, False, False, True, True, False, False, True, True, False, True, True,
          False, True],
    "v": [False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, True,
          False, False, False, True, True, False, False, False, True, False, True, False, True, False, False, False,
          True, False, False],
    "w": [False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, True,
          False, False, False, True, True, False, True, False, True, True, False, True, False, True, False, True, False,
          True, False],
    "x": [False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False,
          True, False, True, False, False, False, True, False, False, False, True, False, True, False, True, False,
          False, False, True],
    "y": [False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, True,
          False, False, False, True, False, True, True, True, True, False, False, False, False, True, False, True, True,
          True, False],
    "z": [False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False,
          False, False, True, False, False, False, True, False, False, False, True, False, False, False, True, True,
          True, True, True],
    "0": [False, True, True, True, False, True, False, False, False, True, True, False, False, True, True, True, False,
          True, False, True, True, True, False, False, True, True, False, False, False, True, False, True, True, True,
          False],
    "1": [False, False, True, False, False, False, True, True, False, False, False, False, True, False, False, False,
          False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, True,
          True, True, False],
    "2": [False, True, True, True, False, True, False, False, False, True, False, False, False, False, True, False,
          False, True, True, False, False, True, False, False, False, True, False, False, False, False, True, True,
          True, True, True],
    "3": [False, True, True, True, False, True, False, False, False, True, False, False, False, False, True, False,
          False, True, True, False, False, False, False, False, True, True, False, False, False, True, False, True,
          True, True, False],
    "4": [False, False, False, True, False, False, False, True, True, False, False, True, False, True, False, True,
          False, False, True, False, True, True, True, True, True, False, False, False, True, False, False, False,
          False, True, False],
    "5": [True, True, True, True, True, True, False, False, False, False, True, True, True, True, False, False, False,
          False, False, True, False, False, False, False, True, True, False, False, False, True, False, True, True,
          True, False],
    "6": [False, False, True, True, False, False, True, False, False, False, True, False, False, False, False, True,
          True, True, True, False, True, False, False, False, True, True, False, False, False, True, False, True, True,
          True, False],
    "7": [True, True, True, True, True, False, False, False, False, True, False, False, False, True, False, False,
          False, True, False, False, False, True, False, False, False, False, True, False, False, False, False, True,
          False, False, False],
    "8": [False, True, True, True, False, True, False, False, False, True, True, False, False, False, True, False, True,
          True, True, False, True, False, False, False, True, True, False, False, False, True, False, True, True, True,
          False],
    "9": [False, True, True, True, False, True, False, False, False, True, True, False, False, False, True, False, True,
          True, True, True, False, False, False, False, True, False, False, False, True, False, False, True, True,
          False, False],
    ".": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False,
          True, True, False, False],
    ",": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False, False, True, True, False, False, False, False, True, False, False, False,
          True, False, False, False],
    "?": [False, True, True, True, False, True, False, False, False, True, False, False, False, False, True, False,
          False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False,
          True, False, False],
    "!": [False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False,
          False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False,
          True, False, False],
    "@": [False, True, True, True, False, True, False, False, False, True, False, False, False, False, True, False,
          True, True, False, True, True, False, True, False, True, True, False, True, False, True, False, True, True,
          True, False],
    "_": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True,
          True, True, True, True],
    "*": [False, False, False, False, False, False, False, True, False, False, True, False, True, False, True, False,
          True, True, True, False, True, False, True, False, True, False, False, True, False, False, False, False,
          False, False, False],
    "#": [False, True, False, True, False, False, True, False, True, False, True, True, True, True, True, False, True,
          False, True, False, True, True, True, True, True, False, True, False, True, False, False, True, False, True,
          False],
    "$": [False, False, True, False, False, False, True, True, True, True, True, False, True, False, False, False, True,
          True, True, False, False, False, True, False, True, True, True, True, True, False, False, False, True, False,
          False],
    "%": [True, True, False, False, False, True, True, False, False, True, False, False, False, True, False, False,
          False, True, False, False, False, True, False, False, False, True, False, False, True, True, False, False,
          False, True, True],
    "&": [False, True, True, False, False, True, False, False, True, False, True, False, True, False, False, False,
          True, False, False, False, True, False, True, False, True, True, False, False, True, False, False, True, True,
          False, True],
    "(": [False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, False,
          True, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False,
          False, True, False],
    ")": [False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False,
          False, False, True, False, False, False, False, True, False, False, False, True, False, False, False, True,
          False, False, False],
    "+": [False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, True,
          True, True, True, True, False, False, True, False, False, False, False, True, False, False, False, False,
          False, False, False],
    "-": [False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False,
          False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False],
    ":": [False, False, False, False, False, False, True, True, False, False, False, True, True, False, False, False,
          False, False, False, False, False, True, True, False, False, False, True, True, False, False, False, False,
          False, False, False],
    ";": [False, False, False, False, False, False, True, True, False, False, False, True, True, False, False, False,
          False, False, False, False, False, True, True, False, False, False, False, True, False, False, False, True,
          False, False, False],
    "<": [False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True,
          False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False,
          False, True, False],
    "=": [False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False,
          False, False, False, False, True, True, True, True, True, False, False, False, False, False, False, False,
          False, False, False],
    ">": [False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False,
          False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True,
          False, False, False],
    "[": [False, True, True, True, False, False, True, False, False, False, False, True, False, False, False, False,
          True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True,
          True, True, False],
    "]": [False, True, True, True, False, False, False, False, True, False, False, False, False, True, False, False,
          False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, True,
          True, True, False],
    "^": [False, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False,
          False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False],
    "£": [False, False, True, True, False, False, True, False, False, False, False, True, False, False, False, True,
          True, True, True, False, False, True, False, False, False, False, True, False, False, True, True, False, True,
          True, False],
    " ": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False],
    "/": [False, False, False, False, True, False, False, False, True, False, False, False, False, True, False, False,
          False, True, False, False, False, True, False, False, False, False, True, False, False, False, True, False,
          False, False, False],
    "°": [False, True, True, True, False, False, True, False, True, False, False, True, True, True, False, False, False,
          False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False]
    }

matrix = [[[0 for k in range(3)] for j in range(MATRIX_W)] for i in range(MATRIX_H)]


def close():
    pygame.quit()
    quit()


def blend(c1, c2, c3=(), c4=(), c5=(), c6=(), c7=(), c8=(), length=MATRIX_W):
    array = [c1, c2]
    for c in c3, c4, c5, c6, c7, c8:
        if c:
            array.append(c)

    steps = int(length / (len(array) - 1))
    blended = []

    for change in range(len(array) - 1):
        rc = array[change][0] - array[change+1][0]
        gc = array[change][1] - array[change+1][1]
        bc = array[change][2] - array[change+1][2]

        ri = rc/steps
        gi = gc/steps
        bi = bc/steps

        for inc in range(steps):
            r = array[change][0] - inc * ri
            g = array[change][1] - inc * gi
            b = array[change][2] - inc * bi

            rgb_tuple = (int(r), int(g), int(b))
            blended.append(rgb_tuple)

    return blended


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


def check_buttons():
    button("", display_width - 40, 8, 32, 32, action=settings)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            close()


def advance_rainbow(skip=1):
    global hsv_i
    if hsv_i + skip + 1 > len(hsv):
        hsv_i = hsv_i + skip - len(hsv)
    else:
        hsv_i += skip

    return hsv[hsv_i]


def reset_matrix(colour=[0, 0, 0], confirm=False):
    # define the blank WxH matrix
    global matrix
    if confirm:
        verify = pag.confirm(text='Are you sure you want to reset the matrix to black', title='Confirm Reset')
    else:
        verify = "OK"

    if verify == "OK":
        for i in range(MATRIX_H):
            for j in range(MATRIX_W):
                matrix[i][j] = colour


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def setColour(savedIndex, x, y, w, h, directory=saved):
    global saved_clock
    global saved

    def hex2rgb(hex_string):
        rgb_tuple = tuple(int(hex_string[i:i + 2], 16) for i in (0, 2, 4))
        return rgb_tuple

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(screen, directory[savedIndex], (x, y, w, h))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    if sum(directory[savedIndex]) > 500:
        textSurf, textRect = text_objects(str(directory[savedIndex]), smallText, black)
    else:
        textSurf, textRect = text_objects(str(directory[savedIndex]), smallText, white)

    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)

    if x + w > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
        raw_text = pag.prompt(text='Type rgb values in the form: r,g,b or hex value in the form #123456',
                              title='Set colour', )
        if raw_text[0] != "#":
            if raw_text != None and len(raw_text) > 3:
                if all(x in "0123456789," for x in raw_text):
                    rgb = tuple(int(x) for x in raw_text.split(','))
        else:
            rgb = hex2rgb(raw_text[1:])

        if len(rgb) == 3 and 0 <= rgb[0] <= 255 and 0 <= rgb[1] <= 255 and 0 <= rgb[2] <= 255:
            directory[savedIndex] = rgb

    return True


def button(msg, x, y, w, h, bg_colour=(), press_colour=(), action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global primaryColour
    global secondaryColour

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if len(press_colour) > 0:
            pygame.draw.rect(screen, press_colour, (x, y, w, h))
        if click[0] == 1:
            if action == None:
                primaryColour = bg_colour
            else:
                action()
        elif click[2] == 1:
            if action == None:
                secondaryColour = bg_colour
    else:
        if len(bg_colour) > 0:
            pygame.draw.rect(screen, bg_colour, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    if sum(bg_colour) > 500:
        textSurf, textRect = text_objects(msg, smallText, black)
    else:
        textSurf, textRect = text_objects(msg, smallText, white)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)


def dim_matrix(severity=1, any_matrix=""):
    global matrix
    if any_matrix == "":
        for i in range(MATRIX_H):
            for j in range(MATRIX_W):
                r = matrix[i][j][0]
                g = matrix[i][j][1]
                b = matrix[i][j][2]

                maximum = max(r, g, b)

                if maximum > 100:
                    fade1 = 0.98 * severity
                    rgb_dimmed = [int(r * fade1), int(g * fade1), int(b * fade1)]
                elif maximum > 60:
                    fade2 = 0.95 * severity
                    rgb_dimmed = [int(r * fade2), int(g * fade2), int(b * fade2)]
                elif maximum > 30:
                    fade3 = 0.9 * severity
                    rgb_dimmed = [int(r * fade3), int(g * fade3), int(b * fade3)]
                elif maximum > 15:
                    fade4 = 0.85 * severity
                    rgb_dimmed = [int(r * fade4), int(g * fade4), int(b * fade4)]
                else:
                    rgb_dimmed = [0, 0, 0]

                matrix[i][j] = rgb_dimmed
    else:
        for i in range(len(any_matrix)):
            r = any_matrix[i][0]
            g = any_matrix[i][1]
            b = any_matrix[i][2]

            maximum = max(r, g, b)

            if maximum > 100:
                fade1 = 0.98 * severity
                rgb_dimmed = [int(r * fade1), int(g * fade1), int(b * fade1)]
            elif maximum > 60:
                fade2 = 0.95 * severity
                rgb_dimmed = [int(r * fade2), int(g * fade2), int(b * fade2)]
            elif maximum > 30:
                fade3 = 0.9 * severity
                rgb_dimmed = [int(r * fade3), int(g * fade3), int(b * fade3)]
            elif maximum > 15:
                fade4 = 0.85 * severity
                rgb_dimmed = [int(r * fade4), int(g * fade4), int(b * fade4)]
            else:
                rgb_dimmed = [0, 0, 0]

            any_matrix[i] = rgb_dimmed
        return any_matrix


def showPixels():
    for i in range(MATRIX_H):
        for j in range(MATRIX_W):
            x = border + j * (pixel_s + border)
            y = display_height - (MATRIX_H * pixel_s) - (MATRIX_H * border) + i * (pixel_s + border)
            pygame.draw.rect(screen, matrix[i][j], (x, y, pixel_s, pixel_s))

    pygame.display.update()


def place_3x5_num(pos, number, p_colour, s_colour):
    for p in range(5):
        for q in range(3):
            matrix[pos[1] + p][pos[0] + q] = p_colour if number_array[number][p * 3 + q] else s_colour


def get_magnitude(vector):
    return (vector[0] ** 2 + vector[1] ** 2) ** 0.5


def output_arduino_code():
    verify = pag.prompt(text="Create a name and press enter to save the matrix to the file 'pixart_code.txt'.",
                        title='Save Matrix', )
    if verify != None:
        outputTxt = open("pixart_code.txt", "a")
        current_time = datetime.now()
        formatted = "Matrix saved at " + str(current_time.hour) + ":" + str(current_time.minute) \
                    + " on the date " + str(current_time.day) + "/" + str(current_time.month) \
                    + "/" + str(current_time.year) + "\n\n" + verify + "[] = " + "{"
        for row in range(MATRIX_H):
            if row % 2 == 0:
                for col in range(MATRIX_W):
                    for rgb in range(3):
                        formatted += str(matrix[row][col][rgb])
                        formatted += ","
            else:
                for col in range(MATRIX_W):
                    for rgb in range(3):
                        formatted += str(matrix[row][MATRIX_W - 1 - col][rgb])
                        formatted += ","

        formatted = formatted[:-2] + "};\n\n"
        outputTxt.write(formatted)
        outputTxt.close()
        time.sleep(1)


def output_code():
    get_name = pag.prompt(text="Create a name and press enter to save the matrix to the file 'image_file.txt'.",
                          title='Save Matrix', )
    if get_name is not None:
        output_file = open("image_file.txt", "a")
        formatted = get_name + " = (" + str(MATRIX_W) + "x" + str(MATRIX_H) + ") ["
        for row in range(MATRIX_H):
            for col in range(MATRIX_W):
                for rgb in range(3):
                    formatted += str(matrix[row][col][rgb]) + ","

        formatted = formatted[:-1] + "]\n"
        output_file.write(formatted)
        output_file.close()


def display_header(not_settings=True):
    screen.fill(grey)
    largeText = pygame.font.Font('freesansbold.ttf', 40)
    TextSurf, TextRect = text_objects("LED Matrix", largeText, (255, 255, 255))
    TextRect.center = (120, 25)
    screen.blit(TextSurf, TextRect)

    if not_settings:
        settings_icon = pygame.image.load('settings_icon.png')
        screen.blit(settings_icon, (display_width - 40, 8))

    pygame.display.update()


def wait_for_delay(delay=100):
    start = datetime.now()
    while datetime.now() < start + timedelta(milliseconds=delay):
        check_buttons()

    return None


def wait_for_click():
    while True:
        check_buttons()
        if pygame.mouse.get_pressed()[0] == 1:
            print("click detected")
            return None


def scroll_text(text, foreground=[255, 255, 255], background=[0, 0, 0], speed=80, height=4):
    for char in text:
        for i in range(MATRIX_H):
            # create a single gap between each character
            matrix[i].pop(0)
            matrix[i].append(background)

        for edge in range(5):
            for t in range(7):
                matrix[height + t].append(foreground if char_array[char][t * 5 + edge] else background)

            for i in range(MATRIX_H):
                if len(matrix[i]) > MATRIX_W:
                    matrix[i].pop(0)

            wait_for_delay(speed)
            showPixels()
            check_buttons()


def load_image(name):
    global matrix
    reset_matrix()
    image_file = open("image_file.txt", "r")

    for line in image_file.readlines():
        l_name = line[:line.find("=") - 1]
        if l_name == name:
            image_width = int(line[line.find("(") + 1: line.find("(") + 3])
            image_height = int(line[line.find(")") - 2: line.find(")")])
            array_text = line[line.find(")") + 3:-2]

            joined_array = [int(x) for x in array_text.split(',')]

            for i in range(image_width):
                for j in range(image_height):
                    p = []
                    for c in range(3):
                        p.append(joined_array[i * image_width * 3 + j * 3 + c])

                    if i <= MATRIX_W - 1 and j <= MATRIX_H - 1:
                        matrix[i][j] = p

    image_file.close()


def draw_loop():
    display_header()

    def get_clicked_pixel(pos):
        x_valid = False
        y_valid = False

        for p in range(MATRIX_W):
            if border * (p + 1) + pixel_s * p < pos[0] < border * (p + 1) + pixel_s * (p + 1):
                x_pixel = p
                x_valid = True
                break

        for p in range(MATRIX_H):
            if top + border * p + pixel_s * p < pos[1] < top + border * p + pixel_s * (p + 1):
                y_pixel = p
                y_valid = True
                break

        if x_valid and y_valid:
            return (x_pixel, y_pixel)
        else:
            return ()

    def change_colours():
        display_header()

        medText = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects("Set drawing colour palette", medText, (255, 255, 255))
        TextRect.center = (display_width / 2, 100)
        screen.blit(TextSurf, TextRect)

        while True:
            for i in range(6):
                setColour(i, 20, 150 + i * 65, display_width - 40, 60)

            button("return", 20, display_height - 100, display_width - 40, 80, (50, 50, 50), action=draw_loop)
            check_buttons()
            pygame.display.update()

    def draw_reset():
        reset_matrix(black, True)

    showPixels()

    click_released = False
    while not click_released:
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONUP:
            click_released = True

    while True:
        button("reset", 5, top - 45, 100, 40, (50, 50, 50), action=draw_reset)
        button("edit", 110, top - 45, 100, 40, (50, 50, 50), action=change_colours)
        button("1", 215, top - 45, 40, 40, saved[0])
        button("2", 260, top - 45, 40, 40, saved[1])
        button("3", 305, top - 45, 40, 40, saved[2])
        button("4", 350, top - 45, 40, 40, saved[3])
        button("5", 395, top - 45, 40, 40, saved[4])
        button("6", 440, top - 45, 40, 40, saved[5])
        button("save", 485, top - 45, 100, 40, (50, 50, 50), action=output_code)

        click = pygame.mouse.get_pressed()

        if click[0] == 1:
            pixel = get_clicked_pixel(pygame.mouse.get_pos())
            if len(pixel) > 0:
                matrix[pixel[1]][pixel[0]] = primaryColour
        elif click[2] == 1:
            pixel = get_clicked_pixel(pygame.mouse.get_pos())
            if len(pixel) > 0:
                matrix[pixel[1]][pixel[0]] = secondaryColour

        showPixels()
        check_buttons()


def clock_loop():
    global saved_clock
    reset_matrix(saved_clock[1])

    display_header()

    h1 = ""
    h2 = ""
    m1 = ""
    m2 = ""
    s1 = ""
    s2 = ""

    while True:
        check_buttons()
        old_saved = saved_clock
        colour_changed_1 = setColour(0, 100, top - 45, 180, 40, directory=saved_clock)
        colour_changed_2 = setColour(1, 285, top - 45, 180, 40, directory=saved_clock)

        if colour_changed_1 or colour_changed_2:
            reset_matrix(saved_clock[1])
            h1 = ""
            h2 = ""
            m1 = ""
            m2 = ""
            s1 = ""
            s2 = ""

        now = datetime.now()

        if h1 != str(now.hour).zfill(2)[0]:
            h1 = str(now.hour).zfill(2)[0]
            place_3x5_num((0, 2), h1, saved_clock[0], saved_clock[1])
        if h2 != str(now.hour).zfill(2)[1]:
            h2 = str(now.hour).zfill(2)[1]
            place_3x5_num((4, 2), h2, saved_clock[0], saved_clock[1])
        if m1 != str(now.minute).zfill(2)[0]:
            m1 = str(now.minute).zfill(2)[0]
            place_3x5_num((10, 2), m1, saved_clock[0], saved_clock[1])
        if m2 != str(now.minute).zfill(2)[1]:
            m2 = str(now.minute).zfill(2)[1]
            place_3x5_num((14, 2), m2, saved_clock[0], saved_clock[1])
        if s1 != str(now.second).zfill(2)[0]:
            s1 = str(now.second).zfill(2)[0]
            place_3x5_num((5, 10), s1, saved_clock[0], saved_clock[1])
        if s2 != str(now.second).zfill(2)[1]:
            s2 = str(now.second).zfill(2)[1]
            place_3x5_num((9, 10), s2, saved_clock[0], saved_clock[1])
            if now.second % 2 == 0:
                matrix[3][8] = saved_clock[0]
                matrix[5][8] = saved_clock[0]
            else:
                matrix[3][8] = saved_clock[1]
                matrix[5][8] = saved_clock[1]

        showPixels()


def squiggle_loop():
    display_header()
    reset_matrix()

    def drawCircle(pos):
        global matrix

        x = pos[0]
        y = pos[1]

        circle_positions = [(0, 0), (-2, -1), (-1, -1), (-1, -2), (1, -2), (1, -1), (2, -1), (1, 1), (2, 1), (1, 2),
                            (-2, 1), (-1, 1), (-1, 2), (0, -2), (0, -1), (1, 0), (2, 0), (0, 1), (0, 2), (-2, 0),
                            (-1, 0)]

        col = advance_rainbow(4)

        for each in circle_positions:
            if 0 <= x + each[0] < MATRIX_W and 0 <= y + each[1] < MATRIX_H:
                matrix[y + each[1]][x + each[0]] = col

    dx = 0
    dy = 0
    mx = 0
    my = 0
    global matrix
    prev = ()
    while True:
        check_buttons()
        dx += 11
        dy += 7

        mx = (math.cos(dx / 243) + math.cos(dy / 253)) * MATRIX_W / 4
        my = (math.sin(dx / 347) + math.cos(dy / 363)) * MATRIX_H / 4

        cent = (int(MATRIX_W / 2 + mx), int(MATRIX_H / 2 + my))

        if cent != prev:
            dim_matrix(0.95)
            drawCircle(cent)
            prev = cent
            showPixels()
            time.sleep(0.005)


def fading_pixels_loop():
    display_header()
    global matrix
    global primaryColour
    reset_matrix()

    while True:
        check_buttons()

        col = advance_rainbow(3)

        for p in range(8):
            matrix[random.randint(0, MATRIX_H - 1)][random.randint(0, MATRIX_W - 1)] = col

        showPixels()
        time.sleep(0.05)

        dim_matrix()


def colour_scroll_loop():
    display_header()
    global matrix
    global hsv_i
    global primaryColour

    for x in range(MATRIX_W):
        col = advance_rainbow(4)
        for y in range(MATRIX_H):
            matrix[y].pop(0)
            matrix[y].append(col)

    showPixels()

    while True:
        check_buttons()

        col = hsv[hsv_i]

        for x in range(MATRIX_H):
            matrix[x].pop(0)
            matrix[x].append(col)

        primaryColour = advance_rainbow(2)

        showPixels()

        time.sleep(0.02)


def line_fill_loop():
    display_header()
    global matrix
    reset_matrix()

    while True:
        for y in range(MATRIX_H):
            for x in range(MATRIX_W):
                check_buttons()

                if y % 2 == 0:
                    matrix[y][x] = advance_rainbow(6)
                else:
                    matrix[y][MATRIX_W - 1 - x] = advance_rainbow(6)

                showPixels()
                time.sleep(0.01)


def spiral_loop():
    display_header()
    global matrix
    reset_matrix()

    path = [[0, 0]]

    directions = {"right": [1, 0],
                  "down": [0, 1],
                  "left": [-1, 0],
                  "up": [0, -1]}

    def get_new_direction():
        if path[-1][0] + 1 <= MATRIX_W - 1 and [path[-1][0] + 1, path[-1][1]] not in path:
            return "right"
        elif path[-1][1] + 1 <= MATRIX_H - 1 and [path[-1][0], path[-1][1] + 1] not in path:
            return "down"
        elif path[-1][0] - 1 >= 0 and [path[-1][0] - 1, path[-1][1]] not in path:
            return "left"
        elif path[-1][1] - 1 >= 0 and [path[-1][0], path[-1][1] - 1] not in path:
            return "up"
        else:
            return "stop"

    direction = "right"

    for _ in range(MATRIX_H * MATRIX_W - 1):
        next_x = path[-1][0] + directions[direction][0]
        next_y = path[-1][1] + directions[direction][1]
        if not 0 <= next_x < MATRIX_W or not 0 <= next_y < MATRIX_H or [next_x, next_y] in path:
            direction = get_new_direction()

        if direction == "right":
            path.append([path[-1][0] + 1, path[-1][1]])
        elif direction == "down":
            path.append([path[-1][0], path[-1][1] + 1])
        elif direction == "left":
            path.append([path[-1][0] - 1, path[-1][1]])
        elif direction == "up":
            path.append([path[-1][0], path[-1][1] - 1])

    while True:
        for pos in path:
            matrix[pos[1]][pos[0]] = advance_rainbow(2)
            showPixels()
            wait_for_delay(10)


def pixel_rain_loop():
    display_header()
    global matrix
    reset_matrix()

    while True:
        check_buttons()

        top_row = dim_matrix(0.9, [element for element in matrix[0]])

        matrix.pop()
        matrix.insert(0, top_row)

        if random.random() > 0.4:
            x = random.randint(0, MATRIX_W - 1)
            matrix[0][x] = advance_rainbow(10)

        showPixels()
        time.sleep(0.05)


def metaballs_loop():
    display_header()
    global matrix
    reset_matrix()

    def draw_metaballs(balls):
        global matrix

        circle_positions = [(-3, -3), (-3, -2), (-3, -1), (-3, 0), (-3, 1), (-3, 2), (-3, 3), (-2, -3), (-2, -2),
                            (-2, -1),
                            (-2, 0), (-2, 1), (-2, 2), (-2, 3), (-1, -3), (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2),
                            (-1, 3), (0, -3), (0, -2), (0, -1), (0, 0), (0, 1), (0, 2), (0, 3), (1, -3), (1, -2),
                            (1, -1),
                            (1, 0), (1, 1), (1, 2), (1, 3), (2, -3), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2), (2, 3),
                            (3, -3), (3, -2), (3, -1), (3, 0), (3, 1), (3, 2), (3, 3), (3,4)]

        col = advance_rainbow(5)

        for ball in balls:
            x = int(ball[0])
            y = int(ball[1])
            for each in circle_positions:
                if 0 <= x + each[0] < MATRIX_W and 0 <= y + each[1] < MATRIX_H:
                    dist = get_magnitude(each)
                    dimmed_col = []

                    for c in col:
                        dim = c / (1 + (dist) ** 2)
                        dimmed_col.append(dim)

                    current_matrix = matrix[y + each[1]][x + each[0]]
                    added_matrix = [a + b if a + b <= 255 else 255 for a, b in zip(current_matrix, dimmed_col)]
                    matrix[y + each[1]][x + each[0]] = added_matrix

    num_balls = 3
    b_pos = []
    b_vel = []

    speed = 1  # pixels/frame

    for n in range(num_balls):
        b_pos.append([random.randint(0, MATRIX_W - 1), random.randint(0, MATRIX_H  - 1)])
        b_vel.append([random.random(), random.random()])

    for vel in b_vel:
        mag = get_magnitude(vel)
        vel[0] *= speed / mag
        vel[1] *= speed / mag

    while True:
        for ball in range(num_balls):
            b_pos[ball][0] = b_pos[ball][0] + b_vel[ball][0]
            b_pos[ball][1] = b_pos[ball][1] + b_vel[ball][1]

            if 0 >= b_pos[ball][0] or b_pos[ball][0] > MATRIX_W:
                b_vel[ball][0] *= -1

                mag = get_magnitude(b_vel[ball])
                b_vel[ball][0] *= speed / mag
                b_vel[ball][1] *= speed / mag

                b_pos[ball][0] = b_pos[ball][0] + b_vel[ball][0]

            if 0 >= b_pos[ball][1] or b_pos[ball][1] > MATRIX_H:
                b_vel[ball][1] *= -1

                mag = get_magnitude(b_vel[ball])
                b_vel[ball][0] *= speed / mag
                b_vel[ball][1] *= speed / mag

                b_pos[ball][1] = b_pos[ball][1] + b_vel[ball][1]

        if 0 <= b_pos[ball][0] <= MATRIX_W and 0 <= b_pos[ball][1] <= MATRIX_H:
            reset_matrix()
            draw_metaballs(b_pos)

        time.sleep(0.028)

        showPixels()

        check_buttons()


def ants_loop():
    display_header()
    global matrix
    reset_matrix()

    directions = {0: (1, 0),  # right
                  1: (0, 1),  # down
                  2: (-1, 0),  # left
                  3: (0, -1)  # up
                  }

    num_ants = 4
    ants = []
    for n in range(num_ants):
        ants.append([random.randint(0, MATRIX_W - 1), random.randint(0, MATRIX_H - 1)])

    col = [255, 255, 255]
    while True:
        for ant in ants:
            error_direction = []
            if ant[0] == MATRIX_W - 1:
                error_direction.append(0)
            if ant[1] == MATRIX_H - 1:
                error_direction.append(1)
            if ant[0] == 0:
                error_direction.append(2)
            if ant[1] == 0:
                error_direction.append(3)

            options = [each for each in [0, 1, 2, 3] if each not in error_direction]

            choice = random.choice(options)

            ant[0] += directions[choice][0]
            ant[1] += directions[choice][1]

            matrix[ant[1]][ant[0]] = col

        showPixels()
        dim_matrix(0.9)
        time.sleep(0.1)

        check_buttons()


def time_scroll_loop():
    display_header()
    global matrix
    reset_matrix()
    scroll_speed = 80

    while True:
        now = datetime.now()
        time_text = now.strftime("%A ") + str(now.day) + \
                    ("th" if 4 <= now.day <= 20 or 24 <= now.day <= 30 else ["st", "nd", "rd"][now.day % 10 - 1]) \
                    + now.strftime(" %B %Y * %H:%M:%S * ")
        scroll_text(time_text, [255, 255, 255], black, scroll_speed, 8)


def blobs_loop():
    display_header()
    global matrix
    reset_matrix()

    num_balls = 3
    b_pos = []
    b_vel = []

    speed = 1  # pixels/frame

    for n in range(num_balls):
        b_pos.append([random.randint(0, MATRIX_W - 1), random.randint(0, MATRIX_H - 1)])
        b_vel.append([random.random(), random.random()])

    for vel in b_vel:
        mag = get_magnitude(vel)
        vel[0] *= speed / mag
        vel[1] *= speed / mag

    while True:
        for ball in range(num_balls):
            b_pos[ball][0] = b_pos[ball][0] + b_vel[ball][0]
            b_pos[ball][1] = b_pos[ball][1] + b_vel[ball][1]

            if 0 >= b_pos[ball][0] or b_pos[ball][0] > MATRIX_W:
                b_vel[ball][0] *= -1

                mag = get_magnitude(b_vel[ball])
                b_vel[ball][0] *= speed / mag
                b_vel[ball][1] *= speed / mag

                b_pos[ball][0] = b_pos[ball][0] + b_vel[ball][0]

            if 0 >= b_pos[ball][1] or b_pos[ball][1] > MATRIX_H:
                b_vel[ball][1] *= -1

                mag = get_magnitude(b_vel[ball])
                b_vel[ball][0] *= speed / mag
                b_vel[ball][1] *= speed / mag

                b_pos[ball][1] = b_pos[ball][1] + b_vel[ball][1]

        for j in range(MATRIX_H):
            for i in range(MATRIX_W):
                min_dist = max(MATRIX_W, MATRIX_H)
                for ball in range(num_balls):
                    dist = ((b_pos[ball][0] - i) ** 2 + (b_pos[ball][1] - j) ** 2) ** 0.5
                    if dist < min_dist:
                        min_dist = dist
                col_index = int(min_dist * 20)
                if col_index >= len(hsv) - 1:
                    col_index = len(hsv) - 1

                matrix[j][i] = hsv[col_index]

        time.sleep(0.1)

        showPixels()

        check_buttons()


def snake_loop():
    display_header()
    global matrix
    reset_matrix()

    def new_food(tail, food):
        global matrix
        f = food
        while f in tail:
            f = [random.randint(0, MATRIX_W - 1), random.randint(0, MATRIX_H - 1)]

        matrix[f[1]][f[0]] = advance_rainbow(50)
        return f

    def get_next_move(c):
        if 0 < c[0] < MATRIX_W - 1 and c[1] % 2 == 1:
            d = "r"
        elif 0 < c[0] < MATRIX_W - 1 and c[1] % 2 == 0:
            d = "l"
        elif c[0] == MATRIX_W - 1 and c[1] % 2 == 0:
            d = "l"
        elif c[0] == 0 and c[1] % 2 == 1:
            d = "r"
        else:
            d = "d"

        return d

    def get_next_move_ai(c, f):
        if c[0] == f[0] and c not in tail[:-1]:
            d = "d"
        elif 0 < c[0] < MATRIX_W - 1 and c[1] % 2 == 1:
            d = "r"
        elif 0 < c[0] < MATRIX_W - 1 and c[1] % 2 == 0:
            d = "l"
        elif c[0] == MATRIX_W - 1 and c[1] % 2 == 0:
            d = "l"
        elif c[0] == 0 and c[1] % 2 == 1:
            d = "r"
        else:
            d = "d"

        return d

    def snake_dead(tail, score):
        for n in range(12):
            matrix[tail[-1][1]][tail[-1][0]] = [0, 0, 255] if n % 2 == 0 else [255, 255, 255]
            showPixels()
            wait_for_delay(100)

        hs_file = open('highscore.txt', 'r')
        highscores = hs_file.readlines()
        if invisible_walls == True:
            hs = int(highscores[1])
        else:
            hs = int(highscores[0])

        if score > hs:
            hs_file = open('highscore.txt', 'w')
            if invisible_walls:
                highscores[1] = str(score)
            else:
                highscores[0] = str(score) + "\n"

            hs_file.writelines(highscores)
            hs_file.close()
            for n in range(8):
                if n % 2 == 0:
                    load_image("first_place")
                else:
                    reset_matrix()
                showPixels()
                wait_for_delay(300)

        reset_matrix()
        if score > 99:
            score = "++"
        place_3x5_num((4, 6), str(score).zfill(2)[0], white, black)
        place_3x5_num((9, 6), str(score).zfill(2)[1], white, black)
        showPixels()
        wait_for_delay(2000)
        snake_loop()

    tail = [[2, 7], [3, 7], [4, 7]]
    invincible_mode = False
    invisible_walls = True
    new_direction = "r"
    food = [random.randint(0, MATRIX_W - 1), random.randint(0, MATRIX_H - 1)]
    new_food(tail, food)
    score = 0
    while True:
        if new_direction == "r":
            current_direction = new_direction
            tail.append([tail[-1][0] + 1, tail[-1][1]])
        elif new_direction == "d":
            current_direction = new_direction
            tail.append([tail[-1][0], tail[-1][1] + 1])
        elif new_direction == "l":
            current_direction = new_direction
            tail.append([tail[-1][0] - 1, tail[-1][1]])
        elif new_direction == "u":
            current_direction = new_direction
            tail.append([tail[-1][0], tail[-1][1] - 1])

        if invisible_walls:
            if tail[-1][0] > MATRIX_W - 1:
                tail[-1][0] = 0
            if tail[-1][1] > MATRIX_H - 1:
                tail[-1][1] = 0
            if tail[-1][0] < 0:
                tail[-1][0] = MATRIX_W - 1
            if tail[-1][1] < 0:
                tail[-1][1] = MATRIX_H - 1

        if tail[-1] == food:
            matrix[tail[-1][1]][tail[-1][0]] = [255, 255, 255]
            score += 1
            food = new_food(tail, food)
        else:
            matrix[tail[0][1]][tail[0][0]] = [0, 0, 0]
            tail.pop(0)

        if not invisible_walls and (not 0 <= tail[-1][0] <= MATRIX_W - 1 or not 0 <= tail[-1][1] <= MATRIX_H - 1):
            tail.pop(len(tail) - 1)
            snake_dead(tail, score)

        if tail[-1] in tail[:-1] and not invincible_mode:
            snake_dead(tail, score)
        else:
            for pos in tail:
                matrix[pos[1]][pos[0]] = [255, 255, 255]

        time.sleep(0.1)
        button("", display_width - 40, 8, 32, 32, action=settings)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and current_direction != "r":
                    new_direction = "l"
                elif event.key == pygame.K_RIGHT and current_direction != "l":
                    new_direction = "r"
                elif event.key == pygame.K_UP and current_direction != "d":
                    new_direction = "u"
                elif event.key == pygame.K_DOWN and current_direction != "u":
                    new_direction = "d"

        # uncomment the line below for cheat mode
        # new_direction = get_next_move(tail[-1])
        # hs 51 without
        # new_direction = get_next_move_ai(tail[-1], food)

        showPixels()


def pong_loop():
    display_header()
    global matrix

    p1_score = 0
    p2_score = 0

    def pong_reset():
        reset_matrix()

        ball = [random.randint((MATRIX_W / 2) - 1, MATRIX_W / 2) if MATRIX_W % 2 == 0 else (MATRIX_W - 1) / 2,
                random.randint((MATRIX_H / 2) - 1, MATRIX_H / 2) if MATRIX_H % 2 == 0 else (MATRIX_H - 1) / 2]

        vel_x = -1 if bool(random.getrandbits(1)) else 1
        vel_y = random.triangular(0.1, 0.3) if bool(random.getrandbits(1)) else random.triangular(-0.1, -0.3)

        vel = [vel_x, vel_y]

        speed = 1
        mag = get_magnitude(vel)
        vel[0] *= speed / mag
        vel[1] *= speed / mag

        p1_bat_length = 5
        p2_bat_length = 5

        p1_bat_s = int((MATRIX_H / 2) - (p1_bat_length / 2))
        p1_bat_e = int((MATRIX_H / 2) + (p1_bat_length / 2))

        p2_bat_s = int((MATRIX_H / 2) - (p2_bat_length / 2))
        p2_bat_e = int((MATRIX_H / 2) + (p2_bat_length / 2))

        p1_bat = [e for e in range(p1_bat_s, p1_bat_e)]
        p2_bat = [e for e in range(p2_bat_s, p2_bat_e)]

        delay = 60

        return ball, vel, p1_bat, p2_bat, delay

    def pong_winner(player):
        reset_matrix()
        scroll_text("Player " + str(player) + " wins!   ", [0, 255, 0] if player == 1 else [0, 0, 255], black, 50)

        pong_loop()

    ball, vel, p1_bat, p2_bat, delay = pong_reset()

    while True:
        # # # # DRAWING SECTION # # # #

        # Draw the bats
        for j in range(MATRIX_H):
            matrix[j][0] = [0, 255, 0] if j in p1_bat else [0, 0, 0]
            matrix[j][MATRIX_W - 1] = [0, 0, 255] if j in p2_bat else [0, 0, 0]

        # Draw the score
        if p1_score <= 9 and p2_score <= 9:
            place_3x5_num((int(MATRIX_W / 2) - 4, 3), str(p1_score), [30, 80, 30], [0, 0, 0])
            place_3x5_num((int(MATRIX_W / 2) + 2, 3), str(p2_score), [30, 30, 80], [0, 0, 0])

        # Draw the ball
        matrix[int(ball[1])][int(ball[0])] = [255, 255, 255]

        showPixels()

        matrix[int(ball[1])][int(ball[0])] = [0, 0, 0]

        # # # # END OF DRAWING SECTION # # # #

        # # # # GAME LOGIC SECTION # # # #

        if int(ball[0]) == 1:
            if int(ball[1]) in p1_bat:
                vel[0] *= -1
                delay -= 2

        if int(ball[0]) == MATRIX_W - 2:
            if int(ball[1]) in p2_bat:
                vel[0] *= -1

        if not 0 < int(ball[1]) < MATRIX_H - 1:
            vel[1] *= -1

        ball[0] += vel[0]
        ball[1] += vel[1]

        if int(ball[0]) == 0:
            p2_score += 1
            if p1_score <= 9 and p2_score <= 9:
                place_3x5_num((int(MATRIX_W / 2) - 4, 3), str(p1_score), [30, 80, 30], [0, 0, 0])
                place_3x5_num((int(MATRIX_W / 2) + 2, 3), str(p2_score), [30, 30, 80], [0, 0, 0])

            for rep in range(7):
                matrix[int(ball[1])][int(ball[0])] = [255, 0, 0] if rep % 2 == 0 else [255, 255, 255]
                showPixels()
                wait_for_delay(100)

            if p1_score == 10: pong_winner(1)
            if p2_score == 10: pong_winner(2)
            ball, vel, p1_bat, p2_bat, delay = pong_reset()

        if int(ball[0]) == MATRIX_W - 1:
            p1_score += 1
            if p1_score <= 9 and p2_score <= 9:
                place_3x5_num((int(MATRIX_W / 2) - 4, 3), str(p1_score), [30, 80, 30], [0, 0, 0])
                place_3x5_num((int(MATRIX_W / 2) + 2, 3), str(p2_score), [30, 30, 80], [0, 0, 0])

            for rep in range(7):
                matrix[int(ball[1])][int(ball[0])] = [255, 0, 0] if rep % 2 == 0 else [255, 255, 255]
                showPixels()
                wait_for_delay(100)

            if p1_score == 10: pong_winner(1)
            if p2_score == 10: pong_winner(2)
            ball, vel, p1_bat, p2_bat, delay = pong_reset()

        # # # # END OF GAME LOGIC SECTION # # # #

        # # # # PLAYER INPUT SECTION # # # #

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and not keys[pygame.K_s] and p1_bat[-1] > 0:
            for i in range(len(p1_bat)):
                p1_bat[i] -= 1
        elif keys[pygame.K_s] and not keys[pygame.K_w] and p1_bat[0] < MATRIX_H - 1:
            for i in range(len(p1_bat)):
                p1_bat[i] += 1

        if keys[pygame.K_UP] and not keys[pygame.K_DOWN] and p2_bat[-1] > 0:
            for i in range(len(p2_bat)):
                p2_bat[i] -= 1
        elif keys[pygame.K_DOWN] and not keys[pygame.K_UP] and p2_bat[0] < MATRIX_H - 1:
            for i in range(len(p2_bat)):
                p2_bat[i] += 1

        # # # # END OF PLAYER INPUT SECTION # # # #

        '''time.sleep(delay)
        
        check_buttons()'''

        wait_for_delay(delay)


def image_viewer_loop():
    display_header()

    def set_image(text, x, y, w, h):
        global current_image

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.draw.rect(screen, (50, 50, 50), (x, y, w, h))
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects(text, smallText, white)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        screen.blit(textSurf, textRect)

        if x + w > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
            current_image = text
            image_viewer_loop()

        return True

    def change_image():
        display_header()

        medText = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects("Select an image to view", medText, (255, 255, 255))
        TextRect.center = (display_width / 2, 100)
        screen.blit(TextSurf, TextRect)

        image_file = open("image_file.txt", "r")
        image_names = []
        for line in image_file.readlines():
            image_name = line[:line.find("=") - 1]
            image_names.append(image_name)
        image_file.close()
        num_cols = 12
        while True:

            for i in range(len(image_names)):
                if len(image_names) > num_cols:
                    set_image(image_names[i], 20 if i < num_cols else display_width / 2 + 10, 120 + (i % num_cols) * 35,
                              display_width / 2 - 30, 30)

            button("return", 20, display_height - 100, display_width - 40, 40, (50, 50, 50), action=image_viewer_loop)
            check_buttons()
            pygame.display.update()

    showPixels()
    last_image = ""
    button("Change Image", 20, top - 45, display_width - 40, 40, (50, 50, 50), action=change_image)
    pygame.display.update()

    while True:
        if current_image != last_image:
            load_image(current_image)
            showPixels()
            last_image = current_image
            button("Change Image", 20, top - 45, display_width - 40, 40, (50, 50, 50), action=change_image)
            pygame.display.update()
        button("Change Image", 20, top - 45, display_width - 40, 40, (50, 50, 50), action=change_image)
        check_buttons()


def rotate_loop():
    display_header()

    angle = 0
    increment = 30
    middle_positions = []

    if MATRIX_H % 2 == 0:
        if MATRIX_W % 2 == 0:
            x_middle = math.floor((MATRIX_W - 1) / 2)
            y_middle = math.floor((MATRIX_H - 1) / 2)
            middle_positions.append((x_middle, y_middle))
            middle_positions.append((x_middle + 1, y_middle))
            middle_positions.append((x_middle, y_middle + 1))
            middle_positions.append((x_middle + 1, y_middle + 1))
        else:
            x_middle = math.floor(MATRIX_W / 2)
            y_middle = math.floor((MATRIX_H - 1) / 2)
            middle_positions.append((x_middle, y_middle))
            middle_positions.append((x_middle, y_middle + 1))
    else:
        if MATRIX_W % 2 == 0:
            x_middle = math.floor((MATRIX_W - 1) / 2)
            y_middle = math.floor(MATRIX_H / 2)
            middle_positions.append((x_middle, y_middle))
            middle_positions.append((x_middle + 1, y_middle))
        else:
            x_middle = math.floor(MATRIX_W / 2)
            y_middle = math.floor(MATRIX_H / 2)
            middle_positions.append((x_middle, y_middle))

    while True:
        reset_matrix()
        col = advance_rainbow(5)
        for i in range(MATRIX_H):
            for j in range(MATRIX_W):
                if MATRIX_H % 2 == 0:
                    dy = i - ((MATRIX_H - 1) / 2)
                else:
                    dy = i - math.floor(MATRIX_H / 2)

                if MATRIX_W % 2 == 0:
                    dx = j - ((MATRIX_W - 1) / 2)
                else:
                    dx = j - math.floor(MATRIX_W / 2)

                pixel_angle = math.degrees(math.atan2(dy, dx))
                if i < 8:
                    pixel_angle += 360

                pixel_angle %= 90

                if angle < 60:
                    if angle < pixel_angle < angle + 30:
                        matrix[i][j] = col
                else:
                    if pixel_angle > angle or pixel_angle < (angle + 30) % 90:
                        matrix[i][j] = col

        for m_pos in middle_positions:
            matrix[m_pos[1]][m_pos[0]] = col

        showPixels()

        if angle < 90:
            angle += 5
        else:
            angle = 5

        time.sleep(0.05)
        check_buttons()


def temp_loop():
    display_header()

    url = "http://api.openweathermap.org/data/2.5/weather?id=2647138"
    units = "&units=metric&"
    auth = "appid=ca7ef74d66875da240c31664dba63e81"

    while True:
        reset_matrix()
        raw_data = urllib.request.urlopen(url + units + auth).read().decode()
        weather = json.loads(raw_data)
        temp = str(int(weather["main"]["temp"])).zfill(2)
        if temp[0] != "0":
            place_3x5_num((2, 5), temp[0], (232, 121, 45), (0, 0, 0))
        place_3x5_num((6, 5), temp[1], (232, 121, 45), (0, 0, 0))
        deg_c = [(10, 5), (13, 5), (12, 5), (12, 6), (12, 7), (13, 7)]
        for i in deg_c:
            matrix[i[1]][i[0]] = [232, 121, 45]

        showPixels()
        wait_for_delay(10000)

        weather_scroll = "  * " + str(weather['weather'][0]['description']) + " * Pressure " \
                         + str(weather['main']['pressure']) + "hPa *   "
        scroll_text(weather_scroll)

        hum = str(int(weather["main"]["humidity"]))
        place_3x5_num((2, 5), hum[0], (255, 255, 255), (0, 0, 0))
        place_3x5_num((6, 5), hum[1], (255, 255, 255), (0, 0, 0))
        place_3x5_num((10, 5), "%", (255, 255, 255), (0, 0, 0))

        showPixels()
        wait_for_delay(10000)


def random_walk_loop():
    display_header()
    global matrix

    x = 7
    y = 7

    directions = {0: (1, 0),  # right
                  1: (0, 1),  # down
                  2: (-1, 0),  # left
                  3: (0, -1)  # up
                  }
    while True:
        col = advance_rainbow(1)

        error_direction = []
        if x == MATRIX_W - 1:
            error_direction.append(0)
        if y == MATRIX_H - 1:
            error_direction.append(1)
        if x == 0:
            error_direction.append(2)
        if y == 0:
            error_direction.append(3)

        options = [each for each in [0, 1, 2, 3] if each not in error_direction]

        choice = random.choice(options)

        x += directions[choice][0]
        y += directions[choice][1]

        matrix[y][x] = col

        showPixels()
        dim_matrix()
        time.sleep(0.02)

        check_buttons()


def bounce_loop():
    display_header()
    global matrix

    pos = [7, MATRIX_H - 1]
    vel = [0, -1]
    acc = [0, 0.05]
    while True:
        if int(pos[1]) > MATRIX_H - 1:
            pos[1] = MATRIX_H - 1
            vel[1] = -1
        if int(pos[1]) < 1:
            pos[1] = 0
        if int(pos[0]) > MATRIX_W - 2:
            pos[0] = MATRIX_W - 2
            vel[0] = -0.1
        if int(pos[0]) < 0:
            pos[0] = 0
            vel[0] = 0.1

        reset_matrix()
        matrix[int(pos[1])-1][int(pos[0])] = [0, 255, 0]
        matrix[int(pos[1])-1][int(pos[0])+1] = [0, 255, 0]
        matrix[int(pos[1])][int(pos[0])] = [0, 255, 0]
        matrix[int(pos[1])][int(pos[0])+1] = [0, 255, 0]

        pos[0] += vel[0]
        pos[1] += vel[1]
        vel[0] += acc[0]
        vel[1] += acc[1]

        showPixels()
        time.sleep(0.01)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    vel[1] = -1
                if event.key == pygame.K_ESCAPE:
                    close()


def seek_loop():
    display_header()
    global matrix

    def get_pixel(pos, old):
        x_valid = False
        y_valid = False

        for p in range(MATRIX_W):
            if border * (p + 1) + pixel_s * p < pos[0] < border * (p + 1) + pixel_s * (p + 1):
                x_pixel = p
                x_valid = True
                break

        for p in range(MATRIX_W):
            if top + border * p + pixel_s * p < pos[1] < top + border * p + pixel_s * (p + 1):
                y_pixel = p
                y_valid = True
                break

        if x_valid and y_valid:
            return (x_pixel, y_pixel)
        else:
            return old

    pos = [8, 8]
    vel = [0, 1]
    acc = [0, 0]

    max_speed = 0.1
    max_force = 0.003

    target = (0, 0)
    force = [0, 0]
    while True:

        # Find and draw the target
        target = get_pixel(pygame.mouse.get_pos(), target)
        if len(target) > 0:
            reset_matrix()
            matrix[int(target[1])][int(target[0])] = [0, 255, 0]

        vel[0] += acc[0]
        vel[1] += acc[1]
        mag = get_magnitude(vel)
        if mag > max_speed:
            vel[0] *= max_speed / mag
            vel[1] *= max_speed / mag

        pos[0] += vel[0]
        pos[1] += vel[1]

        acc = [0, 0]
        acc[0] += force[0]
        acc[1] += force[1]

        desired = [target[0] - pos[0], target[1] - pos[1]]

        force[0] = desired[0] - vel[0]
        force[1] = desired[1] - vel[1]

        mag = get_magnitude(force)
        if mag > max_force:
            force[0] *= max_force / mag
            force[1] *= max_force / mag

        if 0 <= int(pos[0]) <= MATRIX_W - 1 and 0 <= int(pos[1]) <= MATRIX_H - 1:
            matrix[int(pos[1])][int(pos[0])] = [255, 255, 255]

        showPixels()
        time.sleep(0.01)

        check_buttons()


def game_of_life_loop():
    display_header()
    global matrix
    around_positions = [(-1,-1), (0,-1), (1,-1),
                        (-1,0), (1,0),
                        (-1,1), (0,1), (1,1)]



    while True:
        alive = [255, 255, 255]
        showPixels()
        updated_matrix = []
        for i in range(MATRIX_H):
            updated_matrix.append([])
        for j in range(MATRIX_H):
            for rep in range(MATRIX_W):
                updated_matrix[j].append(black)

        for col in range(MATRIX_H):
            for row in range(MATRIX_W):
                alive_count = 0
                for pos in around_positions:
                    if 0 <= row + pos[1] < MATRIX_H and 0 <= col + pos[0] < MATRIX_W:
                        if matrix[row + pos[1]][col + pos[0]] != [0, 0, 0]:
                            alive_count += 1

                if matrix[row][col] != [0, 0, 0]:
                    if alive_count == 2 or alive_count == 3:
                        updated_matrix[row][col] = alive
                    else:
                        updated_matrix[row][col] = [0, 0, 0]
                else:
                    if alive_count == 3:
                        updated_matrix[row][col] = alive
                    else:
                        updated_matrix[row][col] = [0, 0, 0]

        if matrix != updated_matrix:
            matrix = updated_matrix
        else:
            print("the same")
            for i in range(MATRIX_H):
                for j in range(MATRIX_W):
                    if random.random() > 0.9:
                        matrix[i][j] = alive

        wait_for_delay(250)
        check_buttons()


def custom_text_loop():
    display_header()
    global matrix

    def changeText():

        x, y, w, h = 30, 80, 300, 100
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.draw.rect(screen, [200,40, 40], (x, y, w, h))
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects('Customise', smallText, black)

        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        screen.blit(textSurf, textRect)

        if x + w > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
            c_text_input = pag.prompt(text='Type in the custom text to be displayed',
                                  title='Custom text', )
            return c_text_input
        else:
            return "1"

    c_text = "Custom Text    "

    while True:
        check_buttons()
        # Scroll text here
        c_text = changeText()
        scroll_text(c_text)
        wait_for_delay(250)


def flappy_bird_loop():
    display_header()
    global matrix
    reset_matrix()
    pos = int(MATRIX_H / 2)
    vel = 0
    max_vel = 0.4
    force = 0.03

    while True:
        if int(pos) > MATRIX_H - 1:
            pos = MATRIX_H - 1
        if int(pos) < 0:
            pos = 0

        if vel > max_vel:
            vel = max_vel
        if vel < -max_vel:
            vel = -max_vel

        reset_matrix()
        matrix[int(pos)][1] = [255, 0, 0]

        pos += vel

        showPixels()
        wait_for_delay(0.01)

        key_states = pygame.key.get_pressed()

        if key_states[pygame.K_UP] and not key_states[pygame.K_DOWN]:
            vel -= force
        elif key_states[pygame.K_DOWN] and not key_states[pygame.K_UP]:
            vel += force

        check_buttons()


def first_light_loop():
    display_header()
    global matrix
    count = 0

    while True:
        dim_matrix(0.9)
        # reset_matrix()
        matrix[math.floor(count / MATRIX_W)][count % MATRIX_W] = advance_rainbow(20)
        showPixels()
        wait_for_delay(20)
        if count == (MATRIX_W * MATRIX_H) - 1:
            count = 0
        else:
            count += 1


def random_loop():
    display_header()
    global matrix
    count = 1

    while True:
        for i in range(MATRIX_H):
            for j in range(MATRIX_W):
                if i * j % 2 == 0:
                    matrix[i][j] = [255, 255, 0]
                else:
                    matrix[i][j] = [0, 0, 0]

        count += 1
        showPixels()
        wait_for_delay(200)


def squares_loop():
    display_header()
    global matrix

    squares = []

    def new_square(rad=0):
        x = random.randint(0, MATRIX_W - 1)
        y = random.randint(0, MATRIX_H - 1)
        radius = rad
        colour = advance_rainbow(20)
        squares.append([x, y, radius, colour])
        # [x, y, radius, colour]

    amount = math.floor(max((MATRIX_W, MATRIX_H)) / 5)

    for r in range(amount):
        new_square(int(r * (max((MATRIX_W, MATRIX_H)) / amount)))

    while True:
        reset_matrix()
        for square in squares:
            x = square[0]
            y = square[1]
            radius = square[2]
            col = square[3]

            for i in range(MATRIX_H):
                for j in range(MATRIX_W):
                    if (j == x - radius or j == x + radius) and (i >= y - radius and i <= y + radius) \
                            or (i == y - radius or i == y + radius) and (j <= x + radius and j >= x - radius):
                        matrix[i][j] = col

            square[2] += 1

        to_delete = []

        for each in range(len(squares)):
            x = squares[each][0]
            y = squares[each][1]
            radius = squares[each][2]
            top = y - radius
            bottom = y + radius
            left = x - radius
            right = x + radius
            if top < 0 and bottom > MATRIX_H - 1 and left < 0 and right > MATRIX_W -1:
                to_delete.append(each)
                new_square()

        for each in to_delete:
            squares.pop(each)

        showPixels()
        wait_for_delay(50)


def fire_loop():
    display_header()
    global matrix
    reset_matrix()
    fire = []
    inner = []
    for j in range(MATRIX_W):
        inner.append(0)
    for i in range(MATRIX_H):
        fire.append(inner)
    palette = [[0, 0, 0], [4, 0, 0], [8, 0, 0], [12, 0, 0], [16, 0, 0], [20, 0, 0], [24, 1, 0], [28, 1, 0], [32, 2, 0], [36, 2, 0], [40, 3, 0], [44, 3, 0], [48, 4, 0], [52, 5, 0], [56, 6, 0], [60, 7, 0], [64, 8, 0], [68, 9, 0], [72, 10, 0], [76, 11, 0], [80, 12, 0], [84, 13, 0], [88, 15, 0], [92, 16, 0], [96, 18, 0], [100, 19, 0], [104, 21, 0], [108, 22, 0], [112, 24, 0], [116, 26, 0], [120, 28, 0], [124, 30, 0], [128, 32, 0], [132, 34, 0], [136, 36, 0], [140, 38, 0], [144, 40, 0], [148, 42, 0], [152, 45, 0], [156, 47, 0], [160, 50, 0], [164, 52, 0], [168, 55, 0], [172, 58, 0], [176, 60, 0], [180, 63, 0], [184, 66, 0], [188, 69, 0], [192, 72, 0], [196, 75, 0], [200, 78, 0], [204, 81, 0], [208, 84, 0], [212, 88, 0], [216, 91, 0], [220, 94, 0], [224, 98, 0], [228, 101, 0], [232, 105, 0], [236, 109, 0], [240, 112, 0], [244, 116, 0], [248, 120, 0], [252, 124, 0], [255, 128, 0], [255, 132, 4], [254, 136, 9], [254, 140, 13], [254, 143, 17], [254, 147, 21], [255, 151, 25], [255, 154, 29], [255, 158, 32], [255, 161, 36], [255, 165, 41], [255, 168, 45], [255, 171, 48], [255, 174, 52], [255, 178, 57], [255, 181, 61], [255, 184, 65], [255, 187, 68], [254, 190, 73], [254, 192, 77], [254, 195, 81], [254, 198, 85], [255, 200, 89], [255, 203, 93], [255, 206, 97], [255, 208, 100], [255, 210, 105], [255, 213, 109], [255, 215, 113], [255, 217, 116], [255, 219, 121], [255, 221, 125], [255, 223, 129], [255, 225, 132], [254, 227, 137], [254, 229, 141], [254, 231, 145], [254, 232, 149], [255, 234, 153], [255, 236, 157], [255, 237, 161], [255, 239, 164], [255, 240, 169], [255, 241, 173], [255, 243, 177], [255, 244, 180], [255, 245, 185], [255, 246, 189], [255, 247, 193], [255, 248, 196], [254, 249, 201], [254, 250, 205], [254, 250, 209], [254, 251, 213], [255, 252, 217], [255, 252, 221], [255, 253, 225], [255, 253, 228], [255, 254, 233], [255, 254, 237], [255, 254, 241], [255, 254, 244], [255, 254, 249], [255, 254, 253], [255, 255, 257], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]]

    while True:
        for x in range(MATRIX_W):
            fire[MATRIX_H - 1][x] = random.randint(0, 256)

        '''for y in range(MATRIX_H - 2):
            for x in range(MATRIX_W):
                fire[y][x] = (fire[(y + 1) % MATRIX_H][(x - 1 + MATRIX_W) % MATRIX_W] +
                              fire[(y + 1) % MATRIX_H][(x + MATRIX_W) % MATRIX_W] +
                              fire[(y + 1) % MATRIX_H][(x + 1 + MATRIX_W) % MATRIX_W] +
                              fire[(y + 2) % MATRIX_H][(x + MATRIX_W) % MATRIX_W]) / 4.4
        '''
        print(fire)
        for i in range(MATRIX_H):
            for j in range(MATRIX_W):
                matrix[i][j] = palette[int(fire[j][i])]

        showPixels()
        wait_for_delay(1000)


def tetris_loop():
    display_header()
    global matrix
    reset_matrix()

    block_shapes = {1: [[(0, 0), (1, 0), (0, 1), (1, 1)],  # ***Square*** #
                        [(0, 0), (1, 0), (0, 1), (1, 1)],
                        [(0, 0), (1, 0), (0, 1), (1, 1)],
                        [(0, 0), (1, 0), (0, 1), (1, 1)]],
                    2: [[(0, 0), (1, 0), (2, 0), (0, 1)],  # ***L*** #
                        [(0, 0), (0, 1), (0, 2), (1, 2)],
                        [(0, 1), (1, 1), (2, 1), (2, 0)],
                        [(0, 0), (1, 0), (1, 1), (1, 2)]],
                    3: [[(0, 0), (0, 1), (1, 1), (2, 1)],  # ***Backward L*** #
                        [(1, 0), (1, 1), (1, 2), (0, 2)],
                        [(0, 0), (1, 0), (2, 0), (2, 1)],
                        [(0, 0), (0, 1), (0, 2), (1, 0)]],
                    4: [[(0, 1), (1, 1), (2, 1), (1, 0)],  # ***T*** #
                        [(1, 2), (1, 1), (1, 0), (0, 1)],
                        [(2, 1), (1, 1), (0, 1), (1, 2)],
                        [(1, 0), (1, 1), (1, 2), (2, 1)]],
                    5: [[(1, 0), (1, 1), (0, 1), (0, 2)],  # ***Z*** #
                        [(0, 0), (1, 0), (1, 1), (2, 1)],
                        [(1, 0), (1, 1), (0, 1), (0, 2)],
                        [(0, 0), (1, 0), (1, 1), (2, 1)]],
                    6: [[(0, 1), (1, 1), (1, 0), (2, 0)],  # ***Backward Z*** #
                        [(0, 0), (0, 1), (1, 1), (1, 2)],
                        [(0, 1), (1, 1), (1, 0), (2, 0)],
                        [(0, 0), (0, 1), (1, 1), (1, 2)]],
                    7: [[(0, 1), (1, 1), (2, 1), (3, 1)],  # ***Line*** #
                        [(1, 0), (1, 1), (1, 2), (1, 3)],
                        [(0, 1), (1, 1), (2, 1), (3, 1)],
                        [(1, 0), (1, 1), (1, 2), (1, 3)]]
                    }
    block_widths = {
        1: [2, 2, 2, 2],
        2: [3, 2, 3, 2],
        3: [3, 2, 3, 2],
        4: [3, 2, 3, 3],
        5: [2, 3, 2, 3],
        6: [3, 2, 3, 2],
        7: [4, 2, 4, 2]
    }
    block_heights = {
        1: [2, 2, 2, 2],
        2: [2, 3, 2, 3],
        3: [2, 3, 2, 3],
        4: [2, 3, 3, 3],
        5: [3, 2, 3, 2],
        6: [2, 3, 2, 3],
        7: [2, 4, 2, 4]
    }
    block_colours = {1: [240, 240, 0],  # Square -> Yellow
                     2: [240, 160, 0],  # L -> Orange
                     3: [0, 0, 240],  # Backward L -> Blue
                     4: [160, 0, 240],  # T -> Purple
                     5: [240, 0, 0],  # Z -> Red
                     6: [0, 240, 0],  # Backward Z -> Green
                     7: [0, 240, 240]   # Line -> Light Blue
                     }

    blocks = []
    borders = []

    for w in range(MATRIX_W):
        borders.append((w, MATRIX_H - 1))

    for w in range(-3, MATRIX_H):
        borders.append((MATRIX_W - 1, w))
        borders.append((0, w))

    still_positions = []

    def new_block(block_type):
        new_type = block_type
        new_r = random.randint(0, 3)
        new_x = random.randint(1, MATRIX_W - block_widths[new_type][new_r] - 1)
        new_y = -block_heights[new_type][new_r]

        blocks.append([new_type, new_x, new_y, new_r])  # [Block type, x pos, y pos, rotation]

    def check_sides(move_type, direction):
        # A function to return whether a move is permitted or not
        if move_type == "rotate":
            if direction == "left":
                rot = 0 if blocks[-1][3] == 3 else blocks[-1][3] + 1
            else:
                rot = 3 if blocks[-1][3] == 0 else blocks[-1][3] - 1
            future_positions = [(blocks[-1][1] + block_shapes[blocks[-1][0]][rot][n][0],
                                 blocks[-1][2] + block_shapes[blocks[-1][0]][rot][n][1])
                                 for n in range(4)]
        else:
            if direction == "left":
                x_off = -1
                y_off = 0
            elif direction == "right":
                x_off = 1
                y_off = 0
            elif direction == "down":
                x_off = 0
                y_off = 1
            future_positions = [(blocks[-1][1] + block_shapes[blocks[-1][0]][blocks[-1][3]][n][0] + x_off,
                                blocks[-1][2] + block_shapes[blocks[-1][0]][blocks[-1][3]][n][1] + y_off)
                                for n in range(4)]

        # Code here to change intended move into an array of future positions
        still_positions_raw = [(i[0], i[1]) for i in still_positions]
        for pos in future_positions:
            if pos in still_positions_raw or pos in borders:
                return False

        return True

    def dead(score):
        wipe = [150, 150, 150]
        draw_blocks()
        for j in range(MATRIX_H - 1):
            for i in range(1, MATRIX_W - 1):
                matrix[MATRIX_H - 2 - j][i] = wipe
            showPixels()
            wait_for_delay(80)

        for j in range(MATRIX_H):
            draw_borders()
            for char in range(len(str(score))):
                top_left_pos = (int(MATRIX_W / 2) - int(len(str(score)) * 3.5 / 2) + char * 4, int(MATRIX_H / 2) - 3)
                place_3x5_num(top_left_pos, str(score)[char], wipe, [0, 0, 0])
            for rows in range(j, MATRIX_H - 1):
                for i in range(1, MATRIX_W - 1):
                    matrix[rows][i] = wipe
            showPixels()
            wait_for_delay(80)

        wait_for_delay(2000)
        tetris_loop()

    def draw_borders():
        # Draw all of the borders
        for j in range(MATRIX_H):
            for i in range(MATRIX_W):
                if (i, j) in borders:
                    matrix[j][i] = [150, 150, 150]
                else:
                    matrix[j][i] = [0, 0, 0]

    def draw_blocks():
        draw_borders()

        # Draw all of the blocks in the still_positions list
        for pos in still_positions:
            for j in range(MATRIX_H):
                for i in range(MATRIX_W):
                    if i == pos[0] and j == pos[1]:
                        matrix[j][i] = pos[2]

        for j in range(MATRIX_H):
            for i in range(MATRIX_W):
                for k in range(4):
                    if i == blocks[-1][1] + block_shapes[blocks[-1][0]][blocks[-1][3]][k][0] \
                            and j == blocks[-1][2] + block_shapes[blocks[-1][0]][blocks[-1][3]][k][1]:
                        matrix[j][i] = block_colours[blocks[-1][0]]

        matrix[0][MATRIX_W - 1] = block_colours[next_block]
        showPixels()

    def blow_row(rows_to_blow, old_still_pos):
        old_rows = [[t[0], t[1]] for t in old_still_pos if t[1] in rows_to_blow]
        old_rows_col = {(t[0], t[1]): t[2] for t in old_still_pos if t[1] in rows_to_blow}

        for rep in range(8):
            for j in range(MATRIX_H):
                for i in range(MATRIX_W):
                    if [i, j] in old_rows:
                        matrix[j][i] = [255, 255, 255] if rep % 2 == 0 else old_rows_col[(i, j)]
            showPixels()
            wait_for_delay(150)

        temp = [each for each in old_still_pos if each[1] not in rows_to_blow]
        new_still_pos = [[row[0], row[1] + len([x for x in rows_to_blow if x > row[1]]), row[2]] for row in temp]

        return new_still_pos

    def direct_fall():
        # To run when space is pressed
        while check_sides("translate", "down"):
            blocks[-1][2] += 1

    new_block(random.randint(1, 7))
    next_block = random.randint(1, 7)
    score = 0
    last_time = datetime.now()
    pause = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and check_sides("rotate", "left"):
                    blocks[-1][3] = 0 if blocks[-1][3] == 3 else blocks[-1][3] + 1
                elif event.key == pygame.K_x and check_sides("rotate", "right"):
                    blocks[-1][3] = 3 if blocks[-1][3] == 0 else blocks[-1][3] - 1
                elif event.key == pygame.K_UP and check_sides("rotate", "left"):
                    blocks[-1][3] = 0 if blocks[-1][3] == 3 else blocks[-1][3] + 1
                elif event.key == pygame.K_SPACE:
                    direct_fall()
                elif event.key == pygame.K_ESCAPE:
                    close()
                elif event.key == pygame.K_p:
                    pause = False if pause else True
            check_buttons()

        if pause:
            continue

        double_stop = False
        key_states = pygame.key.get_pressed()
        if key_states[pygame.K_LEFT] and not key_states[pygame.K_RIGHT] and check_sides("translate", "left"):
            blocks[-1][1] -= 1
        elif key_states[pygame.K_RIGHT] and not key_states[pygame.K_LEFT] and check_sides("translate", "right"):
            blocks[-1][1] += 1
        if key_states[pygame.K_DOWN] and check_sides("translate", "down"):
            blocks[-1][2] += 1
            double_stop = True

        if datetime.now() > last_time + timedelta(milliseconds=400):
            if not check_sides("translate", "down"):
                for r in range(4):
                    still_positions.append([blocks[-1][1] + block_shapes[blocks[-1][0]][blocks[-1][3]][r][0],
                                            blocks[-1][2] + block_shapes[blocks[-1][0]][blocks[-1][3]][r][1],
                                            block_colours[blocks[-1][0]]])
                new_block(next_block)
                next_block = random.randint(1, 7)

                for pos in still_positions:
                    if pos[1] == -1:
                        dead(score)

            if check_sides("translate", "down") and not double_stop:
                blocks[-1][2] += 1

            last_time = datetime.now()

        to_blow = []
        still_positions_raw = [(t[0], t[1]) for t in still_positions]
        for row in range(MATRIX_H - 1):
            col_complete = True  # Start off by assuming the row is full
            for col in range(1, MATRIX_W - 1):
                if (col, row) not in still_positions_raw:
                    col_complete = False
                    break

            if col_complete:
                to_blow.append(row)

        draw_blocks()

        if len(to_blow) > 0:
            score += len(to_blow)

            still_positions = blow_row(to_blow, still_positions)

        time.sleep(0.08)


def spectrum_loop():
    display_header()
    global matrix

    freq = 8

    t = 0

    while True:
        reset_matrix()

        for col in range(MATRIX_W):
            col_colour = hsv[int(col * len(hsv) / MATRIX_W)]

            height = int(pnoise2(col / freq, t / freq, 1) * MATRIX_H / 2 + MATRIX_H / 2)

            for i in range(height):
                matrix[MATRIX_H - 1 - i][col] = col_colour

        showPixels()

        t += 2

        wait_for_delay(80)


def digit_scroll_clock_loop():
    global saved_clock
    reset_matrix(saved_clock[1])

    display_header()

    h1 = ""
    h2 = ""
    m1 = ""
    m2 = ""

    while True:
        check_buttons()
        old_saved = saved_clock
        colour_changed_1 = setColour(0, 100, top - 45, 180, 40, directory=saved_clock)
        colour_changed_2 = setColour(1, 285, top - 45, 180, 40, directory=saved_clock)

        if colour_changed_1 or colour_changed_2:
            reset_matrix(saved_clock[1])
            h1 = ""
            h2 = ""
            m1 = ""
            m2 = ""
            s1 = ""
            s2 = ""

        now = datetime.now()

        if h1 != str(now.hour).zfill(2)[0]:
            h1 = str(now.hour).zfill(2)[0]
            place_3x5_num((0, 2), h1, saved_clock[0], saved_clock[1])
        if h2 != str(now.hour).zfill(2)[1]:
            h2 = str(now.hour).zfill(2)[1]
            place_3x5_num((4, 2), h2, saved_clock[0], saved_clock[1])
        if m1 != str(now.minute).zfill(2)[0]:
            m1 = str(now.minute).zfill(2)[0]
            place_3x5_num((10, 2), m1, saved_clock[0], saved_clock[1])
        if m2 != str(now.minute).zfill(2)[1]:
            m2 = str(now.minute).zfill(2)[1]
            place_3x5_num((14, 2), m2, saved_clock[0], saved_clock[1])

        matrix[3][8] = saved_clock[0]
        matrix[5][8] = saved_clock[0]

        showPixels()


def vu_meter_loop():
    display_header()
    global matrix

    t = 0
    falling = False

    frequencies = [[index, 0, 0, 0] for index in range(0, MATRIX_W, 2)]

    colour_spectrum = blend([0, 255, 0], [0, 255, 0], [255, 160, 0], [255, 0, 0], length=MATRIX_H + 1)

    while True:
        reset_matrix()

        for column in frequencies:
            raw_vol = math.sin(t + column[0] * (3.14 / 13)) + 2 * math.cos(t / 3)
            vol = 0 # int(translate(raw_vol, -2.8, 2.8, 0, MATRIX_H - 1))

            active = [v for v in range(vol + 1)]

            if falling:
                if vol > column[1]:
                    column[1] = vol
                    column[2] = 0
                    column[3] = datetime.now()

                active.append(int(column[1]))

                if column[1] > 0 and datetime.now() > column[3] + timedelta(milliseconds=300):
                    column[1] -= column[2]
                    column[2] += 0.1

            for i in active:
                matrix[MATRIX_H - 1 - i][column[0]] = colour_spectrum[i]

        showPixels()

        t += 0.2

        wait_for_delay(40)


loops = {1: ["Draw", draw_loop],
         2: ["Clock", clock_loop],
         3: ["Squiggle", squiggle_loop],
         4: ["F Pixels", fading_pixels_loop],
         5: ["Scroll", colour_scroll_loop],
         6: ["Line Fill", line_fill_loop],
         7: ["Spiral", spiral_loop],
         8: ["Rain", pixel_rain_loop],
         9: ["Meta", metaballs_loop],
         10: ["Ants", ants_loop],
         11: ["Time", time_scroll_loop],
         12: ["Blobs", blobs_loop],
         13: ["Snake", snake_loop],
         14: ["Pong", pong_loop],
         15: ["Image", image_viewer_loop],
         16: ["Rotate", rotate_loop],
         17: ["Temp", temp_loop],
         18: ["Walk", random_walk_loop],
         19: ["Bounce", bounce_loop],
         20: ["Seek", seek_loop],
         21: ["G of L", game_of_life_loop],
         22: ["Text", custom_text_loop],
         23: ["Flappy Bird", flappy_bird_loop],
         24: ["First Light", first_light_loop],
         25: ["Random", random_loop],
         26: ["Squares", squares_loop],
         27: ["Fire", fire_loop],
         28: ["Tetris", tetris_loop],
         29: ["Spectrum", spectrum_loop],
         30: ["Clock Animated", digit_scroll_clock_loop],
         31: ["VU Meter", vu_meter_loop],
         32: ["Quit", close]
         }


def settings():
    display_header(False)
    largeText = pygame.font.Font('freesansbold.ttf', 40)
    TextSurf, TextRect = text_objects("Settings", largeText, (255, 255, 255))
    TextRect.center = (90, 65)
    screen.blit(TextSurf, TextRect)

    pygame.draw.rect(screen, (50, 50, 50), (0, 90, display_width, 10))

    medText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects("Change mode", medText, (255, 255, 255))
    TextRect.center = (display_width / 2, 120)
    screen.blit(TextSurf, TextRect)

    cols = 4
    bb = 10 # button border
    bw = (display_width - (cols + 1) * bb) / cols  # button width
    bh = 40 # button height
    num_keys = len(loops.keys())

    while True:

        for num in loops.keys():
            xp = bb + (((num - 1) % cols) * (bw + bb))
            yp = 150 + (math.floor((num - 1) / cols) * (bb + bh))
            button(loops[num][0], xp, yp, bw, bh, (50, 50, 50), (50, 50, 50), action=loops[num][1])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                close()


settings()
print("Loop escaped error")
close()
