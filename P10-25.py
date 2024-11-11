import matplotlib.pyplot as plt
import numpy as np

# Wheel properties
radius = 0.6  # radius in meters
initial_rotation_speed = 25.0  # angular velocity in rad/s
work_done_by_friction = 2600  # work in joules
weight = 392  # weight in Newtons
mass = weight / 9.81  # mass in kg using g = 9.81 m/s^2

# Plot setup
fig, ax = plt.subplots(figsize=(10, 6))

# Draw the hill
hill_x = np.linspace(0, 3, 100)
hill_y = 1.5 * hill_x  # arbitrary slope of the hill
ax.plot(hill_x, hill_y, color="brown", linestyle="--", linewidth=1.5, label="Hill")

# Initial and final positions of the wheel
wheel_bottom_x, wheel_bottom_y = 0.5, 0.5  # start of the hill
wheel_top_x, wheel_top_y = 2, 3  # end position on hill
ax.plot([wheel_bottom_x, wheel_top_x], [wheel_bottom_y, wheel_top_y], "ko")  # mark start and end positions

# Draw the wheel as a circle at the start and end positions
wheel_circle = plt.Circle((wheel_bottom_x, wheel_bottom_y), radius=0.2, color="blue", fill=False, linewidth=2, label="Wheel")
ax.add_patch(wheel_circle)

# Indicate height h
height_line_x = [wheel_top_x, wheel_top_x]
height_line_y = [0, wheel_top_y]
ax.plot(height_line_x, height_line_y, color="purple", linestyle=":", linewidth=1.5, label="Height h")

# Annotate details
ax.annotate("Initial rotation\n25 rad/s", (wheel_bottom_x, wheel_bottom_y - 0.3), color="black", ha="center")
ax.annotate("Work done by friction = 2600 J", (1.5, 2.2), color="red", ha="center", fontsize=10, arrowprops=dict(arrowstyle="->", color="red"))
ax.annotate("Weight = 392 N", (wheel_bottom_x - 0.2, wheel_bottom_y + 0.6), color="black")
ax.annotate("Height h", (wheel_top_x + 0.2, wheel_top_y / 2), color="purple", fontsize=10)

# Labels and plot settings
ax.set_xlim(0, 3)
ax.set_ylim(0, 4)
ax.set_aspect('equal', adjustable='box')
plt.title("Visualization of Wheel Rolling Up Hill")
plt.xlabel("Horizontal Position")
plt.ylabel("Vertical Position")
plt.legend(loc="upper left")
plt.grid(True)

plt.show()
