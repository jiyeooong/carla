import os
import cv2
import numpy

for (path, dirs, files) in os.walk("/home/sungheui/Downloads/R2D"):
    for filename in files:
        if "depth" in str(path) and "new" not in str(path):
            print("%s/%s" % (path, filename))
            arr = cv2.imread(os.path.join(path, filename), cv2.COLOR_RGB2BGR)
            arr = arr.astype(numpy.float32)
            normalized_depth = numpy.dot(arr[:, :, :3], [65536.0, 256.0, 1.0])
            normalized_depth /= 16777215.0  # (256.0 * 256.0 * 256.0 - 1.0)
            normalized_depth *= 1000
            cv2.imwrite(os.path.join(path, filename), normalized_depth)
