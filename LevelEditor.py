import sys
import re  # for using regular expression searches when loading walls/fruit from text
from tkinter import * 
sys.path.insert(0, "/home/deck/Documents")  # needed to import LEDlib
import LEDlib

charRallyX = [(0,14,"#4C3A23"), (0,15,"#4C3A23"), (0,16,"#4C3A23"), (0,17,"#4C3A23"), (0,18,"#4C3A23"), (0,19,"#4C3A23"), (0,20,"#4C3A23"), (1,13,"#4C3A23"), (1,14,"#4C3A23"), (1,15,"#4C3A23"), (1,16,"#4C3A23"), (1,17,"#4C3A23"), (1,18,"#4C3A23"), (1,19,"#4C3A23"), (1,20,"#4C3A23"), (1,21,"#4C3A23"), (2,2,"#4C3A23"), (2,3,"#4C3A23"), (2,4,"#4C3A23"), (2,5,"#4C3A23"), (2,6,"#4C3A23"), (2,13,"#4C3A23"), (2,14,"#4C3A23"), (2,15,"#4C3A23"), (2,16,"#4C3A23"), (2,17,"#4C3A23"), (2,18,"#4C3A23"), (2,19,"#4C3A23"), (2,20,"#4C3A23"), (2,21,"#4C3A23"), (3,1,"#4C3A23"), (3,2,"#4C3A23"), (3,3,"#4C3A23"), (3,4,"#4C3A23"), (3,5,"#4C3A23"), (3,6,"#4C3A23"), (3,7,"#4C3A23"), (3,13,"#4C3A23"), (3,14,"#4C3A23"), (3,15,"#4C3A23"), (3,16,"#4C3A23"), (3,17,"#4C3A23"), (3,18,"#4C3A23"), (3,19,"#4C3A23"), (3,20,"#4C3A23"), (3,21,"#4C3A23"), (4,1,"#4C3A23"), (4,2,"#4C3A23"), (4,3,"#4C3A23"), (4,4,"#4C3A23"), (4,5,"#4C3A23"), (4,6,"#4C3A23"), (4,7,"#4C3A23"), (4,13,"#4C3A23"), (4,14,"#4C3A23"), (4,15,"#4C3A23"), (4,16,"#4C3A23"), (4,17,"#4C3A23"), (4,18,"#4C3A23"), (4,19,"#4C3A23"), (4,20,"#4C3A23"), (4,21,"#4C3A23"), (5,1,"#4C3A23"), (5,2,"#4C3A23"), (5,3,"#4C3A23"), (5,4,"#4C3A23"), (5,5,"#4C3A23"), (5,6,"#4C3A23"), (5,7,"#4C3A23"), (5,13,"#4C3A23"), (5,14,"#4C3A23"), (5,15,"#4C3A23"), (5,16,"#4C3A23"), (5,17,"#4C3A23"), (5,18,"#4C3A23"), (5,19,"#4C3A23"), (5,20,"#4C3A23"), (5,21,"#4C3A23"), (6,1,"#4C3A23"), (6,2,"#4C3A23"), (6,3,"#4C3A23"), (6,4,"#4C3A23"), (6,5,"#4C3A23"), (6,6,"#4C3A23"), (6,7,"#4C3A23"), (6,14,"#4C3A23"), (6,15,"#4C3A23"), (6,16,"#4C3A23"), (6,17,"#4C3A23"), (6,18,"#4C3A23"), (6,19,"#4C3A23"), (6,20,"#4C3A23"), (7,2,"#4C3A23"), (7,3,"#4C3A23"), (7,4,"#4C3A23"), (7,5,"#4C3A23"), (7,6,"#4C3A23"), (7,17,"#FFA07A"), (8,4,"#FFA07A"), (8,10,"#FFA07A"), (8,11,"#FFA07A"), (8,12,"#FFA07A"), (8,13,"#FFA07A"), (8,14,"#FFA07A"), (8,15,"#FFA07A"), (8,16,"#FFA07A"), (8,17,"#FFA07A"), (8,18,"#FFA07A"), (8,19,"#8B4513"), (8,20,"#8B4513"), (8,21,"#FF0000"), (8,22,"#FFFF00"), (8,23,"#FF0000"), (9,4,"#FFA07A"), (9,8,"#FFA07A"), (9,9,"#FFA07A"), (9,10,"#FFA07A"), (9,11,"#FFA07A"), (9,12,"#FFA07A"), (9,13,"#FFA07A"), (9,14,"#FFA07A"), (9,15,"#FFA07A"), (9,16,"#FFA07A"), (9,17,"#FFA07A"), (9,18,"#FFA07A"), (9,19,"#FFA07A"), (9,20,"#8B4513"), (9,21,"#8B4513"), (9,22,"#FF0000"), (9,23,"#FFFF00"), (10,1,"#FFA07A"), (10,2,"#FFA07A"), (10,3,"#FFA07A"), (10,4,"#FFA07A"), (10,5,"#FFA07A"), (10,6,"#FFA07A"), (10,7,"#FFA07A"), (10,8,"#FFA07A"), (10,9,"#FFA07A"), (10,10,"#FFA07A"), (10,11,"#AAAAAA"), (10,12,"#AAAAAA"), (10,13,"#AAAAAA"), (10,14,"#AAAAAA"), (10,15,"#AAAAAA"), (10,16,"#AAAAAA"), (10,17,"#FFA07A"), (10,18,"#FFA07A"), (10,19,"#FFA07A"), (10,20,"#FFA07A"), (11,0,"#FFA07A"), (11,1,"#FFA07A"), (11,2,"#FFA07A"), (11,3,"#FFA07A"), (11,4,"#FFA07A"), (11,5,"#FFA07A"), (11,6,"#FFA07A"), (11,7,"#FFA07A"), (11,8,"#FFA07A"), (11,9,"#FFA07A"), (11,10,"#AAAAAA"), (11,11,"#B5B3F5"), (11,12,"#FFFFFF"), (11,13,"#FFFFFF"), (11,14,"#FFFFFF"), (11,15,"#FFFFFF"), (11,16,"#B5B3F5"), (11,17,"#AAAAAA"), (11,18,"#FFA07A"), (11,19,"#FFA07A"), (11,20,"#FFA07A"), (12,0,"#FFA07A"), (12,1,"#FFA07A"), (12,2,"#FFA07A"), (12,3,"#FFA07A"), (12,4,"#FFA07A"), (12,5,"#FFA07A"), (12,6,"#FFA07A"), (12,7,"#FFA07A"), (12,8,"#FFA07A"), (12,9,"#FFA07A"), (12,10,"#AAAAAA"), (12,11,"#B5B3F5"), (12,12,"#FFFFFF"), (12,13,"#FFFFFF"), (12,14,"#FFFFFF"), (12,15,"#FFFFFF"), (12,16,"#B5B3F5"), (12,17,"#AAAAAA"), (12,18,"#FFA07A"), (12,19,"#FFA07A"), (12,20,"#FFA07A"), (13,1,"#FFA07A"), (13,2,"#FFA07A"), (13,3,"#FFA07A"), (13,4,"#FFA07A"), (13,5,"#FFA07A"), (13,6,"#FFA07A"), (13,7,"#FFA07A"), (13,8,"#FFA07A"), (13,9,"#FFA07A"), (13,10,"#FFA07A"), (13,11,"#AAAAAA"), (13,12,"#AAAAAA"), (13,13,"#AAAAAA"), (13,14,"#AAAAAA"), (13,15,"#AAAAAA"), (13,16,"#AAAAAA"), (13,17,"#FFA07A"), (13,18,"#FFA07A"), (13,19,"#FFA07A"), (13,20,"#FFA07A"), (14,4,"#FFA07A"), (14,8,"#FFA07A"), (14,9,"#FFA07A"), (14,10,"#FFA07A"), (14,11,"#FFA07A"), (14,12,"#FFA07A"), (14,13,"#FFA07A"), (14,14,"#FFA07A"), (14,15,"#FFA07A"), (14,16,"#FFA07A"), (14,17,"#FFA07A"), (14,18,"#FFA07A"), (14,19,"#FFA07A"), (14,20,"#8B4513"), (14,21,"#8B4513"), (14,22,"#FF0000"), (14,23,"#FFFF00"), (15,4,"#FFA07A"), (15,10,"#FFA07A"), (15,11,"#FFA07A"), (15,12,"#FFA07A"), (15,13,"#FFA07A"), (15,14,"#FFA07A"), (15,15,"#FFA07A"), (15,16,"#FFA07A"), (15,17,"#FFA07A"), (15,18,"#FFA07A"), (15,19,"#8B4513"), (15,20,"#8B4513"), (15,21,"#FF0000"), (15,22,"#FFFF00"), (15,23,"#FF0000"), (16,2,"#4C3A23"), (16,3,"#4C3A23"), (16,4,"#4C3A23"), (16,5,"#4C3A23"), (16,6,"#4C3A23"), (16,17,"#FFA07A"), (17,1,"#4C3A23"), (17,2,"#4C3A23"), (17,3,"#4C3A23"), (17,4,"#4C3A23"), (17,5,"#4C3A23"), (17,6,"#4C3A23"), (17,7,"#4C3A23"), (17,14,"#4C3A23"), (17,15,"#4C3A23"), (17,16,"#4C3A23"), (17,17,"#4C3A23"), (17,18,"#4C3A23"), (17,19,"#4C3A23"), (17,20,"#4C3A23"), (18,1,"#4C3A23"), (18,2,"#4C3A23"), (18,3,"#4C3A23"), (18,4,"#4C3A23"), (18,5,"#4C3A23"), (18,6,"#4C3A23"), (18,7,"#4C3A23"), (18,13,"#4C3A23"), (18,14,"#4C3A23"), (18,15,"#4C3A23"), (18,16,"#4C3A23"), (18,17,"#4C3A23"), (18,18,"#4C3A23"), (18,19,"#4C3A23"), (18,20,"#4C3A23"), (18,21,"#4C3A23"), (19,1,"#4C3A23"), (19,2,"#4C3A23"), (19,3,"#4C3A23"), (19,4,"#4C3A23"), (19,5,"#4C3A23"), (19,6,"#4C3A23"), (19,7,"#4C3A23"), (19,13,"#4C3A23"), (19,14,"#4C3A23"), (19,15,"#4C3A23"), (19,16,"#4C3A23"), (19,17,"#4C3A23"), (19,18,"#4C3A23"), (19,19,"#4C3A23"), (19,20,"#4C3A23"), (19,21,"#4C3A23"), (20,1,"#4C3A23"), (20,2,"#4C3A23"), (20,3,"#4C3A23"), (20,4,"#4C3A23"), (20,5,"#4C3A23"), (20,6,"#4C3A23"), (20,7,"#4C3A23"), (20,13,"#4C3A23"), (20,14,"#4C3A23"), (20,15,"#4C3A23"), (20,16,"#4C3A23"), (20,17,"#4C3A23"), (20,18,"#4C3A23"), (20,19,"#4C3A23"), (20,20,"#4C3A23"), (20,21,"#4C3A23"), (21,2,"#4C3A23"), (21,3,"#4C3A23"), (21,4,"#4C3A23"), (21,5,"#4C3A23"), (21,6,"#4C3A23"), (21,13,"#4C3A23"), (21,14,"#4C3A23"), (21,15,"#4C3A23"), (21,16,"#4C3A23"), (21,17,"#4C3A23"), (21,18,"#4C3A23"), (21,19,"#4C3A23"), (21,20,"#4C3A23"), (21,21,"#4C3A23"), (22,13,"#4C3A23"), (22,14,"#4C3A23"), (22,15,"#4C3A23"), (22,16,"#4C3A23"), (22,17,"#4C3A23"), (22,18,"#4C3A23"), (22,19,"#4C3A23"), (22,20,"#4C3A23"), (22,21,"#4C3A23"), (23,14,"#4C3A23"), (23,15,"#4C3A23"), (23,16,"#4C3A23"), (23,17,"#4C3A23"), (23,18,"#4C3A23"), (23,19,"#4C3A23"), (23,20,"#4C3A23")]
charPopsicle = [(0,1,"#8B4513"), (0,2,"#8B4513"), (0,3,"#8B4513"), (0,4,"#8B4513"), (0,5,"#8B4513"), (0,6,"#8B4513"), (0,7,"#8B4513"), (0,8,"#8B4513"), (0,9,"#8B4513"), (0,10,"#8B4513"), (0,11,"#8B4513"), (1,0,"#8B4513"), (1,1,"#8B4513"), (1,2,"#FFFFFF"), (1,3,"#FFFFFF"), (1,4,"#FFFFFF"), (1,5,"#8B4513"), (1,6,"#8B4513"), (1,7,"#8B4513"), (1,8,"#8B4513"), (1,9,"#8B4513"), (1,10,"#8B4513"), (1,11,"#FFFFFF"), (1,12,"#FFFFFF"), (2,0,"#8B4513"), (2,1,"#8B4513"), (2,2,"#8B4513"), (2,3,"#8B4513"), (2,4,"#8B4513"), (2,5,"#8B4513"), (2,6,"#8B4513"), (2,7,"#8B4513"), (2,8,"#8B4513"), (2,9,"#8B4513"), (2,10,"#8B4513"), (2,11,"#8B4513"), (2,12,"#FFFFFF"), (3,0,"#8B4513"), (3,1,"#8B4513"), (3,2,"#8B4513"), (3,3,"#8B4513"), (3,4,"#8B4513"), (3,5,"#8B4513"), (3,6,"#8B4513"), (3,7,"#8B4513"), (3,8,"#8B4513"), (3,9,"#8B4513"), (3,10,"#8B4513"), (3,11,"#FFFFFF"), (3,12,"#FFFFFF"), (3,13,"#C19153"), (3,14,"#C19153"), (3,15,"#C19153"), (3,16,"#C19153"), (3,17,"#C19153"), (4,0,"#8B4513"), (4,1,"#8B4513"), (4,2,"#8B4513"), (4,3,"#8B4513"), (4,4,"#8B4513"), (4,5,"#8B4513"), (4,6,"#8B4513"), (4,7,"#8B4513"), (4,8,"#8B4513"), (4,9,"#8B4513"), (4,10,"#8B4513"), (4,11,"#8B4513"), (4,12,"#FFFFFF"), (4,13,"#C19153"), (4,14,"#C19153"), (4,15,"#C19153"), (4,16,"#C19153"), (4,17,"#C19153"), (5,0,"#8B4513"), (5,1,"#8B4513"), (5,2,"#8B4513"), (5,3,"#8B4513"), (5,4,"#8B4513"), (5,5,"#8B4513"), (5,6,"#8B4513"), (5,7,"#8B4513"), (5,8,"#8B4513"), (5,9,"#8B4513"), (5,10,"#8B4513"), (5,11,"#8B4513"), (5,12,"#FFFFFF"), (6,0,"#8B4513"), (6,1,"#8B4513"), (6,2,"#8B4513"), (6,3,"#8B4513"), (6,4,"#8B4513"), (6,5,"#8B4513"), (6,6,"#8B4513"), (6,7,"#8B4513"), (6,8,"#8B4513"), (6,9,"#8B4513"), (6,10,"#8B4513"), (6,11,"#FFFFFF"), (6,12,"#FFFFFF"), (7,1,"#8B4513"), (7,2,"#8B4513"), (7,3,"#8B4513"), (7,4,"#8B4513"), (7,5,"#8B4513"), (7,6,"#8B4513"), (7,7,"#8B4513"), (7,8,"#8B4513"), (7,9,"#8B4513"), (7,10,"#8B4513"), (7,11,"#8B4513")]
charPacmanStrawberry = [(0,6,"#FF0000"), (0,7,"#FF0000"), (0,8,"#FF0000"), (0,9,"#FF0000"), (1,5,"#FF0000"), (1,6,"#FF0000"), (1,7,"#FFFFFF"), (1,8,"#FF0000"), (1,9,"#FF0000"), (1,10,"#FF0000"), (1,11,"#FF0000"), (2,4,"#279627"), (2,5,"#FF0000"), (2,6,"#FF0000"), (2,7,"#FF0000"), (2,8,"#FF0000"), (2,9,"#FF0000"), (2,10,"#FFFFFF"), (2,11,"#FF0000"), (2,12,"#FF0000"), (3,4,"#279627"), (3,5,"#279627"), (3,6,"#FF0000"), (3,7,"#FF0000"), (3,8,"#FFFFFF"), (3,9,"#FF0000"), (3,10,"#FF0000"), (3,11,"#FF0000"), (3,12,"#FF0000"), (3,13,"#FF0000"), (4,4,"#279627"), (4,5,"#279627"), (4,6,"#FF0000"), (4,7,"#FF0000"), (4,8,"#FF0000"), (4,9,"#FF0000"), (4,10,"#FF0000"), (4,11,"#FF0000"), (4,12,"#FFFFFF"), (4,13,"#FF0000"), (5,3,"#FFFFFF"), (5,4,"#FFFFFF"), (5,5,"#279627"), (5,6,"#279627"), (5,7,"#FF0000"), (5,8,"#FFFFFF"), (5,9,"#FF0000"), (5,10,"#FFFFFF"), (5,11,"#FF0000"), (5,12,"#FF0000"), (5,13,"#FF0000"), (5,14,"#FF0000"), (6,4,"#279627"), (6,5,"#279627"), (6,6,"#FF0000"), (6,7,"#FF0000"), (6,8,"#FF0000"), (6,9,"#FF0000"), (6,10,"#FF0000"), (6,11,"#FF0000"), (6,12,"#FF0000"), (6,13,"#FF0000"), (7,4,"#279627"), (7,5,"#279627"), (7,6,"#FF0000"), (7,7,"#FFFFFF"), (7,8,"#FF0000"), (7,9,"#FF0000"), (7,10,"#FF0000"), (7,11,"#FF0000"), (7,12,"#FFFFFF"), (7,13,"#FF0000"), (8,4,"#279627"), (8,5,"#FF0000"), (8,6,"#FF0000"), (8,7,"#FF0000"), (8,8,"#FF0000"), (8,9,"#FFFFFF"), (8,10,"#FF0000"), (8,11,"#FF0000"), (9,5,"#FF0000"), (9,6,"#FFFFFF"), (9,7,"#FF0000"), (9,8,"#FF0000"), (9,9,"#FF0000"), (9,10,"#FF0000"), (9,11,"#FF0000"), (10,6,"#FF0000"), (10,7,"#FF0000"), (10,8,"#FF0000"), (10,9,"#FF0000")]
charChips = [(0,2,"#C19153"), (0,4,"#C19153"), (0,7,"#8B4513"), (1,3,"#C19153"), (1,4,"#C19153"), (1,5,"#C19153"), (1,6,"#FF5900"), (1,7,"#FF0000"), (1,8,"#FF0000"), (1,9,"#FF0000"), (1,10,"#8B4513"), (1,11,"#8B4513"), (2,1,"#C19153"), (2,2,"#C19153"), (2,5,"#C19153"), (2,6,"#C19153"), (2,7,"#FF0000"), (2,8,"#FF0000"), (2,9,"#FF0000"), (2,10,"#FF0000"), (2,11,"#FF0000"), (2,12,"#FF0000"), (2,13,"#FF0000"), (2,14,"#8B4513"), (2,15,"#8B4513"), (3,3,"#C19153"), (3,4,"#C19153"), (3,5,"#C19153"), (3,6,"#FF0000"), (3,7,"#FF0000"), (3,8,"#FF0000"), (3,9,"#FFFF00"), (3,10,"#FFFF00"), (3,11,"#FFFF00"), (3,12,"#FF0000"), (3,13,"#FF0000"), (3,14,"#FF0000"), (3,15,"#FF0000"), (4,0,"#C19153"), (4,1,"#C19153"), (4,2,"#FF5900"), (4,3,"#FF5900"), (4,4,"#FF5900"), (4,5,"#FF5900"), (4,6,"#FF0000"), (4,7,"#FF0000"), (4,8,"#FF0000"), (4,9,"#FF0000"), (4,10,"#FF0000"), (4,11,"#FF0000"), (4,12,"#FFFF00"), (4,13,"#FF0000"), (4,14,"#FF0000"), (4,15,"#FF0000"), (5,1,"#C19153"), (5,3,"#FF5900"), (5,4,"#C19153"), (5,5,"#C19153"), (5,6,"#FF0000"), (5,7,"#FF0000"), (5,8,"#FF0000"), (5,9,"#FFFF00"), (5,10,"#FFFF00"), (5,11,"#FFFF00"), (5,12,"#FF0000"), (5,13,"#FF0000"), (5,14,"#FF0000"), (5,15,"#FF0000"), (6,2,"#C19153"), (6,3,"#C19153"), (6,5,"#FF5900"), (6,6,"#FF0000"), (6,7,"#FF0000"), (6,8,"#FF0000"), (6,9,"#FF0000"), (6,10,"#FF0000"), (6,11,"#FF0000"), (6,12,"#FFFF00"), (6,13,"#FF0000"), (6,14,"#FF0000"), (6,15,"#FF0000"), (7,0,"#C19153"), (7,1,"#C19153"), (7,4,"#C19153"), (7,5,"#C19153"), (7,6,"#FF0000"), (7,7,"#FF0000"), (7,8,"#FF0000"), (7,9,"#FFFF00"), (7,10,"#FFFF00"), (7,11,"#FFFF00"), (7,12,"#FF0000"), (7,13,"#FF0000"), (7,14,"#FF0000"), (7,15,"#FF0000"), (8,2,"#C19153"), (8,3,"#C19153"), (8,5,"#C19153"), (8,6,"#FF5900"), (8,7,"#FF0000"), (8,8,"#FF0000"), (8,9,"#FF0000"), (8,10,"#FF0000"), (8,11,"#FF0000"), (8,12,"#FF0000"), (8,13,"#FF0000"), (8,14,"#8B4513"), (8,15,"#8B4513"), (9,1,"#C19153"), (9,3,"#C19153"), (9,4,"#C19153"), (9,6,"#C19153"), (9,7,"#FF0000"), (9,8,"#FF0000"), (9,9,"#FF0000"), (9,10,"#8B4513"), (9,11,"#8B4513"), (10,2,"#C19153"), (10,6,"#C19153"), (10,7,"#8B4513"), (11,4,"#C19153"), (11,5,"#C19153")]
charIceCream = [(0,1,"#8B4513"), (0,2,"#8B4513"), (0,3,"#00FFFF"), (0,6,"#BE1CBE"), (0,7,"#BE1CBE"), (0,9,"#C19153"), (1,0,"#8B4513"), (1,1,"#8B4513"), (1,2,"#279627"), (1,3,"#00FFFF"), (1,4,"#00FFFF"), (1,5,"#BE1CBE"), (1,6,"#BE1CBE"), (1,7,"#BE1CBE"), (1,8,"#BE1CBE"), (1,9,"#FF5900"), (1,10,"#C19153"), (1,11,"#C19153"), (2,0,"#8B4513"), (2,1,"#FFFFFF"), (2,2,"#8B4513"), (2,3,"#8B4513"), (2,4,"#00FFFF"), (2,5,"#BE1CBE"), (2,6,"#FFFFFF"), (2,7,"#BE1CBE"), (2,8,"#BE1CBE"), (2,9,"#BE1CBE"), (2,10,"#C19153"), (2,11,"#C19153"), (2,12,"#C19153"), (2,13,"#C19153"), (3,0,"#279627"), (3,1,"#8B4513"), (3,2,"#8B4513"), (3,3,"#00FFFF"), (3,4,"#00FFFF"), (3,5,"#BE1CBE"), (3,6,"#BE1CBE"), (3,7,"#BE1CBE"), (3,8,"#BE1CBE"), (3,9,"#C19153"), (3,10,"#FF5900"), (3,11,"#C19153"), (3,12,"#FF5900"), (3,13,"#C19153"), (3,14,"#C19153"), (3,15,"#C19153"), (4,0,"#8B4513"), (4,1,"#8B4513"), (4,2,"#8B4513"), (4,3,"#00FFFF"), (4,4,"#00FFFF"), (4,5,"#BE1CBE"), (4,6,"#BE1CBE"), (4,7,"#BE1CBE"), (4,8,"#BE1CBE"), (4,9,"#C19153"), (4,10,"#C19153"), (4,11,"#FF5900"), (4,12,"#FF5900"), (4,13,"#C19153"), (4,14,"#C19153"), (4,15,"#C19153"), (5,0,"#8B4513"), (5,1,"#FFFF00"), (5,2,"#8B4513"), (5,3,"#00FFFF"), (5,4,"#00FFFF"), (5,5,"#BE1CBE"), (5,6,"#BE1CBE"), (5,7,"#BE1CBE"), (5,8,"#BE1CBE"), (5,9,"#C19153"), (5,10,"#C19153"), (5,11,"#C19153"), (5,12,"#C19153"), (5,13,"#FF5900"), (5,14,"#C19153"), (5,15,"#C19153"), (6,0,"#8B4513"), (6,1,"#8B4513"), (6,2,"#8B4513"), (6,3,"#8B4513"), (6,4,"#00FFFF"), (6,5,"#BE1CBE"), (6,6,"#BE1CBE"), (6,7,"#BE1CBE"), (6,8,"#BE1CBE"), (6,9,"#BE1CBE"), (6,10,"#C19153"), (6,11,"#FF5900"), (6,12,"#FF5900"), (6,13,"#C19153"), (7,1,"#8B4513"), (7,2,"#FFFF00"), (7,3,"#00FFFF"), (7,4,"#00FFFF"), (7,5,"#BE1CBE"), (7,6,"#BE1CBE"), (7,7,"#BE1CBE"), (7,8,"#BE1CBE"), (7,9,"#C19153"), (7,10,"#FF5900"), (7,11,"#C19153"), (8,6,"#BE1CBE"), (8,7,"#BE1CBE"), (8,9,"#C19153")]
charPacmanCherry = [(0,7,"#FF0000"), (0,8,"#FF0000"), (0,9,"#FF0000"), (0,10,"#FF0000"), (1,6,"#FF0000"), (1,7,"#FF0000"), (1,8,"#FF0000"), (1,9,"#FFFFFF"), (1,10,"#FF0000"), (1,11,"#FF0000"), (2,6,"#FF0000"), (2,7,"#FF0000"), (2,8,"#FF0000"), (2,9,"#FF0000"), (2,10,"#FFFFFF"), (2,11,"#FF0000"), (3,6,"#FF0000"), (3,7,"#8B4513"), (3,8,"#FF0000"), (3,9,"#FF0000"), (3,10,"#FF0000"), (3,11,"#FF0000"), (4,6,"#8B4513"), (4,7,"#FF0000"), (4,8,"#FF0000"), (5,5,"#8B4513"), (5,7,"#FF0000"), (5,9,"#FF0000"), (5,10,"#FF0000"), (5,11,"#FF0000"), (5,12,"#FF0000"), (6,4,"#8B4513"), (6,8,"#FF0000"), (6,9,"#FF0000"), (6,10,"#FF0000"), (6,11,"#FFFFFF"), (6,12,"#FF0000"), (6,13,"#FF0000"), (7,4,"#8B4513"), (7,7,"#8B4513"), (7,8,"#8B4513"), (7,9,"#8B4513"), (7,10,"#FF0000"), (7,11,"#FF0000"), (7,12,"#FFFFFF"), (7,13,"#FF0000"), (8,3,"#8B4513"), (8,6,"#8B4513"), (8,8,"#FF0000"), (8,9,"#FF0000"), (8,10,"#FF0000"), (8,11,"#FF0000"), (8,12,"#FF0000"), (8,13,"#FF0000"), (9,3,"#8B4513"), (9,4,"#8B4513"), (9,5,"#8B4513"), (9,8,"#FF0000"), (9,9,"#FF0000"), (9,10,"#FF0000"), (9,11,"#FF0000"), (9,12,"#FF0000"), (9,13,"#FF0000"), (10,2,"#8B4513"), (10,3,"#8B4513"), (10,9,"#FF0000"), (10,10,"#FF0000"), (10,11,"#FF0000"), (10,12,"#FF0000"), (11,2,"#8B4513"), (11,3,"#8B4513")]
charOrange = [(1,6,"#FFA07A"), (1,7,"#FFA07A"), (1,8,"#FFA07A"), (1,9,"#FFA07A"), (1,10,"#FFA07A"), (1,11,"#FFA07A"), (2,4,"#FFA07A"), (2,5,"#FFA07A"), (2,6,"#FFA07A"), (2,7,"#FFA07A"), (2,8,"#FF5900"), (2,9,"#FF5900"), (2,10,"#FF5900"), (2,11,"#FF5900"), (2,12,"#FF5900"), (2,13,"#FF5900"), (3,3,"#FFA07A"), (3,4,"#FFA07A"), (3,5,"#FFA07A"), (3,6,"#FFFFFF"), (3,7,"#FFFFFF"), (3,8,"#FFA07A"), (3,9,"#FF5900"), (3,10,"#FF5900"), (3,11,"#FF5900"), (3,12,"#FF5900"), (3,13,"#FF5900"), (3,14,"#FF5900"), (4,3,"#FFA07A"), (4,4,"#FFA07A"), (4,5,"#FFA07A"), (4,6,"#FFFFFF"), (4,7,"#FFFFFF"), (4,8,"#FFA07A"), (4,9,"#FF5900"), (4,10,"#FF5900"), (4,11,"#FF5900"), (4,12,"#FF5900"), (4,13,"#FF5900"), (4,14,"#FF5900"), (5,2,"#FF5900"), (5,3,"#FFA07A"), (5,4,"#FF5900"), (5,5,"#FF5900"), (5,6,"#FFA07A"), (5,7,"#FFA07A"), (5,8,"#FFA07A"), (5,9,"#FF5900"), (5,10,"#FF5900"), (5,11,"#FF5900"), (5,12,"#FF5900"), (5,13,"#FF5900"), (5,14,"#FF5900"), (5,15,"#FF5900"), (6,2,"#FF5900"), (6,3,"#FF5900"), (6,4,"#279627"), (6,5,"#FF5900"), (6,6,"#FFA07A"), (6,7,"#FFA07A"), (6,8,"#FF5900"), (6,9,"#FF5900"), (6,10,"#FF5900"), (6,11,"#FF5900"), (6,12,"#FF5900"), (6,13,"#FF5900"), (6,14,"#FF5900"), (6,15,"#FF5900"), (7,3,"#279627"), (7,4,"#90EE90"), (7,5,"#FF5900"), (7,6,"#FFA07A"), (7,7,"#FFA07A"), (7,8,"#FF5900"), (7,9,"#FF5900"), (7,10,"#FF5900"), (7,11,"#FF5900"), (7,12,"#FF5900"), (7,13,"#FF5900"), (7,14,"#FF5900"), (7,15,"#FF5900"), (8,1,"#90EE90"), (8,2,"#90EE90"), (8,3,"#FF5900"), (8,4,"#279627"), (8,5,"#FF5900"), (8,6,"#FFA07A"), (8,7,"#FFA07A"), (8,8,"#FFA07A"), (8,9,"#FF5900"), (8,10,"#FF5900"), (8,11,"#FF5900"), (8,12,"#FF5900"), (8,13,"#FF5900"), (8,14,"#FF5900"), (8,15,"#FF5900"), (9,0,"#90EE90"), (9,1,"#90EE90"), (9,2,"#FF5900"), (9,3,"#FF5900"), (9,4,"#FF5900"), (9,5,"#FF5900"), (9,6,"#FFA07A"), (9,7,"#FFA07A"), (9,8,"#FFA07A"), (9,9,"#FF5900"), (9,10,"#FF5900"), (9,11,"#FF5900"), (9,12,"#FF5900"), (9,13,"#FF5900"), (9,14,"#FF5900"), (9,15,"#FF5900"), (10,0,"#90EE90"), (10,1,"#90EE90"), (10,3,"#FF5900"), (10,4,"#FF5900"), (10,5,"#FFA07A"), (10,6,"#FFA07A"), (10,7,"#FFA07A"), (10,8,"#FF5900"), (10,9,"#FF5900"), (10,10,"#FF5900"), (10,11,"#FF5900"), (10,12,"#FF5900"), (10,13,"#FF5900"), (10,14,"#FF5900"), (10,15,"#FF5900"), (11,0,"#90EE90"), (11,1,"#279627"), (11,3,"#FF5900"), (11,4,"#FF5900"), (11,5,"#FFA07A"), (11,6,"#FFA07A"), (11,7,"#FFA07A"), (11,8,"#FF5900"), (11,9,"#FF5900"), (11,10,"#FF5900"), (11,11,"#FF5900"), (11,12,"#FF5900"), (11,13,"#FF5900"), (11,14,"#FF5900"), (12,0,"#90EE90"), (12,4,"#FF5900"), (12,5,"#FF5900"), (12,6,"#FF5900"), (12,7,"#FF5900"), (12,8,"#FF5900"), (12,9,"#FF5900"), (12,10,"#FF5900"), (12,11,"#FF5900"), (12,12,"#FF5900"), (12,13,"#FF5900"), (12,14,"#FF5900"), (13,5,"#FF5900"), (13,6,"#FF5900"), (13,7,"#FF5900"), (13,8,"#FF5900"), (13,9,"#FF5900"), (13,10,"#FF5900"), (13,11,"#FF5900"), (13,12,"#FF5900"), (13,13,"#FF5900"), (14,7,"#FF5900"), (14,8,"#FF5900"), (14,9,"#FF5900"), (14,10,"#FF5900"), (14,11,"#FF5900")]


charWall2 = [(0,2,"#FFFFFF"), (0,3,"#FFFFFF"), (0,4,"#FFFFFF"), (0,5,"#FFFFFF"), (0,6,"#FFFFFF"), (0,7,"#FFFFFF"), (0,8,"#FFFFFF"), (0,9,"#FFFFFF"), (0,10,"#FFFFFF"), (0,11,"#FFFFFF"), (0,12,"#FFFFFF"), (0,13,"#FFFFFF"), (0,14,"#FFFFFF"), (1,1,"#FFFFFF"), (1,2,"#B5B3F5"), (1,3,"#B5B3F5"), (1,4,"#B5B3F5"), (1,5,"#B5B3F5"), (1,6,"#B5B3F5"), (1,7,"#B5B3F5"), (1,8,"#B5B3F5"), (1,9,"#B5B3F5"), (1,10,"#B5B3F5"), (1,11,"#B5B3F5"), (1,12,"#B5B3F5"), (1,13,"#B5B3F5"), (1,14,"#B5B3F5"), (1,15,"#FFFFFF"), (2,0,"#FFFFFF"), (2,1,"#B5B3F5"), (2,2,"#B5B3F5"), (2,3,"#B5B3F5"), (2,4,"#B5B3F5"), (2,5,"#B5B3F5"), (2,6,"#B5B3F5"), (2,7,"#B5B3F5"), (2,8,"#B5B3F5"), (2,9,"#B5B3F5"), (2,10,"#B5B3F5"), (2,11,"#B5B3F5"), (2,12,"#B5B3F5"), (2,13,"#B5B3F5"), (2,14,"#B5B3F5"), (2,15,"#B5B3F5"), (2,16,"#FFFFFF"), (3,0,"#FFFFFF"), (3,1,"#B5B3F5"), (3,2,"#B5B3F5"), (3,3,"#B5B3F5"), (3,4,"#B5B3F5"), (3,5,"#B5B3F5"), (3,6,"#B5B3F5"), (3,7,"#B5B3F5"), (3,8,"#B5B3F5"), (3,9,"#B5B3F5"), (3,10,"#B5B3F5"), (3,11,"#B5B3F5"), (3,12,"#B5B3F5"), (3,13,"#B5B3F5"), (3,14,"#B5B3F5"), (3,15,"#B5B3F5"), (3,16,"#FFFFFF"), (4,0,"#FFFFFF"), (4,1,"#B5B3F5"), (4,2,"#B5B3F5"), (4,3,"#B5B3F5"), (4,4,"#B5B3F5"), (4,5,"#B5B3F5"), (4,6,"#B5B3F5"), (4,7,"#B5B3F5"), (4,8,"#B5B3F5"), (4,9,"#B5B3F5"), (4,10,"#B5B3F5"), (4,11,"#B5B3F5"), (4,12,"#B5B3F5"), (4,13,"#B5B3F5"), (4,14,"#B5B3F5"), (4,15,"#B5B3F5"), (4,16,"#FFFFFF"), (5,0,"#FFFFFF"), (5,1,"#B5B3F5"), (5,2,"#B5B3F5"), (5,3,"#B5B3F5"), (5,4,"#B5B3F5"), (5,5,"#B5B3F5"), (5,6,"#B5B3F5"), (5,7,"#B5B3F5"), (5,8,"#B5B3F5"), (5,9,"#B5B3F5"), (5,10,"#B5B3F5"), (5,11,"#B5B3F5"), (5,12,"#B5B3F5"), (5,13,"#B5B3F5"), (5,14,"#B5B3F5"), (5,15,"#B5B3F5"), (5,16,"#FFFFFF"), (6,0,"#FFFFFF"), (6,1,"#B5B3F5"), (6,2,"#B5B3F5"), (6,3,"#B5B3F5"), (6,4,"#B5B3F5"), (6,5,"#B5B3F5"), (6,6,"#B5B3F5"), (6,7,"#B5B3F5"), (6,8,"#B5B3F5"), (6,9,"#B5B3F5"), (6,10,"#B5B3F5"), (6,11,"#B5B3F5"), (6,12,"#B5B3F5"), (6,13,"#B5B3F5"), (6,14,"#B5B3F5"), (6,15,"#B5B3F5"), (6,16,"#FFFFFF"), (7,0,"#FFFFFF"), (7,1,"#B5B3F5"), (7,2,"#B5B3F5"), (7,3,"#B5B3F5"), (7,4,"#B5B3F5"), (7,5,"#B5B3F5"), (7,6,"#B5B3F5"), (7,7,"#B5B3F5"), (7,8,"#B5B3F5"), (7,9,"#B5B3F5"), (7,10,"#B5B3F5"), (7,11,"#B5B3F5"), (7,12,"#B5B3F5"), (7,13,"#B5B3F5"), (7,14,"#B5B3F5"), (7,15,"#B5B3F5"), (7,16,"#FFFFFF"), (8,0,"#FFFFFF"), (8,1,"#B5B3F5"), (8,2,"#B5B3F5"), (8,3,"#B5B3F5"), (8,4,"#B5B3F5"), (8,5,"#B5B3F5"), (8,6,"#B5B3F5"), (8,7,"#B5B3F5"), (8,8,"#B5B3F5"), (8,9,"#B5B3F5"), (8,10,"#B5B3F5"), (8,11,"#B5B3F5"), (8,12,"#B5B3F5"), (8,13,"#B5B3F5"), (8,14,"#B5B3F5"), (8,15,"#B5B3F5"), (8,16,"#FFFFFF"), (9,0,"#FFFFFF"), (9,1,"#B5B3F5"), (9,2,"#B5B3F5"), (9,3,"#B5B3F5"), (9,4,"#B5B3F5"), (9,5,"#B5B3F5"), (9,6,"#B5B3F5"), (9,7,"#B5B3F5"), (9,8,"#B5B3F5"), (9,9,"#B5B3F5"), (9,10,"#B5B3F5"), (9,11,"#B5B3F5"), (9,12,"#B5B3F5"), (9,13,"#B5B3F5"), (9,14,"#B5B3F5"), (9,15,"#B5B3F5"), (9,16,"#FFFFFF"), (10,0,"#FFFFFF"), (10,1,"#B5B3F5"), (10,2,"#B5B3F5"), (10,3,"#B5B3F5"), (10,4,"#B5B3F5"), (10,5,"#B5B3F5"), (10,6,"#B5B3F5"), (10,7,"#B5B3F5"), (10,8,"#B5B3F5"), (10,9,"#B5B3F5"), (10,10,"#B5B3F5"), (10,11,"#B5B3F5"), (10,12,"#B5B3F5"), (10,13,"#B5B3F5"), (10,14,"#B5B3F5"), (10,15,"#B5B3F5"), (10,16,"#FFFFFF"), (11,0,"#FFFFFF"), (11,1,"#B5B3F5"), (11,2,"#B5B3F5"), (11,3,"#B5B3F5"), (11,4,"#B5B3F5"), (11,5,"#B5B3F5"), (11,6,"#B5B3F5"), (11,7,"#B5B3F5"), (11,8,"#B5B3F5"), (11,9,"#B5B3F5"), (11,10,"#B5B3F5"), (11,11,"#B5B3F5"), (11,12,"#B5B3F5"), (11,13,"#B5B3F5"), (11,14,"#B5B3F5"), (11,15,"#B5B3F5"), (11,16,"#FFFFFF"), (12,0,"#FFFFFF"), (12,1,"#B5B3F5"), (12,2,"#B5B3F5"), (12,3,"#B5B3F5"), (12,4,"#B5B3F5"), (12,5,"#B5B3F5"), (12,6,"#B5B3F5"), (12,7,"#B5B3F5"), (12,8,"#B5B3F5"), (12,9,"#B5B3F5"), (12,10,"#B5B3F5"), (12,11,"#B5B3F5"), (12,12,"#B5B3F5"), (12,13,"#B5B3F5"), (12,14,"#B5B3F5"), (12,15,"#B5B3F5"), (12,16,"#FFFFFF"), (13,0,"#FFFFFF"), (13,1,"#B5B3F5"), (13,2,"#B5B3F5"), (13,3,"#B5B3F5"), (13,4,"#B5B3F5"), (13,5,"#B5B3F5"), (13,6,"#B5B3F5"), (13,7,"#B5B3F5"), (13,8,"#B5B3F5"), (13,9,"#B5B3F5"), (13,10,"#B5B3F5"), (13,11,"#B5B3F5"), (13,12,"#B5B3F5"), (13,13,"#B5B3F5"), (13,14,"#B5B3F5"), (13,15,"#B5B3F5"), (13,16,"#FFFFFF"), (14,1,"#FFFFFF"), (14,2,"#B5B3F5"), (14,3,"#B5B3F5"), (14,4,"#B5B3F5"), (14,5,"#B5B3F5"), (14,6,"#B5B3F5"), (14,7,"#B5B3F5"), (14,8,"#B5B3F5"), (14,9,"#B5B3F5"), (14,10,"#B5B3F5"), (14,11,"#B5B3F5"), (14,12,"#B5B3F5"), (14,13,"#B5B3F5"), (14,14,"#B5B3F5"), (14,15,"#FFFFFF"), (15,2,"#FFFFFF"), (15,3,"#FFFFFF"), (15,4,"#FFFFFF"), (15,5,"#FFFFFF"), (15,6,"#FFFFFF"), (15,7,"#FFFFFF"), (15,8,"#FFFFFF"), (15,9,"#FFFFFF"), (15,10,"#FFFFFF"), (15,11,"#FFFFFF"), (15,12,"#FFFFFF"), (15,13,"#FFFFFF"), (15,14,"#FFFFFF")]


wallsize = 30  # put blocks in grid from (0,0) to (22,12)

# do not change these o/w leveleditor will not work correctly
popiscletype  = 1
strawberrytype = 2
chipstype = 3
icecreamtype = 4
strawberrytype = 5
cherrytype = 6
orangetype = 7
 # put blocks in grid from (0,0) to (22,12)

MAXx = 1000
MAXy = 400

class LEDobj:
    def __init__(self, canvas,x=0,y=0,dx=0,dy=0, CharPoints = [], pixelsize = 2, typestring = "unknown"):
         self.x = x
         self.y = y
         self.dx = dx
         self.dy = dy
         self.canvas = canvas
         self.typestring = typestring
         self.typenumber = 0
         self.LEDPoints = []
         self.OriginalCharPoints = CharPoints
         self.CharPoints = CharPoints.copy()
         self.PointsType = 0
         self.collisionrect = (0,0,0,0)  # top left to bottom right
         self.collisionimage = 0
         self.collisionrectshow = False
         self.pixelsize = pixelsize
         LEDlib.psize = self.pixelsize
         LEDlib.createCharColourSolid(canvas,x,y,CharPoints,self.LEDPoints)
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


mainwin = Tk()
mainwin.geometry(str(MAXx)+"x"+str(MAXy+200)) 
canvas1 = Canvas(mainwin,width=MAXx,height= MAXy+200,bg="black")
canvas1.place(x=0,y=0)

fruitlist = []
solidlist = []

def findobj(x,y):
    for f in fruitlist:
        if f.x == x*wallsize and f.y == y*wallsize:
            return f
    for w in solidlist:
        if w.x == x*wallsize and w.y == y*wallsize:
            return w
    return 0

def showclick(event):
    x,y = event.x//wallsize, event.y//wallsize
    mychar = charWall2
    typenumber = 0
    if selected_type.get() == "Wall":
        mychar = charWall2
    if selected_type.get() == "Chips":
        mychar = charChips
        typenumber = chipstype
    if selected_type.get() == "Icecream":
        mychar = charIceCream
        typenumber = icecreamtype
    if selected_type.get() == "Popiscle":
        mychar = charPopsicle 
        typenumber = popiscletype
    if selected_type.get() == "Strawberry":
        mychar = charPacmanStrawberry 
        typenumber = strawberrytype
    if selected_type.get() == "Cherry":
        mychar = charPacmanCherry 
        typenumber = cherrytype
    if selected_type.get() == "Orange":
        mychar = charOrange 
        typenumber = orangetype
    if selected_type.get() == "Erase Mode":
        myobj = findobj(x,y) 
        if myobj != 0:
            if myobj.typestring == "wall":
                solidlist.remove(myobj)
            else:
                fruitlist.remove(myobj)
            myobj.undraw()
        return
    if selected_type.get() == "Wall":
      wall = LEDobj(canvas1,x*wallsize,y*wallsize,dx = 0,dy = 0,CharPoints=mychar, pixelsize = 2,typestring = "wall")
      solidlist.append(wall)
    else:
      fruit = LEDobj(canvas1,x*wallsize,y*wallsize,dx = 0,dy = 0,CharPoints=mychar, pixelsize = 2,typestring = "fruit")
      fruit.typenumber = typenumber
      fruitlist.append(fruit) 
   
selected_type = StringVar(value="Wall")

def set_object_type(obj_type):
    selected_type.set(obj_type)
    print("selected: ", selected_type.get() )

button_frame = Frame(mainwin)
button_frame.pack(side="bottom",pady=5)

for obj in ["Wall", "Chips", "Icecream", "Popiscle","Strawberry","Cherry","Orange","Erase Mode"]:
    btn = Button(button_frame, text=obj, width=10,
                    command=lambda o=obj: set_object_type(o))
    btn.pack(side="left", padx=5)


for x in range(0, MAXx, wallsize):
    canvas1.create_line(x, 0, x, MAXy, fill="white")

for y in range(0, MAXy, wallsize):
    canvas1.create_line(0, y, MAXx, y, fill="white")

def CopyWallData():
    print("Copied wall data to clipboard")
    wallstring  = "walls = {"
    for i,w in enumerate(solidlist):
        wallstring = wallstring + "("+str(w.x//wallsize)+","+str(w.y//wallsize)+")"
        if i != len(solidlist)-1:
            wallstring += ","
    wallstring += "}"
    textOutput.delete('1.0','end')
    textOutput.insert(INSERT,wallstring)
    textOutput.tag_add('sel','1.0','end')
    selected_text = textOutput.get(SEL_FIRST, SEL_LAST)
    mainwin.clipboard_clear()
    mainwin.clipboard_append(selected_text)

btnCopyWallData = Button(mainwin,text="Copy wall data", command = CopyWallData)
btnCopyWallData.place(x=20,y=500)

def CopyFruitData():
    print("Copied fruit data to clipboard")
    fruitstring  = "pointsset = {"
    for i,f in enumerate(fruitlist):
        fruitstring += "("+str(f.x//wallsize)+","+str(f.y//wallsize)+","+str(f.typenumber)+")"
        if i != len(fruitlist)-1:
            fruitstring += ","
    fruitstring += "}"
    textOutput.delete('1.0','end')
    textOutput.insert(INSERT,fruitstring)
    textOutput.tag_add('sel','1.0','end')
    selected_text = textOutput.get(SEL_FIRST, SEL_LAST)
    mainwin.clipboard_clear()
    mainwin.clipboard_append(selected_text)

btnCopyFruitData = Button(mainwin,text="Copy fruit data", command = CopyFruitData)
btnCopyFruitData.place(x=180,y=500)

textOutput = Text(mainwin,width=50,height=6,bg="black",fg="orange")
textOutput.place(x=10,y=410)

textInput = Text(mainwin,width=50,height=6,bg="black",fg="orange")
textInput.place(x=350,y=410)
textInput.insert(INSERT,"Paste Text Data Here")

def ReadFruitData():
    print("reading fruit from text data")
    count = 0
    coordinate_string = textInput.get("1.0", END)
    # Regular expression to extract pairs of numbers
    matches = re.findall(r'\((\d+),(\d+),(\d+)\)', coordinate_string)
    # Convert matches to a list of tuples
    coordinates = [(int(x),int(y),int(z)) for x,y,z in matches]
    for x,y,z in coordinates:
          typenumber = z
          if typenumber == popiscletype:
              mychar = charPopsicle
          if typenumber == strawberrytype:
              mychar = charPacmanStrawberry
          if typenumber == chipstype:
              mychar = charChips
          if typenumber == icecreamtype:
              mychar = charIceCream
          if typenumber == cherrytype:
              mychar = charPacmanCherry
          if typenumber == orangetype:
              mychar = charOrange
          fruit = LEDobj(canvas1,x*wallsize,y*wallsize,dx = 0,dy = 0,CharPoints=mychar, pixelsize = 2,typestring = "fruit")
          fruit.typenumber = typenumber
          fruitlist.append(fruit)
          count = count + 1
          print("reading ...", count)

def ReadWallData():
    print("reading walls from text data")
    count = 0
    coordinate_string = textInput.get("1.0", END)
    # Regular expression to extract pairs of numbers
    matches = re.findall(r'\((\d+),(\d+)\)', coordinate_string)
    # Convert matches to a list of tuples
    coordinates = [(int(x),int(y)) for x,y in matches]
    for x,y in coordinates:
          mychar = charWall2
          wall = LEDobj(canvas1,x*wallsize,y*wallsize,dx = 0,dy = 0,CharPoints=mychar, pixelsize = 2,typestring = "wall")
          solidlist.append(wall)
          count = count + 1
          print("reading ...", count)

btnReadFruitData = Button(mainwin,text="Read fruit data", command = ReadFruitData)
btnReadFruitData.place(x=520,y=500)

btnReadWallData = Button(mainwin,text="Read wall data", command = ReadWallData)
btnReadWallData.place(x=360,y=500)

canvas1.bind("<Button-1>", showclick)

mainwin.mainloop()