import numpy as np
import matplotlib.pyplot as plt

# Time
t = np.linspace(0,100, 2000)

# Time period

T = np.pi/4

#Frequency

f = 1/T

# Displacement

#-2sin(8t)
dis = -2 * np.sin(8 * t)

# Velocity
vel = -16 * (np.cos(8 * t))

# Acceleration
acc = 128 *(np.sin(8 * t))

dis[np.abs(dis) > 1000] = np.nan
vel[np.abs(vel) > 1000] = np.nan
acc[np.abs(acc) > 5000] = np.nan

plt.figure(figsize=(10, 10))

# Displacement
plt.subplot(3, 1, 1)
plt.plot(t, dis)
plt.title(r"$x(t)= -2sin(8t)$")
plt.xlabel("Time")
plt.ylabel("Displacement")
plt.grid(True)

# Velocity
plt.subplot(3, 1, 2)
plt.plot(t, vel)
plt.title(r"$x'(t)= -16cos(8t)$")
plt.xlabel("Time")
plt.ylabel("Velocity")
plt.grid(True)

# Acceleration
plt.subplot(3, 1, 3)
plt.plot(t, acc)
plt.title(r"$x''(t)= 128sin(8t)$")
plt.xlabel("Time")
plt.ylabel("Acceleration")
plt.grid(True)

plt.tight_layout()
plt.show()