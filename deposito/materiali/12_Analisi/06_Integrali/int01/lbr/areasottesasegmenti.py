# 2017 --- Area sottesa a segmenti --- Daniele Zambelli
"""Area sottesa a sementi:
- paralleli all'asse x;
- lunghi 0.5;
- di ordinata rispettivamente: 5, 4, 6, 3, 7, 5
"""
delta_x = 0.5
ordinate = [5, 4, 6, 3, 7, 5]
area = 0
for y_i in ordinate:
    area += y_i * delta_x
print(area)

def areasottesa_segmenti(delta_x, ordinate):
    """Restituisce l'area sottesa a sementi:
- paralleli all'asse x;
- lunghi delta_x;
- con le ordinate contenute in ordinate."""
    result = 0
    for y_i in ordinate:
        result += y_i * delta_x
    return result
    
def areasottesa_segmenti(delta_x, ordinate):
    """Restituisce l'area sottesa a sementi:
- paralleli all'asse x;
- lunghi delta_x;
- con le ordinate contenute in ordinate."""
    return sum(y_i * delta_x for y_i in ordinate)

print(areasottesa_segmenti(delta_x=0.5, ordinate=[5, 4, 6, 3, 7, 5]))
