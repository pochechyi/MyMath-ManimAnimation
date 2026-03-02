from manim import *
import numpy as np
from manim import *
import math
pi = math.pi
e = math.e



class ExampleFunctionGraph(Scene):
    def construct(self):
        colors = ["#0000ff", "#8bff26", "#26e9ff", "#ff3c00", "#ffa600", "#ff4900"]
        self.wait(1)
        text_rus = Text("Ядро оператора", color=RED, font_size=90)
        text_math = MathTex("P(\mathbf{\partial})", color=RED, font_size=110)
        title = VGroup(text_rus, text_math).arrange(RIGHT, buff=0.3)
        self.play(Write(title))
        self.wait(1.2)


        # Литература
        literature = Text(
            """Лит-ра: Элементы общей теории диф-ых уравнений\nАвтор: Гончарик Родион \nГруппа: 3823Б1МА1""",
            color=RED,
            font_size=24
        ).to_edge(DOWN)

        self.play(Write(literature))
        self.wait(2.7)
        self.play(Unwrite(title))
        self.play(Unwrite(literature))

        # Определение ядра
        definition = Text(
            "\"Ядром Оператора\" - называется класс функций\n"
            "u ∈ L2(Ω) таких, что P(d)u = 0.",
            color=WHITE,
            font_size=36
        )
        definition[:16].set_color_by_gradient(GREEN, BLUE)
        self.play(Write(definition))
        self.wait(2)
        self.play(Unwrite(definition,run_time=0.9))


        #Выкладка
        line1 = Text("Будем говорить, что P(∂)u ∈ L₂(Ω)", font_size=26)
        line2 = MarkupText('для u ∈ L₂( <span foreground="green">Ω</span>), если существует функция', font_size=26)
        line3 = MarkupText('g ∈ L₂(<span foreground="green">Ω</span>) такая, что для любой функции', font_size=26)
        line4 = MarkupText('φ ∈ <span foreground="blue">D</span>(<span foreground="green">Ω</span>) выполняется:',
                           font_size=26)
        line5 = MathTex(r"\int_{\Omega} u(x)P^*(\partial)\varphi(x)dx = \int_{\Omega} g(x)\varphi(x)dx", font_size=48)
        line6 = Text("при этом по определению считается, что P(∂)u = g.", font_size=26)

        # Объединяем все строки вертикально
        all_lines = VGroup(line1, line2, line3, line4, line5, line6)
        all_lines.scale(0.8)
        all_lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        all_lines.move_to(UL * 2.25 + LEFT)  # UL - верхний левый угол

        self.wait(0.5)
        arrow = MathTex(r"\Rightarrow", font_size=85)
        # Правый блок
        right_line1 = Text("Функция", font_size=26)
        right_line2 = MarkupText('u ∈ L₂(<span foreground="green">Ω</span>) принадлежит ядру тогда', font_size=26)
        right_line3 = Text("и только тогда, когда", font_size=26)
        right_line4 = MathTex(r"\int_{\Omega} u(x)P^*(\partial)\varphi(x)dx = 0", font_size=48)
        right_line5 = MarkupText('при всех φ ∈ <span foreground="blue">D</span>(<span foreground="green">Ω</span>).',
                                 font_size=26)

        right_block = VGroup(right_line1, right_line2, right_line3, right_line4, right_line5)
        right_block.arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        # Верхняя строка
        top_row = VGroup(all_lines, arrow, right_block)
        top_row.arrange(RIGHT, buff=0.3)
        top_row.move_to(UP * 1.5)

        # Нижний текст
        bottom_text = MarkupText(
            'В дальнейшем ядро оператора P(∂) будет обозначаться через Ker(P(∂); <span foreground="green">Ω</span>).',
            font_size=22
        )

        omega_text = MarkupText(
            '<span foreground="green">Ω</span> - открытое ограниченное подмножество пространства Rⁿ', font_size=20)
        D_text = MarkupText(
            '<span foreground="blue">D</span>(<span foreground="green">Ω</span>) - класс пробных функций  бесконечно диф-мых финитных функций',
            font_size=22
        )
        bottom_text.next_to(top_row, DOWN, buff=0.5)
        omega_text.next_to(bottom_text, DOWN, buff=0.5)
        D_text.next_to(omega_text, DOWN, buff=0.5)
        right_block.align_to(all_lines, UP)

        # Анимация
        self.play(LaggedStartMap(Write, all_lines, lag_ratio=0.15))
        self.wait(2)
        self.play(GrowFromCenter(arrow))
        self.wait(0.5)
        self.play(Write(right_block))
        self.wait(2.5)
        self.play(Write(bottom_text))
        self.wait(1)
        self.play(Write(omega_text))
        self.wait(2)
        self.play(Write(D_text))
        self.wait(4)

        self.play(FadeOut(all_lines, shift=LEFT))
        self.play(ShrinkToCenter(arrow))
        self.play(FadeOut(right_block, shift=RIGHT))
        self.play(FadeOut(bottom_text, shift=DOWN))
        self.play(FadeOut(omega_text, shift=DOWN))
        self.play(FadeOut(D_text, shift=DOWN))
        self.wait(1)

        #Lemmachhka
        # part1 = Text(r"Лемма.", font_size=36)
        # part2 = MathTex(r"\text{Ker}(P(\mathbf{\partial});Q)", font_size=36)
        # part3 = MathTex(r"-", font_size=36)
        # part4 = Text(r"{линейное подпространство пространства}", font_size=36)
        # part5 = MathTex(r"L_2(Q),", font_size=36)
        # part6 = Text(r"{замкнутое в нем}.", font_size=36)

        # Располагаем части
        # group1 = VGroup(part1, part2, part3, part4).arrange(RIGHT, buff=0.1)
        # group2 = VGroup(part5, part6).arrange(RIGHT, buff=0.1)
        # full_text = VGroup(group1, group2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        # full_text.move_to(ORIGIN)
        #
        # # Анимация появления по частям
        # self.play(Write(part1))
        # self.wait(0.3)
        # self.play(Write(part2))
        # self.wait(0.3)
        # self.play(Write(part3))
        # self.wait(0.3)
        # self.play(Write(part4))
        # self.wait(0.5)
        # self.play(Write(part5))
        # self.wait(0.3)
        # self.play(Write(part6))
        # self.wait(2)


