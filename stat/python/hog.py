import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
import skimage.data

from skimage import data, color, feature, transform
from sklearn.datasets import fetch_lfw_people
from sklearn.feature_extraction.image import PatchExtractor

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

def extract_patches(img, N, scale=1.0, patch_size=positive_patches[0].shape):
    """
    Extract patches from images.
    """
    extracted_patch_size = tuple((scale * np.array(patch_size)).astype(int))
    extractor = PatchExtractor(patch_size=extracted_patch_size,
                               max_patches=N, random_state=0)
    patches = extractor.transform(img[np.newaxis])
    if scale != 1:
        patches = np.array([transform.resize(patch, patch_size)
                            for patch in patches])
    return patches
negative_patches = np.vstack([extract_patches(im, 1000, scale)
                              for im in images for scale in [0.5, 1.0, 2.0]])
negative_patches.shape
