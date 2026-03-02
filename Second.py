from manim import *


class rod (Scene):
    def construct(self):
        arrow = Arrow()
        arrow1 = Arrow(LEFT, RIGHT * 1)
        arrow2 = Arrow(LEFT, RIGHT * 2, tip_length= 0.4 )
        arrow3 = Arrow(LEFT, RIGHT * 3, tip_length= 0.6 )
        arrow4 = Arrow(LEFT, RIGHT * 4, tip_length= 0.8 )
        arrow40 = DoubleArrow(LEFT, RIGHT * 4, tip_length= 0.8 )
        arrow5 = DoubleArrow(LEFT , RIGHT)
        arrow6 = DoubleArrow(LEFT * 2 , RIGHT , tip_length= 0.4)
        arrow7 = DoubleArrow(LEFT * 3 , RIGHT , tip_length= 0.6)
        arrow8 = DoubleArrow(LEFT * 4 , RIGHT , tip_length= 0.8)
        arrow9 = CurvedArrow(LEFT , RIGHT)
        arrow10 = CurvedArrow(LEFT * 2 , RIGHT * 2  , radius= 3)
        arrow11 = CurvedArrow(LEFT *3 , RIGHT * 3 , radius=4)
        arrow12 = CurvedArrow(LEFT * 4 , RIGHT * 4, radius=5)
        arrow13 = CurvedArrow(RIGHT  , UP * 2)
        arrow14 = Arrow(UP* 2)
        arrow15 = CurvedArrow(LEFT , UP * 2)
        arrow16 = CurvedArrow(RIGHT, UP * 3, radius=3)
        arrow17 = Arrow(UP * 3)
        arrow18 = CurvedArrow(LEFT, UP * 3, radius=3)
        arrow19 = CurvedArrow(RIGHT *2, UP * 4, radius=4)
        arrow20 = Arrow(UP * 4)
        arrow21 = CurvedArrow(LEFT*2, UP * 4, radius=4)
        arrow22 = CurvedArrow(RIGHT*3, UP * 5, radius=5)
        arrow23 = Arrow(UP * 5)
        arrow24 = CurvedArrow(LEFT*3, UP * 5, radius=5)


        self.play(Create(arrow))
        self.play(Transform(arrow,arrow1))
        self.play(Transform(arrow1,arrow2))
        self.play(Transform(arrow2, arrow3))
        self.play(Transform(arrow3, arrow4))
        self.remove(arrow)
        self.wait(1)
        self.remove(arrow1)
        self.wait(1)
        self.remove(arrow2)

        self.wait(1)
        self.play(Transform(arrow4,arrow5))
        self.play(Transform(arrow5,arrow6))
        self.play(Transform(arrow6,arrow7))
        self.play(Transform(arrow7,arrow8))
        self.play(Transform(arrow4,arrow40))
        self.remove(arrow5)
        self.wait(1)
        self.remove(arrow6)
        self.wait(1)

        self.play(Transform(arrow8,arrow9))
        self.play(Transform(arrow9,arrow10))
        self.play(Transform(arrow10,arrow11))
        self.play(Transform(arrow11,arrow12))

        self.play(Create(arrow13))
        self.play(Create(arrow14))
        self.play(Create(arrow15))
        self.play(Create(arrow16))
        self.play(Create(arrow17))
        self.play(Create(arrow18))
        self.play(Create(arrow19))
        self.play(Create(arrow20))
        self.play(Create(arrow21))

        self.wait(1)


















