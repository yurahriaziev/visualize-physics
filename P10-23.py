import matplotlib.pyplot as plt
import numpy as np

# Define angle for the slope in radians
angle_slope = np.radians(65)  # slope angle in degrees

# Define the parameters for drawing
slope_length = 10  # arbitrary slope length
x_slope = np.linspace(0, slope_length * np.cos(angle_slope), 100)
y_slope = x_slope * np.tan(angle_slope)

# Ball position at the start
ball_x, ball_y = x_slope[0], y_slope[0] + 1

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_slope, y_slope, color="brown", label="Slope (65°)")
plt.scatter(ball_x, ball_y, color="blue", s=100, label="Solid Ball (Start Point)")

# Draw the weight, friction, and normal force vectors
g_force_x = -np.sin(angle_slope)
g_force_y = -np.cos(angle_slope)

# Draw the gravity force arrow
plt.arrow(ball_x, ball_y, 0.5 * g_force_x, 0.5 * g_force_y, head_width=0.2, color="black", label="Gravity")

# Normal force vector (perpendicular to slope)
normal_force_x = -np.cos(angle_slope + np.pi / 2)
normal_force_y = np.sin(angle_slope + np.pi / 2)
plt.arrow(ball_x, ball_y, 0.5 * normal_force_x, 0.5 * normal_force_y, head_width=0.2, color="green", label="Normal Force")

# Frictional force vector (opposite to motion along slope)
friction_force_x = np.cos(angle_slope)
friction_force_y = np.sin(angle_slope)
plt.arrow(ball_x, ball_y, 0.3 * friction_force_x, 0.3 * friction_force_y, head_width=0.15, color="red", label="Friction")

# Labels and legend
plt.title("Forces Acting on a Solid Ball Sliding Down a 65° Slope")
plt.xlabel("Horizontal Distance")
plt.ylabel("Vertical Distance")
plt.legend(loc="upper left")
plt.grid(True)
plt.axis("equal")

plt.show()
