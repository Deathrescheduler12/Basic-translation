from ..point import Point
point1 = Point((1, 1))
point2 = Point((1, 3))
point3 = Point((4, 2))
for z in [point1, point2, point3]:
    z.enlarge(np.array([1, 4]))
plt.plot([point1.coordinates[0], point2.coordinates[0], point3.coordinates[0]], [point1.coordinates[1], point2.coordinates[1], point3.coordinates[1]], "ro")
plt.axis([-2, 8, -2, 5])
plt.show()
