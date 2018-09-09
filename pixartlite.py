# Pixart Image Maker

import time
from datetime import datetime
from datetime import timedelta
import math
import random
from neopixel import *

# LED strip configuration:
LED_COUNT      = 256      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

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
"'" : [False, False, True, True, False, False, True, False, False, False, False, True, False, False, False, True, True, True, True, False, False, True, False, False, False, False, True, False, False, True, True, False, True, True, False],
" " : [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
"/" : [False, False, False, False, True, False, False, False, True, False, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, False, True, False, False, False, True, False, False, False, False],
"\"" : [False, True, True, True, False, False, True, False, True, False, False, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
}

matrix = []
for i in range(16):
    matrix.append([])
for j in range(16):
    for rep in range(16):
        matrix[j].append(black)


def check_input():
    #Nothing for now
    return None


def advance_rainbow(skip=1):
    global hsv_i
    if hsv_i + skip + 1 > len(hsv):
        hsv_i = hsv_i + skip - len(hsv)
    else:
        hsv_i += skip

    return hsv[hsv_i]


def reset_matrix(colour=black, confirm=False):
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
            if i % 2 == 1:
                j = 15 - j
            strip.setPixelColor(i * 16 + j, Color(matrix[i][j][0], matrix[i][j][1], matrix[i][j][2]))

    strip.show()


def place_3x5_num(pos, number, p_colour, s_colour):
    for p in range(5):
        for q in range(3):
            matrix[pos[1] + p][pos[0] + q] = p_colour if number_array[number][p*3+q] else s_colour


def get_magnitude(vector):
    return (vector[0] ** 2 + vector[1] ** 2) ** 0.5


def wait_for_delay(delay = 100):
    start = datetime.now()
    while datetime.now() < start + timedelta(milliseconds=delay):
        check_buttons()

    return None


def scroll_text(text, foreground, background, speed, height = 4):
    for char in text:
        for i in range(16):
            # create a single gap between each character
            matrix[i].pop(0)
            matrix[i].append(background)

        for edge in range(5):
            for t in range(7):
                matrix[height + t].append(foreground if char_array[char][t * 5 + edge] else background)

            for i in range(16):
                if len(matrix[i]) == 17:
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
            array_text = line[line.find("=") + 3:-2]

            joined_array = [int(x) for x in array_text.split(',')]

            if len(joined_array) == 16 * 16 * 3:
                for i in range(16):
                    for j in range(16):
                        p = []
                        for c in range(3):
                            p.append(joined_array[i * 16 * 3 + j * 3 + c])
                        matrix[i][j] = p

    image_file.close()


def clock_loop():
    global saved_clock
    reset_matrix(saved_clock[1])


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
            place_3x5_num((9, 2), m1, saved_clock[0], saved_clock[1])
        if m2 != str(now.minute).zfill(2)[1]:
            m2 = str(now.minute).zfill(2)[1]
            place_3x5_num((13, 2), m2, saved_clock[0], saved_clock[1])
        if s1 != str(now.second).zfill(2)[0]:
            s1 = str(now.second).zfill(2)[0]
            place_3x5_num((4, 9), s1, saved_clock[0], saved_clock[1])
        if s2 != str(now.second).zfill(2)[1]:
            s2 = str(now.second).zfill(2)[1]
            place_3x5_num((9, 9), s2, saved_clock[0], saved_clock[1])

        showPixels()


def rainbow_squiggle_loop():
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
            if 0 <= x + each[0] < 16 and 0 <= y + each[1] < 16:
                matrix[x + each[0]][y + each[1]] = col

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
    global matrix
    global primaryColour
    reset_matrix()

    while True:
        check_buttons()

        col = advance_rainbow(3)

        for p in range(8):
            matrix[random.randint(0, 15)][random.randint(0, 15)] = col

        showPixels()
        time.sleep(0.05)

        dim_matrix()


def colour_scroll_loop():
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

        primaryColour = advance_rainbow(2)

        showPixels()

        time.sleep(0.02)


def line_fill_loop():
    global matrix
    reset_matrix()

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
    global matrix
    reset_matrix()
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
    global matrix
    reset_matrix()

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


def metaballs_loop():
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
                            (3, -3), (3, -2), (3, -1), (3, 0), (3, 1), (3, 2), (3, 3)]

        col = advance_rainbow(5)

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
            reset_matrix()
            draw_metaballs(b_pos)

        time.sleep(0.028)

        showPixels()

        check_buttons()


def ants_loop():
    global matrix
    reset_matrix()

    num_ants = 30
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

            matrix[ant[0]][ant[1]] = advance_rainbow(1)

        showPixels()
        dim_matrix(0.8)
        time.sleep(0.1)

        check_buttons()


def time_scroll_loop():
    global matrix
    reset_matrix()
    scroll_speed = 80

    while True:
        now = datetime.now()
        time_text = now.strftime("%A ") + str(now.day) + ("th" if 4 <= now.day <= 20 or 24 <= now.day <= 30 else ["st","nd","rd"][now.day % 10 -1]) + now.strftime(" %B %Y * %H:%M:%S * ")
        scroll_text(time_text, [200,200,200], black, scroll_speed, 8)


def blobs_loop():
    global matrix
    reset_matrix()

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


        for j in range(16):
            for i in range(16):
                min_dist = 16
                for ball in range(num_balls):
                    dist = ((b_pos[ball][0] - i) ** 2 + (b_pos[ball][1] - j) ** 2) ** 0.5
                    if dist < min_dist:
                        min_dist = dist
                col_index = int((min_dist * 400 / 16) + 400)
                matrix[j][i] = hsv[col_index]

        time.sleep(0.1)

        showPixels()

        check_buttons()

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

metaballs_loop()
