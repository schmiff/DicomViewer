import numpy as np 
import nibabel as nib
import matplotlib.pyplot as plt
from private_path import sample_path

img = nib.load(sample_path)
array = img.get_fdata()
array = np.rot90(array)

plt.figure(figsize=(20,15))
plt.imshow(array[..., 50].astype(np.float32), cmap='bone')
plt.show()

