import numpy as np
import matplotlib.pyplot as plt

# Time
t = np.linspace(-1, 1, 2000)

# Displacement
dis = 16 * np.tan(8 * t)

# Velocity
vel = 128 / ((np.cos(8 * t)) ** 2)

# Acceleration
acc = 2048 * np.tan(8 * t) / ((np.cos(8 * t))** 2)

dis[np.abs(dis) > 1000] = np.nan
vel[np.abs(vel) > 1000] = np.nan
acc[np.abs(acc) > 5000] = np.nan

plt.figure(figsize=(10, 10))

# Displacement
plt.subplot(3, 1, 1)
plt.plot(t, dis)
plt.title(r"$x(t)=16tan(8t)$")
plt.xlabel("Time")
plt.ylabel("Displacement")
plt.grid(True)

# Velocity
plt.subplot(3, 1, 2)
plt.plot(t, vel)
plt.title(r"$x'(t)=128sec^2(8t)$")
plt.xlabel("Time")
plt.ylabel("Velocity")
plt.grid(True)

# Acceleration
plt.subplot(3, 1, 3)
plt.plot(t, acc)
plt.title(r"$x''(t)=2048sec^2(8t)tan(8t)$")
plt.xlabel("Time")
plt.ylabel("Acceleration")
plt.grid(True)

plt.tight_layout()
plt.show()