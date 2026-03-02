from manim import *
import numpy as np


class KochSnowflake(Scene):
    def construct(self):
        # Заголовок
        title = Text("Снежинка Коха", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Функция для генерации кривой Коха
        def koch_curve(p1, p2, order):
            """Рекурсивно генерирует точки кривой Коха между p1 и p2"""
            if order == 0:
                return [p1, p2]
            else:
                p1 = np.array(p1)
                p2 = np.array(p2)
                v = p2 - p1

                # Точки на 1/3 и 2/3 отрезка
                pA = p1 + v / 3
                pB = p1 + 2 * v / 3

                # Вершина "пика" (поворот на -60 градусов для направления вверх)
                angle = -np.pi / 3  # Отрицательный угол = поворот по часовой стрелке
                rotation = np.array([
                    [np.cos(angle), -np.sin(angle)],
                    [np.sin(angle), np.cos(angle)]
                ])
                pC = pA + np.dot(rotation, v / 3)

                # Рекурсивно строим четыре части
                return (koch_curve(p1, pA, order - 1)[:-1] +
                        koch_curve(pA, pC, order - 1)[:-1] +
                        koch_curve(pC, pB, order - 1)[:-1] +
                        koch_curve(pB, p2, order - 1))

        def get_snowflake(order, scale=5):
            """Возвращает VGroup с снежинкой Коха заданного порядка"""
            # Вершины равностороннего треугольника (с z=0)
            p1 = np.array([0.0, -scale / 2, 0])
            p2 = np.array([scale * np.cos(np.pi / 6), scale / 4, 0])
            p3 = np.array([-scale * np.cos(np.pi / 6), scale / 4, 0])

            # Три стороны снежинки (получаем 2D точки)
            curve1_2d = koch_curve(p1[:2], p2[:2], order)
            curve2_2d = koch_curve(p2[:2], p3[:2], order)
            curve3_2d = koch_curve(p3[:2], p1[:2], order)

            # Преобразуем 2D точки в 3D (добавляем z=0)
            curve1 = [np.array([x, y, 0]) for x, y in curve1_2d]
            curve2 = [np.array([x, y, 0]) for x, y in curve2_2d]
            curve3 = [np.array([x, y, 0]) for x, y in curve3_2d]

            # Объединяем все точки
            all_points = curve1 + curve2[1:] + curve3[1:]

            # Создаем ломаную линию
            snowflake = VMobject()
            snowflake.set_points_as_corners(all_points)
            snowflake.set_color(WHITE)
            snowflake.set_stroke(width=2)

            return snowflake

        # Центрируем снежинку первого порядка
        snowflake = get_snowflake(1).center()
        self.add(snowflake)

        # Постепенно увеличиваем порядок от 1 до 7
        max_order = 4

        for order in range(1, max_order + 1):
            # Создаем снежинку следующего порядка
            new_snowflake = get_snowflake(order).center()

            if order == 1:
                # Для первого порядка просто показываем
                self.play(Create(snowflake), run_time=2)
            else:
                # Плавно трансформируем в новый порядок
                self.play(
                    Transform(snowflake, new_snowflake),
                    run_time=2
                )

            # Показываем текущий порядок
            order_text = Text(f"Порядок: {order}", font_size=24, color=YELLOW)
            order_text.next_to(title, DOWN, buff=0.3)

            if order > 1:
                self.play(
                    Transform(order_text_old, order_text),
                    run_time=0.5
                )
            else:
                order_text_old = order_text
                self.play(Write(order_text))

            self.wait(0.5)

        # Финальный текст
        final_text = Text(
            "Снежинка Коха - фрактальная кривая\nс размерностью Хаусдорфа ≈ 1.2619",
            font_size=24,
            color=GREEN,
            line_spacing=1.2
        )
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(3)