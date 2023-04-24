"""Задача 4
В первом ящике находится 10 мячей, из которых 7 - белые.
Во втором ящике - 11 мячей, из которых 9 белых. 
Из каждого ящика вытаскивают случайным образом по два мяча. Какова вероятность того, что все мячи белые? 
Какова вероятность того, что ровно два мяча белые? Какова вероятность того, что хотя бы один мяч белый?
"""

# Вероятность того, что все мячи белые
p1 = 7/10 * 6/9 * 9/11 * 8/10
print("Вероятность того, что все мячи белые:", round(p1, 4))

# Вероятность того, что ровно два мяча белые
p2 = (7/10 * 6/9 * 2/11 * 1/10) + (3/10 * 2/9 * 9/11 * 8/10) + (7/10 * 3/9 * 9/11 * 2/10) + (3/10 * 7/9 * 2/11 * 9/10)
print("Вероятность того, что ровно два мяча белые:", round(p2, 4))

# Вероятность того, что хотя бы один мяч белый
p3 = 1 - (3/10 * 2/9 * 2/11 * 1/10)
print("Вероятность того, что хотя бы один мяч белый:", round(p3, 4))
