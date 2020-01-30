from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# "L" : B&W  "RGBA" : rgba  "CMYK" : cmyk
gbr = np.array(Image.open("yoda.jpg").convert("L"))
print(gbr)
# print(gbr.shape)
# plt.imshow(gbr, cmap="gray")
# plt.show()

img = Image.fromarray(gbr, "L")
# img.show()
img.save("1.jpg")