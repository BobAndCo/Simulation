import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

import Particle as p

particle1 = p.Particle(1, 1, 1, 0, 0)
particle2 = p.Particle(10, 0, 0, 0, 0)

print(particle1.angleTo(particle2))

plt.plot(particle1.x, particle1.y, 'ro')
plt.plot(particle2.x, particle2.y, 'go')

plt.show()