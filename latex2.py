from manim import *


class Bra(Scene):
    def construct(self):
        equation = MathTex("2\\sin \\tfrac{x}{2} \cos \\tfrac{x}{2}",
                           "=", "\cos (2\pi - x)").to_edge(UP, buff=1.7)
        sinx_eq_cosx = MathTex("\sin x = \cos x")
        tgx_eq_1 = MathTex("tg x = 1")
        answer = MathTex("x = \\tfrac{\pi}{4} + \pi n, \; "
                         "n \in \mathbb{Z}")

        brace_sinx = Brace(equation[0], DOWN, sharpness=0.7)
        brace_cosx = Brace(equation[2], DOWN, sharpness=0.7)
        note_sinx = MathTex("\sin x").scale(0.7)
        note_cosx = MathTex("\cos x").scale(0.7)
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
