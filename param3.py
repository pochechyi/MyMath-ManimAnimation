from manim import *
import numpy as np
from manim import *
import math
pi = math.pi
e = math.e
def func(t):
    return np.array([6.2*(np.cos(t)-(np.cos(3.1*t)/3.1)) , 6.2*(np.sin(t)-(np.sin(3.1*t)/3.1)),2])



class ExampleFunctionGraph(Scene):
    def construct(self):
        colors = ["#0000ff", "#8bff26", "#26e9ff", "#ff3c00", "#ffa600", "#ff4900"]
        f = ParametricFunction(
            func, t_range=np.array([0,20*pi])
        ).set_color(RED)
        f.set_color_by_gradient(colors)
        ax = Axes(x_range=[-10, 10, 1], y_range=[-6, 6, 1], x_length=14, y_length=8)
        text = Text("Параметрическая функция", fill_color=RED,fill_opacity=0.99,font_size=80)
        text1 = Text("автор: Гончарик Родион", fill_color=RED, fill_opacity=0.99, font_size=80)

        self.play(Write(text,run_time=1.5))
        self.play(Unwrite(text,run_time=0.5))
        self.play(Write(text1,run_time=1.5))
        self.play(Unwrite(text1,run_time=0.5))
        self.add(ax)
        self.wait(0.5)
        self.play(Create(f.scale(0.25), run_time=10))
        self.wait(1)