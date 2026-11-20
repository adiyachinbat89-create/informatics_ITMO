import numpy as np


def method_1_areas(o, d, a, b, c):
    # Том үсэгтэй хувьсагчид руу шилжүүлэх
    O = o
    A = a
    B = b
    C = c

    AB = B - A
    AC = C - A
    n = np.cross(AB, AC)

    # Пересечение с плоскостью
    denom = np.dot(n, d)
    if abs(denom) < 1e-9:
        return "Луч параллелен плоскости или лежит в ней"

    t = np.dot(n, A - O) / denom
    if t < 0:
        return "Треугольник позади луча"

    Q = O + t * d

    # Площади
    S_ABC = 0.5 * np.linalg.norm(np.cross(AB, AC))
    S_QBC = 0.5 * np.linalg.norm(np.cross(B - Q, C - Q))
    S_AQC = 0.5 * np.linalg.norm(np.cross(A - Q, C - Q))
    S_ABQ = 0.5 * np.linalg.norm(np.cross(A - Q, B - Q))

    if abs((S_QBC + S_AQC + S_ABQ) - S_ABC) < 1e-7:
        return f"Внутри (или на границе). Q={Q}, t={t}"
    else:
        return f"Вне треугольника. Q={Q}, t={t}"


# Тест
O = np.array([1., 1., 5.])
d = np.array([0., 0., -1.])
A = np.array([0., 0., 0.])
B = np.array([4., 0., 0.])
C = np.array([0., 4., 0.])

print(method_1_areas(O, d, A, B, C))