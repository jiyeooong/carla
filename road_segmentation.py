import os
import cv2
import numpy

for (path, dirs, files) in os.walk("./Downloads/R2D"):
    for filename in files:
        if "label" in str(path):
            print("%s/%s" % (path, filename))
            arr = cv2.imread(os.path.join(path, filename), cv2.COLOR_RGB2BGR)
            arr = arr.astype(numpy.uint8)
            arr = arr[:,:,2]
            classes = {
                0: [0, 0, 0],  # None
                1: [0, 0, 0],  # Buildings
                2: [0, 0, 0],  # Fences
                3: [0, 0, 0],  # Other
                4: [0, 0, 0],  # Pedestrians
                5: [0, 0, 0],  # Poles
                6:[128, 64, 128], # RoadLines
                7: [128, 64, 128],  # Roads
                8:[0, 0, 0],  # Sidewalks
                9:[0, 0, 0],  # Vegetation
                10: [0, 0, 0],  # Vehicles
                11: [0, 0, 0],  # Walls
                12: [0, 0, 0]  # TrafficSigns
            }
            result = numpy.zeros((arr.shape[0], arr.shape[1], 3))
            for key, value in classes.items():
                result[numpy.where(arr == key)] = value
            cv2.imwrite(os.path.join(path, filename), result)
