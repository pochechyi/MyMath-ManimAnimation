from manim import *


class Prim (Scene):
    def construct(self):
        uslov = Text(" Задание  №12 профильной  математике " , font_size= 50 )
        self.play(Write(uslov , run_time=2))
        self.wait()
        self.play(Unwrite(uslov , run_time=1))

        uslov1 = Text(" Решите уравнение :")
        self.play(Write(uslov1.shift(1.2*UP)))

        uslov2 = MathTex(" \\ cos2x \\ =sin( x + \\frac{\pi}{2})\\ ", font_size=80 )
        self.play(Write(uslov2.shift(0.2*UP),run_time=2))
        self.wait(0.5)


        self.play(Unwrite(uslov2, run_time=0.7))
        self.play(Unwrite(uslov1, run_time=0.7))
        self.play(Unwrite(uslov,run_time=0.6))
        self.wait(1)

        resh = MathTex(" \\ cos2x \\ =sin( x + \\frac{\pi}{2})\\ ")
        self.play(Write(resh.shift(4.5*LEFT+3*UP)))

        resh1 = MathTex(r"\sin(x + \frac{\pi}{2}) ="," \cos x", tex_to_color_map={" \cos x":YELLOW})
        self.play(Write(resh1.shift(3.5 * RIGHT + 3 * UP)))
        self.wait(2)

        resh12 = MathTex(" \\ cos2x \\ =cosx")
        self.play(Transform(resh1,resh12.shift(5.21*LEFT+2.45*UP)))

        resh3 = MathTex(" \\ cos2x \\ -cosx \\ = 0")
        self.play(Write(resh3.shift(4.7*LEFT+1.75* UP) ))

        resh4 = MathTex(" \\ cos2x \\ = 2cos^2x \\ - 1", tex_to_color_map={"2cos^2x \\ - 1":YELLOW} )
        self.play(Write(resh4.shift(3.5*RIGHT+1.8*UP)))
        self.wait()

        resh5 = MathTex("(2cos^2x \\ - 1) \\ - cosx \\ = 0 ")
        self.wait()
        self.play(Transform(resh4,resh5.shift(4*LEFT+1.05*UP)))

        resh6 = MathTex("2cos^2x \\ - cosx \\ - 1 \\ = 0")
        self.play(Write(resh6.shift(4.1*LEFT+0.3*UP)))

        resh7 = Text("Замена : cosx = t", font_size= 30  )
        self.play(Write(resh7.shift(5.2*LEFT+0.4 * DOWN)))
        self.wait(1)

        resh8 = MathTex("2t^2 - t - 1 = 0")
        self.play(Write(resh8.shift(LEFT*5.1+0.9*DOWN)))
        self.wait()
        resh9 = MathTex("D = \\ b^2 - 4ac")
        self.play(Write(resh9.shift(LEFT*5.2+1.5*DOWN)))
        self.wait(1)

        resh10 = MathTex("D = (-1)^2 - 4*2*(-1)=")
        self.play(Write(resh10.shift(LEFT*3.8+2.2*DOWN)))
        self.wait(0.5)

        resh11 = MathTex(" = 1 + 8 = 9")
        self.play(Write(resh11.shift(LEFT*5.4+2.8*DOWN)))
        self.wait(1)

        wer = MathTex("t_1 = \\frac{-b + \\sqrt{D}}{2a}\\ = \\frac{1 + 3}{4} = \\frac{4}{4} = 1 ")
        self.play(Write(wer.shift(2.5*RIGHT+3*UP),run_time=3))

        wer1 = MathTex("t_2 = \\frac{-b + \\sqrt{D}}{2a}\\ = \\frac{1 - 3}{4} = \\frac{-2}{4} = -\\frac{1}{2}\\")
        self.play(Write(wer1.shift(3*RIGHT+1.9*UP),run_time=3 ))

        wer2 = Text("Обратная замена : cosx = t ",font_size= 28)
        self.play(Create(wer2.shift(RIGHT*3+UP*0.8),run_time=0.5))
        self.wait(1.5)

        wer3 = MathTex(r"\left[ \begin{gathered} "
                       r" cosx = 1, \\ cosx= -\frac{1}{2} \hfill "
                       r"\end{gathered} \right.")
        self.play(Write(wer3.shift(DOWN*0.5)))
        self.wait(1.5)

        wer4 = MathTex("\\Leftrightarrow")
        self.play(Write(wer4.shift(1.5*RIGHT+0.5*DOWN)))

        wer5 = MathTex(r"\left[ \begin{gathered} "
                       r" x = 2 \pi k, k \in Z \\ x = \pm \frac{2\pi}{3} + 2 \pi n,n \in Z \hfill "
                       r"\end{gathered} \right.")

        self.play(Write(wer5.shift(4.5*RIGHT+0.5*DOWN)))

        self.play(Unwrite(resh,run_time=0.2 ))
        self.remove(resh1)
        self.play(Unwrite( resh3,run_time=0.2))
        self.play(Unwrite(resh4,run_time=0.2))
        self.play(Unwrite(resh5,run_time=0.2))
        self.play(Unwrite(resh6,run_time=0.2))
        self.play(Unwrite(resh7,run_time=0.2))
        self.play(Unwrite(resh8,run_time=0.2))
        self.play(Unwrite(resh9,run_time=0.2))
        self.play(Unwrite(resh10,run_time=0.2))
        self.play(Unwrite(resh11,run_time=0.2))
        self.play(Unwrite(wer,run_time=0.2))
        self.play(Unwrite(wer1,run_time=0.2))
        self.play(Unwrite(wer2,run_time=0.2))
        self.play(Unwrite(wer3,run_time=0.2))
        self.play(Unwrite(wer4,run_time=0.2))
        self.play(Unwrite(wer5,run_time=0.2))


        avtor = Text("Автор : Родион Гончарик")
        self.play(Create(avtor))
























#(r"\left[ \begin{gathered} "
#r"x = \pm 1, \\ x \geqslant 3. \hfill "
#r"\end{gathered} \right.")



#("\left[ \\begin{gathered} "
#"cosx = 1 \\ cosx = \\frac{-1}{2}"
#"\\end{gathered} \\right.")






