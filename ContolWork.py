from manim import *
import numpy as np
from manim import *
import math
pi = math.pi
e = math.e

class ControlWORK(Scene):
    def construct(self):
        colors = ["#0000ff", "#8bff26", "#26e9ff", "#ff3c00", "#ffa600", "#ff4900"]

        Begin1 = Text("Контрольная работа №2 ", fill_color=RED,fill_opacity=0.99,font_size=50)
        self.play(Write(Begin1.shift(2*UP),run_time=1.25))
        self.wait(0.25)

        Begin2 = Text("Автор: Гончарик Родион", fill_color=RED, fill_opacity=0.99, font_size=50).next_to(Begin1,2.5*DOWN)
        self.play(Write(Begin2, run_time=1.5))
        self.wait(0.75)
        self.play(Unwrite(Begin1, run_time=0.5))
        self.play(Unwrite(Begin2, run_time=0.5))

        Begin3 = Text("№ 21.24 (4) ", fill_color=WHITE, fill_opacity=0.99, font_size=20)
        self.play(Write(Begin3.shift(3.5*UP+6*LEFT), run_time=1.5))
        self.wait(0.75)

        Begin4 = MathTex(r"\begin{cases} x(t) = t^3 - 3t, \\"  
                    r"y(t) =  (\frac{t-1}{t}\ )^2  \end{cases}",fill_color=WHITE, fill_opacity=0.99, font_size=35)

        Begin4.next_to(Begin3,DOWN)
        Begin4.align_to(Begin3,LEFT)
        self.play(Write(Begin4,run_time=0.5))
        self.wait(0.75)


        Func1 = Text("Исследование функции x(t):",fill_color=WHITE, fill_opacity=0.99, font_size=25)
        Func1.next_to(Begin4, DOWN)
        Func1.align_to(Begin3, LEFT)
        self.play(Write(Func1, run_time=0.5))
        self.wait(0.75)

        Func15 = MathTex(r"1)  x \in (-  \infty , +  \infty) \\", fill_color=WHITE,
                        fill_opacity=0.99, font_size=40)
        Func15.next_to(Func1, DOWN)
        Func15.align_to(Begin3, LEFT)
        self.play(Write(Func15, run_time=0.5))
        self.wait(1.75)

        Func2 = MathTex(r"2) x(-t) = (-t)^3 - 3(-t) =\\= -t^3 + 3t = - (t^3 - 3t) ",fill_color=WHITE, fill_opacity=0.99, font_size=40)
        Func2.next_to(Func15, DOWN)
        Func2.align_to(Begin3, LEFT)
        self.play(Write(Func2, run_time=0.5))
        self.wait(1.75)

        Func3 = Text("- Функция нечетная ", fill_color=WHITE, fill_opacity=0.99, font_size=30)
        Func3.next_to(Func2, DOWN)
        Func3.align_to(Begin3, LEFT)
        self.play(Write(Func3, run_time=0.5))
        self.wait(1.25)

        Func4 = Text("3) Функция не периодична ", fill_color=WHITE, fill_opacity=0.99, font_size=30)
        Func4.next_to(Func3, DOWN)
        Func4.align_to(Begin3, LEFT)
        self.play(Write(Func4, run_time=0.5))
        self.wait(1.25)


        Func5 = MathTex(r"4) k = \lim_{x \to \infty} \ \frac{x(t)}{t}\  =  \lim_{x \to \infty} t^2 -3 \Rightarrow \infty  ",fill_color=WHITE, fill_opacity=0.99, font_size=40)
        Func5.next_to(Func4, DOWN)
        Func5.align_to(Begin3, LEFT)
        self.play(Write(Func5, run_time=0.95))
        self.wait(2.25)
        Func55 = Text(r"Функция не имеет горизонтальных и вертикальных ассимптот",fill_color=WHITE, fill_opacity=0.99, font_size=25)
        Func55.next_to(Func5, DOWN)
        Func55.align_to(Begin3, LEFT)
        self.play(Write(Func55, run_time=0.95))
        self.wait(1.25)


        Func6 =MathTex(r"5) x'(t) = 3t^2 - 3 = 3(t- 1)(t+1)",fill_color=WHITE, fill_opacity=0.99, font_size=40)
        Func6.next_to(Func1,RIGHT*10)
        Func6.align_to(Func1, DOWN)
        self.play(Write(Func6, run_time=0.95))
        self.wait(1.25)

        arrow = Arrow(3 * LEFT, 3 * RIGHT, tip_length=0.2,
                      buff=0).set_stroke(WHITE, 2)

        arrow2 = Arrow(LEFT,UR, tip_length=0.2,
                       buff=0).set_stroke(YELLOW, 2)
        arrow2.next_to(arrow, DOWN*0.3)
        arrow2.align_to(Func6, LEFT)


        arrow1 =Arrow(UL,RIGHT, tip_length=0.2,
                      buff=0).set_stroke(YELLOW, 2)
        arrow1.next_to(arrow2, RIGHT)


        arrow3 = Arrow(LEFT,UR, tip_length=0.2,
                       buff=0).set_stroke(YELLOW, 2)
        arrow3.next_to(arrow1, RIGHT)

        dot_1 = Dot(LEFT, color=YELLOW).set_stroke(WHITE, 2)
        dot_2 = Dot(RIGHT, 0.09, color=YELLOW).set_stroke(WHITE, 2)
        number_line = VGroup(arrow, dot_1, dot_2).shift(DOWN)
        number_line.next_to(Func6,DOWN*3)
        number_line.align_to(Func6, LEFT)
        self.play(Create(number_line), run_time=2)
        self.wait()

        label = MathTex("-1", "1", "t")
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

        self.play(FadeIn(arrow2.scale(0.6), shift=UP), run_time=2)
        self.wait(0.25)
        self.play(FadeIn(arrow1.scale(0.6), shift=UP), run_time=2)
        self.wait(0.25)
        self.play(FadeIn(arrow3.scale(0.6), shift=UP), run_time=2)
        self.wait(0.25)


        Func7 = MathTex(r"6) x''(t) = (3t^2 -3)'=6t",fill_color=WHITE, fill_opacity=0.99, font_size=40)
        Func7.next_to(arrow2, DOWN * 0.3)
        Func7.align_to(Func6, LEFT)
        self.play(Write(Func7,run_time=1.45))
        self.wait()

        arrow4 = Arrow(3 * LEFT, 3 * RIGHT, tip_length=0.2,
                      buff=0).set_stroke(WHITE, 2)
        dot_3 = Dot(color=YELLOW).set_stroke(WHITE, 2)
        number_line1 = VGroup(arrow4, dot_3)
        number_line1.next_to(Func7,DOWN*2)
        number_line1.align_to(Func7,LEFT)
        self.play(Create(number_line1), run_time=1.5)
        sign = MathTex("-", "+").arrange(buff=2.5)
        sign.next_to(arrow4, UP, buff=0.15)
        lab = MathTex("0","t")
        lab[0].next_to(dot_3, DOWN)
        lab[1].next_to(arrow4, DOWN)
        lab[1].align_to(arrow4, RIGHT)
        self.play(FadeIn(lab, shift=DOWN),
                  lag_ratio=0.5, run_time=2)
        self.wait()
        self.play(FadeIn(sign, shift=DOWN),
                  lag_ratio=0.5, run_time=2)
        arc1=Arc(angle=pi)
        arc1.next_to(Func5,RIGHT*2.5)
        arc2 = Arc(angle=-pi)
        arc2.next_to(arc1,RIGHT*4)
        self.play(Create(arc1.scale(0.4),run_time=1.25))
        self.play(Create(arc2.scale(0.4), run_time=1.25))
        self.wait(3)


        Del = VGroup(Func15,Func2,Func3,Func4,Func5,Func55,Func6,Func7,arrow1,arrow2,arrow3,number_line1,number_line,label,sign,signs,label,lab,arc1,arc2)
        self.play(Uncreate(Del,run_time=4))
        self.wait(1.5)

        Func8 = Text("7)Значение точек максимума и минимума:\n x(-1)= -1+3=2 , x(1)=1-3=2",fill_color=WHITE, fill_opacity=0.99, font_size=20)
        Func8.next_to(Func1,DOWN)
        Func8.align_to(Func1,LEFT)
        self.play(Write(Func8,run_time=1.25))
        self.wait(1.25)
        Func9 = Text("7.25)Замечание: функция \n в точках x(-1) и x(1) будет 'гладенькой' ,\n так как производная в этих точках равна нулю ", fill_color=WHITE,
                        fill_opacity=0.99, font_size=20)
        Func9.next_to(Func8, DOWN)
        Func9.align_to(Func1, LEFT)
        self.play(Write(Func9, run_time=1.25))
        self.wait(1.25)

        Func10 = Text(
            "7.5)Функция пересекает ось OX \n в точках корень из трех и минус корень из трех ",
            fill_color=WHITE,
            fill_opacity=0.99, font_size=20)
        Func10.next_to(Func9, DOWN)
        Func10.align_to(Func1, LEFT)
        self.play(Write(Func10, run_time=1.25))
        self.wait(1.25)

        Func10 = Text("8) График функции x(t): ", fill_color=WHITE,
                     fill_opacity=0.99, font_size=20)

        Func10.next_to(Func1,RIGHT*14)
        self.play(Write(Func10.shift(UP*1.75),run_time=1.25))
        self.wait(1.25)

        axes = Axes(
            x_range=[-4.5, 4.5],
            y_range=[-2.5, 3.0],
            x_length=6.25,
            y_length=6.25,
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
                "numbers_to_include": [-4,-3,-2, -1, 0, 1, 2,3,4],
                "numbers_with_elongated_ticks": [-3, 3],
            },
            y_axis_config={
                "tip_width": 0.15,
                "tip_height": 0.15,
                "numbers_to_include": [-2, -1, 0, 1, 2],
                "tick_size": 0.08,
                "font_size": 25,
                "numbers_with_elongated_ticks": [-1, 1],
            }
        )

        axes.next_to(Func10, DOWN)
        x_lab = axes.get_x_axis_label("t", direction=DOWN, buff=0.2)
        y_lab = axes.get_y_axis_label("x", direction=LEFT, buff=0.2)
        labels = VGroup(x_lab.scale(0.6), y_lab.scale(0.6))
        graph1 = axes.plot(lambda x: x*x*x - 3 * x, color=TEAL, x_range=[-4, 3])
        self.play(Write(axes, run_time=5), lag_ratio=0.2)
        self.play(Write(labels))
        self.play(Create(graph1), run_time=3)
        self.wait(6)




























