from manim import *


class ChangableText(Text):
    def change_text(self, s: str):
        self.target = ChangableText(s,font_size=0.7)
        self.target.move_to(self)
        return MoveToTarget(self)


class board(Scene):
    def construct(self):
        width = 4
        height = 4
        arr = [
            [1, 3, 4, 6],
            [2, 2, 3, 3],
            [9, 1, 4, 2],
            [8, 3, 7, 8]
        ]
        coords = [[i,j] for i in range(4) for j in range(4)]
        print(coords)
        group = []
        for y,x in coords:
            s = Square(side_length=1).add(Text(str(arr[y][x])))
            s.set_x(x)
            s.set_y(-y)
            self.add(s)
            group.append(s)
        g = VGroup(*group)
        g.set_x(0)
        g.set_y(0)
        self.play(FadeIn(g))
        self.wait(1)

        score = ChangableText(str(0))
        score.scale(0.7)
        score.shift(UP*3)
        self.add(score)

        # rect 1
        s1 = Rectangle(color=RED, height=2, width=4)
        g[8][0].set_color(YELLOW)
        self.remove(score)
        score = ChangableText(str(9))
        score.scale(0.7)
        score.shift(UP*3)
        self.add(score)
        s1.set_y(-1)
        self.play(FadeIn(s1))
        self.wait(1)
        self.remove(s1)
        self.play(FadeOut(g[:8]))
        self.play(g[8:].animate().move_to(UP*0.5))
        #self.play(i.animate().move_to(UP))
        #self.play(g.move_to(UP))
        self.wait(1)

        # rect 2
        s2 = Rectangle(color=RED, height=1, width=4)
        #s2.set_y(-0.)
        g[12][0].set_color(YELLOW)
        self.remove(score)
        score = ChangableText(str(17))
        score.scale(0.7)
        score.shift(UP*3)
        self.add(score)
        self.play(FadeIn(s2))
        self.wait(1)
        self.remove(s2)
        self.play(FadeOut(g[8:12]))
        #self.play(g[12:].animate().move_to(UP*0.25))

        # rect 3
        s3 = Rectangle(color=RED, height=1, width=2)
        #s3.set_y()
        g[15][0].set_color(YELLOW)
        self.remove(score)
        score = ChangableText(str(25))
        score.scale(0.7)
        score.shift(UP*3)
        self.add(score)
        s3.set_x(1)
        self.play(FadeIn(s3))
        self.wait(1)
        self.remove(s3)
        self.play(FadeOut(g[12:14]))
        self.play(g[14:].animate().move_to(0))

        # rect 4
        s4 = Rectangle(color=RED, height=1, width=1)
        s4.set_x(-0.5)
        g[14][0].set_color(YELLOW)
        self.remove(score)
        score = ChangableText(str(32))
        score.scale(0.7)
        score.shift(UP*3)
        self.add(score)
        self.play(FadeIn(s4))
        self.wait(1)
        self.remove(s4)
        self.play(FadeOut(g[15]))
        self.play(g[14].animate().move_to(0))


