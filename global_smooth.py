import numpy as np
import skimage.io as sio
from skimage.filters import gaussian

def normalize(sal):
    sal -= sal.min()
    sal /= sal.max()

def global_smooth(smap, std=None):
    """
    Gaussian filter used for a global smoothing process proposed by our paper:
    "Revisiting Saliency Metrics: Farthest-Neighbor Area Under Curve".

    Parameters
    ----------
    smap: Array-like input saliency map.
    std: scalar or sequence of scalars, optional
    Standard deviation for Gaussian kernel, a quarter of the shortest side if not specified.

    Returns
    -------
    smoothed saliency map.
    """
    eps = 1e-6
    if std:
        h, w = smap.shape[:2]
        std = min(h/4, w/4)
    smoothed = gaussian(smap, std)
    smoothed = smap + (smoothed * eps)
    normalize(smoothed)
    return smoothed

def demo():
    smap_path = "d54.jpg"
    smap = sio.imread(smap_path) / 255.

    print ("Number of total pixels", smap.size, "Number of unique values", len(np.unique(smap)))

    smoothed = global_smooth(smap)
    print ("After global smoothing.", "Number of unique values", len(np.unique(smoothed)))


if __name__ == "__main__" : demo()
