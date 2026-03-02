from manim import *
import numpy as np


class PythagorasTreeNaked(Scene):
    def construct(self):
        # Заголовок
        title = Text("Склонившееся дерево Пифагора", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Параметры
        max_order = 10  # Глубина рекурсии
        angle = 45 * DEGREES  # Угол наклона веток
        base_size = 2.0  # Размер начального квадрата
        reduction = 0.7  # Коэффициент уменьшения

        def draw_branch(p1, p2, order):
            """
            Рекурсивно рисует ветки дерева Пифагора.
            p1, p2 - нижние вершины квадрата (2D точки)
            """
            if order == 0:
                return VGroup()

            # Берем только x,y координаты для вычислений
            p1_2d = p1[:2]
            p2_2d = p2[:2]

            # Вычисляем вектор основания квадрата
            v = p2_2d - p1_2d

            # Поворачиваем вектор на 90 градусов (для верхних вершин)
            rotation_up = np.array([
                [0, -1],
                [1, 0]
            ])
            v_up = np.dot(rotation_up, v)

            # Верхние вершины квадрата (в 2D)
            p3_2d = p2_2d + v_up
            p4_2d = p1_2d + v_up

            # Преобразуем обратно в 3D для Manim
            p3 = np.array([p3_2d[0], p3_2d[1], 0])
            p4 = np.array([p4_2d[0], p4_2d[1], 0])

            # Рисуем четыре стороны квадрата
            square_lines = VGroup(
                Line(p1, p2, color=WHITE, stroke_width=1.5),
                Line(p2, p3, color=WHITE, stroke_width=1.5),
                Line(p3, p4, color=WHITE, stroke_width=1.5),
                Line(p4, p1, color=WHITE, stroke_width=1.5)
            )

            # Поворот для левого квадрата (-angle)
            rot_left = np.array([
                [np.cos(-angle), -np.sin(-angle)],
                [np.sin(-angle), np.cos(-angle)]
            ])
            v_left = np.dot(rot_left, v) * reduction

            # Поворот для правого квадрата (+angle)
            rot_right = np.array([
                [np.cos(angle), -np.sin(angle)],
                [np.sin(angle), np.cos(angle)]
            ])
            v_right = np.dot(rot_right, v) * reduction

            # Новые базовые точки (в 2D)
            p_left_base_2d = p4_2d + v_left
            p_right_base_2d = p3_2d + v_right

            # Преобразуем в 3D
            p_left_base = np.array([p_left_base_2d[0], p_left_base_2d[1], 0])
            p_right_base = np.array([p_right_base_2d[0], p_right_base_2d[1], 0])

            # Рекурсивно рисуем следующие уровни
            left_branch = draw_branch(p4, p_left_base, order - 1)
            right_branch = draw_branch(p3, p_right_base, order - 1)

            return VGroup(square_lines, left_branch, right_branch)

        # Начальный квадрат (основание дерева) - сразу в 3D
        start_left = np.array([-base_size / 2, -3, 0])
        start_right = np.array([base_size / 2, -3, 0])

        print(f"Генерация дерева порядка {max_order}...")
        tree = draw_branch(start_left, start_right, max_order)
        tree.center()

        print("Анимация...")
        self.play(Create(tree), run_time=8)
        self.wait(1)





        self.wait(4)


# Альтернативная версия с более простым углом для теста
class PythagorasTreeSimple(Scene):
    def construct(self):
        title = Text("Дерево Пифагора (упрощенное)", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Простые параметры для теста
        max_order = 8
        angle = 45 * DEGREES
        base_size = 2.0
        reduction = 0.7

        def draw_branch(p1, p2, order):
            if order == 0:
                return VGroup()

            # Работаем в 2D
            p1_2d = p1[:2]
            p2_2d = p2[:2]
            v = p2_2d - p1_2d

            # Верхние вершины
            v_up = np.array([-v[1], v[0]])  # Поворот на 90 градусов
            p3_2d = p2_2d + v_up
            p4_2d = p1_2d + v_up

            p3 = np.array([p3_2d[0], p3_2d[1], 0])
            p4 = np.array([p4_2d[0], p4_2d[1], 0])

            square_lines = VGroup(
                Line(p1, p2, color=WHITE, stroke_width=1.5),
                Line(p2, p3, color=WHITE, stroke_width=1.5),
                Line(p3, p4, color=WHITE, stroke_width=1.5),
                Line(p4, p1, color=WHITE, stroke_width=1.5)
            )

            # Упрощенные повороты
            angle_rad = angle
            cos_a, sin_a = np.cos(angle_rad), np.sin(angle_rad)

            # Левый квадрат (поворот на -angle)
            v_left = np.array([
                v[0] * cos_a + v[1] * sin_a,
                -v[0] * sin_a + v[1] * cos_a
            ]) * reduction

            # Правый квадрат (поворот на +angle)
            v_right = np.array([
                v[0] * cos_a - v[1] * sin_a,
                v[0] * sin_a + v[1] * cos_a
            ]) * reduction

            p_left_base = np.array([p4_2d[0] + v_left[0], p4_2d[1] + v_left[1], 0])
            p_right_base = np.array([p3_2d[0] + v_right[0], p3_2d[1] + v_right[1], 0])

            left_branch = draw_branch(p4, p_left_base, order - 1)
            right_branch = draw_branch(p3, p_right_base, order - 1)

            return VGroup(square_lines, left_branch, right_branch)

        start_left = np.array([-base_size / 2, -3, 0])
        start_right = np.array([base_size / 2, -3, 0])

        tree = draw_branch(start_left, start_right, max_order)
        tree.center()

        self.play(Create(tree), run_time=6)
        self.wait(2)


# Функция вызова
if __name__ == "__main__":
    print("""
    Запустите командой:
    manim -pql pythagoras_tree.py PythagorasTreeNaked

    Или для упрощенной версии:
    manim -pql pythagoras_tree.py PythagorasTreeSimple
    """)