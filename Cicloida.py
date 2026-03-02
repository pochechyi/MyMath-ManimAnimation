from manim import *
import numpy as np
from manim import *
import math
pi = math.pi
e = math.e
def func(t):
    return np.array([t-np.sin(t),1-np.cos(t),2])

def func1(t):
    return np.array([np.cos(t) + np.emath.log((np.sin(t/2))/(np.cos(t/2))),np.sin(t),2])


class ExampleFunctionGraph(Scene):
    def construct(self):
        colors = ["#0000ff", "#8bff26", "#26e9ff", "#ff3c00", "#ffa600", "#ff4900"]
        f = ParametricFunction(
            func, t_range=np.array([-10,10])
        ).set_color(RED)
        f1 = ParametricFunction(
            func1, t_range=np.array([1, 10])
        ).set_color(RED)



        f.set_color_by_gradient(colors)
        f1.set_color_by_gradient(colors)
        ax = Axes(x_range=[-10, 10, 1], y_range=[-6, 6, 1], x_length=14, y_length=8)
        text = Text("Примеры параметрических функций", fill_color=RED,fill_opacity=0.99,font_size=50)
        text1 = Text("Автор: Гончарик Родион", fill_color=RED, fill_opacity=0.99, font_size=80)
        text2 = Text("Циклоида", fill_color=RED_B,fill_opacity=0.99,font_size=80)
        text3 = Text("1) ""Циклоида"" - кривая ,\n которую описывает точка окружности ,\n катящейся без скольжения \n по неподвижной окружности.",
                     fill_color=WHITE, fill_opacity=0.99, font_size=40,
                     t2c={"Циклоида": RED})
        text4 = Text("Уравнение циклоиды: " ,fill_color=WHITE, fill_opacity=0.99, font_size=40)

        text5 = MathTex(r"\begin{cases} x(t) = t - sin(t), \\"  
                    r"y(t) = 1 - cos(t) \end{cases}",fill_color=WHITE, fill_opacity=0.99, font_size=40)

        text4.next_to(text3,DOWN)
        text4.align_to(text3,LEFT)
        text5.next_to(text4, DOWN)
        text5.align_to(text4, LEFT)

        self.play(Write(text,run_time=1.5))
        self.wait(0.75)
        self.play(Unwrite(text,run_time=0.5))
        self.play(Write(text1,run_time=1.5))
        self.wait(0.75)
        self.play(Unwrite(text1,run_time=0.5))
        self.play(Write(text2.shift(2*UP), run_time=1))

        self.play(Write(text3, run_time=1))
        self.wait(1.5)
        self.play(Write(text4, run_time=0.75))
        self.play(Write(text5, run_time=0.75))
        self.wait(1.5)

        self.play(FadeOut(text2, shift=UP,run_time=0.7))
        self.play(Unwrite(text3,run_time=0.7))
        self.play(Unwrite(text4, run_time=0.7))
        self.play(FadeOut(text5, shift=DOWN,run_time=0.7))

        self.add(ax)
        self.wait(0.25)

        # Create circle and dot
        circ = Circle(color=BLUE).shift(7.8 * LEFT+ UP)
        dot = Dot(color=RED_D).move_to(circ.get_start())

        # Group dot and circle
        rolling_circle = VGroup(circ, dot)
        trace = TracedPath(circ.get_start)

        rolling_circle.add_updater(lambda m: m.rotate(-0.05))  # Rotate the circle

        self.add(trace, rolling_circle)  # add trace and rolling circle to the scene

        # Shift the circle to 8*RIGHT
        self.play((rolling_circle.animate.shift(24 * RIGHT)),run_time=8)
        self.play( Create(f.scale(1), run_time=8))
        self.wait(1.9)
        self.play(Uncreate(f.scale(1), run_time=3))
        self.play(Create(f1.scale(1), run_time=10))
        self.wait(1.9)
        self.play(Uncreate(f1.scale(1), run_time=3))




