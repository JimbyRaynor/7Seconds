import math
import sys
import random
import time
from tkinter import *

sys.path.insert(0, "/home/deck/Documents")
import LEDlib

# TODO
# mapping levels
# animation list
# 2x flags
# 2x+1 flags


# pinball like? bouncers, speed increasers, ?
# moving walls/obsticles? -> moving away from original idea. Not a platformer


charRallyX = [(0,14,"#4C3A23"), (0,15,"#4C3A23"), (0,16,"#4C3A23"), (0,17,"#4C3A23"), (0,18,"#4C3A23"), (0,19,"#4C3A23"), (0,20,"#4C3A23"), (1,13,"#4C3A23"), (1,14,"#4C3A23"), (1,15,"#4C3A23"), (1,16,"#4C3A23"), (1,17,"#4C3A23"), (1,18,"#4C3A23"), (1,19,"#4C3A23"), (1,20,"#4C3A23"), (1,21,"#4C3A23"), (2,2,"#4C3A23"), (2,3,"#4C3A23"), (2,4,"#4C3A23"), (2,5,"#4C3A23"), (2,6,"#4C3A23"), (2,13,"#4C3A23"), (2,14,"#4C3A23"), (2,15,"#4C3A23"), (2,16,"#4C3A23"), (2,17,"#4C3A23"), (2,18,"#4C3A23"), (2,19,"#4C3A23"), (2,20,"#4C3A23"), (2,21,"#4C3A23"), (3,1,"#4C3A23"), (3,2,"#4C3A23"), (3,3,"#4C3A23"), (3,4,"#4C3A23"), (3,5,"#4C3A23"), (3,6,"#4C3A23"), (3,7,"#4C3A23"), (3,13,"#4C3A23"), (3,14,"#4C3A23"), (3,15,"#4C3A23"), (3,16,"#4C3A23"), (3,17,"#4C3A23"), (3,18,"#4C3A23"), (3,19,"#4C3A23"), (3,20,"#4C3A23"), (3,21,"#4C3A23"), (4,1,"#4C3A23"), (4,2,"#4C3A23"), (4,3,"#4C3A23"), (4,4,"#4C3A23"), (4,5,"#4C3A23"), (4,6,"#4C3A23"), (4,7,"#4C3A23"), (4,13,"#4C3A23"), (4,14,"#4C3A23"), (4,15,"#4C3A23"), (4,16,"#4C3A23"), (4,17,"#4C3A23"), (4,18,"#4C3A23"), (4,19,"#4C3A23"), (4,20,"#4C3A23"), (4,21,"#4C3A23"), (5,1,"#4C3A23"), (5,2,"#4C3A23"), (5,3,"#4C3A23"), (5,4,"#4C3A23"), (5,5,"#4C3A23"), (5,6,"#4C3A23"), (5,7,"#4C3A23"), (5,13,"#4C3A23"), (5,14,"#4C3A23"), (5,15,"#4C3A23"), (5,16,"#4C3A23"), (5,17,"#4C3A23"), (5,18,"#4C3A23"), (5,19,"#4C3A23"), (5,20,"#4C3A23"), (5,21,"#4C3A23"), (6,1,"#4C3A23"), (6,2,"#4C3A23"), (6,3,"#4C3A23"), (6,4,"#4C3A23"), (6,5,"#4C3A23"), (6,6,"#4C3A23"), (6,7,"#4C3A23"), (6,14,"#4C3A23"), (6,15,"#4C3A23"), (6,16,"#4C3A23"), (6,17,"#4C3A23"), (6,18,"#4C3A23"), (6,19,"#4C3A23"), (6,20,"#4C3A23"), (7,2,"#4C3A23"), (7,3,"#4C3A23"), (7,4,"#4C3A23"), (7,5,"#4C3A23"), (7,6,"#4C3A23"), (7,17,"#FFA07A"), (8,4,"#FFA07A"), (8,10,"#FFA07A"), (8,11,"#FFA07A"), (8,12,"#FFA07A"), (8,13,"#FFA07A"), (8,14,"#FFA07A"), (8,15,"#FFA07A"), (8,16,"#FFA07A"), (8,17,"#FFA07A"), (8,18,"#FFA07A"), (8,19,"#8B4513"), (8,20,"#8B4513"), (8,21,"#FF0000"), (8,22,"#FFFF00"), (8,23,"#FF0000"), (9,4,"#FFA07A"), (9,8,"#FFA07A"), (9,9,"#FFA07A"), (9,10,"#FFA07A"), (9,11,"#FFA07A"), (9,12,"#FFA07A"), (9,13,"#FFA07A"), (9,14,"#FFA07A"), (9,15,"#FFA07A"), (9,16,"#FFA07A"), (9,17,"#FFA07A"), (9,18,"#FFA07A"), (9,19,"#FFA07A"), (9,20,"#8B4513"), (9,21,"#8B4513"), (9,22,"#FF0000"), (9,23,"#FFFF00"), (10,1,"#FFA07A"), (10,2,"#FFA07A"), (10,3,"#FFA07A"), (10,4,"#FFA07A"), (10,5,"#FFA07A"), (10,6,"#FFA07A"), (10,7,"#FFA07A"), (10,8,"#FFA07A"), (10,9,"#FFA07A"), (10,10,"#FFA07A"), (10,11,"#AAAAAA"), (10,12,"#AAAAAA"), (10,13,"#AAAAAA"), (10,14,"#AAAAAA"), (10,15,"#AAAAAA"), (10,16,"#AAAAAA"), (10,17,"#FFA07A"), (10,18,"#FFA07A"), (10,19,"#FFA07A"), (10,20,"#FFA07A"), (11,0,"#FFA07A"), (11,1,"#FFA07A"), (11,2,"#FFA07A"), (11,3,"#FFA07A"), (11,4,"#FFA07A"), (11,5,"#FFA07A"), (11,6,"#FFA07A"), (11,7,"#FFA07A"), (11,8,"#FFA07A"), (11,9,"#FFA07A"), (11,10,"#AAAAAA"), (11,11,"#B5B3F5"), (11,12,"#FFFFFF"), (11,13,"#FFFFFF"), (11,14,"#FFFFFF"), (11,15,"#FFFFFF"), (11,16,"#B5B3F5"), (11,17,"#AAAAAA"), (11,18,"#FFA07A"), (11,19,"#FFA07A"), (11,20,"#FFA07A"), (12,0,"#FFA07A"), (12,1,"#FFA07A"), (12,2,"#FFA07A"), (12,3,"#FFA07A"), (12,4,"#FFA07A"), (12,5,"#FFA07A"), (12,6,"#FFA07A"), (12,7,"#FFA07A"), (12,8,"#FFA07A"), (12,9,"#FFA07A"), (12,10,"#AAAAAA"), (12,11,"#B5B3F5"), (12,12,"#FFFFFF"), (12,13,"#FFFFFF"), (12,14,"#FFFFFF"), (12,15,"#FFFFFF"), (12,16,"#B5B3F5"), (12,17,"#AAAAAA"), (12,18,"#FFA07A"), (12,19,"#FFA07A"), (12,20,"#FFA07A"), (13,1,"#FFA07A"), (13,2,"#FFA07A"), (13,3,"#FFA07A"), (13,4,"#FFA07A"), (13,5,"#FFA07A"), (13,6,"#FFA07A"), (13,7,"#FFA07A"), (13,8,"#FFA07A"), (13,9,"#FFA07A"), (13,10,"#FFA07A"), (13,11,"#AAAAAA"), (13,12,"#AAAAAA"), (13,13,"#AAAAAA"), (13,14,"#AAAAAA"), (13,15,"#AAAAAA"), (13,16,"#AAAAAA"), (13,17,"#FFA07A"), (13,18,"#FFA07A"), (13,19,"#FFA07A"), (13,20,"#FFA07A"), (14,4,"#FFA07A"), (14,8,"#FFA07A"), (14,9,"#FFA07A"), (14,10,"#FFA07A"), (14,11,"#FFA07A"), (14,12,"#FFA07A"), (14,13,"#FFA07A"), (14,14,"#FFA07A"), (14,15,"#FFA07A"), (14,16,"#FFA07A"), (14,17,"#FFA07A"), (14,18,"#FFA07A"), (14,19,"#FFA07A"), (14,20,"#8B4513"), (14,21,"#8B4513"), (14,22,"#FF0000"), (14,23,"#FFFF00"), (15,4,"#FFA07A"), (15,10,"#FFA07A"), (15,11,"#FFA07A"), (15,12,"#FFA07A"), (15,13,"#FFA07A"), (15,14,"#FFA07A"), (15,15,"#FFA07A"), (15,16,"#FFA07A"), (15,17,"#FFA07A"), (15,18,"#FFA07A"), (15,19,"#8B4513"), (15,20,"#8B4513"), (15,21,"#FF0000"), (15,22,"#FFFF00"), (15,23,"#FF0000"), (16,2,"#4C3A23"), (16,3,"#4C3A23"), (16,4,"#4C3A23"), (16,5,"#4C3A23"), (16,6,"#4C3A23"), (16,17,"#FFA07A"), (17,1,"#4C3A23"), (17,2,"#4C3A23"), (17,3,"#4C3A23"), (17,4,"#4C3A23"), (17,5,"#4C3A23"), (17,6,"#4C3A23"), (17,7,"#4C3A23"), (17,14,"#4C3A23"), (17,15,"#4C3A23"), (17,16,"#4C3A23"), (17,17,"#4C3A23"), (17,18,"#4C3A23"), (17,19,"#4C3A23"), (17,20,"#4C3A23"), (18,1,"#4C3A23"), (18,2,"#4C3A23"), (18,3,"#4C3A23"), (18,4,"#4C3A23"), (18,5,"#4C3A23"), (18,6,"#4C3A23"), (18,7,"#4C3A23"), (18,13,"#4C3A23"), (18,14,"#4C3A23"), (18,15,"#4C3A23"), (18,16,"#4C3A23"), (18,17,"#4C3A23"), (18,18,"#4C3A23"), (18,19,"#4C3A23"), (18,20,"#4C3A23"), (18,21,"#4C3A23"), (19,1,"#4C3A23"), (19,2,"#4C3A23"), (19,3,"#4C3A23"), (19,4,"#4C3A23"), (19,5,"#4C3A23"), (19,6,"#4C3A23"), (19,7,"#4C3A23"), (19,13,"#4C3A23"), (19,14,"#4C3A23"), (19,15,"#4C3A23"), (19,16,"#4C3A23"), (19,17,"#4C3A23"), (19,18,"#4C3A23"), (19,19,"#4C3A23"), (19,20,"#4C3A23"), (19,21,"#4C3A23"), (20,1,"#4C3A23"), (20,2,"#4C3A23"), (20,3,"#4C3A23"), (20,4,"#4C3A23"), (20,5,"#4C3A23"), (20,6,"#4C3A23"), (20,7,"#4C3A23"), (20,13,"#4C3A23"), (20,14,"#4C3A23"), (20,15,"#4C3A23"), (20,16,"#4C3A23"), (20,17,"#4C3A23"), (20,18,"#4C3A23"), (20,19,"#4C3A23"), (20,20,"#4C3A23"), (20,21,"#4C3A23"), (21,2,"#4C3A23"), (21,3,"#4C3A23"), (21,4,"#4C3A23"), (21,5,"#4C3A23"), (21,6,"#4C3A23"), (21,13,"#4C3A23"), (21,14,"#4C3A23"), (21,15,"#4C3A23"), (21,16,"#4C3A23"), (21,17,"#4C3A23"), (21,18,"#4C3A23"), (21,19,"#4C3A23"), (21,20,"#4C3A23"), (21,21,"#4C3A23"), (22,13,"#4C3A23"), (22,14,"#4C3A23"), (22,15,"#4C3A23"), (22,16,"#4C3A23"), (22,17,"#4C3A23"), (22,18,"#4C3A23"), (22,19,"#4C3A23"), (22,20,"#4C3A23"), (22,21,"#4C3A23"), (23,14,"#4C3A23"), (23,15,"#4C3A23"), (23,16,"#4C3A23"), (23,17,"#4C3A23"), (23,18,"#4C3A23"), (23,19,"#4C3A23"), (23,20,"#4C3A23")]
charPopsicle = [(0,1,"#8B4513"), (0,2,"#8B4513"), (0,3,"#8B4513"), (0,4,"#8B4513"), (0,5,"#8B4513"), (0,6,"#8B4513"), (0,7,"#8B4513"), (0,8,"#8B4513"), (0,9,"#8B4513"), (0,10,"#8B4513"), (0,11,"#8B4513"), (1,0,"#8B4513"), (1,1,"#8B4513"), (1,2,"#FFFFFF"), (1,3,"#FFFFFF"), (1,4,"#FFFFFF"), (1,5,"#8B4513"), (1,6,"#8B4513"), (1,7,"#8B4513"), (1,8,"#8B4513"), (1,9,"#8B4513"), (1,10,"#8B4513"), (1,11,"#FFFFFF"), (1,12,"#FFFFFF"), (2,0,"#8B4513"), (2,1,"#8B4513"), (2,2,"#8B4513"), (2,3,"#8B4513"), (2,4,"#8B4513"), (2,5,"#8B4513"), (2,6,"#8B4513"), (2,7,"#8B4513"), (2,8,"#8B4513"), (2,9,"#8B4513"), (2,10,"#8B4513"), (2,11,"#8B4513"), (2,12,"#FFFFFF"), (3,0,"#8B4513"), (3,1,"#8B4513"), (3,2,"#8B4513"), (3,3,"#8B4513"), (3,4,"#8B4513"), (3,5,"#8B4513"), (3,6,"#8B4513"), (3,7,"#8B4513"), (3,8,"#8B4513"), (3,9,"#8B4513"), (3,10,"#8B4513"), (3,11,"#FFFFFF"), (3,12,"#FFFFFF"), (3,13,"#C19153"), (3,14,"#C19153"), (3,15,"#C19153"), (3,16,"#C19153"), (3,17,"#C19153"), (4,0,"#8B4513"), (4,1,"#8B4513"), (4,2,"#8B4513"), (4,3,"#8B4513"), (4,4,"#8B4513"), (4,5,"#8B4513"), (4,6,"#8B4513"), (4,7,"#8B4513"), (4,8,"#8B4513"), (4,9,"#8B4513"), (4,10,"#8B4513"), (4,11,"#8B4513"), (4,12,"#FFFFFF"), (4,13,"#C19153"), (4,14,"#C19153"), (4,15,"#C19153"), (4,16,"#C19153"), (4,17,"#C19153"), (5,0,"#8B4513"), (5,1,"#8B4513"), (5,2,"#8B4513"), (5,3,"#8B4513"), (5,4,"#8B4513"), (5,5,"#8B4513"), (5,6,"#8B4513"), (5,7,"#8B4513"), (5,8,"#8B4513"), (5,9,"#8B4513"), (5,10,"#8B4513"), (5,11,"#8B4513"), (5,12,"#FFFFFF"), (6,0,"#8B4513"), (6,1,"#8B4513"), (6,2,"#8B4513"), (6,3,"#8B4513"), (6,4,"#8B4513"), (6,5,"#8B4513"), (6,6,"#8B4513"), (6,7,"#8B4513"), (6,8,"#8B4513"), (6,9,"#8B4513"), (6,10,"#8B4513"), (6,11,"#FFFFFF"), (6,12,"#FFFFFF"), (7,1,"#8B4513"), (7,2,"#8B4513"), (7,3,"#8B4513"), (7,4,"#8B4513"), (7,5,"#8B4513"), (7,6,"#8B4513"), (7,7,"#8B4513"), (7,8,"#8B4513"), (7,9,"#8B4513"), (7,10,"#8B4513"), (7,11,"#8B4513")]
charRobotron = [(1,4,"#FF0000"), (1,5,"#FFFF00"), (1,6,"#FFFF00"), (1,7,"#FFFF00"), (2,4,"#FF0000"), (2,5,"#FF0000"), (2,11,"#FFFF00"), (3,1,"#90EE90"), (3,2,"#00FFFF"), (3,4,"#FFFFFF"), (3,5,"#FF0000"), (3,6,"#FF0000"), (3,9,"#FF0000"), (3,10,"#FF0000"), (3,11,"#FFFF00"), (4,0,"#FF0000"), (4,1,"#90EE90"), (4,2,"#00FFFF"), (4,3,"#FF0000"), (4,4,"#FF0000"), (4,5,"#FFFFFF"), (4,6,"#FF0000"), (4,7,"#FF0000"), (4,8,"#FF0000"), (4,9,"#FF0000"), (4,10,"#FF0000"), (4,11,"#FFFF00"), (5,0,"#FF0000"), (5,1,"#90EE90"), (5,2,"#00FFFF"), (5,3,"#FF0000"), (5,4,"#FF0000"), (5,5,"#FFFFFF"), (5,6,"#FFFFFF"), (5,7,"#FF0000"), (5,8,"#FF0000"), (6,0,"#FF0000"), (6,1,"#90EE90"), (6,2,"#00FFFF"), (6,3,"#FF0000"), (6,4,"#FF0000"), (6,5,"#FFFFFF"), (6,6,"#FF0000"), (6,7,"#FF0000"), (6,8,"#FF0000"), (6,9,"#FF0000"), (6,10,"#FF0000"), (6,11,"#FFFF00"), (7,1,"#90EE90"), (7,2,"#00FFFF"), (7,4,"#FFFFFF"), (7,5,"#FF0000"), (7,6,"#FF0000"), (7,9,"#FF0000"), (7,10,"#FF0000"), (7,11,"#FFFF00"), (8,4,"#FF0000"), (8,5,"#FF0000"), (8,11,"#FFFF00"), (9,4,"#FF0000"), (9,5,"#FFFF00"), (9,6,"#FFFF00"), (9,7,"#FFFF00")]
charWall = [(0,2,"#FFFFFF"), (0,3,"#FFFFFF"), (0,4,"#FFFFFF"), (0,5,"#FFFFFF"), (0,6,"#FFFFFF"), (0,7,"#FFFFFF"), (0,8,"#FFFFFF"), (0,9,"#FFFFFF"), (0,10,"#FFFFFF"), (0,11,"#FFFFFF"), (0,12,"#FFFFFF"), (0,13,"#FFFFFF"), (0,14,"#FFFFFF"), (0,15,"#FFFFFF"), (0,16,"#FFFFFF"), (0,17,"#FFFFFF"), (0,18,"#FFFFFF"), (0,19,"#FFFFFF"), (0,20,"#FFFFFF"), (0,21,"#FFFFFF"), (1,1,"#FFFFFF"), (1,2,"#B5B3F5"), (1,3,"#B5B3F5"), (1,4,"#B5B3F5"), (1,5,"#B5B3F5"), (1,6,"#B5B3F5"), (1,7,"#B5B3F5"), (1,8,"#B5B3F5"), (1,9,"#B5B3F5"), (1,10,"#B5B3F5"), (1,11,"#B5B3F5"), (1,12,"#B5B3F5"), (1,13,"#B5B3F5"), (1,14,"#B5B3F5"), (1,15,"#B5B3F5"), (1,16,"#B5B3F5"), (1,17,"#B5B3F5"), (1,18,"#B5B3F5"), (1,19,"#B5B3F5"), (1,20,"#B5B3F5"), (1,21,"#B5B3F5"), (1,22,"#FFFFFF"), (2,0,"#FFFFFF"), (2,1,"#B5B3F5"), (2,2,"#B5B3F5"), (2,3,"#B5B3F5"), (2,4,"#B5B3F5"), (2,5,"#B5B3F5"), (2,6,"#B5B3F5"), (2,7,"#B5B3F5"), (2,8,"#B5B3F5"), (2,9,"#B5B3F5"), (2,10,"#B5B3F5"), (2,11,"#B5B3F5"), (2,12,"#B5B3F5"), (2,13,"#B5B3F5"), (2,14,"#B5B3F5"), (2,15,"#B5B3F5"), (2,16,"#B5B3F5"), (2,17,"#B5B3F5"), (2,18,"#B5B3F5"), (2,19,"#B5B3F5"), (2,20,"#B5B3F5"), (2,21,"#B5B3F5"), (2,22,"#B5B3F5"), (2,23,"#FFFFFF"), (3,0,"#FFFFFF"), (3,1,"#B5B3F5"), (3,2,"#B5B3F5"), (3,3,"#B5B3F5"), (3,4,"#B5B3F5"), (3,5,"#B5B3F5"), (3,6,"#B5B3F5"), (3,7,"#B5B3F5"), (3,8,"#B5B3F5"), (3,9,"#B5B3F5"), (3,10,"#B5B3F5"), (3,11,"#B5B3F5"), (3,12,"#B5B3F5"), (3,13,"#B5B3F5"), (3,14,"#B5B3F5"), (3,15,"#B5B3F5"), (3,16,"#B5B3F5"), (3,17,"#B5B3F5"), (3,18,"#B5B3F5"), (3,19,"#B5B3F5"), (3,20,"#B5B3F5"), (3,21,"#B5B3F5"), (3,22,"#B5B3F5"), (3,23,"#FFFFFF"), (4,0,"#FFFFFF"), (4,1,"#B5B3F5"), (4,2,"#B5B3F5"), (4,3,"#B5B3F5"), (4,4,"#B5B3F5"), (4,5,"#B5B3F5"), (4,6,"#B5B3F5"), (4,7,"#B5B3F5"), (4,8,"#B5B3F5"), (4,9,"#B5B3F5"), (4,10,"#B5B3F5"), (4,11,"#B5B3F5"), (4,12,"#B5B3F5"), (4,13,"#B5B3F5"), (4,14,"#B5B3F5"), (4,15,"#B5B3F5"), (4,16,"#B5B3F5"), (4,17,"#B5B3F5"), (4,18,"#B5B3F5"), (4,19,"#B5B3F5"), (4,20,"#B5B3F5"), (4,21,"#B5B3F5"), (4,22,"#B5B3F5"), (4,23,"#FFFFFF"), (5,0,"#FFFFFF"), (5,1,"#B5B3F5"), (5,2,"#B5B3F5"), (5,3,"#B5B3F5"), (5,4,"#B5B3F5"), (5,5,"#B5B3F5"), (5,6,"#B5B3F5"), (5,7,"#B5B3F5"), (5,8,"#B5B3F5"), (5,9,"#B5B3F5"), (5,10,"#B5B3F5"), (5,11,"#B5B3F5"), (5,12,"#B5B3F5"), (5,13,"#B5B3F5"), (5,14,"#B5B3F5"), (5,15,"#B5B3F5"), (5,16,"#B5B3F5"), (5,17,"#B5B3F5"), (5,18,"#B5B3F5"), (5,19,"#B5B3F5"), (5,20,"#B5B3F5"), (5,21,"#B5B3F5"), (5,22,"#B5B3F5"), (5,23,"#FFFFFF"), (6,0,"#FFFFFF"), (6,1,"#B5B3F5"), (6,2,"#B5B3F5"), (6,3,"#B5B3F5"), (6,4,"#B5B3F5"), (6,5,"#B5B3F5"), (6,6,"#B5B3F5"), (6,7,"#B5B3F5"), (6,8,"#B5B3F5"), (6,9,"#B5B3F5"), (6,10,"#B5B3F5"), (6,11,"#B5B3F5"), (6,12,"#B5B3F5"), (6,13,"#B5B3F5"), (6,14,"#B5B3F5"), (6,15,"#B5B3F5"), (6,16,"#B5B3F5"), (6,17,"#B5B3F5"), (6,18,"#B5B3F5"), (6,19,"#B5B3F5"), (6,20,"#B5B3F5"), (6,21,"#B5B3F5"), (6,22,"#B5B3F5"), (6,23,"#FFFFFF"), (7,0,"#FFFFFF"), (7,1,"#B5B3F5"), (7,2,"#B5B3F5"), (7,3,"#B5B3F5"), (7,4,"#B5B3F5"), (7,5,"#B5B3F5"), (7,6,"#B5B3F5"), (7,7,"#B5B3F5"), (7,8,"#B5B3F5"), (7,9,"#B5B3F5"), (7,10,"#B5B3F5"), (7,11,"#B5B3F5"), (7,12,"#B5B3F5"), (7,13,"#B5B3F5"), (7,14,"#B5B3F5"), (7,15,"#B5B3F5"), (7,16,"#B5B3F5"), (7,17,"#B5B3F5"), (7,18,"#B5B3F5"), (7,19,"#B5B3F5"), (7,20,"#B5B3F5"), (7,21,"#B5B3F5"), (7,22,"#B5B3F5"), (7,23,"#FFFFFF"), (8,0,"#FFFFFF"), (8,1,"#B5B3F5"), (8,2,"#B5B3F5"), (8,3,"#B5B3F5"), (8,4,"#B5B3F5"), (8,5,"#B5B3F5"), (8,6,"#B5B3F5"), (8,7,"#B5B3F5"), (8,8,"#B5B3F5"), (8,9,"#B5B3F5"), (8,10,"#B5B3F5"), (8,11,"#B5B3F5"), (8,12,"#B5B3F5"), (8,13,"#B5B3F5"), (8,14,"#B5B3F5"), (8,15,"#B5B3F5"), (8,16,"#B5B3F5"), (8,17,"#B5B3F5"), (8,18,"#B5B3F5"), (8,19,"#B5B3F5"), (8,20,"#B5B3F5"), (8,21,"#B5B3F5"), (8,22,"#B5B3F5"), (8,23,"#FFFFFF"), (9,0,"#FFFFFF"), (9,1,"#B5B3F5"), (9,2,"#B5B3F5"), (9,3,"#B5B3F5"), (9,4,"#B5B3F5"), (9,5,"#B5B3F5"), (9,6,"#B5B3F5"), (9,7,"#B5B3F5"), (9,8,"#B5B3F5"), (9,9,"#B5B3F5"), (9,10,"#B5B3F5"), (9,11,"#B5B3F5"), (9,12,"#B5B3F5"), (9,13,"#B5B3F5"), (9,14,"#B5B3F5"), (9,15,"#B5B3F5"), (9,16,"#B5B3F5"), (9,17,"#B5B3F5"), (9,18,"#B5B3F5"), (9,19,"#B5B3F5"), (9,20,"#B5B3F5"), (9,21,"#B5B3F5"), (9,22,"#B5B3F5"), (9,23,"#FFFFFF"), (10,0,"#FFFFFF"), (10,1,"#B5B3F5"), (10,2,"#B5B3F5"), (10,3,"#B5B3F5"), (10,4,"#B5B3F5"), (10,5,"#B5B3F5"), (10,6,"#B5B3F5"), (10,7,"#B5B3F5"), (10,8,"#B5B3F5"), (10,9,"#B5B3F5"), (10,10,"#B5B3F5"), (10,11,"#B5B3F5"), (10,12,"#B5B3F5"), (10,13,"#B5B3F5"), (10,14,"#B5B3F5"), (10,15,"#B5B3F5"), (10,16,"#B5B3F5"), (10,17,"#B5B3F5"), (10,18,"#B5B3F5"), (10,19,"#B5B3F5"), (10,20,"#B5B3F5"), (10,21,"#B5B3F5"), (10,22,"#B5B3F5"), (10,23,"#FFFFFF"), (11,0,"#FFFFFF"), (11,1,"#B5B3F5"), (11,2,"#B5B3F5"), (11,3,"#B5B3F5"), (11,4,"#B5B3F5"), (11,5,"#B5B3F5"), (11,6,"#B5B3F5"), (11,7,"#B5B3F5"), (11,8,"#B5B3F5"), (11,9,"#B5B3F5"), (11,10,"#B5B3F5"), (11,11,"#B5B3F5"), (11,12,"#B5B3F5"), (11,13,"#B5B3F5"), (11,14,"#B5B3F5"), (11,15,"#B5B3F5"), (11,16,"#B5B3F5"), (11,17,"#B5B3F5"), (11,18,"#B5B3F5"), (11,19,"#B5B3F5"), (11,20,"#B5B3F5"), (11,21,"#B5B3F5"), (11,22,"#B5B3F5"), (11,23,"#FFFFFF"), (12,0,"#FFFFFF"), (12,1,"#B5B3F5"), (12,2,"#B5B3F5"), (12,3,"#B5B3F5"), (12,4,"#B5B3F5"), (12,5,"#B5B3F5"), (12,6,"#B5B3F5"), (12,7,"#B5B3F5"), (12,8,"#B5B3F5"), (12,9,"#B5B3F5"), (12,10,"#B5B3F5"), (12,11,"#B5B3F5"), (12,12,"#B5B3F5"), (12,13,"#B5B3F5"), (12,14,"#B5B3F5"), (12,15,"#B5B3F5"), (12,16,"#B5B3F5"), (12,17,"#B5B3F5"), (12,18,"#B5B3F5"), (12,19,"#B5B3F5"), (12,20,"#B5B3F5"), (12,21,"#B5B3F5"), (12,22,"#B5B3F5"), (12,23,"#FFFFFF"), (13,0,"#FFFFFF"), (13,1,"#B5B3F5"), (13,2,"#B5B3F5"), (13,3,"#B5B3F5"), (13,4,"#B5B3F5"), (13,5,"#B5B3F5"), (13,6,"#B5B3F5"), (13,7,"#B5B3F5"), (13,8,"#B5B3F5"), (13,9,"#B5B3F5"), (13,10,"#B5B3F5"), (13,11,"#B5B3F5"), (13,12,"#B5B3F5"), (13,13,"#B5B3F5"), (13,14,"#B5B3F5"), (13,15,"#B5B3F5"), (13,16,"#B5B3F5"), (13,17,"#B5B3F5"), (13,18,"#B5B3F5"), (13,19,"#B5B3F5"), (13,20,"#B5B3F5"), (13,21,"#B5B3F5"), (13,22,"#B5B3F5"), (13,23,"#FFFFFF"), (14,0,"#FFFFFF"), (14,1,"#B5B3F5"), (14,2,"#B5B3F5"), (14,3,"#B5B3F5"), (14,4,"#B5B3F5"), (14,5,"#B5B3F5"), (14,6,"#B5B3F5"), (14,7,"#B5B3F5"), (14,8,"#B5B3F5"), (14,9,"#B5B3F5"), (14,10,"#B5B3F5"), (14,11,"#B5B3F5"), (14,12,"#B5B3F5"), (14,13,"#B5B3F5"), (14,14,"#B5B3F5"), (14,15,"#B5B3F5"), (14,16,"#B5B3F5"), (14,17,"#B5B3F5"), (14,18,"#B5B3F5"), (14,19,"#B5B3F5"), (14,20,"#B5B3F5"), (14,21,"#B5B3F5"), (14,22,"#B5B3F5"), (14,23,"#FFFFFF"), (15,0,"#FFFFFF"), (15,1,"#B5B3F5"), (15,2,"#B5B3F5"), (15,3,"#B5B3F5"), (15,4,"#B5B3F5"), (15,5,"#B5B3F5"), (15,6,"#B5B3F5"), (15,7,"#B5B3F5"), (15,8,"#B5B3F5"), (15,9,"#B5B3F5"), (15,10,"#B5B3F5"), (15,11,"#B5B3F5"), (15,12,"#B5B3F5"), (15,13,"#B5B3F5"), (15,14,"#B5B3F5"), (15,15,"#B5B3F5"), (15,16,"#B5B3F5"), (15,17,"#B5B3F5"), (15,18,"#B5B3F5"), (15,19,"#B5B3F5"), (15,20,"#B5B3F5"), (15,21,"#B5B3F5"), (15,22,"#B5B3F5"), (15,23,"#FFFFFF"), (16,0,"#FFFFFF"), (16,1,"#B5B3F5"), (16,2,"#B5B3F5"), (16,3,"#B5B3F5"), (16,4,"#B5B3F5"), (16,5,"#B5B3F5"), (16,6,"#B5B3F5"), (16,7,"#B5B3F5"), (16,8,"#B5B3F5"), (16,9,"#B5B3F5"), (16,10,"#B5B3F5"), (16,11,"#B5B3F5"), (16,12,"#B5B3F5"), (16,13,"#B5B3F5"), (16,14,"#B5B3F5"), (16,15,"#B5B3F5"), (16,16,"#B5B3F5"), (16,17,"#B5B3F5"), (16,18,"#B5B3F5"), (16,19,"#B5B3F5"), (16,20,"#B5B3F5"), (16,21,"#B5B3F5"), (16,22,"#B5B3F5"), (16,23,"#FFFFFF"), (17,0,"#FFFFFF"), (17,1,"#B5B3F5"), (17,2,"#B5B3F5"), (17,3,"#B5B3F5"), (17,4,"#B5B3F5"), (17,5,"#B5B3F5"), (17,6,"#B5B3F5"), (17,7,"#B5B3F5"), (17,8,"#B5B3F5"), (17,9,"#B5B3F5"), (17,10,"#B5B3F5"), (17,11,"#B5B3F5"), (17,12,"#B5B3F5"), (17,13,"#B5B3F5"), (17,14,"#B5B3F5"), (17,15,"#B5B3F5"), (17,16,"#B5B3F5"), (17,17,"#B5B3F5"), (17,18,"#B5B3F5"), (17,19,"#B5B3F5"), (17,20,"#B5B3F5"), (17,21,"#B5B3F5"), (17,22,"#B5B3F5"), (17,23,"#FFFFFF"), (18,0,"#FFFFFF"), (18,1,"#B5B3F5"), (18,2,"#B5B3F5"), (18,3,"#B5B3F5"), (18,4,"#B5B3F5"), (18,5,"#B5B3F5"), (18,6,"#B5B3F5"), (18,7,"#B5B3F5"), (18,8,"#B5B3F5"), (18,9,"#B5B3F5"), (18,10,"#B5B3F5"), (18,11,"#B5B3F5"), (18,12,"#B5B3F5"), (18,13,"#B5B3F5"), (18,14,"#B5B3F5"), (18,15,"#B5B3F5"), (18,16,"#B5B3F5"), (18,17,"#B5B3F5"), (18,18,"#B5B3F5"), (18,19,"#B5B3F5"), (18,20,"#B5B3F5"), (18,21,"#B5B3F5"), (18,22,"#B5B3F5"), (18,23,"#FFFFFF"), (19,0,"#FFFFFF"), (19,1,"#B5B3F5"), (19,2,"#B5B3F5"), (19,3,"#B5B3F5"), (19,4,"#B5B3F5"), (19,5,"#B5B3F5"), (19,6,"#B5B3F5"), (19,7,"#B5B3F5"), (19,8,"#B5B3F5"), (19,9,"#B5B3F5"), (19,10,"#B5B3F5"), (19,11,"#B5B3F5"), (19,12,"#B5B3F5"), (19,13,"#B5B3F5"), (19,14,"#B5B3F5"), (19,15,"#B5B3F5"), (19,16,"#B5B3F5"), (19,17,"#B5B3F5"), (19,18,"#B5B3F5"), (19,19,"#B5B3F5"), (19,20,"#B5B3F5"), (19,21,"#B5B3F5"), (19,22,"#B5B3F5"), (19,23,"#FFFFFF"), (20,0,"#FFFFFF"), (20,1,"#B5B3F5"), (20,2,"#B5B3F5"), (20,3,"#B5B3F5"), (20,4,"#B5B3F5"), (20,5,"#B5B3F5"), (20,6,"#B5B3F5"), (20,7,"#B5B3F5"), (20,8,"#B5B3F5"), (20,9,"#B5B3F5"), (20,10,"#B5B3F5"), (20,11,"#B5B3F5"), (20,12,"#B5B3F5"), (20,13,"#B5B3F5"), (20,14,"#B5B3F5"), (20,15,"#B5B3F5"), (20,16,"#B5B3F5"), (20,17,"#B5B3F5"), (20,18,"#B5B3F5"), (20,19,"#B5B3F5"), (20,20,"#B5B3F5"), (20,21,"#B5B3F5"), (20,22,"#B5B3F5"), (20,23,"#FFFFFF"), (21,0,"#FFFFFF"), (21,1,"#B5B3F5"), (21,2,"#B5B3F5"), (21,3,"#B5B3F5"), (21,4,"#B5B3F5"), (21,5,"#B5B3F5"), (21,6,"#B5B3F5"), (21,7,"#B5B3F5"), (21,8,"#B5B3F5"), (21,9,"#B5B3F5"), (21,10,"#B5B3F5"), (21,11,"#B5B3F5"), (21,12,"#B5B3F5"), (21,13,"#B5B3F5"), (21,14,"#B5B3F5"), (21,15,"#B5B3F5"), (21,16,"#B5B3F5"), (21,17,"#B5B3F5"), (21,18,"#B5B3F5"), (21,19,"#B5B3F5"), (21,20,"#B5B3F5"), (21,21,"#B5B3F5"), (21,22,"#B5B3F5"), (21,23,"#FFFFFF"), (22,1,"#FFFFFF"), (22,2,"#B5B3F5"), (22,3,"#B5B3F5"), (22,4,"#B5B3F5"), (22,5,"#B5B3F5"), (22,6,"#B5B3F5"), (22,7,"#B5B3F5"), (22,8,"#B5B3F5"), (22,9,"#B5B3F5"), (22,10,"#B5B3F5"), (22,11,"#B5B3F5"), (22,12,"#B5B3F5"), (22,13,"#B5B3F5"), (22,14,"#B5B3F5"), (22,15,"#B5B3F5"), (22,16,"#B5B3F5"), (22,17,"#B5B3F5"), (22,18,"#B5B3F5"), (22,19,"#B5B3F5"), (22,20,"#B5B3F5"), (22,21,"#B5B3F5"), (22,22,"#FFFFFF"), (23,2,"#FFFFFF"), (23,3,"#FFFFFF"), (23,4,"#FFFFFF"), (23,5,"#FFFFFF"), (23,6,"#FFFFFF"), (23,7,"#FFFFFF"), (23,8,"#FFFFFF"), (23,9,"#FFFFFF"), (23,10,"#FFFFFF"), (23,11,"#FFFFFF"), (23,12,"#FFFFFF"), (23,13,"#FFFFFF"), (23,14,"#FFFFFF"), (23,15,"#FFFFFF"), (23,16,"#FFFFFF"), (23,17,"#FFFFFF"), (23,18,"#FFFFFF"), (23,19,"#FFFFFF"), (23,20,"#FFFFFF"), (23,21,"#FFFFFF")]
charWall2 = [(4,6,"#FFFFFF"), (4,7,"#FFFFFF"), (4,8,"#FFFFFF"), (4,9,"#FFFFFF"), (4,10,"#FFFFFF"), (4,11,"#FFFFFF"), (4,12,"#FFFFFF"), (4,13,"#FFFFFF"), (4,14,"#FFFFFF"), (4,15,"#FFFFFF"), (4,16,"#FFFFFF"), (4,17,"#FFFFFF"), (5,5,"#FFFFFF"), (5,6,"#B5B3F5"), (5,7,"#B5B3F5"), (5,8,"#B5B3F5"), (5,9,"#B5B3F5"), (5,10,"#B5B3F5"), (5,11,"#B5B3F5"), (5,12,"#B5B3F5"), (5,13,"#B5B3F5"), (5,14,"#B5B3F5"), (5,15,"#B5B3F5"), (5,16,"#B5B3F5"), (5,17,"#B5B3F5"), (5,18,"#FFFFFF"), (6,4,"#FFFFFF"), (6,5,"#B5B3F5"), (6,6,"#B5B3F5"), (6,7,"#B5B3F5"), (6,8,"#B5B3F5"), (6,9,"#B5B3F5"), (6,10,"#B5B3F5"), (6,11,"#B5B3F5"), (6,12,"#B5B3F5"), (6,13,"#B5B3F5"), (6,14,"#B5B3F5"), (6,15,"#B5B3F5"), (6,16,"#B5B3F5"), (6,17,"#B5B3F5"), (6,18,"#B5B3F5"), (6,19,"#FFFFFF"), (7,4,"#FFFFFF"), (7,5,"#B5B3F5"), (7,6,"#B5B3F5"), (7,7,"#B5B3F5"), (7,8,"#B5B3F5"), (7,9,"#B5B3F5"), (7,10,"#B5B3F5"), (7,11,"#B5B3F5"), (7,12,"#B5B3F5"), (7,13,"#B5B3F5"), (7,14,"#B5B3F5"), (7,15,"#B5B3F5"), (7,16,"#B5B3F5"), (7,17,"#B5B3F5"), (7,18,"#B5B3F5"), (7,19,"#FFFFFF"), (8,4,"#FFFFFF"), (8,5,"#B5B3F5"), (8,6,"#B5B3F5"), (8,7,"#B5B3F5"), (8,8,"#B5B3F5"), (8,9,"#B5B3F5"), (8,10,"#B5B3F5"), (8,11,"#B5B3F5"), (8,12,"#B5B3F5"), (8,13,"#B5B3F5"), (8,14,"#B5B3F5"), (8,15,"#B5B3F5"), (8,16,"#B5B3F5"), (8,17,"#B5B3F5"), (8,18,"#B5B3F5"), (8,19,"#FFFFFF"), (9,4,"#FFFFFF"), (9,5,"#B5B3F5"), (9,6,"#B5B3F5"), (9,7,"#B5B3F5"), (9,8,"#B5B3F5"), (9,9,"#B5B3F5"), (9,10,"#B5B3F5"), (9,11,"#B5B3F5"), (9,12,"#B5B3F5"), (9,13,"#B5B3F5"), (9,14,"#B5B3F5"), (9,15,"#B5B3F5"), (9,16,"#B5B3F5"), (9,17,"#B5B3F5"), (9,18,"#B5B3F5"), (9,19,"#FFFFFF"), (10,4,"#FFFFFF"), (10,5,"#B5B3F5"), (10,6,"#B5B3F5"), (10,7,"#B5B3F5"), (10,8,"#B5B3F5"), (10,9,"#B5B3F5"), (10,10,"#B5B3F5"), (10,11,"#B5B3F5"), (10,12,"#B5B3F5"), (10,13,"#B5B3F5"), (10,14,"#B5B3F5"), (10,15,"#B5B3F5"), (10,16,"#B5B3F5"), (10,17,"#B5B3F5"), (10,18,"#B5B3F5"), (10,19,"#FFFFFF"), (11,4,"#FFFFFF"), (11,5,"#B5B3F5"), (11,6,"#B5B3F5"), (11,7,"#B5B3F5"), (11,8,"#B5B3F5"), (11,9,"#B5B3F5"), (11,10,"#B5B3F5"), (11,11,"#B5B3F5"), (11,12,"#B5B3F5"), (11,13,"#B5B3F5"), (11,14,"#B5B3F5"), (11,15,"#B5B3F5"), (11,16,"#B5B3F5"), (11,17,"#B5B3F5"), (11,18,"#B5B3F5"), (11,19,"#FFFFFF"), (12,4,"#FFFFFF"), (12,5,"#B5B3F5"), (12,6,"#B5B3F5"), (12,7,"#B5B3F5"), (12,8,"#B5B3F5"), (12,9,"#B5B3F5"), (12,10,"#B5B3F5"), (12,11,"#B5B3F5"), (12,12,"#B5B3F5"), (12,13,"#B5B3F5"), (12,14,"#B5B3F5"), (12,15,"#B5B3F5"), (12,16,"#B5B3F5"), (12,17,"#B5B3F5"), (12,18,"#B5B3F5"), (12,19,"#FFFFFF"), (13,4,"#FFFFFF"), (13,5,"#B5B3F5"), (13,6,"#B5B3F5"), (13,7,"#B5B3F5"), (13,8,"#B5B3F5"), (13,9,"#B5B3F5"), (13,10,"#B5B3F5"), (13,11,"#B5B3F5"), (13,12,"#B5B3F5"), (13,13,"#B5B3F5"), (13,14,"#B5B3F5"), (13,15,"#B5B3F5"), (13,16,"#B5B3F5"), (13,17,"#B5B3F5"), (13,18,"#B5B3F5"), (13,19,"#FFFFFF"), (14,4,"#FFFFFF"), (14,5,"#B5B3F5"), (14,6,"#B5B3F5"), (14,7,"#B5B3F5"), (14,8,"#B5B3F5"), (14,9,"#B5B3F5"), (14,10,"#B5B3F5"), (14,11,"#B5B3F5"), (14,12,"#B5B3F5"), (14,13,"#B5B3F5"), (14,14,"#B5B3F5"), (14,15,"#B5B3F5"), (14,16,"#B5B3F5"), (14,17,"#B5B3F5"), (14,18,"#B5B3F5"), (14,19,"#FFFFFF"), (15,4,"#FFFFFF"), (15,5,"#B5B3F5"), (15,6,"#B5B3F5"), (15,7,"#B5B3F5"), (15,8,"#B5B3F5"), (15,9,"#B5B3F5"), (15,10,"#B5B3F5"), (15,11,"#B5B3F5"), (15,12,"#B5B3F5"), (15,13,"#B5B3F5"), (15,14,"#B5B3F5"), (15,15,"#B5B3F5"), (15,16,"#B5B3F5"), (15,17,"#B5B3F5"), (15,18,"#B5B3F5"), (15,19,"#FFFFFF"), (16,4,"#FFFFFF"), (16,5,"#B5B3F5"), (16,6,"#B5B3F5"), (16,7,"#B5B3F5"), (16,8,"#B5B3F5"), (16,9,"#B5B3F5"), (16,10,"#B5B3F5"), (16,11,"#B5B3F5"), (16,12,"#B5B3F5"), (16,13,"#B5B3F5"), (16,14,"#B5B3F5"), (16,15,"#B5B3F5"), (16,16,"#B5B3F5"), (16,17,"#B5B3F5"), (16,18,"#B5B3F5"), (16,19,"#FFFFFF"), (17,4,"#FFFFFF"), (17,5,"#B5B3F5"), (17,6,"#B5B3F5"), (17,7,"#B5B3F5"), (17,8,"#B5B3F5"), (17,9,"#B5B3F5"), (17,10,"#B5B3F5"), (17,11,"#B5B3F5"), (17,12,"#B5B3F5"), (17,13,"#B5B3F5"), (17,14,"#B5B3F5"), (17,15,"#B5B3F5"), (17,16,"#B5B3F5"), (17,17,"#B5B3F5"), (17,18,"#B5B3F5"), (17,19,"#FFFFFF"), (18,5,"#FFFFFF"), (18,6,"#B5B3F5"), (18,7,"#B5B3F5"), (18,8,"#B5B3F5"), (18,9,"#B5B3F5"), (18,10,"#B5B3F5"), (18,11,"#B5B3F5"), (18,12,"#B5B3F5"), (18,13,"#B5B3F5"), (18,14,"#B5B3F5"), (18,15,"#B5B3F5"), (18,16,"#B5B3F5"), (18,17,"#B5B3F5"), (18,18,"#FFFFFF"), (19,6,"#FFFFFF"), (19,7,"#FFFFFF"), (19,8,"#FFFFFF"), (19,9,"#FFFFFF"), (19,10,"#FFFFFF"), (19,11,"#FFFFFF"), (19,12,"#FFFFFF"), (19,13,"#FFFFFF"), (19,14,"#FFFFFF"), (19,15,"#FFFFFF"), (19,16,"#FFFFFF"), (19,17,"#FFFFFF")]



STEPD = 4 # speed of car. This changes dx,dy.

MAXx = 700
MAXy = 400

score = 0

ShowAllCollisions = False

HitWall = False
PlayerAlive = False

def rotatepoints(points,angle,center):
         newpoints = []
         anglerad = math.radians(angle)
         cx,cy = center
         for x,y,z in points:
              x = x - cx
              y = y - cy
              newx = x* math.cos(anglerad)- y*math.sin(anglerad) + cx
              newy = x * math.sin(anglerad) + y*math.cos(anglerad) + cy
              newpoints.append((newx,newy,z))
         return newpoints


class LEDobj:
    def __init__(self, canvas,x=0,y=0,dx=0,dy=0, CharPoints = [], pixelsize = 2, typestring = "unknown"):
         self.x = x
         self.y = y
         self.dx = dx
         self.dy = dy
         self.canvas = canvas
         self.typestring = typestring
         self.LEDPoints = []
         self.OriginalCharPoints = CharPoints
         self.CharPoints = CharPoints.copy()
         self.collisionrect = (0,0,0,0)  # top left to bottom right
         self.collisionimage = 0
         self.collisionrectshow = False
         self.pixelsize = pixelsize
         LEDlib.psize = self.pixelsize
         LEDlib.createCharColourSolid(canvas,x,y,CharPoints,self.LEDPoints)
    def resetposition(self,x,y):
        self.x, self.y = x,y
        self.dx, self.dy = 0,0
        self.draw()
    def undraw(self):
         for p in self.LEDPoints:
            self.canvas.delete(p)
         self.LEDPoints.clear()
    def draw(self):
        self.undraw()
        LEDlib.psize = self.pixelsize
        LEDlib.createCharColourSolid(self.canvas,self.x,self.y,self.CharPoints,self.LEDPoints)
        if self.collisionrectshow:
              canvas1.delete(self.collisionimage)
              self.showcollisionrect() 
    def move(self): 
         self.x = self.x + self.dx
         self.y = self.y + self.dy
         if self.x > MAXx-48: self.x = MAXx-48
         if self.y > MAXy-48: self.y = MAXy-48
         if self.x < 0 : self.x = 0
         if self.y < 0 : self.y = 0
         self.draw()
    def rotate(self,angledeg):
         centerx = sum(x for x,y,z in self.OriginalCharPoints)/len(self.OriginalCharPoints)
         centery = sum(y for x,y,z in self.OriginalCharPoints)/len(self.OriginalCharPoints)
         self.CharPoints = rotatepoints(self.OriginalCharPoints,angle=angledeg,center=(centerx,centery))
         self.draw()
    def showcollisionrect(self):
         self.collisionrectshow = True
         x1,y1,x2,y2 = self.collisionrect 
         self.collisionimage = canvas1.create_rectangle(self.x+x1,self.y+y1,self.x+x2,self.y+y2,fill="", outline = "white") 
         
class LEDscoreobj:
    def __init__(self, canvas,x=0,y=0, score = 0, colour = "white", pixelsize = 2, charwidth=23, numzeros = 0):
         self.x = x
         self.y = y
         self.score = score
         self.canvas = canvas
         self.LEDPoints = []
         self.colour = colour
         self.pixelsize = pixelsize
         self.charwidth = charwidth
         self.numzeros = numzeros 
         self.draw()
    def draw(self):
        self.undraw()
        LEDlib.charwidth = self.charwidth
        LEDlib.psize = self.pixelsize
        LEDlib.ShowColourScore(self.canvas,self.x,self.y,self.colour,self.score,self.LEDPoints, self.numzeros) 
    def undraw(self):
         for p in self.LEDPoints:
            self.canvas.delete(p)
         self.LEDPoints.clear()
    def update(self,myscore):
        self.score = myscore
        self.draw()





def checkcollisionrect(object1,object2):
     x1,y1,x2,y2 = object1.collisionrect 
     a1,b1,a2,b2 = object2.collisionrect
     x1 = x1 + object1.x
     y1 = y1 + object1.y
     x2 = x2 + object1.x
     y2 = y2 + object1.y 
     a1 = a1 + object2.x
     b1 = b1 + object2.y
     a2 = a2 + object2.x
     b2 = b2 + object2.y 
     if x2 < a1 or x1 > a2 or y2 < b1 or y1 > b2:
          return False
     else:
          return True

mainwin = Tk()
mainwin.geometry(str(MAXx)+"x"+str(MAXy)) 
canvas1 = Canvas(mainwin,width=MAXx,height= MAXy,bg="black")
canvas1.place(x=0,y=0)

myship = LEDobj(canvas1,MAXx//2,MAXy//2,dx = 0,dy = 0,CharPoints=charRallyX, pixelsize = 2,typestring = "car")
myship.collisionrect = (4,3,44,45)
if ShowAllCollisions: myship.showcollisionrect()

fruitlist = []
solidlist = []
scoreddisplay = []

wallsize = 30  # put blocks in grid from (0,0) to (22,12)
def block(x,y,n): # make an nxn block at (x,y)
    myset = set()  # cannot use {} for emptyset, o/w it is a dictionary
    for i in range(n):
        for j in range(n):
            myset.add((x+i,y+j))
    return myset          
            
walls = {(0,2),(1,2),(2,2),(2,1),(2,0),(5,0),(5,1),(5,2),(5,3)} | block(10,10,3) | block(4,8,2)
walls = walls | block(18,4,2) | block(10,4,2)
# {...} is a set. Take union with {..} | {..}


popiscletype  = 1
 # put blocks in grid from (0,0) to (22,12)
pointsset = {(4,4,popiscletype),(4,2,popiscletype), (8,2,popiscletype),
             (10,2,popiscletype),(12,2,popiscletype),(14,2,popiscletype),
             (16,2,popiscletype), (18,2,popiscletype),
             (0,12,popiscletype), (22,12,popiscletype) }

displayscore = LEDscoreobj(canvas1,x=MAXx-200,y=20,score=0,colour="white",pixelsize=3, charwidth = 24,numzeros=8)

starttime = time.time()

displayclock = LEDscoreobj(canvas1,x=10,y=10,score=7,colour="light green",pixelsize=6, charwidth = 24,numzeros=0)


def makewalls():
    for x,y in walls:
        wall = LEDobj(canvas1,x*wallsize-8,y*wallsize-8,dx = 0,dy = 0,CharPoints=charWall2, pixelsize = 2,typestring = "solid")
        wall.collisionrect = (8,8,40,40)
        solidlist.append(wall) 

def createplayfield():
   makewalls()
   for x,y,stype in pointsset:
       if stype == popiscletype:
           fruit = LEDobj(canvas1,x*wallsize+8,y*wallsize,dx = 0,dy = 0,CharPoints=charPopsicle, pixelsize = 2,typestring = "fruit")
           fruit.collisionrect = (0,0,16,36)
           fruitlist.append(fruit)
       

def eraseplayfield():
    for itemlist in (fruitlist, solidlist, scoreddisplay):
        for item in itemlist:
           item.undraw()
        itemlist.clear()
    
  

createplayfield()

def updateclock():
    global PlayerAlive
    seconds = time.time()-starttime
    if seconds <= 7 and PlayerAlive : 
        displayclock.update(int(abs(7-seconds)))
    else:
        PlayerAlive = False
    if seconds >= 3 : displayclock.colour = "red"
    mainwin.after(1000,updateclock)

updateclock()

def gameloop():
    global HitWall, score 
    if PlayerAlive: myship.move()
    for fruit in fruitlist:
       if checkcollisionrect(myship,fruit):
            points100 = LEDscoreobj(canvas1,x=fruit.x-14,y=fruit.y+10,score=100,colour="white",pixelsize=2, charwidth = 12)
            scoreddisplay.append(points100)
            fruit.undraw()
            fruitlist.remove(fruit)
            score = score + 100
            displayscore.update(score)
            print(len(fruitlist))
    for solid in solidlist:
         if checkcollisionrect(myship,solid): 
            if not HitWall:
              myship.x = myship.x - myship.dx
              myship.y = myship.y - myship.dy
            myship.dx = 0
            myship.dy = 0
            HitWall = True
            break # exit the for loop
    mainwin.after(10,gameloop)

gameloop()

def mykey(event):
    global HitWall, PlayerAlive, starttime,score
    key = event.keysym
    if key == "1":
        PlayerAlive = True
        starttime = time.time()
        eraseplayfield()
        createplayfield()
        myship.resetposition(MAXx//2,MAXy//2)
        score = 0
        displayclock.colour = "lightgreen"
        displayclock.update(7)
    if HitWall:
         HitWall = False
    elif   key == "w":
         myship.rotate(0)
         myship.dy = -STEPD
         myship.dx = 0
    elif key == "d":
         myship.rotate(90)
         myship.dy = 0
         myship.dx = STEPD
    elif key == "a":
         myship.rotate(270)
         myship.dy = 0
         myship.dx = -STEPD
    elif key == "s":
         myship.rotate(180)
         myship.dy = STEPD
         myship.dx = 0


mainwin.bind("<KeyPress>", mykey)
mainwin.mainloop()