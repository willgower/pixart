# Pixart Image Maker

import pygame
import time
import pyautogui as pag
from datetime import datetime
from datetime import timedelta
import math
import random

pygame.init()

disp_width = 642
disp_height = 742
border = 4
pixel_s = (disp_width - (border * 17)) / 16
top = disp_height - (border * 16) - (pixel_s * 16)

screen = pygame.display.set_mode((disp_width, disp_height))
pygame.display.set_caption('Pixart Image Maker')

# Define some basic colours
black = [0, 0, 0]
grey = (100, 100, 100)
white = (255, 255, 255)
red = [200, 0, 0]
green = (0, 200, 0)
blue = (0, 0, 200)

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
        ":": [False, False, False, False, True, False, False, False, False, False, True, False, False, False, False]}

char_array = {"A" : [False, False, True, False, False, False, True, False, True, False, True, False, False, False, True, True, False, False, False, True, True, True, True, True, True, True, False, False, False, True, True, False, False, False, True],
"B" : [True, True, True, True, False, False, True, False, False, True, False, True, False, False, True, False, True, True, True, False, False, True, False, False, True, False, True, False, False, True, True, True, True, True, False],
"C" : [False, True, True, True, False, True, False, False, False, True, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, True, False, True, True, True, False],
"D" : [True, True, True, True, False, False, True, False, False, True, False, True, False, False, True, False, True, False, False, True, False, True, False, False, True, False, True, False, False, True, True, True, True, True, False],
"E" : [True, True, True, True, True, True, False, False, False, False, True, False, False, False, False, True, True, True, True, False, True, False, False, False, False, True, False, False, False, False, True, True, True, True, True],
"F" : [True, True, True, True, True, True, False, False, False, False, True, False, False, False, False, True, True, True, True, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False],
"G" : [False, True, True, True, False, True, False, False, False, True, True, False, False, False, False, True, False, False, True, True, True, False, False, False, True, True, False, False, False, True, False, True, True, True, True],
"H" : [True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, True, True, True, True, True, True, False, False, False, True, True, False, False, False, True, True, False, False, False, True],
"I" : [False, True, True, True, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, True, True, True, False],
"J" : [False, False, True, True, True, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, True, False, False, True, False, False, True, True, False, False],
"K" : [True, False, False, False, True, True, False, False, True, False, True, False, True, False, False, True, True, False, False, False, True, False, True, False, False, True, False, False, True, False, True, False, False, False, True],
"L" : [True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, True, True, True, True],
"M" : [True, False, False, False, True, True, True, False, True, True, True, False, True, False, True, True, False, True, False, True, True, False, False, False, True, True, False, False, False, True, True, False, False, False, True],
"N" : [True, False, False, False, True, True, False, False, False, True, True, True, False, False, True, True, False, True, False, True, True, False, False, True, True, True, False, False, False, True, True, False, False, False, True],
"O" : [False, True, True, True, False, True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, False, True, True, True, False],
"P" : [True, True, True, True, False, True, False, False, False, True, True, False, False, False, True, True, True, True, True, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False],
"Q" : [False, True, True, True, False, True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, True, False, True, False, True, True, False, False, True, False, False, True, True, False, True],
"R" : [True, True, True, True, False, True, False, False, False, True, True, False, False, False, True, True, True, True, True, False, True, False, True, False, False, True, False, False, True, False, True, False, False, False, True],
"S" : [False, True, True, True, False, True, False, False, False, True, True, False, False, False, False, False, True, True, True, False, False, False, False, False, True, True, False, False, False, True, False, True, True, True, False],
"T" : [True, True, True, True, True, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False],
"U" : [True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, False, True, True, True, False],
"V" : [True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, False, True, False, True, False, False, False, True, False, False],
"W" : [True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, True, False, True, False, True, True, False, True, False, True, True, False, True, False, True, False, True, False, True, False],
"X" : [True, False, False, False, True, True, False, False, False, True, False, True, False, True, False, False, False, True, False, False, False, True, False, True, False, True, False, False, False, True, True, False, False, False, True],
"Y" : [True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, False, True, False, True, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False],
"Z" : [True, True, True, True, True, False, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, False, True, True, True, True, True],
"a" : [False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, True, False, True, True, True, True, True, False, False, False, True, False, True, True, True, True],
"b" : [True, False, False, False, False, True, False, False, False, False, True, False, True, True, False, True, True, False, False, True, True, False, False, False, True, True, False, False, False, True, True, True, True, True, False],
"c" : [False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, True, False, True, True, True, False],
"d" : [False, False, False, False, True, False, False, False, False, True, False, True, True, False, True, True, False, False, True, True, True, False, False, False, True, True, False, False, False, True, False, True, True, True, True],
"e" : [False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, True, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, False],
"f" : [False, False, True, True, False, False, True, False, False, True, False, True, False, False, False, True, True, True, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False],
"g" : [False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, True, False, True, True, True, True, False, False, False, False, True, False, True, True, True, False],
"h" : [True, False, False, False, False, True, False, False, False, False, True, False, True, True, False, True, True, False, False, True, True, False, False, False, True, True, False, False, False, True, True, False, False, False, True],
"i" : [False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, True, True, False, False, False, False, True, False, False, False, False, True, False, False, False, True, True, True, False],
"j" : [False, False, False, True, False, False, False, False, False, False, False, False, True, True, False, False, False, False, True, False, False, False, False, True, False, True, False, False, True, False, False, True, True, False, False],
"k" : [True, False, False, False, False, True, False, False, False, False, True, False, False, True, False, True, False, True, False, False, True, True, False, False, False, True, False, True, False, False, True, False, False, True, False],
"l" : [False, True, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, True, True, True, False],
"m" : [False, False, False, False, False, False, False, False, False, False, True, True, False, True, False, True, False, True, False, True, True, False, True, False, True, True, False, True, False, True, True, False, True, False, True],
"n" : [False, False, False, False, False, False, False, False, False, False, True, False, True, True, False, True, True, False, False, True, True, False, False, False, True, True, False, False, False, True, True, False, False, False, True],
"o" : [False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, False, True, True, True, False],
"p" : [False, False, False, False, False, False, False, False, False, False, True, True, True, True, False, True, False, False, False, True, True, True, True, True, False, True, False, False, False, False, True, False, False, False, False],
"q" : [False, False, False, False, False, False, False, False, False, False, False, True, True, False, True, True, False, False, True, True, False, True, True, True, True, False, False, False, False, True, False, False, False, False, True],
"r" : [False, False, False, False, False, False, False, False, False, False, True, False, True, True, False, True, True, False, False, True, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False],
"s" : [False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, True, False, False, False, False, False, True, True, True, False, False, False, False, False, True, True, True, True, True, False],
"t" : [False, True, False, False, False, False, True, False, False, False, True, True, True, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, True, False, False, True, True, False],
"u" : [False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, True, False, False, True, True, False, True, True, False, True],
"v" : [False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, True, False, False, False, True, True, False, False, False, True, False, True, False, True, False, False, False, True, False, False],
"w" : [False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, True, False, False, False, True, True, False, True, False, True, True, False, True, False, True, False, True, False, True, False],
"x" : [False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, False, False, True, False, True, False, True, False, False, False, True],
"y" : [False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, True, False, False, False, True, False, True, True, True, True, False, False, False, False, True, False, True, True, True, False],
"z" : [False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True, True, True, True, True],
"0" : [False, True, True, True, False, True, False, False, False, True, True, False, False, True, True, True, False, True, False, True, True, True, False, False, True, True, False, False, False, True, False, True, True, True, False],
"1" : [False, False, True, False, False, False, True, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, True, True, True, False],
"2" : [False, True, True, True, False, True, False, False, False, True, False, False, False, False, True, False, False, True, True, False, False, True, False, False, False, True, False, False, False, False, True, True, True, True, True],
"3" : [False, True, True, True, False, True, False, False, False, True, False, False, False, False, True, False, False, True, True, False, False, False, False, False, True, True, False, False, False, True, False, True, True, True, False],
"4" : [False, False, False, True, False, False, False, True, True, False, False, True, False, True, False, True, False, False, True, False, True, True, True, True, True, False, False, False, True, False, False, False, False, True, False],
"5" : [True, True, True, True, True, True, False, False, False, False, True, True, True, True, False, False, False, False, False, True, False, False, False, False, True, True, False, False, False, True, False, True, True, True, False],
"6" : [False, False, True, True, False, False, True, False, False, False, True, False, False, False, False, True, True, True, True, False, True, False, False, False, True, True, False, False, False, True, False, True, True, True, False],
"7" : [True, True, True, True, True, False, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False],
"8" : [False, True, True, True, False, True, False, False, False, True, True, False, False, False, True, False, True, True, True, False, True, False, False, False, True, True, False, False, False, True, False, True, True, True, False],
"9" : [False, True, True, True, False, True, False, False, False, True, True, False, False, False, True, False, True, True, True, True, False, False, False, False, True, False, False, False, True, False, False, True, True, False, False],
"." : [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, True, True, False, False],
"," : [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, True, False, False, False, True, False, False, False],
"?" : [False, True, True, True, False, True, False, False, False, True, False, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False],
"!" : [False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False],
"@" : [False, True, True, True, False, True, False, False, False, True, False, False, False, False, True, False, True, True, False, True, True, False, True, False, True, True, False, True, False, True, False, True, True, True, False],
"_" : [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True],
"*" : [False, False, False, False, False, False, False, True, False, False, True, False, True, False, True, False, True, True, True, False, True, False, True, False, True, False, False, True, False, False, False, False, False, False, False],
"#" : [False, True, False, True, False, False, True, False, True, False, True, True, True, True, True, False, True, False, True, False, True, True, True, True, True, False, True, False, True, False, False, True, False, True, False],
"$" : [False, False, True, False, False, False, True, True, True, True, True, False, True, False, False, False, True, True, True, False, False, False, True, False, True, True, True, True, True, False, False, False, True, False, False],
"%" : [True, True, False, False, False, True, True, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False, True, True, False, False, False, True, True],
"&" : [False, True, True, False, False, True, False, False, True, False, True, False, True, False, False, False, True, False, False, False, True, False, True, False, True, True, False, False, True, False, False, True, True, False, True],
"(" : [False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False],
")" : [False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False],
"+" : [False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, True, True, True, True, True, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False],
"-" : [False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
":" : [False, False, False, False, False, False, True, True, False, False, False, True, True, False, False, False, False, False, False, False, False, True, True, False, False, False, True, True, False, False, False, False, False, False, False],
";" : [False, False, False, False, False, False, True, True, False, False, False, True, True, False, False, False, False, False, False, False, False, True, True, False, False, False, False, True, False, False, False, True, False, False, False],
"<" : [False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False],
"=" : [False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False],
">" : [False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False],
"[" : [False, True, True, True, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, True, True, False],
"]" : [False, True, True, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, True, True, True, False],
"^" : [False, False, True, False, False, False, True, False, True, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
"£" : [False, False, True, True, False, False, True, False, False, False, False, True, False, False, False, True, True, True, True, False, False, True, False, False, False, False, True, False, False, True, True, False, True, True, False],
" " : [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
"/" : [False, False, False, False, True, False, False, False, True, False, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, False, True, False, False, False, True, False, False, False, False],
"°" : [False, True, True, True, False, False, True, False, True, False, False, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
}

matrix = []
for i in range(16):
    matrix.append([])
for j in range(16):
    for rep in range(16):
        matrix[j].append(black)

new_matrix = matrix


def close():
    pygame.quit()
    quit()


def check_buttons():
    button("", disp_width - 40, 8, 32, 32, action=settings)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close()


def advance_rainbow(skip=1):
    global hsv_i
    if hsv_i + skip + 1 > len(hsv):
        hsv_i = hsv_i + skip - len(hsv)
    else:
        hsv_i += skip

    return hsv[hsv_i]


def resetMatrix(colour=black, confirm=True):
    # define the blank 16x16 matrix
    global matrix
    if confirm:
        verify = pag.confirm(text='Are you sure you want to reset the matrix to black', title='Confirm Reset')
    else:
        verify = "OK"

    if verify == "OK":
        for i in range(16):
            for j in range(16):
                matrix[i][j] = colour


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def setColour(savedIndex, x, y, w, h, directory=saved):
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


def drawCircle(pos):
    global matrix

    x = pos[0]
    y = pos[1]

    circle_positions = [(0, 0), (-2, -1), (-1, -1), (-1, -2), (1, -2), (1, -1), (2, -1), (1, 1), (2, 1), (1, 2),
                        (-2, 1), (-1, 1), (-1, 2), (0, -2), (0, -1), (1, 0), (2, 0), (0, 1), (0, 2), (-2, 0), (-1, 0)]

    col = advance_rainbow(4)

    for each in circle_positions:
        if 0 <= x + each[0] < 16 and 0 <= y + each[1] < 16:
            matrix[x + each[0]][y + each[1]] = col


def dim_matrix(severity=1, any_matrix=""):
    global matrix
    if any_matrix == "":
        for i in range(16):
            for j in range(16):
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
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            x = border + j * (pixel_s + border)
            y = disp_height - (16 * pixel_s) - (16 * border) + i * (pixel_s + border)
            pygame.draw.rect(screen, matrix[i][j], (x, y, pixel_s, pixel_s))

    pygame.display.update()


def get_clicked_pixel(pos):
    x_valid = False
    y_valid = False

    for p in range(16):
        if border * (p + 1) + pixel_s * p < pos[0] < border * (p + 1) + pixel_s * (p + 1):
            x_pixel = p
            x_valid = True
            break

    for p in range(16):
        if top + border * p + pixel_s * p < pos[1] < top + border * p + pixel_s * (p + 1):
            y_pixel = p
            y_valid = True
            break

    if x_valid and y_valid:
        return (x_pixel, y_pixel)
    else:
        return ()


def hex2rgb(hex_string):
    rgb_tuple = tuple(int(hex_string[i:i + 2], 16) for i in (0, 2, 4))
    return rgb_tuple


def show_time(pos, number):
    for p in range(5):
        for q in range(3):
            matrix[pos[1] + p][pos[0] + q] = saved_clock[0] if number_array[number][p*3+q] else saved_clock[1]


def get_magnitude(vector):
    return (vector[0] ** 2 + vector[1] ** 2) ** 0.5


def outputCode():
    verify = pag.prompt(text="Create a name and press enter to save the matrix to the file 'pixart_code.txt'.",
                        title='Save Matrix', )
    if verify != None:
        outputTxt = open("pixart_code.txt", "a")
        current_time = datetime.now()
        formatted = "Matrix saved at " + str(current_time.hour) + ":" + str(current_time.minute) \
                    + " on the date " + str(current_time.day) + "/" + str(current_time.month) \
                    + "/" + str(current_time.year) + "\n\n" + verify + "[] = " + "{"
        for row in range(16):
            if row % 2 == 0:
                for col in range(16):
                    for rgb in range(3):
                        formatted += str(matrix[row][col][rgb])
                        formatted += ","
            else:
                for col in range(16):
                    for rgb in range(3):
                        formatted += str(matrix[row][15 - col][rgb])
                        formatted += ","

        formatted = formatted[:-2] + "};\n\n"
        outputTxt.write(formatted)
        outputTxt.close()
        time.sleep(1)


def display_header(not_settings = True):
    screen.fill(grey)
    largeText = pygame.font.Font('freesansbold.ttf', 40)
    TextSurf, TextRect = text_objects("Pixart Image Maker", largeText, (255, 255, 255))
    TextRect.center = (200, 25)
    screen.blit(TextSurf, TextRect)

    if not_settings:
        settings_icon = pygame.image.load('settings_icon.png')
        screen.blit(settings_icon, (disp_width - 40, 8))

    pygame.display.update()


def draw_loop():
    display_header()

    showPixels()

    click_released = False
    while not click_released:
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONUP:
            click_released = True

    while True:
        button("reset", 5, top - 45, 108, 40, (50, 50, 50), action=resetMatrix)
        button("1", 118, top - 45, 40, 40, saved[0])
        button("2", 163, top - 45, 40, 40, saved[1])
        button("3", 208, top - 45, 40, 40, saved[2])
        button("4", 253, top - 45, 40, 40, saved[3])
        button("5", 298, top - 45, 40, 40, saved[4])
        button("6", 343, top - 45, 40, 40, saved[5])
        button("save", 388, top - 45, 108, 40, (50, 50, 50), action=outputCode)

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
    global primaryColour
    global secondaryColour

    resetMatrix(secondaryColour, confirm=False)

    display_header()

    h1 = ""
    h2 = ""
    m1 = ""
    m2 = ""
    s1 = ""
    s2 = ""

    while True:
        check_buttons()

        setColour(0, 100, top - 45, 180, 40, directory=saved_clock)
        setColour(1, 285, top - 45, 180, 40, directory=saved_clock)

        if primaryColour != saved_clock[0] or secondaryColour != saved_clock[1]:
            h1 = ""
            h2 = ""
            m1 = ""
            m2 = ""
            s1 = ""
            s2 = ""
            setColour(0, 100, top - 45, 180, 40, directory=saved_clock)
            setColour(1, 285, top - 45, 180, 40, directory=saved_clock)
            primaryColour = saved_clock[0]
            secondaryColour = saved_clock[1]
            resetMatrix(secondaryColour, False)

        now = datetime.now()

        if h1 != str(now.hour).zfill(2)[0]:
            h1 = str(now.hour).zfill(2)[0]
            show_time((0, 2), h1)
        if h2 != str(now.hour).zfill(2)[1]:
            h2 = str(now.hour).zfill(2)[1]
            show_time((4, 2), h2)
        if m1 != str(now.minute).zfill(2)[0]:
            m1 = str(now.minute).zfill(2)[0]
            show_time((9, 2), m1)
        if m2 != str(now.minute).zfill(2)[1]:
            m2 = str(now.minute).zfill(2)[1]
            show_time((13, 2), m2)
        if s1 != str(now.second).zfill(2)[0]:
            s1 = str(now.second).zfill(2)[0]
            show_time((4, 9), s1)
        if s2 != str(now.second).zfill(2)[1]:
            s2 = str(now.second).zfill(2)[1]
            show_time((9, 9), s2)

        showPixels()


def rainbow_squiggle_loop():
    display_header()
    resetMatrix(confirm=False)
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

        mx = (math.cos(dx / 243) + math.cos(dy / 253)) * 4
        my = (math.sin(dx / 347) + math.cos(dy / 363)) * 4

        cent = (int(8 + mx), int(8 + my))

        if cent != prev:
            dim_matrix(0.95)
            drawCircle(cent)

        prev = cent

        showPixels()

        time.sleep(0.003)


def fading_pixels_loop():
    display_header()
    global matrix
    global primaryColour
    resetMatrix(black, False)

    while True:
        check_buttons()

        col = advance_rainbow(3)

        for p in range(8):
            x = random.randint(0, 15)
            y = random.randint(0, 15)

            matrix[y][x] = col

        showPixels()
        time.sleep(0.05)

        dim_matrix()


def colour_scroll_loop():
    display_header()
    global matrix
    global hsv_i
    global primaryColour

    for x in range(16):
        col = advance_rainbow(4)
        for y in range(16):
            matrix[y].pop(0)
            matrix[y].append(col)

    showPixels()

    while True:
        check_buttons()

        col = hsv[hsv_i]

        for x in range(16):
            matrix[x].pop(0)
            matrix[x].append(col)

        primaryColour = advance_rainbow(30)

        showPixels()

        time.sleep(0.25)


def line_fill_loop():
    display_header()
    global matrix
    resetMatrix(black, False)

    while True:
        for y in range(16):
            for x in range(16):
                check_buttons()

                if y % 2 == 0:
                    matrix[y][x] = advance_rainbow(6)
                else:
                    matrix[y][15 - x] = advance_rainbow(6)

                showPixels()
                time.sleep(0.01)


def spiral_loop():
    display_header()
    global matrix
    resetMatrix(black, False)
    movements = {"right": [1, 0, 1],
                 "down": [0, 1, 0],
                 "left": [-1, 0, 0],
                 "up": [0, -1, -1]}
    while True:
        start = [0, 0]
        matrix[0][0] = advance_rainbow()
        showPixels()

        for rotation in range(8):
            rotation = 15 - rotation * 2
            for direction in ["right", "down", "left", "up"]:
                for i in range(rotation + movements[direction][2]):
                    if rotation == 15 and i == 15:
                        break
                    matrix[start[1] + movements[direction][1]][start[0] + movements[direction][0]] = advance_rainbow()
                    start = [start[0] + movements[direction][0], start[1] + movements[direction][1]]
                    time.sleep(0.01)
                    showPixels()

                    check_buttons()


def pixel_rain_loop():
    display_header()
    global matrix
    resetMatrix(black, False)

    while True:
        check_buttons()

        top_row = dim_matrix(0.9, [element for element in matrix[0]])

        matrix.pop()
        matrix.insert(0, top_row)

        if random.random() > 0.4:
            x = random.randint(0, 15)
            matrix[0][x] = advance_rainbow(10)

        showPixels()
        time.sleep(0.05)


def draw_metaballs(balls):
    global matrix

    circle_positions = [(-3, -3), (-3, -2), (-3, -1), (-3, 0), (-3, 1), (-3, 2), (-3, 3), (-2, -3), (-2, -2), (-2, -1),
                        (-2, 0), (-2, 1), (-2, 2), (-2, 3), (-1, -3), (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2),
                        (-1, 3), (0, -3), (0, -2), (0, -1), (0, 0), (0, 1), (0, 2), (0, 3), (1, -3), (1, -2), (1, -1),
                        (1, 0), (1, 1), (1, 2), (1, 3), (2, -3), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2), (2, 3),
                        (3, -3), (3, -2), (3, -1), (3, 0), (3, 1), (3, 2), (3, 3)]

    col = advance_rainbow(1)

    for ball in balls:
        x = int(ball[0])
        y = int(ball[1])
        for each in circle_positions:
            if 0 <= x + each[0] < 16 and 0 <= y + each[1] < 16:
                dist = get_magnitude(each)
                dimmed_col = []

                for c in col:
                    # dim = int(((13 * dist ** 2 - 116 * dist + 249) / 249) * c)
                    dim = c / (1 + (dist) ** 2)
                    dimmed_col.append(dim)

                current_matrix = matrix[x + each[0]][y + each[1]]
                added_matrix = [a + b if a + b <= 255 else 255 for a, b in zip(current_matrix, dimmed_col)]
                matrix[x + each[0]][y + each[1]] = added_matrix


def metaballs_loop():
    display_header()
    global matrix
    resetMatrix(black, False)

    num_balls = 3
    b_pos = []
    b_vel = []

    speed = 1  # pixels/frame

    for n in range(num_balls):
        b_pos.append([random.randint(0, 15), random.randint(0, 15)])
        b_vel.append([random.random(), random.random()])

    for vel in b_vel:
        mag = get_magnitude(vel)
        vel[0] *= speed / mag
        vel[1] *= speed / mag

    while True:
        for ball in range(num_balls):
            b_pos[ball][0] = b_pos[ball][0] + b_vel[ball][0]
            b_pos[ball][1] = b_pos[ball][1] + b_vel[ball][1]

            if 0 >= b_pos[ball][0] or b_pos[ball][0] > 16:
                b_vel[ball][0] *= -1

                mag = get_magnitude(b_vel[ball])
                b_vel[ball][0] *= speed / mag
                b_vel[ball][1] *= speed / mag

                b_pos[ball][0] = b_pos[ball][0] + b_vel[ball][0]

            if 0 >= b_pos[ball][1] or b_pos[ball][1] > 16:
                b_vel[ball][1] *= -1

                mag = get_magnitude(b_vel[ball])
                b_vel[ball][0] *= speed / mag
                b_vel[ball][1] *= speed / mag

                b_pos[ball][1] = b_pos[ball][1] + b_vel[ball][1]

        if 0 <= b_pos[ball][0] <= 16 and 0 <= b_pos[ball][1] <= 16:
            resetMatrix(black, False)
            draw_metaballs(b_pos)

        time.sleep(0.028)

        showPixels()

        check_buttons()


def ants_loop():
    display_header()
    global matrix
    resetMatrix(black, False)

    num_ants = 10
    ants = []
    for n in range(num_ants):
        ants.append([random.randint(0,15), random.randint(0,15)])

    while True:
        for ant in ants:
            if random.random() > 0.5:
                if random.random() > 0.5:
                    if ant[0] == 15:
                        ant[0] -= 1
                    else:
                        ant[0] += 1
                else:
                    if ant[0] == 0:
                        ant[0] += 1
                    else:
                        ant[0] -= 1
            else:
                if random.random() > 0.5:
                    if ant[1] == 15:
                        ant[1] -= 1
                    else:
                        ant[1] += 1
                else:
                    if ant[1] == 0:
                        ant[1] += 1
                    else:
                        ant[1] -= 1

            matrix[ant[0]][ant[1]] = [255,255,255]

        showPixels()
        dim_matrix(0.8)
        time.sleep(0.1)

        check_buttons()


def wait_for_delay(delay, scroll_speed):
    while datetime.now() < delay + timedelta(milliseconds=scroll_speed):
        time.sleep(0.000001)

    return datetime.now()


def time_scroll_loop():
    display_header()
    global matrix
    resetMatrix(black, False)
    height = 4
    scroll_speed = 100

    while True:
        now = datetime.now()
        delay = datetime.now()
        time_text = now.strftime("%A ") + str(now.day) + ("th" if 4 <= now.day <= 20 or 24 <= now.day <= 30 else ["st","nd","rd"][now.day % 10 -1]) + now.strftime(" %B %Y * %H:%M:%S * ")
        for char in time_text:
            for i in range(16):
                #create a single gap between each character
                matrix[i].pop(0)
                matrix[i].append([0, 0, 0])

            for edge in range(5):
                col = [255, 255, 255]
                for t in range(7):
                    matrix[height + t].append(col if char_array[char][t*5 + edge] else [0, 0, 0])

                for i in range(16):
                    if len(matrix[i]) == 17:
                        matrix[i].pop(0)

                delay = wait_for_delay(delay, scroll_speed)
                showPixels()
                check_buttons()


def settings():
    display_header(False)
    button_border = 20
    button_width = (disp_width - 5 * button_border) / 4

    while True:
        largeText = pygame.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = text_objects("Settings", largeText, (255, 255, 255))
        TextRect.center = (90, 65)
        screen.blit(TextSurf, TextRect)

        pygame.draw.rect(screen, (50, 50, 50), (0, 90, disp_width, 10))

        medText = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects("Change mode", medText, (255, 255, 255))
        TextRect.center = (disp_width / 2, 120)
        screen.blit(TextSurf, TextRect)

        button("Draw", button_border * 1 + button_width * 0, 150, button_width, 40, (50, 50, 50), (50, 50, 50), action=draw_loop)
        button("Clock", button_border * 2 + button_width * 1, 150, button_width, 40, (50, 50, 50), (50, 50, 50), action=clock_loop)
        button("Squiggle", button_border * 3 + button_width * 2, 150, button_width, 40, (50, 50, 50), (50, 50, 50), action=rainbow_squiggle_loop)
        button("F Pixels", button_border * 4 + button_width * 3, 150, button_width, 40, (50, 50, 50), (50, 50, 50), action=fading_pixels_loop)
        button("Scroll", button_border * 1 + button_width * 0, 200, button_width, 40, (50, 50, 50), (50, 50, 50), action=colour_scroll_loop)
        button("Line Fill", button_border * 2 + button_width * 1, 200, button_width, 40, (50, 50, 50), (50, 50, 50), action=line_fill_loop)
        button("Spiral", button_border * 3 + button_width * 2, 200, button_width, 40, (50, 50, 50), (50, 50, 50), action=spiral_loop)
        button("Rain", button_border * 4 + button_width * 3, 200, button_width, 40, (50, 50, 50), (50, 50, 50), action=pixel_rain_loop)
        button("Meta", button_border * 1 + button_width * 0, 250, button_width, 40, (50, 50, 50), (50, 50, 50), action=metaballs_loop)
        button("Ants", button_border * 2 + button_width * 1, 250, button_width, 40, (50, 50, 50), (50, 50, 50), action=ants_loop)
        button("Time", button_border * 3 + button_width * 2, 250, button_width, 40, (50, 50, 50), (50, 50, 50), action=time_scroll_loop)

        pygame.draw.rect(screen, (50, 50, 50), (0, 300, disp_width, 10))

        medText = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects("Set colour palette", medText, (255, 255, 255))
        TextRect.center = (disp_width / 2, 330)
        screen.blit(TextSurf, TextRect)

        setColour(0, 20, 360, disp_width - 40, 40)
        setColour(1, 20, 410, disp_width - 40, 40)
        setColour(2, 20, 460, disp_width - 40, 40)
        setColour(3, 20, 510, disp_width - 40, 40)
        setColour(4, 20, 560, disp_width - 40, 40)
        setColour(5, 20, 610, disp_width - 40, 40)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()


settings()
print("Loop escaped error")