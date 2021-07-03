import matplotlib.pyplot as plt
import numpy as np

#X軸:時刻
x = np.arrange(0,100,0.5)

# Y軸:Sin波
Hz = 5.
y = np.sin(2.0 * np.pi * (x * Hz)/100)

#グラフを描画
plt.plot (x, y)
plt.savefig ('test.png')
