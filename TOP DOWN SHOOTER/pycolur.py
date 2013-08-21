#!/usr/bin/python
# Filename: pycolur.py

import pygame as pg
import random
import math
import sys
import os




colors = {
  "blue": (0, 0, 255),
  "red": (255, 0, 0),
  "green": (0, 255, 0),
  "fuchsia": (255, 0, 255),
  "yellow": (255, 255, 0),
  "purple": (128, 0, 128),
  "orange": (255, 128, 128),
  "sky": (100, 100, 208),
  "black": (0, 0, 0),
  "white": (255, 255, 255),
  "gred": (240, random.uniform(40, 80), random.uniform(40, 80)),
  "red": (255, 0, 0),
  "green": (0, 255, 0),
  "fuchsia": (255, 0, 255),
  "yellow": (255, 255, 0),
  "purple": (128, 0, 128),
  "orange": (255, 128, 128),
  "sky": (100, 100, 208),
  "black": (0, 0, 0),
  "white": (255, 255, 255),
  "gray": (128, 128, 128),
  "random": (random.uniform(0, 256), random.uniform(0, 256), random.uniform(0, 256))
}

version = '0.1'

