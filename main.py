import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = ["toji1.jpg", "toji2.jpg"]
target_size = (800, 600)  
images = []

for filename in filenames:
    img = Image.open(filename).resize(target_size)
    images.append(np.array(img))

iio.imwrite("toji.gif", images, duration=500, loop=0)