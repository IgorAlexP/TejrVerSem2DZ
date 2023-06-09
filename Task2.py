"""Задача 2
Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
В жилом комплексе после ремонта в один день включили 5000 новых лампочек. 
Какова вероятность, что ни одна из них не перегорит в первый день? Какова вероятность, что перегорят ровно две?"""

import math

n = 5000
k = 0
p = 0.0004

P = math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
print('Вероятность того, что ни одна лампочка не перегорит:', round(P, 4))
