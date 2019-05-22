import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
import skimage.data

from skimage import data, color, feature

"""
Histogram of gradients pipeline.
"""

image = color.rgb2gray(data.chelsea())
hog_vec, hog_vis = feature.hog(image, visualise=True)
fig, ax = plt.subplots(1, 2, figsize=(12, 6),
                       subplot_kw=dict(xticks=[], yticks=[]))
ax[0].imshow(image, cmap="gray")
ax[0].set_title('input image')
ax[1].imshow(hog_vis)
ax[1].set_title("visualization of HOG features")
