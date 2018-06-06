from typing import Tuple

import numpy as np
import matplotlib.pyplot as plt
from numpy.core.multiarray import ndarray


lengthy = np.linspace(0, 18, 96)  # type: Tuple[ndarray, float]

plt.plot(lengthy)
plt.show()