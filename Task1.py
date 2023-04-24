"""Задача 1
Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. 
Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз."""

import math

n = 100
k = 85
p = 0.8

P = math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
print('Вероятность того, что стрелок попадет в цель ровно 85 раз:', round(P, 4))
