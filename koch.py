import matplotlib.pyplot as plt
import numpy as np

def koch_snowflake(order, scale=10):
    """
    Генерирует кривую Коха (снежинку) заданного порядка.
    Порядок 0 — просто отрезок.
    """
    def koch_curve(p1, p2, order):
        if order == 0:
            return [p1, p2]
        else:
            # Вычисляем три промежуточные точки
            p1 = np.array(p1)
            p2 = np.array(p2)
            v = p2 - p1
            # Точки на 1/3 и 2/3 отрезка
            pA = p1 + v / 3
            pB = p1 + 2 * v / 3
            # Вершина "пика" (поворот на 60 градусов)
            # Поворачиваем вектор v/3 на 60 градусов
            angle = np.pi / 3  # 60 градусов
            rotation = np.array([
                [np.cos(angle), -np.sin(angle)],
                [np.sin(angle), np.cos(angle)]
            ])
            pC = pA + np.dot(rotation, v / 3)

            # Рекурсивно строим четыре части кривой
            return (koch_curve(p1, pA, order - 1)[:-1] +
                    koch_curve(pA, pC, order - 1)[:-1] +
                    koch_curve(pC, pB, order - 1)[:-1] +
                    koch_curve(pB, p2, order - 1))
    # Для снежинки берём три стороны равностороннего треугольника
    # Вершины треугольника
    p1 = np.array([0.0, 0.0])
    p2 = np.array([scale, 0.0])
    p3 = np.array([scale / 2, scale * np.sqrt(3) / 2])

    # Строим три кривые Коха
    curve1 = koch_curve(p1, p2, order)
    curve2 = koch_curve(p2, p3, order)
    curve3 = koch_curve(p3, p1, order)

    # Объединяем точки для замкнутой снежинки
    # Убираем дублирующиеся точки на стыках
    points = curve1 + curve2[1:] + curve3[1:]
    return points

# Параметры
order = 2  # Порядок снежинки
scale = 10

# Генерация снежинки
points = koch_snowflake(order, scale)

# Разделяем координаты X и Y
x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]

# Рисуем
plt.figure(figsize=(8, 8))
plt.plot(x_coords, y_coords, 'b-', linewidth=1)
plt.axis('equal')
plt.axis('off')  # Убираем оси для красоты
plt.title(f'Снежинка Коха порядка {order}')
plt.show()