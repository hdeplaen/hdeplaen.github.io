import rkm
from matplotlib import pyplot as plt

k = rkm.kernel.rbf(sample=range(10), sigma=3)

plt.imshow(k.K)
plt.colorbar()
plt.title("RBF with sigma " + str(k.sigma))