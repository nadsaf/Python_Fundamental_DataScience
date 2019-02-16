import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('63.png')
lum_img = img[:, :, 0]
imgplot = plt.imshow(lum_img, cmap='Blues')

plt.colorbar()
plt.show()

# 'viridis', 'plasma', 'inferno', 'magma', 'cividis'
# 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
# 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
# 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'
# 'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
# 'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
# 'hot', 'afmhot', 'gist_heat', 'copper'
# 'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
# 'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic'
# 'twilight', 'twilight_shifted', 'hsv'
# 'Pastel1', 'Pastel2', 'Paired', 'Accent',
# 'Dark2', 'Set1', 'Set2', 'Set3',
# 'tab10', 'tab20', 'tab20b', 'tab20c'
# 'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
# 'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
# 'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar'