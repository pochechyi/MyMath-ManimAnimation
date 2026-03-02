from manim import *


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