from manim import *
import numpy as np
import random

class BinaryTree(Scene):
    def construct(self):
        # Заголовок и задача
        First_Title = Text("Функциональный анализ", font_size=38, color=BLUE)
        First_Title.to_edge(UP)
        self.play(Write(First_Title))
        self.wait(1.8)

        Task = Text("Найти мощность множества состоящего из непересекающихся восьмёрок", font_size=22, color=WHITE)
        Task.next_to(First_Title, DOWN)
        self.play(Write(Task))
        self.wait(2)

        # Текст про структуру (обычный Text)
        Structure_text = Text(
            "Структура вложенных восьмёрок совпадает со структурой\n"
            "бесконечного бинарного дерева, поэтому для изучения\n"
            "мощности множества восьмёрок мы будем исследовать\n"
            "мощность дерева.",
            font_size=18,
            color=WHITE,
            line_spacing=1.2
        )


        # Функция создания восьмерки
        def create_eight(width, height, center_x, center_y, color, stroke_width):
            return ParametricFunction(
                lambda t: np.array([
                    width * np.sin(t) + center_x,
                    height * np.sin(2 * t) + center_y,
                    0
                ]),
                t_range=[0, 2 * PI],
                color=color,
                stroke_width=stroke_width
            )

        # Словарь восьмерок
        eights = {
            0: [5.0, 2.0, 0, 0, WHITE, 4],
            1: [2, 2/2.5, -2.8, 0, BLUE, 3],
            2: [2, 2/2.5, 2.8, 0, WHITE, 3],
            3: [0.75, 0.75/2.5, -4, 0, BLUE, 2.5],
            4: [0.75, 0.75/2.5, -1.6, 0, WHITE, 2.5],
            5: [0.75, 0.75/2.5, 1.6, 0, BLUE, 2.5],
            6: [0.75, 0.75/2.5, 4, 0, WHITE, 2.5],
            7: [0.25, 0.25/2.5, -4.4, 0, BLUE, 2],
            8: [0.25, 0.25/2.5, -3.6, 0, WHITE, 2],
            9: [0.25, 0.25/2.5, -2, 0, BLUE, 2],
            10: [0.25, 0.25/2.5, -1.2, 0, WHITE, 2],
            11: [0.25, 0.25/2.5, 1.2, 0, BLUE, 2],
            12: [0.25, 0.25/2.5, 2, 0, WHITE, 2],
            13: [0.25, 0.25/2.5, 3.6, 0, BLUE, 2],
            14: [0.25, 0.25/2.5, 4.4, 0, WHITE, 2],
        }

        all_eights = VGroup()

        # Рисуем уровни
        eight0 = create_eight(*eights[0])
        all_eights.add(eight0)
        self.play(Create(eight0), run_time=2)
        self.wait(0.5)

        eight1 = create_eight(*eights[1])
        eight2 = create_eight(*eights[2])
        all_eights.add(eight1, eight2)
        self.play(Create(eight1), Create(eight2), run_time=2)
        self.wait(0.5)

        eight3 = create_eight(*eights[3])
        eight4 = create_eight(*eights[4])
        eight5 = create_eight(*eights[5])
        eight6 = create_eight(*eights[6])
        all_eights.add(eight3, eight4, eight5, eight6)
        self.play(Create(eight3), Create(eight4), Create(eight5), Create(eight6), run_time=2.5)
        self.wait(0.5)

        eights_level3 = [create_eight(*eights[i]) for i in range(7, 15)]
        for eight in eights_level3:
            all_eights.add(eight)
        self.play(*[Create(eight) for eight in eights_level3], run_time=3)
        self.wait(2)

        Structure_text.next_to(Task, 10 * DOWN, buff=0.5)
        self.play(Write(Structure_text))
        self.wait(3.5)



        # ---- Анимация исчезновения текста ----
        # Создаем группу отдельных символов, точно повторяющих позиции исходного текста
        symbols = VGroup()
        for char in Structure_text.text:
            if char != '\n':
                sym = Text(char, font_size=18, color=WHITE)
                symbols.add(sym)

        # Располагаем символы в той же позиции, что и исходный текст
        # Для этого используем тот факт, что Structure_text состоит из отдельных символов (подобъектов)
        # после Write они доступны. Если Write не разбил на символы, то можно скопировать вручную.
        # Попробуем получить символы из Structure_text:
        if hasattr(Structure_text, "__getitem__") and len(Structure_text) > 0:
            # Если Structure_text уже разбит на символы (как в случае с Text), то просто используем их
            symbols = Structure_text.copy()
        else:
            # Иначе (если не разбит) - располагаем приблизительно по центру исходного текста
            symbols.arrange(DOWN, center=False, aligned_edge=LEFT)
            symbols.move_to(Structure_text.get_center())

        # Удаляем исходный текст и добавляем группу символов
        self.remove(Structure_text)
        self.add(symbols)

        # Создаем анимации исчезновения
        anims = [FadeOut(sym, shift=UP*0.3 + RIGHT*random.uniform(-0.2, 0.2), scale=0.5) for sym in symbols]
        random.shuffle(anims)
        self.play(AnimationGroup(*anims, lag_ratio=0.02), run_time=3)
        self.wait(1)

        # Убираем все восьмерки
        self.play(*[Uncreate(eight) for eight in all_eights], run_time=2)
        self.wait(1)

        self.play(FadeOut(First_Title,Task,run_time=1))
        self.wait(0.5)
        

        # --- Бинарное дерево (без повторов) ---
        branch_params = {
            1: [3.5, 82], 2: [2, 60], 3: [1.75, 30],
            4: [0.9, 30], 5: [0.9, 17], 6: [0.6, 10.5],
        }
        levels = len(branch_params)

        title_tree = Text("Бинарное дерево", font_size=36, color=BLUE)
        title_tree.to_edge(UP)
        self.play(Write(title_tree))

        root = Dot(point=[0, -3.25, 0], color=WHITE, radius=0.05)
        root_label = Text("0", font_size=16, color=WHITE).next_to(root, DOWN, buff=0.1)
        self.play(FadeIn(root), Write(root_label))
        self.wait(0.5)

        all_tree_elements = VGroup(root, root_label)
        all_points = [root]
        all_labels = [root_label]

        def create_branch(parent_point, direction, level):
            x, y = parent_point.get_center()[:2]
            length, angle = branch_params[level]
            base_angle = 90
            if direction == "left":
                final_angle = base_angle + angle
            else:
                final_angle = base_angle - angle
            rad = np.radians(final_angle)
            new_x = x + length * np.cos(rad)
            new_y = y + length * np.sin(rad)
            new_point = Dot(point=[new_x, new_y, 0], color=WHITE, radius=0.04)
            line = Line(parent_point.get_center(), new_point.get_center(), color=WHITE, stroke_width=2)
            if direction == "left":
                label = Text("0", font_size=12, color=BLUE).next_to(new_point, DOWN, buff=0.1)
            else:
                label = Text("1", font_size=12, color=RED).next_to(new_point, DOWN, buff=0.1)
            return new_point, line, label

        def create_level(prev_points, level):
            if level > levels:
                return
            new_points = []
            all_edges = []
            new_labels = []
            for point in prev_points:
                left_point, left_line, left_label = create_branch(point, "left", level)
                right_point, right_line, right_label = create_branch(point, "right", level)
                new_points.extend([left_point, right_point])
                all_edges.extend([left_line, right_line])
                new_labels.extend([left_label, right_label])
            nonlocal all_tree_elements, all_points, all_labels
            for edge in all_edges:
                all_tree_elements.add(edge)
            for point in new_points:
                all_tree_elements.add(point)
                all_points.append(point)
            for label in new_labels:
                all_tree_elements.add(label)
                all_labels.append(label)
            self.play(
                *[Create(edge) for edge in all_edges],
                *[FadeIn(point) for point in new_points],
                *[Write(label) for label in new_labels],
                run_time=2
            )
            self.wait(0.3)
            create_level(new_points, level + 1)

        create_level([root], 1)
        self.wait(3)

        # Сдвиг дерева влево
        self.play(all_tree_elements.animate.scale(0.55).shift(LEFT * 2.5), run_time=2)

        # Доказательство
        text_x = 2
        proof_title = Text("Доказательство:", font_size=32, color=YELLOW)
        proof_title.move_to([text_x, 2.5, 0], aligned_edge=LEFT)
        self.play(Write(proof_title))
        self.wait(1.5)
        line1 = Text("1. Любому пути в дереве соответствует", font_size=20, color=WHITE)
        line1.next_to(proof_title, DOWN, buff=0.4, aligned_edge=LEFT).move_to([text_x, line1.get_center()[1], 0], aligned_edge=LEFT)
        self.play(Write(line1))
        line1b = Text("   бесконечная последовательность 0 и 1", font_size=20, color=WHITE)
        line1b.next_to(line1, DOWN, buff=0.1, aligned_edge=LEFT).move_to([text_x, line1b.get_center()[1], 0], aligned_edge=LEFT)
        self.play(Write(line1b))
        self.wait(1.5)
        line2 = Text("2. Каждая последовательность 0/1", font_size=20, color=WHITE)
        line2.next_to(line1b, DOWN, buff=0.4, aligned_edge=LEFT).move_to([text_x, line2.get_center()[1], 0], aligned_edge=LEFT)
        self.play(Write(line2))
        line2b = Text("   соответствует двоичной записи", font_size=20, color=WHITE)
        line2b.next_to(line2, DOWN, buff=0.1, aligned_edge=LEFT).move_to([text_x, line2b.get_center()[1], 0], aligned_edge=LEFT)
        self.play(Write(line2b))
        line2c = Text("   числа из отрезка [0, 1]", font_size=20, color=WHITE)
        line2c.next_to(line2b, DOWN, buff=0.1, aligned_edge=LEFT).move_to([text_x, line2c.get_center()[1], 0], aligned_edge=LEFT)
        self.play(Write(line2c))
        self.wait(1.5)
        line3 = Text("3. Отрезок [0, 1] имеет мощность", font_size=20, color=WHITE)
        line3.next_to(line2c, DOWN, buff=0.4, aligned_edge=LEFT).move_to([text_x, line3.get_center()[1], 0], aligned_edge=LEFT)
        self.play(Write(line3))
        line3b = Text("   континуум (несчетен)", font_size=20, color=WHITE)
        line3b.next_to(line3, DOWN, buff=0.1, aligned_edge=LEFT).move_to([text_x, line3b.get_center()[1], 0], aligned_edge=LEFT)
        self.play(Write(line3b))
        self.wait(1.5)
        conclusion = Text("Мощность восьмёрок - континуум", font_size=36, color=BLUE)
        conclusion.to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(3)

        # --- ПУНКТ 2: убираем всё со второго слайда и показываем автора ---
        second_slide_elements = VGroup(
            title_tree,
            all_tree_elements,
            proof_title,
            line1, line1b,
            line2, line2b, line2c,
            line3, line3b,
            conclusion
        )

        self.play(FadeOut(second_slide_elements, shift=DOWN*0.5), run_time=2)
        self.wait(1)

        author = Text("Автор: Гончарик Родион - 3823Б1МА1", font_size=32, color=ORANGE)
        music = Text("Музыка: Camerata Romana, Eugen Duvier - Violin Concerto No. 1 in A Minor, BWV 1041 I. Allegro moderato", font_size=16, color=ORANGE)
        author.move_to(ORIGIN)
        music.next_to(author,DOWN)
        self.play(Write(author))
        self.play(Write(music))
        self.wait(3)