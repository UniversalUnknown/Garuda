import numpy as np
import matplotlib.pyplot as plt

# Constants
wavelength = 1 # Wavelength of the light (in arbitrary units)
slit_distance =1 # Distance between the slits (in arbitrary units)
screen_distance = 0.1  # Distance from the slits to the screen (in arbitrary units)
num_points = 500  # Reduced number of points for faster computation

# Create an array of positions on the screen
x = np.linspace(-1, 1, num_points)

# Calculate the angle from the slits to the screen
theta = np.arctan(x / screen_distance)

# Calculate the path difference for each slit
# Precompute the sine values to avoid recalculating
sin_theta = np.sin(theta)
path_difference = slit_distance * sin_theta

# Calculate the intensity pattern using the interference formula
# Use numpy's vectorized operations for efficiency
intensity = np.cos(2 * np.pi * path_difference / wavelength) ** 2

# Normalize the intensity
intensity /= np.max(intensity)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(x, intensity, color='blue')
plt.title('Double-Slit Experiment Interference Pattern')
plt.xlabel('Position on Screen (arbitrary units)')
plt.ylabel('Normalized Intensity')
plt.grid()
plt.xlim(-5, 5)
plt.ylim(0, 1.1)
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.show()