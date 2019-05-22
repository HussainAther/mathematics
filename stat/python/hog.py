import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
import skimage.data

from skimage import data, color, feature, transform
from sklearn.datasets import fetch_lfw_people

"""
Histogram of gradients (HOG) pipeline.
"""

image = color.rgb2gray(data.chelsea())
hog_vec, hog_vis = feature.hog(image, visualise=True)
fig, ax = plt.subplots(1, 2, figsize=(12, 6),
                       subplot_kw=dict(xticks=[], yticks=[]))
ax[0].imshow(image, cmap="gray")
ax[0].set_title('input image')
ax[1].imshow(hog_vis)
ax[1].set_title("visualization of HOG features")

faces = fetch_lfw_people()
positive_patches = faces.images
positive_patches.shape

imgs_to_use = ["camera", "text", "coins", "moon",
               "page", "clock", "immunohistochemistry",
               "chelsea", "coffee", "hubble_deep_field"]
images = [color.rgb2gray(getattr(data, name)())
          for name in imgs_to_use]
