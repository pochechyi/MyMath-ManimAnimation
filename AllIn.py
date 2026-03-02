from manim import *


# 1. Создание сцены. Окружность
class Introduction(Scene):
    def construct(self):
        circ = Circle()
        self.add(circ)
        self.wait(3)


# 2. Добавление и удаление объектов. Квадрат
class AddAndRemoveMethods(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.wait(4)
        self.remove(square)
        self.wait(2)


# 3. Смена цвета фона. Прямая
class BackgroundColor(Scene):
    def construct(self):
        # Изменение фона в отдельной сцене
        self.camera.background_color = DARK_GREY

        # Изменение фона во всех сценах
        # config.background_color = DARK_GREY

        line_1 = Line()
        self.add(line_1)
        self.wait(3)

        line_2 = Line(DOWN, UP)
        self.add(line_2)
        self.wait(3)

        self.remove(line_1, line_2)
        self.wait(3)

    # 4. Анимация. Появление и выцветание


class FadeAnimation(Scene):
    def construct(self):
        circ = Circle(radius=2)
        self.play(FadeIn(circ))
        self.wait()
        self.play(FadeOut(circ))

        square = Square(side_length=3)
        self.play(FadeIn(square))
        self.wait()
        self.play(FadeOut(square))

        line = Line(LEFT, RIGHT + UP)
        self.play(FadeIn(line))
        self.wait()
        self.play(FadeOut(line))
        self.wait(3)


# 5. Многоугольники
class PolygonalShapes(Scene):
    def construct(self):
        rectangle = Rectangle(height=2, width=3)
        self.play(FadeIn(rectangle))
        self.wait()

        regular_polygon = RegularPolygon(n=8, radius=1.5)
        self.play(FadeIn(regular_polygon), FadeOut(rectangle))
        self.wait()

        triangle = Triangle(radius=2)
        self.play(FadeIn(triangle), FadeOut(regular_polygon))
        self.wait()

        polygon = Polygon(DOWN + 2 * LEFT, UP + LEFT, ORIGIN,
                          UP + RIGHT, DOWN + 2 * RIGHT)
        self.play(FadeIn(polygon), FadeOut(triangle))
        self.wait(3)

    # 6. Дуга, точка, эллипс, сектор, кольцо


class ArcShapes(Scene):
    def construct(self):
        arc = Arc(
            radius=2,
            start_angle=PI / 4,
            angle=PI / 3
        )
        self.play(FadeIn(arc))
        self.wait()

        dot = Dot(radius=0.05)
        self.play(FadeIn(dot))
        self.wait()

        ellipse = Ellipse(height=2, width=4)
        self.play(FadeIn(ellipse))
        self.wait()

        annulus = Annulus(
            outer_radius=1,
            inner_radius=0.8
        )
        self.play(FadeIn(annulus))
        self.wait()

        sector = Sector(
            outer_radius=0.8,
            angle=PI / 6
        )
        self.play(FadeIn(sector))
        self.wait(3)

    # 7. Указательные стрелки и векторы


class ArrowShapes(Scene):
    def construct(self):
        arrow = Arrow(LEFT, 3 * RIGHT, tip_length=0.2)
        self.play(FadeIn(arrow))
        self.wait()
        self.play(FadeOut(arrow))

        double_arrow = DoubleArrow(2 * LEFT, 2 * RIGHT,
                                   tip_length=0.4)
        self.play(FadeIn(double_arrow))
        self.wait()
        self.play(FadeOut(double_arrow))

        curved_arrow = CurvedArrow(3 * LEFT, 3 * RIGHT,
                                   radius=10)
        self.play(FadeIn(curved_arrow))
        self.wait()
        self.play(FadeOut(curved_arrow))

        curved_double_arrow = CurvedDoubleArrow(2 * DOWN, 2 * UP)
        self.play(FadeIn(curved_double_arrow))
        self.wait(3)

    # 8. Декоративные фигуры. Углы. Пунктир


class DecorativeShapes(Scene):
    def construct(self):
        dashed_line_1 = DashedLine(ORIGIN, 3 * UP)
        self.play(FadeIn(dashed_line_1))
        self.wait()

        dashed_line_2 = DashedLine(2 * LEFT, 2 * RIGHT, dash_length=0.2)
        self.play(FadeIn(dashed_line_2))
        self.wait()

        right_angle = RightAngle(dashed_line_1, dashed_line_2)
        self.play(FadeIn(right_angle))
        self.wait()

        line = Line(ORIGIN, 2 * UP + 1.5 * RIGHT)
        self.play(FadeOut(dashed_line_1, right_angle),
                  FadeIn(line))
        self.wait()

        angle = Angle(dashed_line_2, line, radius=0.7)
        self.play(FadeIn(angle))
        self.wait()

        rounded_rect = RoundedRectangle(corner_radius=0.12)
        self.play(FadeOut(angle, dashed_line_2, line),
                  FadeIn(rounded_rect))
        self.wait()
        self.play(FadeOut(rounded_rect))

        star = Star(n=5)
        self.play(FadeIn(star))
        self.wait()

        circ = DashedVMobject(Circle(radius=2), num_dashes=50)
        self.play(FadeIn(circ))
        self.wait(3)


# 9. Кривая Безье и скругленные углы
class BezierAndRounded(Scene):
    def construct(self):
        spline = CubicBezier(
            3 * LEFT,
            4 * UP,
            3 * RIGHT + 2 * DOWN,
            4 * RIGHT + 3 * UP
        )
        self.play(FadeIn(spline))
        self.wait()

        star = Star(n=7).round_corners(radius=0.1)
        self.play(FadeIn(star))
        self.wait()

        triangle = Triangle(radius=2)
        triangle.round_corners(radius=0.05)
        self.play(FadeIn(triangle))
        self.wait(3)


# 10. Настройки анимации. Длительность
class AnimationAttributes(Scene):
    def construct(self):
        circ = Circle()
        line = Line()
        dot = Dot()

        self.play(FadeIn(dot), run_time=1)
        self.wait(1)
        self.play(FadeIn(circ, shift=UP), run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(line, shift=RIGHT), run_time=2)
        self.wait()
        self.play(
            FadeOut(line, run_time=1.2),
            FadeOut(circ, run_time=2, shift=UP)
        )
        self.wait()
        self.play(FadeOut(line, circ, shift=UP), run_time=1.5)
        self.wait(3)

    # 11. Анимация. Создание и исчезновение. Появление


class CreationUncreationGrow(Scene):
    def construct(self):
        arrow = Arrow()
        circ = Circle(1.5)
        square = Square(3)
        polygon = Polygon(2 * UP, ORIGIN, 2 * RIGHT)

        self.play(Create(arrow))
        self.wait()
        self.play(Uncreate(arrow))
        self.play(Create(circ), run_time=2)
        self.wait()
        self.play(Uncreate(circ), run_time=2)
        self.wait()
        self.play(GrowFromCenter(square))
        self.wait()
        self.play(GrowFromCenter(polygon))
        self.wait(3)


# 12. LaTeX. Простейшие примеры. Анимация
class LaTexSimple(Scene):
    def construct(self):
        # Урок по LaTeX: https://vk.com/wall-91031095_20849
        pythagoras = MathTex('a^2 + b^2 = c^2')
        self.play(Write(pythagoras), run_time=3)
        self.wait()
        self.play(Unwrite(pythagoras))

        fibonacci = MathTex("a_n = a_{n-1} + a_{n-2}", font_size=48)
        self.play(Create(fibonacci), run_time=3)
        self.wait()
        self.play(Uncreate(fibonacci))

        inequality = MathTex("f(x,y) > g(x,y)", font_size=60)
        self.wait()
        self.play(FadeIn(inequality))
        self.wait()
        self.play(FadeOut(inequality))
        self.wait(3)


# 13. LaTeX. Примеры команд. Экранирование двойным слешем
class LaTexCommands(Scene):
    def construct(self):
        pi_not_3_14 = MathTex("\\pi \\neq 3 \\!,14", font_size=100)
        self.play(Write(pi_not_3_14), run_time=2)
        self.wait()
        self.play(Unwrite(pi_not_3_14))

        sin_and_cos = MathTex("\\sin^2 \\alpha + \\cos ^2 \\alpha = 1")
        self.play(Write(sin_and_cos), run_time=3)
        self.wait()
        self.play(Unwrite(sin_and_cos))

        sum_of_logs = MathTex("\\log_2(a \\cdot b) = \\log_2a + \\log_2b")
        self.wait()
        self.play(GrowFromCenter(sum_of_logs), run_time=1.5)
        self.wait(3)

    # 14. LaTeX. Другие команды. Цвет. Экранирование r-строками


class LaTexSizeAndColor(Scene):
    def construct(self):
        tangent_value = MathTex(
            r"\tg \frac{\pi}{3} = \sqrt{3}",
            font_size=70,
            color=YELLOW
        )
        self.play(Write(tangent_value), run_time=3)
        self.wait()
        self.play(Unwrite(tangent_value))

        number_set = MathTex(
            r"(\infty; -1] \cup \{0\} \cup [1; + \infty)"
        )
        self.play(Write(number_set), run_time=3)
        self.wait()
        self.play(Unwrite(number_set))

        sim_of_triangles = MathTex(
            r"\triangle ABC \sim \triangle A_1B_1C_1",
            color=BLUE
        )
        self.wait()
        self.play(FadeIn(sim_of_triangles))
        self.wait(3)

    # 15. LaTeX. Оформление кода. Пробелы


class LaTexDisign(Scene):
    def construct(self):
        latex_str = r"(a\perp l,\  b\perp l) \Rightarrow a\parallel b"
        parallel_test = MathTex(latex_str)
        self.play(Write(parallel_test), run_time=3)
        self.wait()
        self.play(Unwrite(parallel_test), run_time=2)

        limit_def = MathTex(
            r"\lim _{n\to \infty }x_n=a",
            r"\ \Leftrightarrow \,",
            r"\forall \varepsilon >0" +
            r"\hspace{2mm} \exists N(\varepsilon )"
            r"\in \mathbb {N} \colon "
            r"n\geqslant N \Rightarrow |x_{n}-a|<\varepsilon"
        )
        # Если при генерации формул с помощью Manim возникают ошибки,
        # попробуйте сначала скомпилировать документ в редакторе LaTeX.
        # Как правило, промахи случаются в именах команд, скобках,
        # экранировании. Некоторые команды могут не соответствовать
        # используемой преамбуле.
        # Не используйте \newline, \break в классе MathTex.
        # '\colon' + 'n' = '\colonn' (ошибка)

        self.play(FadeIn(limit_def[0], shift=DOWN))
        self.wait()
        self.play(GrowFromCenter(limit_def[1]))
        self.wait()
        self.play(FadeIn(limit_def[2], shift=DOWN))
        self.wait()
        self.play(Unwrite(limit_def), run_time=3)
        self.wait(3)


# 16. LaTeX. Системы и совокупности
class LaTexBraceBracket(Scene):
    def construct(self):
        system_brace = MathTex(r"\begin{cases}x>0, \\ x <1. \end{cases}")
        self.play(Write(system_brace), run_time=3)
        self.wait()
        self.play(Unwrite(system_brace))

        union_bracket = MathTex(r"\left[ \begin{gathered} "
                                r"x = \pm 1, \\ x \geqslant 3. \hfill "
                                r"\end{gathered} \right.")
        self.play(Write(union_bracket), run_time=3)
        self.wait(3)


# 17. LaTeX. Текст
class LaTexText(Scene):
    def construct(self):
        hello = Tex("Hello, Manim!", color=GOLD)
        self.play(Write(hello), run_time=2)
        self.wait(2)
        self.play(Unwrite(hello))

        kolmogorov = Tex("Andrey Nikolaevich Kolmogorov (1903—1987) "
                         "was a Soviet mathematician who contributed to the "
                         "mathematics of probability theory, topology, \\newline intuition"
                         "istic logic, turbulence, classical mechanics, algorithmic"
                         " information theory and computational complexity \\break \\ldots",
                         font_size=36)
        self.wait()
        self.play(FadeIn(kolmogorov), run_time=1.5)
        self.wait(3)


# 17b. LaTeX. Опционально: текст на русском языке
class LaTexRussian(Scene):
    def construct(self):
        russian_language = Tex(r"Чтобы генерировать текст \LaTeX \ "
                               "с использованием кириллицы, добавьте русский язык "
                               "в преамбулу, которая используется библиотекой Manim. "
                               r"Преамбула находится здесь: $\backslash$manim"
                               r"$\backslash$utils$\backslash$tex\_templates.py",
                               font_size=32)
        self.play(Write(russian_language), run_time=5)
        self.wait(3)
        self.play(FadeOut(russian_language))

        replace_line = Tex(r"Строчку \break $\backslash$usepackage"
                           r"[english]\{babel\} \break следует заменить на \break"
                           r"$\backslash$usepackage[english, russian]\{babel\}",
                           font_size=36)
        self.play(FadeIn(replace_line))
        self.wait(3)


# 18. LaTeX. Формулы внутри текста
class LaTexTextWithFormulas(Scene):
    def construct(self):
        euler = Tex(r"Euler's identity: $e^{i\pi}+1=0$")
        self.play(GrowFromCenter(euler), run_time=1.5)
        self.wait()
        self.play(Unwrite(euler))

        imo_problem = Tex(r"Let $n \geqslant 1$ be an odd integer. "
                          r"Determine all functions $f$ from the set of integers "
                          r"to itself such that for all integers $x$ and $y$ the "
                          r"difference $f(x)-f(y)$ divides $x^{n}-y^{n}$.",
                          font_size=32)
        self.play(FadeIn(imo_problem))
        self.wait(3)


# 19. Формулы LaTeX. Выравнивание по ширине
class LaTexAlignment(Scene):
    def construct(self):
        perelman = Tex(r"\begin{justify}"
                       r"Recall that every smooth vector field "
                       r"$X^{\alpha}=X^{\alpha}(x)$ on a manifold $(M, g)$ "
                       r"generates an infinitesimal diffeomorphism "
                       r"$x^{\alpha} \mapsto x^{\alpha}+\varepsilon "
                       r"X^{\alpha}+O\left(\varepsilon^{2}\right)$. "
                       r"Pulling back the metric $g_{\alpha \beta}$ by this "
                       r"diffeomorphism creates a infinitesimally deformed "
                       r"metric $g_{\alpha \beta} \mapsto g_{\alpha \beta}+$ "
                       r"$\varepsilon \pi_{\alpha \beta}"
                       r"O\left(\varepsilon^{2}\right)$."
                       r"\end{justify}", font_size=32)

        self.play(Write(perelman), run_time=7)
        self.wait(3)


# 20. Текст, не требующий LaTeX
class TextExample(Scene):
    def construct(self):
        # Если у вас отсутствует шрифт Arial или Times New Roman,
        # то укажите любой другой в качестве параметра font.
        hello = Text(
            "Этот текст генерируется моментально",
            font="Times New Roman",
            color=LIGHT_GREY,
            font_size=32
        )
        self.play(Write(hello), run_time=2)
        self.wait()

        message = Text("LaTeX не требуется, кириллица поддерживается",
                       font="Arial", font_size=32)
        self.play(FadeOut(hello, shift=DOWN),
                  FadeIn(message, shift=DOWN))
        self.wait(3)


# 20b. Опционально: Шрифт как в LaTeX. Форматирование
class LaTexFake(Scene):
    def construct(self):
        # По умолчанию в LaTeX используется шрифт CMU Serif.
        # Вы можете установить его самостоятельно и использовать
        # для обычного текста.
        fake_latex = Text("CMU Serif удобен для цифр:"
                          " 0, 1, 2, 3, 4, 5, 6, 7, 8, 9", font="CMU Serif",
                          color=WHITE, font_size=32)
        self.play(Write(fake_latex), run_time=3)
        self.wait()

        message = Text("Для перехода к новой строке "
                       "используйте \\n.\nПри необходимости форматировать "
                       "большие\nфрагменты текста присмотритесь к классу\n"
                       "Paragraph.", font_size=32, font="CMU Serif")
        self.play(FadeOut(fake_latex), FadeIn(message))
        self.wait(3)

    # 21. Абсолютное положение в кадре. Дуги, окружности и точки


class ArcCenter(Scene):
    def construct(self):
        arc = Arc(arc_center=LEFT, radius=2)
        self.play(GrowFromCenter(arc))
        self.wait()

        circle = Circle(arc_center=2 * RIGHT)
        self.play(GrowFromCenter(circle))
        self.wait()

        dot = Dot(point=5 * RIGHT + 3.5 * UP)
        self.play(GrowFromCenter(dot))
        self.wait()

        curver_double_arrow = CurvedDoubleArrow(
            ORIGIN, 5 * RIGHT + 3.3 * UP,
            arc_center=3 * RIGHT,
            tip_length=0.2)
        self.play(GrowFromCenter(curver_double_arrow))
        self.wait(3)

    # 22. Абсолютное положение в кадре. Произвольные объекты


class MoveToMethod(Scene):
    def construct(self):
        star = Star().move_to(RIGHT)
        # RIGHT = np.array([1, 0, 0])
        self.play(FadeIn(star))
        self.wait()

        square = Square().move_to(np.array([-1.5, 0, 0]))
        self.play(FadeIn(square))
        self.wait()

        polygon = Polygon([0, 1, 0], [0, 0, 0], [1, 0, 0])
        polygon.move_to(2 * UP)
        self.play(FadeIn(polygon))
        self.wait()

        rectangle = Rectangle(height=5, width=6)
        rectangle.move_to(7 * np.array([0, 0.1, 0]))
        self.play(FadeIn(rectangle))
        self.wait(3)

    # 23. Смещение объекта. Метод копирования


class ShiftMethod(Scene):
    def construct(self):
        # Прямоугольник, сместись на единицу вправо
        rect = Rectangle(width=0.85).shift(RIGHT)
        self.play(FadeIn(rect))
        self.wait()

        # Прямоугольник 2, сместись на единицу вправо
        rect_2 = rect.copy()
        rect_2.shift(RIGHT)
        self.play(FadeIn(rect_2))
        self.wait(3)


# 23b. Сравните этот пример с предыдущим
class ShiftOrMove(Scene):
    def construct(self):
        # Прямоугольник, встань в точке np.array([1, 0, 0])
        rect = Rectangle(width=0.85).move_to(RIGHT)
        self.play(FadeIn(rect))
        self.wait()

        # Прямоугольник 2, встань в точке np.array([1, 0, 0])
        rect_2 = rect.copy()
        rect_2.move_to(RIGHT)
        self.play(FadeIn(rect_2))
        self.wait(3)


# 24. Абсолютное положение в кадре и смещение объекта
class BetterShiftThanMove(Scene):
    def construct(self):
        ellipse = Ellipse().shift(UP + 3 * RIGHT)
        self.play(GrowFromCenter(ellipse))
        self.wait()

        circ_1 = Circle().move_to(ellipse)
        self.play(FadeIn(circ_1))
        self.wait()

        circ_2 = circ_1.copy().shift(2 * LEFT)
        self.play(FadeIn(circ_2))
        self.wait(3)


# 25. Положение относительно краев кадра
class ToEdgeMethod(Scene):
    def construct(self):
        square_1 = Square().to_edge(UP)
        self.play(Create(square_1))
        self.wait()

        square_2 = Square().to_edge(LEFT)
        self.play(Create(square_2))
        self.wait()

        square_3 = Square().to_edge(DOWN, buff=0.5)
        self.play(Create(square_3))
        self.wait()

        # Высота кадра — 8 единиц: ориентируйтесь на нее
        # при использовании параметра buff.

        square_4 = Square().to_edge(RIGHT, buff=1.2)
        self.play(Create(square_4))
        self.wait()

        square_5 = Square().shift(2.2 * UP).to_edge(RIGHT)
        self.play(Create(square_5))
        self.wait(3)


# 26. Положение относительно углов кадра. Константы
class MoreConstants(Scene):
    def construct(self):
        # ORIGIN = np.array([0, 0, 0])
        # UP = np.array([0, 1, 0])
        # RIGHT = np.array([1, 0, 0])
        # WHITE = "#FFFFFF"
        # UR = UP + RIGHT = np.array([1, 1, 0])
        # UL = UP + LEFT
        # DL = DOWN + LEFT
        # DR = DOWN + RIGHT

        circ_1 = Circle().to_edge(UR)
        self.play(GrowFromCenter(circ_1))
        self.wait()

        circ_2 = Circle().to_edge(UL, buff=2)
        self.play(GrowFromCenter(circ_2))
        self.wait()

        circ_3 = Circle().to_edge(DL, buff=LARGE_BUFF)
        self.play(GrowFromCenter(circ_3))
        self.wait()

        circ_4 = Circle().to_edge(DR, buff=SMALL_BUFF)
        self.play(GrowFromCenter(circ_4))
        self.wait(3)

    # 27. Положение относительно других объектов


class NextToMethod(Scene):
    def construct(self):
        dot = Dot(3 * RIGHT)
        self.play(GrowFromCenter(dot))
        self.wait()
        square_1 = Square().move_to(dot)
        square_1.shift(1.3 * RIGHT)
        self.play(FadeIn(square_1))
        self.wait()
        self.play(FadeOut(square_1))

        square_2 = Square().next_to(dot, RIGHT)
        self.play(FadeIn(square_2))
        self.wait()
        square_3 = Square().next_to(dot, UP)
        self.play(FadeIn(square_3))
        self.wait()
        square_4 = Square().next_to(dot, LEFT)
        self.play(FadeIn(square_4))
        self.wait(3)


# 28. Положение относительно других объектов (и не только)
class NextToMethodAttributes(Scene):
    def construct(self):
        circ = Circle()
        self.play(FadeIn(circ))
        self.wait()

        square_1 = Square().next_to(circ)
        self.play(FadeIn(square_1))
        self.wait()

        square_2 = Square().next_to(circ, UL, buff=0.1)
        self.play(FadeIn(square_2), shift=UR)
        self.wait()

        square_3 = Square().next_to(circ, np.array([1, 3, 0]))
        self.play(FadeIn(square_3), shift=DL)
        self.wait()

        square_4 = Square().next_to(5 * RIGHT, DR, buff=0)
        self.play(FadeIn(square_4))
        self.wait(3)


# 29. Выравнивание относительно других объектов
class AlignToMethod(Scene):
    def construct(self):
        problem_a = MathTex(r"a)\ -1 \leqslant \log_2 x "
                            r"\leqslant 1 ")
        self.play(FadeIn(problem_a, shift=DOWN))
        self.wait()

        problem_b = MathTex(r"b)\ \sin x = \frac{1}{2}")
        problem_b.next_to(problem_a, DOWN)
        problem_b.align_to(problem_a, LEFT)
        self.play(GrowFromCenter(problem_b))
        self.wait()

        problem_c = Tex(r"$c)\ \arcsin (-1) = ?$")
        problem_c.next_to(problem_b, DOWN, aligned_edge=LEFT)
        self.play(Write(problem_c), run_time=2)
        self.wait()

        # Выравнивание трех и более объектов
        # см. в примере 56.


# 29b. Сравните этот пример с предыдущим
class WithoutAlignTo(Scene):
    def construct(self):
        problem_a = MathTex(r"a)\ -1 \leqslant \log_2 x "
                            r"\leqslant 1 ")
        self.play(FadeIn(problem_a, shift=DOWN))
        self.wait()

        problem_b = MathTex(r"b)\  \sin x = \frac{1}{2}")
        problem_b.next_to(problem_a, DOWN)
        self.play(GrowFromCenter(problem_b))
        self.wait()

        problem_c = Tex(r"$c) \ \arcsin (-1) = ?$")
        problem_c.next_to(problem_b, DOWN)
        self.play(Write(problem_c), run_time=2)
        self.wait()


# 30. Параметры объектов. Окружность и круг
class CircleAttributes(Scene):
    def construct(self):
        circ_1 = Circle(
            radius=2,
            arc_center=2 * LEFT,
            fill_color=DARK_BLUE,
            fill_opacity=0.3,
            stroke_color=WHITE,
            stroke_width=5,
            stroke_opacity=0.9,
        )
        self.play(FadeIn(circ_1, shift=DOWN))
        self.wait()

        circ_2 = Circle(stroke_color=YELLOW, stroke_width=3)
        circ_2.next_to(circ_1, RIGHT)
        self.play(FadeIn(circ_2, shift=RIGHT))
        self.wait()

        circ_3 = Circle(fill_color=ORANGE, fill_opacity=1,
                        radius=0.85, stroke_opacity=0)
        circ_3.next_to(circ_2)
        self.play(FadeIn(circ_3, shift=LEFT))
        self.wait(3)


# 31. Параметры объектов. Многоугольники
class PolygonAttributes(Scene):
    def construct(self):
        rectangle = Polygon(
            2 * LEFT, 2 * RIGHT, 2 * UR, 2 * UL,
            fill_color=GOLD_A,
            fill_opacity=0.5,
            stroke_color=GOLD_E,
            stroke_width=1,
            stroke_opacity=0.8
        ).to_edge(RIGHT, buff=1)
        self.play(FadeIn(rectangle))
        self.wait()

        triangle = Polygon(
            2 * UP, ORIGIN, [2, 0, 0],
            color=BLUE,
            fill_opacity=0.5,
        )
        triangle.to_edge(UL, buff=2)
        self.play(GrowFromCenter(triangle))

        hexagon = RegularPolygon(
            n=6,
            radius=1.5,
            start_angle=30 * DEGREES,
            stroke_width=2,
            stroke_color=TEAL
        ).shift(2 * UP)
        self.play(Create(hexagon))
        self.wait()

        trapezoid = Polygon(
            DL, UP, UR, DR + RIGHT,
            fill_opacity=0.4,
            color=LIGHT_BROWN,
        ).shift(0.5 * DL)
        self.play(TransformFromCopy(rectangle, trapezoid),
                  run_time=1.5)
        self.wait()
        self.play(FadeOut(rectangle, triangle,
                          hexagon, trapezoid, shift=DOWN))
        self.wait(3)


# 32. Параметры объектов. Квадрат, прямоугольник
class SquareRectangleAttributes(Scene):
    def construct(self):
        square = Square(
            side_length=3,
            fill_color=GREEN,
            fill_opacity=1,
            stroke_color=TEAL,
            stroke_width=1,
            stroke_opacity=0.8
        ).move_to(2.4 * LEFT)
        self.play(FadeIn(square, shift=2 * DOWN + RIGHT))
        self.wait()

        rectangle = Rectangle(width=3.8, height=2.9,
                              color=PURPLE, stroke_width=10)
        rectangle.move_to(2 * RIGHT)
        self.play(FadeIn(rectangle, shift=2 * DOWN - RIGHT))
        self.wait()

        rounded_rect = RoundedRectangle(
            corner_radius=0.3,
            height=3.6,
            width=9,
            stroke_color=WHITE,
            stroke_width=1.5,
            fill_color=BLACK,
            fill_opacity=1
        )
        self.play(Create(rounded_rect), run_time=3)
        self.wait(3)


# 33. Параметры объектов. Прямая
class LineAttributes(Scene):
    def construct(self):
        line_1 = Line(
            start=5 * LEFT,
            end=5 * RIGHT,
            stroke_width=3,
            stroke_color=BLUE_A,
            stroke_opacity=0.8
        )
        self.play(Create(line_1), run_time=2)
        self.wait()

        line_2 = Line(4 * LEFT, 4 * RIGHT, color=BLUE_B)
        line_2.shift(UP)
        self.play(Create(line_2), run_time=2)

        dashed_line_1 = DashedLine(
            start=3 * DOWN,
            end=3 * UP,
            stroke_width=5,
            stroke_opacity=1,
            stroke_color=BLUE_C,
            dashed_ratio=0.8,
            dash_length=0.3
        )
        dashed_line_1.shift(LEFT)
        self.play(Create(dashed_line_1), run_time=2)

        dashed_line_2 = DashedLine(
            3 * DOWN, 3 * UP,
            stroke_color=BLUE_E,
            dashed_ratio=0.5,
            dash_length=0.1
        )
        dashed_line_2.shift(RIGHT)
        self.play(Create(dashed_line_2))
        self.wait(3)

    # 34. Параметры объектов. Дуга окружности, круговой сегмент. Пунктир


class ArcAttributes(Scene):
    def construct(self):
        arc_1 = Arc(
            radius=1.5,
            start_angle=0,
            angle=PI,
            arc_center=RIGHT,
            stroke_width=5,
            stroke_color=TEAL_A,
            stroke_opacity=0.8,
            fill_color=GREEN_B,
            fill_opacity=0.8,
        )
        self.play(Create(arc_1))
        self.wait(1)

        arc_2 = Arc(0.5, TAU / 6, TAU / 3, color=YELLOW,
                    fill_opacity=0.4, arc_center=2 * UR)
        self.play(Create(arc_2))
        self.wait(1.5)

        # Сравните эту дугу с предыдущей.
        # Почему их положение не совпадает?
        arc_2b = Arc(0.5, TAU / 6, TAU / 3, color=YELLOW,
                     fill_opacity=0.4).move_to(2 * UR)
        self.play(Create(arc_2b))
        self.wait(1.5)
        self.play(FadeOut(arc_2b))
        self.wait()

        arc_3 = Arc(radius=2, stroke_color=PURPLE_D)
        arc_3.move_to(2 * RIGHT + 2 * DOWN)
        self.play(Create(arc_3))
        self.wait(2)

        arc_4 = DashedVMobject(
            Arc(radius=2.5, angle=TAU),
            num_dashes=45,
            dashed_ratio=0.6,
            equal_lengths=True,
            stroke_width=2)
        self.play(Create(arc_4), run_time=2)
        self.wait(2.5)


# 35. Параметры объектов. Указательные стрелки
class ArrowAttributes(Scene):
    def construct(self):
        arrow_1 = Arrow(
            start=3 * LEFT,
            end=3 * RIGHT,
            buff=0.25,
            stroke_width=3,
            stroke_color=GOLD_A,
            stroke_opacity=0.8,
            tip_length=0.25,
            max_tip_length_to_length_ratio=0.1,
            max_stroke_width_to_length_ratio=0.2
        )
        self.play(FadeIn(arrow_1, shift=RIGHT))
        self.wait()

        arrow_2 = Arrow(
            3 * RIGHT,
            3 * LEFT,
            tip_length=0.3,
            stroke_color=GOLD_E,
            buff=0
        )
        arrow_2.next_to(arrow_1, UP)
        self.play(FadeIn(arrow_2, shift=LEFT))
        self.wait()

        double_arrow_1 = DoubleArrow(
            3 * LEFT + UP, 3 * RIGHT + UP,
            buff=0.1,
            stroke_width=3,
            stroke_color=LIGHT_GREY,
            stroke_opacity=0.8,
            tip_length=0.15
        )
        self.play(GrowFromCenter(double_arrow_1))
        self.wait()

        double_arrow_2 = DoubleArrow(
            3 * LEFT,
            2 * RIGHT,
            stroke_color=GRAY_D
        )
        double_arrow_2.shift(1.5 * UP)
        self.play(GrowFromCenter(double_arrow_2))
        self.wait()

        curved_arrow = CurvedArrow(
            start_point=2 * DOWN,
            end_point=3 * UP,
            radius=2.5
        ).shift(RIGHT)
        self.play(GrowFromCenter(curved_arrow))
        self.wait()

        curved_double_arrow = CurvedDoubleArrow(
            2 * DOWN, 3 * UP,
            radius=10,
            tip_length=0.2,
            stroke_width=2
        ).shift(LEFT)
        self.play(GrowFromCenter(curved_double_arrow))
        self.wait(3)

    # 36. Параметры объектов. LaTeX


class LaTexAttributes(Scene):
    def construct(self):
        identity = MathTex(
            "3^3+4^3+5^3", "=", "6^3",
            font_size=100,
            fill_color=DARK_BLUE,
            fill_opacity=0.8,
            stroke_color=BLUE_A,
            stroke_width=2,
            tex_to_color_map={"6^3": YELLOW}
        )
        self.play(Write(identity.shift(2 * UP)), run_time=2)
        self.wait()

        viet = Tex("The roots $x_1$, $x_2$ of quadratic "
                   "polinomial $P(x)=x^2+bx+c$ satisfy "
                   "\\mbox{$x_1$ $+$ $x_2$ $=-b$}, $x_1$$x_2$ $=c$",
                   color=LIGHT_GREY,
                   width=200,
                   tex_environment="flushright",
                   tex_to_color_map={
                       "$x_1$": YELLOW,
                       "$x_2$": ORANGE,
                   }
                   )
        self.play(Write(viet), run_time=5)
        self.wait(3)

    # 37. Параметры объектов. Текст


class TextAttributes(Scene):
    def construct(self):
        text_1 = Text("Настройка линий и цвета "
                      "осуществляется \nстандартным образом. "
                      "Но существуют \nи другие параметры.",
                      font="Arial",
                      font_size=30,
                      color=WHITE,
                      weight=NORMAL,
                      fill_opacity=0.8,
                      line_spacing=0.3,
                      t2c={"цвета": YELLOW, "параметры": BLUE},
                      t2s={"существуют": ITALIC},
                      t2w={"линий": BOLD}
                      )
        self.play(FadeIn(text_1))
        self.wait()
        self.play(FadeOut(text_1))

        text_2 = Text("Полужирный \nтекст", font="Arial",
                      line_spacing=1, weight=BOLD)
        self.play(FadeIn(text_2))
        self.wait(3)

    # 38. Параметры объектов. Звезда, сектор, кольцо


class StarSectorAnnulusAttributes(Scene):
    def construct(self):
        star = Star(
            n=5,
            inner_radius=0.35,
            outer_radius=1,
            start_angle=PI / 2,
            stroke_color=YELLOW
        )
        self.play(FadeIn(star, shift=DOWN))
        self.wait()

        annulus = Annulus(
            inner_radius=1.1,
            outer_radius=2,
            stroke_color=WHITE,
            stroke_width=2,
            stroke_opacity=0.9,
            fill_color=YELLOW,
            fill_opacity=0.8,
        )
        self.play(GrowFromCenter(annulus))
        self.wait()

        sector = Sector(inner_radius=1.35, outer_radius=0)
        sector.shift(2 * UR)
        self.play(GrowFromCenter(sector))
        self.wait(3)

    # 39. Параметры объектов. Угол


class AngleAttributes(Scene):
    def construct(self):
        line_1 = Line(2 * LEFT, 4 * RIGHT, stroke_width=1.5)
        line_2 = Line(2 * DOWN, 2.5 * UR, stroke_width=1.5)
        self.play(Create(line_1), Create(line_2))
        self.wait()

        angle_1 = Angle(
            line_1,
            line_2,
            radius=0.7,
            quadrant=(1, 1),
            stroke_width=3,
            stroke_color=YELLOW
        )
        self.play(Create(angle_1))
        self.wait()

        angle_2 = Angle(
            line_1,
            line_2,
            quadrant=(-1, 1),
            radius=0.45
        )
        self.play(Create(angle_2), FadeOut(angle_1))
        self.wait()
        self.play(FadeOut(angle_2))

        angle_3 = Angle(line_2, line_1, quadrant=(1, -1))
        self.play(Create(angle_3))
        self.wait()

        angle_4 = Angle(line_1, line_2, quadrant=(-1, -1))
        self.play(Create(angle_4), FadeOut(angle_3))
        self.wait()

        angle_5 = Angle(line_2, line_1, quadrant=(-1, 1))
        self.play(Create(angle_5), FadeOut(angle_4))
        self.wait(3)


# 40. Параметры объектов. Прямой угол
class RightAngleAttributes(Scene):
    def construct(self):
        line_1 = Line(LEFT, RIGHT)
        line_2 = Line(DOWN, UP)
        self.play(Create(line_1), Create(line_2))

        angle_1 = RightAngle(
            line_1,
            line_2,
            stroke_width=2,
            stroke_color=YELLOW,
            length=0.4,
            quadrant=(1, 1)
        )
        self.play(Create(angle_1))
        self.wait()

        angle_2 = RightAngle(line_1, Line(UP, DOWN), quadrant=(1, 1))
        self.play(Create(angle_2))
        self.wait()
        self.play(FadeOut(angle_1, angle_2, line_1, line_2))

        line_3 = Line(DL, UR)
        line_4 = Line(DL, DR)
        self.play(Create(line_3), Create(line_4))
        self.wait()

        angle_3 = RightAngle(line_3, line_4, length=0.5)
        self.play(Create(angle_3))
        self.wait()
        self.play(FadeOut(angle_3, line_3, line_4))

        square = Square(4)
        self.play(Create(square), run_time=2)
        self.wait()

        elbow_1 = Elbow(
            width=0.4,
            stroke_width=2,
            angle=0
        ).shift(2 * DL)
        self.play(Create(elbow_1))
        self.wait()

        elbow_2 = Elbow(
            stroke_width=2,
            width=0.4,
            angle=-PI / 2
        ).shift(2 * UL)
        self.play(Create(elbow_2))
        self.wait(3)

    # 41. Параметры объектов. Рамка, фигурная скобка, подчеркивание


class DecorativeAttributes(Scene):
    def construct(self):
        zeta = MathTex(r"\zeta (s) = 0", font_size=72)
        self.play(Write(zeta), run_time=2)
        self.wait()

        underline = Underline(
            mobject=zeta,
            buff=0.1,
            stroke_width=2,
            color=YELLOW
        )
        self.play(Create(underline), run_time=1.5)
        self.wait()
        self.play(FadeOut(underline))

        box_1 = SurroundingRectangle(
            zeta,
            buff=0.3,
            stroke_width=1.5
        )
        self.play(Create(box_1), run_time=2)
        self.wait()
        self.play(FadeOut(box_1), run_time=1.5)

        box_2 = SurroundingRectangle(
            zeta,
            corner_radius=0.25,
            buff=0.2,
            stroke_width=2,
            stroke_color=WHITE
        )
        self.play(Create(box_2), run_time=2)
        self.wait()
        self.play(Uncreate(box_2), run_time=1.5)

        brace = Brace(
            mobject=zeta,
            direction=DOWN,
            buff=0.15,
            sharpness=1.2,
            color=LIGHT_GREY
        )
        self.play(FadeIn(brace, shift=UP))

        note = Tex("Hard problem", font_size=28)
        note.next_to(brace, DOWN)
        self.play(FadeIn(note, shift=UP))
        self.wait(3)


# 42. Удобная настройка параметров. Линии
class SetStrokeMethod(Scene):
    def construct(self):
        square = Square(2).set_stroke(YELLOW, 3, 0.5)
        # square = Square(YELLOW, 3, 0.5) — некорректно
        self.play(GrowFromCenter(square))
        self.wait()

        line = Line(UL, DR)
        line.set_stroke(color=TEAL_A, width=2, opacity=0.7)
        self.play(Create(line))
        self.wait()

        polygon = Polygon(UP, DOWN, RIGHT,
                          fill_color=DARK_GREY, fill_opacity=0.5)
        polygon.set_stroke(ORANGE, 2.5).shift(2 * RIGHT)
        self.play(GrowFromCenter(polygon))
        self.wait(3)


# 43. Удобная настройка параметров. Заливка
class SetFillMethod(Scene):
    def construct(self):
        circle = Circle(1.5).set_fill(GREY, 0.8)
        # circle = Circle().set_fill(0.8, GREY) — некорректно
        self.play(GrowFromCenter(circle))
        self.wait()

        square = Square(3).set_fill(color=RED_E, opacity=0.3)
        # line = Line().set_fill(RED_E) — некорректно
        self.play(GrowFromCenter(square))
        self.wait()

        note = Tex("$ABCD$ — квадрат", font_size=28, color=YELLOW)
        note.next_to(square, UP)
        self.play(Write(note), run_time=2)

        latex = MathTex(r"\angle A + \angle B + \angle C" +
                        r" + \angle D = 360^\circ", font_size=28)
        latex.set_fill(YELLOW).next_to(square, DOWN, buff=0.4)
        self.play(Write(latex), run_time=2)
        self.wait(3)


# 44. Удобная настройка параметров. Цвет и непрозрачность
class SetColorSetOpacityMethods(Scene):
    def construct(self):
        # Метод set_color меняет цвет границы
        # и цвет заливки одновременно.
        parallelogram = Polygon(ORIGIN, UR, UR + 2 * RIGHT, 2 * RIGHT,
                                fill_opacity=0.5).set_color(ORANGE)
        parallelogram.move_to(3 * RIGHT)
        self.play(GrowFromCenter(parallelogram))
        self.wait()
        self.play(FadeOut(parallelogram))

        # Метод set_opacity меняет прозрачность границы
        # и заливки одновременно.
        triangle = Triangle(radius=2, fill_color=PINK)
        triangle.set_opacity(0.75)
        self.play(GrowFromCenter(triangle))
        self.wait()

        latex = MathTex(r"\alpha + \beta + \gamma " +
                        r" = 180^\circ", font_size=40)
        latex.set_color(YELLOW).next_to(triangle, DOWN)
        self.play(Write(latex), run_time=2)
        self.wait(3)


# 45. Порядок слоев
class LayerOrder(Scene):
    def construct(self):
        star = Star(n=12, inner_radius=0.5, outer_radius=1.5)
        star.set_color(YELLOW).set_opacity(1)
        star.shift(0.5 * UL)
        square = Square(fill_opacity=1)
        square.set_color(GREEN).shift(0.5 * UR)
        circle = Circle(fill_opacity=1)
        circle.set_color(DARK_BLUE)

        self.play(FadeIn(star, square, circle))
        self.wait()
        self.remove(star, square, circle)
        self.add(square, circle, star)
        self.wait()
        self.add(circle, star, square)
        self.wait()
        self.play(FadeOut(circle, star, square,
                          shift=DOWN))

        dot_A = Dot(LEFT, 0.12)
        dot_B = Dot(RIGHT, radius=0.12)
        line_AB = Line(LEFT, RIGHT, color=PINK)

        self.play(GrowFromCenter(dot_A), GrowFromCenter(dot_B))
        self.play(Create(line_AB), run_time=2)
        self.wait()
        self.add(dot_A, dot_B)
        self.wait(3)
        self.play(FadeOut(dot_A, dot_B, line_AB, shift=DOWN))

        line_AB = Line(LEFT, RIGHT, color=YELLOW, z_index=-1)
        self.play(GrowFromCenter(dot_A), GrowFromCenter(dot_B))
        self.play(Create(line_AB), run_time=2)
        self.wait()
        self.play(FadeOut(line_AB, dot_A, dot_B, shift=DOWN))
        self.wait()

        circle.scale(1.5)
        rect = RoundedRectangle(fill_opacity=1, z_index=1)
        self.play(FadeIn(rect, circle))
        self.wait(2)
        circle.set_z_index(2)
        self.wait(2)
        rect.set_z_index(3)
        self.wait(3)


# 46. Работа с цветом
class ColorCode(Scene):
    def construct(self):
        # Определить цвет пикселя: https://sanstv.ru/color
        # Константы для цветов: https://vk.cc/cebPvC
        # (Используйте заглавные буквы)

        pentagon = RegularPolygon(n=5).set_stroke("#fb9503")
        pentagon.to_edge(UP, buff=1)
        self.play(FadeIn(pentagon, shift=DOWN))
        self.wait()

        hexagon = RegularPolygon(n=6).set_fill("#56f", opacity=0.2)
        self.play(GrowFromCenter(hexagon))
        self.wait()

        octagon = RegularPolygon(8, stroke_color=TEAL)
        octagon.next_to(hexagon)
        self.play(FadeIn(octagon, shift=DOWN))
        self.wait()

        ellipse = Ellipse(fill_opacity=0.4, height=1.5, width=2.5)
        ellipse.set_color(TEAL_E).next_to(hexagon, DOWN, buff=0.5)
        self.play(FadeIn(ellipse, shift=UP))
        self.wait(3)


# 47. Поворот объекта
class RotateMethod(Scene):
    def construct(self):
        square_1 = Square().rotate(PI / 4)
        self.play(FadeIn(square_1))
        self.wait()

        dot = Dot(color=YELLOW)
        self.play(GrowFromCenter(dot))
        self.wait()

        square_2 = Square().shift(2.7 * RIGHT)
        self.play(FadeIn(square_2))
        self.wait()
        # Поворот будет произведен мгновенно.
        # Анимацию этих методов см. в примерах 51-53.
        square_2.rotate(90 * DEGREES, about_point=ORIGIN)
        self.wait()

        # При вращении около центра окружность переходит на себя:
        # не забывайте о параметре about_point.
        circle = Circle().shift(2 * LEFT)
        self.play(Create(circle), run_time=2.5)
        self.wait()
        circle.rotate(-TAU / 4)
        self.wait()
        self.play(Create(circle), run_time=2.5)
        self.wait(3)

    # 48. Изменение масштаба и гомотетия


class ScaleMethod(Scene):
    def construct(self):
        star_1 = Star(n=12, inner_radius=0.5)
        star_1.set_stroke(YELLOW)
        self.play(GrowFromCenter(star_1))
        self.wait()

        star_2 = star_1.copy()
        star_2.scale(2)
        self.play(GrowFromCenter(star_2))
        self.wait()

        self.play(FadeOut(star_1, star_2, shift=DOWN),
                  lag_ratio=0.1)

        triangle = Triangle(fill_opacity=0.7)
        triangle.set_color(GOLD_A).shift(UP)
        self.play(Create(triangle))
        self.wait()

        triangle_a = triangle.copy()
        triangle_b = triangle.copy()
        triangle_a.scale(scale_factor=2, about_point=3 * UL)
        dot_a = Dot(3 * UL, color=YELLOW, z_index=1)
        line_a = DashedLine(
            3 * UL,
            3 * RIGHT + DOWN,
            dashed_ratio=0.8,
            dash_length=0.15
        )
        line_a.set_stroke(GREY_A, 2)
        self.play(GrowFromCenter(dot_a))
        self.play(Create(line_a, run_time=1.5))
        self.play(TransformFromCopy(triangle, triangle_a),
                  run_time=1.5)
        self.wait()

        triangle_b.scale(scale_factor=-1.5, about_point=ORIGIN)
        dot_b = Dot(ORIGIN, color=YELLOW, z_index=1)
        line_b = DashedLine(UP, 1.5 * DOWN,
                            dashed_ratio=0.8, dash_length=0.15)
        line_b.set_stroke(GREY_A, 2)
        self.play(GrowFromCenter(dot_b))
        self.play(Create(line_b))
        self.play(TransformFromCopy(triangle, triangle_b),
                  run_time=1.5)
        self.wait(3)


# 49. Анимация. Появление
class AppearanceAnimation(Scene):
    def construct(self):
        circ = Circle(fill_opacity=0.7)
        circ.set_color(GREEN)
        inequality = MathTex(r"e^\pi > \pi ^ e")
        text = Text("Посимвольное появление", font="Arial")
        text.set_color(WHITE).shift(2 * UP).scale(0.5)
        arrow = Arrow().scale(1.5).shift(1.5 * DOWN)

        self.play(FadeIn(circ))
        self.wait()
        self.play(FadeIn(circ, shift=DOWN))
        self.wait()
        self.play(FadeIn(circ, shift=2 * DR, scale=0.5, run_time=2))
        self.wait()
        self.play(FadeIn(circ, target_position=UR + 2 * UP))
        self.wait()
        self.play(FadeOut(circ))
        circ.set_color(YELLOW)

        self.play(FadeIn(circ, scale=0))
        self.wait()
        self.play(GrowFromCenter(circ))
        self.wait()
        self.play(GrowFromCenter(circ, point_color=WHITE))
        self.wait()
        self.play(GrowFromPoint(circ, 3 * UR))
        self.wait()
        self.play(GrowFromEdge(circ, RIGHT))
        self.wait()
        self.play(FadeOut(circ))
        circ.set_color(RED)
        self.wait()

        self.play(Create(arrow), run_time=2.5)
        self.wait()
        self.play(FadeIn(arrow, shift=RIGHT))
        self.wait()
        self.play(GrowArrow(arrow))
        self.wait()
        self.play(SpinInFromNothing(Square()))
        self.wait()
        self.play(Create(circ))
        self.wait()
        self.play(DrawBorderThenFill(circ))
        self.wait()
        self.play(Write(inequality), run_time=1.5)
        self.wait()
        self.play(AddTextLetterByLetter(text), run_time=1.5)
        self.wait(3)


# 50. Анимация. Выделение
class IndicationAnimation(Scene):
    def construct(self):
        circ = Circle().set_fill(WHITE, 0.9).set_stroke(WHITE, 2)
        identity = MathTex("a^2+b^2=c^2")
        identity.scale(2)
        box_1 = SurroundingRectangle(identity, buff=0.4)
        box_1.set_stroke(WHITE, 3)
        box_2 = SurroundingRectangle(identity,
                                     corner_radius=0.2, buff=0.3)
        title = Tex("Pythagorean theorem", color=ORANGE)
        title.scale(0.8).next_to(identity, UP)
        underline = Underline(identity, color=YELLOW)

        self.play(Write(identity, run_time=3))
        self.wait()
        self.play(Create(box_1, run_time=2.5))
        self.play(FadeOut(box_1), run_time=1.5)
        self.wait()
        self.play(Create(box_2, run_time=2.5))
        self.play(FadeOut(box_2), run_time=1.5)
        self.wait()
        self.play(Create(underline), run_time=1.5)
        self.play(FadeOut(underline))
        self.wait()

        self.play(ShowPassingFlash(box_1), run_time=2)
        self.wait()
        self.play(ShowPassingFlash(box_2), run_time=2)
        self.wait()
        self.play(ShowPassingFlash(underline))
        self.wait()

        self.play(Indicate(identity), run_time=4,
                  scale_factor=1.5, color=YELLOW_D)
        self.wait()
        self.play(Indicate(identity[0][-1]), run_time=3)
        self.wait()
        self.play(GrowFromCenter(title))
        self.wait()
        self.play(Wiggle(identity, run_time=4))
        self.wait(3)


# 51. Анимация. Движение
class MovementAnimation(Scene):
    def construct(self):
        circle = Circle()
        square = Square(3)
        self.play(circle.animate.shift(RIGHT))
        self.wait()
        self.play(circle.animate.to_edge(UP, buff=0.5))
        self.wait()
        self.play(circle.animate.move_to(ORIGIN))
        self.wait()
        self.play(FadeIn(square))
        self.wait()
        self.play(circle.animate.next_to(square, DOWN))
        self.wait()
        self.play(circle.animate.align_to(square, LEFT))
        self.wait()

        self.play(ApplyMethod(square.shift, 2 * UL))
        self.wait()
        self.play(ApplyMethod(square.to_edge, UR, buff=SMALL_BUFF))
        self.wait()
        self.play(ApplyMethod(square.move_to, DR + 3 * RIGHT))
        self.wait()
        self.play(ApplyMethod(square.next_to, circle))
        self.wait()
        self.play(ApplyMethod(square.align_to, circle, UP))
        self.wait()

        self.play(ApplyMethod(circle.move_to, ORIGIN))
        dot = Dot()
        self.play(GrowFromCenter(dot))
        self.wait()
        self.play(dot.animate.shift(RIGHT))
        self.wait()
        self.play(MoveAlongPath(dot, circle), run_time=3)
        self.wait()
        self.play(FadeOut(circle))
        self.play(square.animate.next_to(dot, DL, buff=-0.08))
        self.wait()
        self.play(MoveAlongPath(dot, square), run_time=4)
        self.wait()
        self.play(FadeOut(square))
        spline = CubicBezier(3 * LEFT, 3 * UP, 2 * DR, 3 * UR)
        self.play(Create(spline), run_time=2)
        self.wait()
        self.play(ApplyMethod(dot.move_to, 3 * LEFT))
        self.wait()
        self.play(MoveAlongPath(dot, spline), run_time=4)
        self.wait(3)

    # 52. Анимация. Трансформации


class TransformAnimation(Scene):
    def construct(self):
        triangle = Triangle().shift(3 * LEFT)
        circle = Circle()
        square = Square().shift(3 * RIGHT)
        dot = Dot(color=BLACK, radius=0)

        self.play(FadeIn(triangle))
        self.wait()
        self.play(Transform(triangle, circle))
        self.wait()
        self.play(Transform(triangle, square), run_time=2)
        self.wait()
        self.play(ReplacementTransform(triangle, dot))
        self.wait()

        euler_1 = MathTex(r"\sum _{n=1}^\infty \frac {1}{n^2}="
                          r"\frac{\pi ^2}{6}").shift(1.7 * UP)
        euler_1_copy = euler_1.copy()
        euler_2 = MathTex(r"\sum _{n=1}^\infty \frac {1}{n^s}="
                          r"\prod _{p}\frac {1}{1-p^{-s}}")
        euler_3 = MathTex(r"e^{iy}=\cos y+i\sin y").shift(1.3 * DOWN)

        self.play(FadeIn(circle))
        self.wait()
        self.play(ReplacementTransform(circle, euler_1))
        self.wait()
        self.play(ClockwiseTransform(euler_1, euler_2))
        self.wait()
        self.play(CounterclockwiseTransform(euler_1, euler_3))
        self.wait()
        self.play(TransformFromCopy(euler_1, euler_2))
        self.wait()
        self.play(TransformFromCopy(euler_1, euler_1_copy))
        self.wait(3)

    # 53. Анимация. Преобразования


class OtherMethodsAnimation(Scene):
    def construct(self):
        hexagon = RegularPolygon(n=6, radius=2)
        hexagon.set_color(MAROON_A).set_opacity(0.5)

        self.play(GrowFromCenter(hexagon))
        self.wait()
        self.play(hexagon.animate.rotate(PI / 2))
        self.wait()
        self.play(ApplyMethod(hexagon.rotate, -PI / 2))
        self.wait()
        self.play(ApplyMethod(hexagon.scale, 0.5))
        self.wait()
        dot = Dot().shift(LEFT)
        self.play(hexagon.animate.scale(2, about_point=2 * LEFT),
                  run_time=2)
        self.wait()

        self.play(ApplyMethod(hexagon.set_fill, PURPLE, 0.5))
        self.wait()
        self.play(hexagon.animate.set_stroke(DARK_BLUE, 10, 0.9))
        self.wait()

        self.play(GrowFromCenter(dot))
        self.wait()
        self.play(ScaleInPlace(dot, 5))
        self.wait()
        self.play(FadeToColor(dot, YELLOW))
        self.wait()
        self.play(Rotate(dot, np.arctan(1.7), about_point=2 * RIGHT))
        self.wait()
        self.play(Rotate(hexagon, PI / 2), run_time=2)
        self.wait(3)


# 54. Анимация. Исчезновение
class DisappearanceAnimation(Scene):
    def construct(self):
        circ = Circle().set_fill(WHITE, 0.9)
        circ.set_stroke(WHITE, 2)

        self.play(DrawBorderThenFill(circ))
        self.wait()
        self.play(FadeOut(circ))
        self.wait()
        self.play(DrawBorderThenFill(circ))
        self.wait()
        self.play(FadeOut(circ, shift=DOWN))
        self.wait()
        self.play(DrawBorderThenFill(circ))
        self.play(FadeOut(circ, scale=0))
        self.wait()

        # Uncreate и Unwrite удаляют объект из сцены
        self.play(FadeIn(circ))
        self.wait()
        self.play(Uncreate(circ), run_time=2)
        self.wait()
        self.play(DrawBorderThenFill(circ))
        self.wait()

        isomorphism = MathTex(r"D_3 \cong S_3").scale(2)
        self.play(Write(isomorphism), run_time=2)
        self.wait()
        self.play(Unwrite(isomorphism, reverse=True))
        self.wait()
        self.play(Write(isomorphism))
        self.wait(3)


# 55. Синхронная анимация. Группы объектов
class TimedAnimation(Scene):
    def construct(self):
        circ = Circle(1.4, color=YELLOW).shift(1.9 * LEFT)
        star = Star(color=GOLD).shift(2 * DOWN)
        rect = Rectangle().to_edge(UP, buff=1).scale(0.7)
        shapes = VGroup(circ, star, rect)

        # Метод add добавляет элемент в группу
        tex = MathTex(r"\int \limits _a^b f(x)\,dx=F(b)-F(a)")
        shapes.add(tex)

        self.play(FadeIn(shapes))
        self.wait()
        self.play(FadeOut(shapes, shift=DOWN))
        self.wait()

        # lag_ratio=0 — воспроизведение анимаций одновременно,
        # lag_ratio=1 — воспроизведение анимаций последовательно,
        # Значения от 0 до 1 позволяют начать новую анимацию,
        # пока еще идет предыдущая.

        self.play(FadeIn(shapes, shift=UP), run_time=3, lag_ratio=0.1)
        self.wait()
        self.play(FadeOut(shapes, shift=UP), run_time=5, lag_ratio=0.4)
        self.wait()
        self.play(
            AnimationGroup(
                FadeIn(circ, shift=2 * RIGHT),
                Write(tex, run_time=2),
                FadeIn(star, shift=2 * LEFT),
                FadeIn(rect),
                lag_ratio=0.7
            )
        )
        self.wait()
        self.play(ApplyMethod(shapes.move_to, 2 * RIGHT),
                  lag_ratio=0.1, run_time=2)
        self.wait()
        self.play(
            AnimationGroup(
                Unwrite(shapes[:3], run_time=2),
                Unwrite(tex, run_time=2),
                lag_ratio=0.2
            )
        )
        self.wait(3)


# 56. Построение группы объектов в одну шеренгу или фалангой
class ArrangeMethod(Scene):
    def construct(self):
        square = VGroup()
        for i in range(6):
            square.add(Square(1 + i / 10))

            # В одну шеренгу
        square.arrange()
        self.play(Write(square), run_time=2)
        self.wait()
        self.play(FadeOut(square))

        # В одну шеренгу с выравниванием
        square.arrange(LEFT, aligned_edge=DOWN)
        self.play(Write(square), run_time=2)
        self.wait()
        self.play(FadeOut(square))

        # По диагонали без зазора
        square.arrange(UR, buff=0)
        self.play(Write(square), run_time=2)
        self.wait()
        self.play(FadeOut(square))

        # Поле 2x2
        square[:4].arrange_in_grid()
        self.play(Write(square[:4]), run_time=2)
        self.wait()
        self.play(FadeOut(square[:4]))

        # Поле 2x3
        square.arrange_in_grid(rows=2, aligned_edge=LEFT)
        self.play(Write(square), run_time=2)
        self.wait()
        self.play(FadeOut(square))

        # Поле 3x2
        square.arrange_in_grid(cols=2)
        self.play(Write(square), run_time=2)
        self.wait()

        # Анимация методов
        self.play(square.animate.arrange())
        self.wait()
        self.play(ApplyMethod(square.arrange_in_grid, rows=2))
        self.wait(3)


# 57. Срезы. Работа с LaTeX и группами объектов
class LaTexWithSlices(Scene):
    def construct(self):
        area = MathTex("S", "=", r"\pi R^2", "=", r"4\pi")
        area.scale(2)

        self.play(FadeIn(area[0], shift=UP))
        self.wait()
        self.play(TransformFromCopy(area[0], area[2]),
                  Write(area[1]))
        self.wait()
        self.play(TransformFromCopy(area[2], area[4]),
                  Write(area[3]))
        self.wait()
        self.play(Indicate(area[-1], run_time=3, scale_factor=1.5))
        self.wait()
        self.play(FadeOut(area, shift=DOWN), lag_ratio=0.1)
        self.wait()

        cases = MathTex(r"\begin{cases} x > 0, \\ "
                        r"x \neq 1. \end{cases}")
        self.play(FadeIn(cases[0][0], shift=RIGHT))
        self.wait()
        self.play(FadeIn(cases[0][1:5], shift=LEFT))
        self.wait()
        self.play(FadeIn(cases[0][5:], shift=LEFT))
        self.wait()
        self.play(FadeToColor(cases[0][0], YELLOW))
        self.wait()
        self.play(Indicate(cases[0][1:5]), run_time=3,
                  color=ORANGE)
        self.wait()
        self.play(cases[0][6].animate.set_color(PINK))
        self.wait(3)


# 58. Получение координат центра объекта
class GetCenterMethod(Scene):
    def construct(self):
        circle = Circle(color=GOLD_A)
        circle.shift(3 * RIGHT)
        self.play(GrowFromCenter(circle))
        self.wait()
        self.play(Rotate(circle, TAU / 3, about_point=ORIGIN),
                  run_time=2)
        self.wait()

        dot = Dot().move_to(circle.get_center())
        self.play(GrowFromCenter(dot))
        self.wait()

        dot_A = Dot().to_edge(UL, buff=0.5)
        dot_B = Dot().to_edge(DR, buff=0.5)

        double_arrow = DoubleArrow(
            dot_A,
            dot_B.get_center(),
            tip_length=0.2
        ).set_stroke(WHITE, 2)
        self.play(GrowArrow(double_arrow), run_time=2)
        self.wait()
        self.play(FadeOut(double_arrow))

        triangle = Polygon(dot.get_center(), LEFT, DR)
        triangle.shift(3 * RIGHT).set_stroke(BLUE, 2)
        self.play(GrowFromCenter(triangle))
        group = VGroup(circle, triangle)
        self.wait()

        self.play(ApplyMethod(dot.move_to, group.get_center()))
        self.wait()

        line = Line(triangle.get_center(), circle.get_center())
        self.play(Create(line))
        self.wait()
        box_1 = SurroundingRectangle(triangle, buff=0)
        box_2 = SurroundingRectangle(circle, buff=0)
        box_3 = SurroundingRectangle(group, buff=0)
        boxes = VGroup(box_1, box_2, box_3)
        self.play(FadeIn(boxes), lag_ratio=1, run_time=5)
        self.wait(3)

    # 59. Графики функций инт


class PlotMethod(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-6.5, 6.5],
            y_range=[-2.5, 2.5],
            x_axis_config={"numbers_to_include": range(-6, 7)},
            y_axis_config={"numbers_to_include": [-2, -1, 1, 2]}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        cos = axes.plot(lambda x: 1.5 * np.cos(x))
        cos.set_stroke(YELLOW, 4)
        self.play(Write(axes, run_time=5), lag_ratio=0.2)
        self.play(Write(labels))
        self.play(Create(cos), run_time=3)
        self.wait(3)


# 60. Координатная плоскость. Детали
class AxesAttributes(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-6.5, 6.5],
            y_range=[-2.5, 2.5],
            x_length=13,
            y_length=5,
            axis_config={
                "include_tip": True,
                "color": GREY,
                "stroke_width": 2,
                "font_size": 24,
                "tick_size": 0.07,
                "longer_tick_multiple": 1.5,
                "line_to_number_buff": 0.15,
                "decimal_number_config": {
                    "color": ORANGE,
                    "num_decimal_places": 0
                },
            },
            x_axis_config={
                "tip_width": 0.15,
                "tip_height": 0.15,
                "numbers_to_include": np.arange(-6, 7, 1),
                "numbers_with_elongated_ticks": [-3, 3],
            },
            y_axis_config={
                "tip_width": 0.15,
                "tip_height": 0.15,
                "numbers_to_include": [-2, -1, 1, 2],
                "tick_size": 0.08,
                "font_size": 25,
                "numbers_with_elongated_ticks": [-1, 1],
            }
        )
        x_lab = axes.get_x_axis_label("x", direction=DOWN, buff=0.2)
        y_lab = axes.get_y_axis_label("y", direction=LEFT, buff=0.2)
        labels = VGroup(x_lab.scale(0.6), y_lab.scale(0.6))

        # В v0.15.01 размеры стрелок (tip) не работают,
        # но разработчики знают о проблеме, планируют исправить.
        # Вы можете самостоятельно изменить значение
        # DEFAULT_ARROW_TIP_LENGTH в файле constants.py.

        cos = axes.plot(lambda x: 1.5 * np.cos(x), color=TEAL, x_range=[-6, 6])
        self.play(Write(axes, run_time=5), lag_ratio=0.2)
        self.play(Write(labels))
        self.play(Create(cos), run_time=3)
        self.wait(3)


# 61. Графики функций. Непосредственное создание
class AxesByHand(Scene):
    def construct(self):
        sin = FunctionGraph(lambda x: np.sin(x),
                            x_range=[-5.5, 5.5]).set_stroke(YELLOW, 3)
        x_axis = Arrow(6 * LEFT, 6 * RIGHT, tip_length=0.15, buff=0)
        y_axis = Arrow(2 * DOWN, 2 * UP, tip_length=0.15, buff=0)
        VGroup(x_axis, y_axis).set_stroke(LIGHT_GREY, 2)

        label = MathTex("x", "y", "y=\sin x").scale(0.8)
        label[0].next_to(5.9 * RIGHT, DOWN, buff=0.17)
        label[1].next_to(1.9 * UP, LEFT, buff=0.17)
        label[2].next_to(4.6 * LEFT + UP, UP, buff=0.15)

        self.play(GrowArrow(x_axis), GrowArrow(y_axis),
                  run_time=2.5)
        self.play(Create(sin), run_time=3)
        self.play(Write(label), run_time=2)
        self.wait(3)


# 62. Клетчатая решетка
class GridPlane(Scene):
    def construct(self):
        number_plane = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        self.play(Create(number_plane), run_time=4)
        polygon = Polygon(2 * UL, 3 * RIGHT + UP, 2 * DR, DOWN, 3 * DL)
        polygon.set_fill(DARK_BLUE, 0.4).set_stroke(WHITE, 3)
        self.play(DrawBorderThenFill(polygon), run_time=3)
        self.wait()
        self.play(FadeOut(polygon))

        arrow = Arrow(ORIGIN, 5 * RIGHT + 2 * UP, tip_length=0.2, buff=0)
        arrow.set_stroke(YELLOW, 3)
        label = MathTex("(5, 2)").next_to(5 * RIGHT + 2 * UP, UP)

        self.play(GrowArrow(arrow), run_time=1.5)
        self.play(Create(label))
        self.wait(3)

        # См. также ComplexPlane и PolarPlane


# 63. Линейная, обратная и возвратная анимации
class RateFuncAttribute(Scene):
    def construct(self):
        line_1 = DashedLine(
            LEFT, 4 * RIGHT,
            dash_length=0.2,
            dashed_ratio=0.7,
        ).set_stroke(GREY_A, 2)
        line_2 = line_1.copy().shift(UP)
        dot_1 = Dot(LEFT, 0.12, color=YELLOW, z_index=1)
        dot_2 = dot_1.copy().set_color(RED_E).shift(UP)

        # По умолчанию в анимациях rate_func=smooth
        self.play(
            Create(line_1, run_time=1.1),
            Create(line_2, run_time=1.2),
            rate_func=smooth
        )
        self.play(GrowFromCenter(dot_1), GrowFromCenter(dot_2))
        self.wait()
        self.play(
            ApplyMethod(dot_2.shift, 5 * RIGHT, rate_func=smooth),
            ApplyMethod(dot_1.shift, 5 * RIGHT, rate_func=linear),
            run_time=5
        )
        self.wait()
        self.play(FadeOut(line_1, line_2, dot_2), lag_ratio=0.1)

        arctg = FunctionGraph(lambda x: np.arctan(x),
                              x_range=[-5, 5]).set_stroke(GREY, 2)

        self.play(Create(arctg), run_time=1.5)
        self.wait()
        self.play(
            ApplyMethod(
                dot_1.move_to,
                5 * LEFT + np.arctan(5) * DOWN,
                run_time=2
            )
        )
        self.play(MoveAlongPath(dot_1, arctg), run_time=3)
        self.wait()
        self.play(
            MoveAlongPath(dot_1, arctg),
            rate_func=lambda t: smooth(1 - t),
            run_time=2
        )
        self.wait()
        self.play(
            MoveAlongPath(dot_1, arctg),
            rate_func=there_and_back,
            run_time=4
        )
        self.wait(3)

    # 64. Апдейтеры. Пересчет положения каждый кадр


class AlwaysRedrawMethod(Scene):
    def construct(self):
        dot = Dot()
        label_1 = MathTex("A").next_to(dot, UP)

        self.play(GrowFromCenter(dot), Write(label_1))
        self.wait()
        self.play(ApplyMethod(dot.shift, 2 * RIGHT),
                  run_time=4, rate_func=there_and_back)
        self.wait()

        label_2 = always_redraw(lambda: MathTex("B").next_to(dot, UP))
        self.play(FadeOut(label_1))
        self.play(FadeIn(label_2))
        self.play(ApplyMethod(dot.shift, 2 * RIGHT),
                  run_time=4, rate_func=there_and_back)
        self.wait(3)

    # 65. Геометрия. Принцип Ферма


class Fermat(Scene):
    def construct(self):
        # Однобуквенные заглавные переменные — двойное нарушение.
        # Но если очень хочется — можно.

        # Основные объекты
        A = Dot(3 * UL)
        B = Dot(2 * UR + RIGHT)
        P = Dot(LEFT)
        line = Line(4 * LEFT, 4 * RIGHT).set_stroke(BLUE, 2)
        AP = always_redraw(lambda:
                           Line(A.get_center(), P.get_center())
                           )
        BP = always_redraw(lambda:
                           Line(B.get_center(), P.get_center())
                           )
        # Симметричные точки и отрезки
        A_sym = Dot(3 * DL)
        line_sym = DashedLine(A_sym, A)
        right_angle = RightAngle(line, line_sym, 0.3)
        right_angle.set_stroke(BLUE, 2)
        AP_sym = always_redraw(lambda:
                               Line(A_sym.get_center(), P.get_center())
                               )
        # Лейблы
        label = MathTex("A", "B", "l", "A'").scale(0.75)
        label[0].next_to(A, UL, buff=0.1)
        label[1].next_to(B, UR, buff=0.1)
        label[2].next_to(4 * RIGHT, UL, buff=0.1)
        label[3].next_to(A_sym, DL, buff=0.1)
        label_P = always_redraw(
            lambda: MathTex("P")
            .scale(0.75)
            .next_to(P, UP, buff=0.15)
        )
        # Анимация задачи
        self.play(
            AnimationGroup(
                Create(line),
                GrowFromCenter(A),
                GrowFromCenter(B),
                lag_ratio=1
            )
        )
        self.play(
            Create(AP),
            Create(BP),
            Create(P),
            run_time=3
        )
        self.play(
            Write(label[:-1]),
            GrowFromCenter(label_P),
            run_time=2
        )
        self.wait()
        self.play(
            P.animate.shift(3 * RIGHT),
            rate_func=there_and_back,
            run_time=6
        )
        self.wait()

        # Симметричные построения
        self.play(
            AnimationGroup(
                Create(line_sym),
                GrowFromCenter(A_sym),
                GrowFromCenter(label[-1]),
                Create(right_angle),
                lag_ratio=0.2,
                run_time=2
            )
        )
        self.play(Create(AP_sym), run_time=1.5)
        self.play(
            P.animate.shift(3 * RIGHT),
            rate_func=there_and_back,
            run_time=6
        )
        self.wait()

        # Ответ
        shortest_way = Line(A_sym.get_center(),
                            B.get_center()).set_stroke(YELLOW, 3)
        self.play(Create(shortest_way), run_time=2)
        self.play(P.animate.shift(1.6 * RIGHT), run_time=3)
        self.wait(3)

        # P.S. Капслок уместен для глобальных констант,
        # однобуквенные переменные — для циклов.


# 66. Решение уравнения. Фигурные скобки для уточнений
class BraceNote(Scene):
    def construct(self):
        equation = MathTex(r"2\sin \tfrac{x}{2} \cos \tfrac{x}{2}",
                           "=", r"\cos (2\pi - x)").to_edge(UP, buff=1.7)
        sinx_eq_cosx = MathTex(r"\sin x = \cos x")
        tgx_eq_1 = MathTex(r"\tg x = 1")
        answer = MathTex(r"x = \tfrac{\pi}{4} + \pi n, \; "
                         r"n \in \mathbb{Z}")

        brace_sinx = Brace(equation[0], DOWN, sharpness=0.7)
        brace_cosx = Brace(equation[2], DOWN, sharpness=0.7)
        note_sinx = MathTex(r"\sin x").scale(0.7)
        note_cosx = MathTex(r"\cos x").scale(0.7)
        note_sinx.next_to(brace_sinx, DOWN)
        note_cosx.next_to(brace_cosx, DOWN)
        braces_notes = VGroup(brace_sinx, note_sinx,
                              brace_cosx, note_cosx)
        braces_notes.set_color(LIGHT_GREY)

        solution = VGroup(sinx_eq_cosx, tgx_eq_1, answer)
        solution.arrange(DOWN, buff=0.4)
        solution.next_to(braces_notes, DOWN, buff=0.5)

        self.play(Write(equation), run_time=3)
        self.wait()
        self.play(FadeIn(brace_sinx, shift=UP))
        self.play(GrowFromEdge(note_sinx, UP))
        self.wait()
        self.play(FadeIn(brace_cosx, shift=UP))
        self.play(GrowFromEdge(note_cosx, UP))
        self.wait()
        self.play(TransformFromCopy(equation, sinx_eq_cosx))
        self.wait()
        self.play(TransformFromCopy(sinx_eq_cosx, tgx_eq_1))
        self.wait()
        self.play(TransformFromCopy(tgx_eq_1, answer))
        self.wait(3)

    # 67. Вспомогательная формула. Композиция


class FormulaAnimation(Scene):
    def construct(self):
        identity = MathTex(r"a\cos{x}-b\sin{x}"
                           r"=\sqrt{a^2+b^2} \cos (x+\varphi )")
        note = MathTex(r"\cos{\varphi}="
                       r"\dfrac{a}{\sqrt{a^2+b^2}}, \, "
                       r"a \neq 0 \neq b").set_color(GREY)
        note.scale(0.8).next_to(identity, DOWN)

        formula = VGroup(identity, note).scale(0.75)
        formula.move_to(ORIGIN)

        self.play(GrowFromCenter(formula), run_time=1.5)
        frame = SurroundingRectangle(formula, buff=0.3)
        frame.set_stroke(WHITE, 1.5)
        self.play(Create(frame), run_time=2.5)
        self.wait()
        self.play(FadeOut(frame), run_time=1.5)
        self.wait(0.1)
        self.play(FadeOut(note), FadeOut(identity),
                  lag_ratio=0.1)
        self.wait(3)

    # 68. Выделение элементов треугольника


class Highlight(Scene):
    def construct(self):
        A, B, C = 3 * UR, 2 * LEFT, 4 * RIGHT
        triangle_ABC = Polygon(A, B, C)
        side_BA = Line(B, A)
        side_BC = Line(B, C)
        arc_B = Angle(side_BC, side_BA, radius=0.7)
        angle_B = VGroup(side_BA, side_BC, arc_B)
        angle_B.set_stroke(YELLOW, 3)
        label_BA = MathTex("x").next_to((A + B) / 2, UL, buff=0.1)
        label_BC = MathTex("y").next_to(side_BC, DOWN)

        self.play(Create(triangle_ABC), run_time=3)
        self.wait()
        self.play(Create(arc_B))
        self.play(arc_B.animate.scale(2, about_point=B),
                  rate_func=there_and_back, run_time=4)
        self.wait()
        self.play(Create(side_BA), run_time=2)
        self.play(GrowFromCenter(label_BA))
        self.wait()
        self.play(Create(side_BC), run_time=2)
        self.play(GrowFromCenter(label_BC))
        self.wait()
        self.play(Uncreate(side_BA), Uncreate(side_BC),
                  run_time=2)
        self.wait(3)


# 69. Движение точки с лейблом
class DotWithLabel(Scene):
    def construct(self):
        circle = Circle(radius=3).set_stroke(WHITE, 2)
        dot = Dot(3 * RIGHT, color=YELLOW)
        label = always_redraw(lambda:
                              MathTex("A").move_to(1.12 * dot.get_center())
                              )
        self.play(Create(circle), run_time=3)
        self.play(GrowFromCenter(dot))
        self.play(Write(label))
        self.wait()
        self.play(MoveAlongPath(dot, circle), run_time=6)
        self.wait(3)


# 70. Тригонометрическая окружность
class TrigonometricCircle(Scene):
    def construct(self):
        circ = Circle(3)
        x_axis = Arrow(4 * LEFT, 4 * RIGHT, tip_length=0.12)
        y_axis = x_axis.copy().rotate(PI / 2)
        trig_circ = VGroup(circ, x_axis, y_axis).set_stroke(WHITE, 2)
        self.play(Create(trig_circ, run_time=3), lag_ratio=0.1)

        zero = Tex("0").scale(0.85).shift(0.25 * DL)
        pi = MathTex(r"\pi").shift(3 * LEFT + 0.25 * UL)
        two_pi = MathTex(r"2\pi").shift(3 * RIGHT + 0.35 * UR)
        self.play(GrowFromCenter(zero))
        self.play(GrowFromCenter(pi))
        self.play(GrowFromCenter(two_pi))

        arc = Arc(3, PI, PI, color=YELLOW)
        dot = Dot(3 * RIGHT, 0.1, color=YELLOW).set_stroke(BLACK, 3)
        dot.rotate(11 * PI / 6, about_point=ORIGIN)
        self.play(Create(arc), run_time=2)

        root = MathTex(r"\dfrac{11\pi}{6}").scale(0.8)
        root.next_to(dot, DR, buff=0.1)
        self.play(FadeIn(root, scale=0), FadeIn(dot, scale=0))
        self.wait(3)


# 71. Теорема Пифагора
class Pythagoras(Scene):
    def construct(self):
        # Фигуры и лейблы
        triangle = Polygon(4 * UP, ORIGIN, 3 * RIGHT)
        triangle.set_stroke(YELLOW, 2.5).set_z_index(1)
        square = VGroup(Square(3), Square(4), Square(5))
        square.set_opacity(0.12)
        angle = Elbow(width=0.4).set_stroke(YELLOW, 1.5)
        theorem = MathTex("c^2 = a^2 + b^2")
        label = MathTex("a", "b", "c")

        # Расположение
        square[0].next_to(triangle, DOWN, buff=0)
        square[1].next_to(triangle, LEFT, buff=0)
        square[2].shift(3.5 * UR).rotate(np.arctan(3 / 4))
        theorem.move_to(square[2].get_center())
        label[0].next_to(triangle, DOWN, buff=0.15)
        label[1].next_to(triangle, LEFT, buff=0.15)
        label[2].next_to(2 * UP + 1.5 * RIGHT, UR, buff=0.15)
        picture = VGroup(triangle, square, label, angle, theorem)
        picture.move_to(ORIGIN).scale(0.75)

        # Анимация
        self.play(Create(triangle), run_time=3)
        self.play(GrowFromCenter(angle))
        self.play(GrowFromCenter(label))
        self.play(FadeIn(square[0], shift=UP))
        self.play(FadeIn(square[1], shift=RIGHT))
        self.play(FadeIn(square[2], shift=LEFT + 0.75 * DOWN))
        self.play(Write(theorem), run_time=2)
        box = SurroundingRectangle(theorem, buff=0.2)
        box.set_stroke(YELLOW, 2)
        self.play(ShowPassingFlash(box), run_time=2)
        self.wait(3)


# 72. Теорема Помпею
class Pompeiu(Scene):
    def construct(self):
        A = 3 * UP
        B = 1.5 * DOWN + 2.6 * LEFT
        C = 1.5 * DOWN + 2.6 * RIGHT
        circ = Circle(3).set_stroke(BLUE_D)
        triangle_ABC = Polygon(A, B, C).set_stroke(BLUE_D, 5)
        vertices = VGroup(Dot(A), Dot(B), Dot(C))
        vertices.set_color(BLUE).set_z_index(1)
        self.play(Create(circ), run_time=2)
        self.play(Create(triangle_ABC), Create(vertices), run_time=3)

        dot_P = Dot(2.6 * DOWN + 1.5 * LEFT, color=YELLOW, z_index=1)
        P_path = Arc(3, 4 * PI / 3, PI / 3)
        # Попробуйте три следующих строки переписать с помощью цикла.
        line_PA = always_redraw(lambda: Line(dot_P.get_center(), A))
        line_PB = always_redraw(lambda: Line(dot_P.get_center(), B))
        line_PC = always_redraw(lambda: Line(dot_P.get_center(), C))
        lines = VGroup(line_PA, line_PB, line_PC)
        self.play(GrowFromCenter(dot_P))
        self.play(Create(lines), run_time=3, lag_ratio=0.1)
        self.play(MoveAlongPath(dot_P, P_path), run_time=6,
                  rate_func=there_and_back)
        self.wait(3)


# 73. Неравенство Йенсена
class Jensen(Scene):
    def construct(self):
        def get_square(x):
            return x ** 2 / 5

        parabola = FunctionGraph(get_square, [-4.2, 4.2])
        x_axis = Arrow(5 * LEFT, 5 * RIGHT, tip_length=0.15)
        y_axis = Arrow(2 * DOWN, 4.5 * UP, tip_length=0.15)
        axes = VGroup(x_axis, y_axis).set_stroke(GREY_A, 2)

        dot_A = Dot(4 * LEFT + 3.2 * UP, color=YELLOW)
        dot_B = Dot(2 * RIGHT + 0.8 * UP, color=YELLOW)
        path_A = FunctionGraph(get_square, [-4, -2])
        path_B = FunctionGraph(get_square, [2, 4])
        line_AB = always_redraw(lambda:
                                Line(
                                    dot_A.get_center(),
                                    dot_B.get_center(),
                                    stroke_color=YELLOW,
                                    stroke_width=3
                                )
                                )
        picture = VGroup(parabola, path_A, path_B, dot_A, dot_B,
                         axes, line_AB).shift(2 * DOWN)
        jensen = MathTex(r"f\left(\frac{x_1+x_2}{2}\right)"
                         r"\leqslant \frac{f(x_1)+f(x_2)}{2}")
        jensen.scale(0.8).to_edge(UP, buff=0.5)

        self.play(Create(axes), run_time=2)
        self.play(Create(parabola), run_time=2.5)
        self.play(GrowFromCenter(dot_A), GrowFromCenter(dot_B))
        self.play(Create(line_AB), run_time=1.5)
        self.play(Write(jensen), run_time=3.5)
        self.play(
            MoveAlongPath(dot_A, path_A),
            MoveAlongPath(dot_B, path_B),
            run_time=6,
            rate_func=there_and_back,
        )
        self.wait(3)

    # 74. Метод интервалов


class Intervals(Scene):
    def construct(self):
        inequality = MathTex(r"\frac{2^x-2}{(x+1)^3} \geqslant 0")
        inequality.to_edge(UP, buff=1)
        solution = MathTex(r"\frac{x-1}{x+1} \geqslant 0")
        solution.next_to(inequality, DOWN)
        self.play(Write(inequality), run_time=3)
        self.wait()
        self.play(TransformFromCopy(inequality, solution))
        self.wait()

        arrow = Arrow(3 * LEFT, 3 * RIGHT, tip_length=0.2,
                      buff=0).set_stroke(YELLOW, 2)
        dot_1 = Dot(LEFT, color=BLACK).set_stroke(YELLOW, 2)
        dot_2 = Dot(RIGHT, 0.09, color=YELLOW).set_stroke(BLACK, 2)
        number_line = VGroup(arrow, dot_1, dot_2).shift(DOWN)
        self.play(Create(number_line), run_time=3)
        self.wait()

        label = MathTex("-1", "1", "x")
        label[0].next_to(dot_1, DOWN)
        label[1].next_to(dot_2, DOWN)
        label[2].next_to(arrow, DOWN)
        label[2].align_to(arrow, RIGHT)
        signs = MathTex("+", "-", "+").arrange(buff=1.5)
        signs.next_to(arrow, UP, buff=0.15)
        self.play(FadeIn(label, shift=UP),
                  lag_ratio=0.5, run_time=2)
        self.wait()
        self.play(FadeIn(signs, shift=DOWN),
                  lag_ratio=0.5, run_time=2)
        self.wait()

        answer = Tex(r"OTBET: $(-\infty ; -1)" +
                     r"\cup [1; +\infty)$", color=MAROON_B)
        answer.to_edge(DOWN, buff=1)
        self.play(Write(answer), run_time=3)
        self.wait(3)


# 75. Высота треугольника
class TriangleHeight(Scene):
    def construct(self):
        A = Dot(ORIGIN)
        B = Dot(2 * RIGHT + 6 * UP)
        C = Dot(7 * RIGHT)
        vertices = VGroup(A, B, C).move_to(ORIGIN)
        vertices.set_stroke(BLACK, 2)
        ABC = always_redraw(lambda:
                            Polygon(
                                A.get_center(),
                                B.get_center(),
                                C.get_center(),
                            )
                            )
        self.play(Create(ABC), Create(vertices), run_time=3)

        H = always_redraw(lambda:
                          Dot(B.get_center() + 6 * DOWN)
                          .set_stroke(BLACK, 2.5)
                          )
        BH = always_redraw(lambda:
                           Line(
                               B.get_center(),
                               H.get_center(),
                               z_index=-1
                           ).set_stroke(BLUE, 3)
                           )
        angle = always_redraw(lambda:
                              Elbow(width=0.3)
                              .set_stroke(BLUE, 2)
                              .next_to(H.get_center(), UR, buff=0)
                              )
        # Попробуйте поменять местами появление точки H
        # и отрезка BH. Видите разницу в результате?
        self.play(Create(H), Create(BH, run_time=2),
                  Create(angle), lag_ratio=0.3)
        self.play(B.animate.shift(3.5 * RIGHT), run_time=7,
                  rate_func=there_and_back)
        self.wait(3)


# 76. Логотип YouTube
class YouTubeLogo(Scene):
    def construct(self):
        rect = RoundedRectangle(1, height=4, width=5.64)
        rect.set_stroke(width=0).set_fill("#da271e", 1)
        triangle = Triangle(
            start_angle=0,
            color=WHITE,
            radius=1.3,
            fill_opacity=1,
        )
        triangle.round_corners(0.17)

        # Необходим шрифт YouTube Sans
        youtube = Text("YouTube", font="YouTube Sans")
        youtube.scale(2.4).next_to(rect, DOWN)
        logo = VGroup(rect, triangle, youtube).move_to(ORIGIN)

        self.play(Write(logo), run_time=3)
        self.wait(3)


