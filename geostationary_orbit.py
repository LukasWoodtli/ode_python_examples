
import numpy as np
import math

G = 6.67e-11

m_E = 5.97e24

T = 24 * 3600


r = math.pow((G * m_E * T**2)/(4 * np.pi**2), 1/3)

r_km = r/1000.

print(r_km)
