from manim import *


class home(Scene):
    def construct(self):

        dot = Dot(radius=0.05)
        self.play(Create(dot))

        circ1 = Circle(radius=1 , color=RED)
        self.play(GrowFromCenter(circ1))
        self.wait(0.05)

        circ2 = Circle(radius=2, color=RED)
        self.play(GrowFromCenter(circ2))
        self.wait(0.05)

        circ3 = Circle(radius=3, color=RED)
        self.play(GrowFromCenter(circ3))

        self.remove(dot,circ1,circ2,circ3)

        rec1 = RegularPolygon(n = 8 , color= BLUE, radius=3)
        self.play(GrowFromCenter(rec1))

        sq = Square(4.25 , color= WHITE)
        self.play(FadeIn(sq))

        circ4 = Circle(radius=2.12 , color=RED)
        self.play(Create(circ4,run_time=2))

        trian = Triangle(radius=2.12, color=BLUE)
        self.play(GrowFromCenter(trian))

        self.remove(rec1,sq,circ4,trian)

        trian1 =Polygon( 1.25 *DOWN + 1.47 * LEFT , 1.35 * UP + 1.47 * LEFT, 1.25 * DOWN + 1.5 * RIGHT )
        self.play(FadeIn(trian1, shift=UP))

        cir5 = Circle(radius=2 ,
                      color=RED,
                      )
        self.play(Create(cir5, run_time=1))

        kostul1 = Line( DOWN + LEFT * 1.2, LEFT * 1.45 + DOWN , color=WHITE)
        kostul2 = Line(LEFT * 1.2 + DOWN *1.25, LEFT *1.2 + DOWN, color=WHITE )
        self.play(Create(kostul1,run_time=0.5))
        self.play(Create( kostul2,run_time=0.5))

        self.remove(trian1 , cir5 , kostul2 , kostul1)

        six = Star (n = 6, color=BLUE)
        self.play(GrowFromCenter(six))

        arc1 = Arc(radius=1.2,
                   start_angle= PI / 6 ,
                   angle= PI / 3
        )
        self.play(Create(arc1 ))

        arc2 =Arc(radius=1.2 , start_angle= 2.5 * PI / 3 , angle= PI / 3)
        self.play(Create(arc2))

        arc3 = Arc(radius=1.2 , start_angle= 3 * PI / 2 , angle= PI / 3)
        self.play(Create(arc3))

        self.remove(six , arc3 , arc2 , arc1)

        cir6 = Circle(radius=3 , color = ORANGE)
        self.play(Create(cir6))

        lian1 = Arrow(4.1*LEFT , RIGHT*4.1, tip_length= 0.2)
        self.play(FadeIn(lian1,shift= RIGHT))

        lian2 = Arrow(DOWN * 4.1, UP * 4.1 , tip_length=0.2 )
        self.play(FadeIn(lian2,shift=UP))

        arc4 = CurvedArrow(3.3 * RIGHT + 0.02* UP, 3.3 *UP , radius= 3.5, tip_length=0.2)
        self.play(Create(arc4))

        self.play(FadeOut(cir6,lian2,lian1,arc4))

        line1 = Line(3 * LEFT ,3 * RIGHT )
        self.play(Create(line1))

        line2 = Line(3 * LEFT + 4 * DOWN , 4 * UP + 3 * RIGHT)
        self.play(Create(line2))

        ugol = Angle(line1 , line2 , radius=1)
        self.play(Create(ugol,run_time=0.5))

        self.play(FadeOut(line1,line2,ugol))

        trian2 = Polygon(0.82 * DOWN + 0.8 * LEFT, 1.9 * UP + 0.8 * LEFT, 0.82 * DOWN + 1.95 * RIGHT)
        self.play(Create(trian2, shift=UP))

        cir7 = Circle(radius=0.75 , color= ORANGE)
        self.play(GrowFromCenter(cir7))

        dot1 = Dot(radius=0.05)
        self.play(GrowFromCenter(dot1))

        line3 = Line(0.9* LEFT + 0.5 *UP , 0.7 * LEFT + 0.5 *UP)
        self.play(FadeIn(line3 , shift=LEFT,run_time=0.5))

        line4 = Line( 0.9 * DOWN + 0.8 * RIGHT ,  0.73 * DOWN + 0.8 * RIGHT)
        line5 = Line(0.9 * DOWN + 0.9 * RIGHT, 0.73 * DOWN + 0.9 * RIGHT)
        self.play(FadeIn(line4, line5, shift=UP,run_time=0.5))

        self.play(FadeOut(trian2,dot1,line5,line4,line3,cir7))

        rec2 = RegularPolygon(n=6, color=BLUE, radius=3)
        self.play(GrowFromCenter(rec2))

        lone = DashedLine(DOWN * 4 , UP * 4)
        self.play(FadeIn(lone , shift=UP))

        lone1 = CurvedDoubleArrow( 1.55 * RIGHT + 2.7 * UP, 1.55 * LEFT + 2.7 * UP, tip_length=0.2 )
        self.play(FadeIn(lone1, shift=DOWN))

        self.play(FadeOut(rec2,lone,lone1))

        poli = DashedVMobject(RoundedRectangle(width=10, height=6),num_dashes=200)
        self.play(GrowFromCenter(poli))

        tri1 = Polygon(LEFT + DOWN * 1.4, LEFT + UP * 1.4 , RIGHT * 1.8 )
        tri1.round_corners(radius=0.1)
        self.play(GrowFromCenter(tri1))

        self.play(FadeOut(poli,tri1))

        duga = CubicBezier (
            3 * LEFT + 2 * DOWN,
            7 * UP  ,
            3 * RIGHT + 7 * DOWN ,
            4 * RIGHT + 3 * UP  )
        self.play(Create(duga))

        stre = Arrow(3* LEFT + 2 * DOWN , 4 * RIGHT + 3 * UP, tip_length=0.1)
        self.play(Create(stre))

        self.remove(duga,stre)

        sev = Circle(radius=2 , color = ORANGE)
        self.play(Create(sev))

        urc = Arc(start_angle= 7 * PI / 6 , angle= 2 *PI / 3 , radius= 1.5)
        self.play(Create(urc))

        urc1 = ArcBetweenPoints(1.2 *RIGHT + UP , 0.3 * RIGHT + UP , radius= 1)
        self.play(GrowFromCenter(urc1))

        urc2 = ArcBetweenPoints(0.3 * LEFT + UP,1.2 * LEFT + UP, radius=1)
        self.play(GrowFromCenter(urc2))

        krug = Ellipse(height=0.2 , width= 0.4)
        self.play(Create(krug))