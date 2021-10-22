from textwrap import fill
from manim import *
import math

class ChangableText(Text):
    def change_text(self, s: str):
        self.target = ChangableText(s,font_size=0.7)
        self.target.move_to(self)
        return MoveToTarget(self)


class daram(Scene):
    def construct(self):

        arr = [2, 3, 2, 3, 0, 3, 1, 4, 5]
        
        c_list = VGroup(*[Circle(0.7,color=WHITE).set_fill(WHITE, opacity=1).add(Text(str(arr[i])).set_color(BLACK)) for i in range(len(arr))])
        #c_list[0].move_to(UP*3.2)
        self.play(c_list[0].animate().move_to(UP*3.2))
        
        for i in [1,2]:
            root2 = 0.7/math.sqrt(2)
            if i==1:
                self.play(c_list[1].animate().shift(UP*1.75))
                self.play(c_list[1].animate().shift(LEFT*3.5))
                edge_start = (c_list[0].get_center()+(-root2,-root2,0))
                edge_end = (c_list[i].get_center()+(root2,+root2,0))
            if i==2:
                self.play(c_list[2].animate().shift(UP*1.5))
                self.play(c_list[2].animate().shift(RIGHT*4))
                edge_start = (c_list[0].get_center()+(root2,-root2,0))
                edge_end = (c_list[i].get_center()+(-root2,+root2,0))
            edge = Line(edge_start, edge_end, stroke_color=WHITE)
            self.play(edge.animate())
            #self.add(edge)
        
        #self.play(c_list[2].animate().shift(UP*1.5))
        #self.play(c_list[2].animate().shift(RIGHT*4))

        #c_list[3].shift(UP*1)
        #c_list[3].shift(DOWN*2)
        #c_list[4].shift(UP*1)
        for i in [3,4]:
            if i==3:
                self.play(c_list[3].animate().shift(LEFT*5))
                edge_start = (c_list[1].get_center()+(-root2,-root2,0))
                edge_end = (c_list[i].get_center()+(root2,root2,0))
            if i==4:
                self.play(c_list[4].animate().shift(LEFT*2))
                edge_start = (c_list[1].get_center()+(root2,-root2,0))
                edge_end = (c_list[i].get_center()+(-root2,+root2,0))
            
            edge = Line(edge_start, edge_end, stroke_color=WHITE)
            self.play(edge.animate())
        
        #self.play(c_list[3].animate().shift(LEFT*5))

        #c_list[4].shift(DOWN*1)
        #c_list[4].shift(UP*1)
        #self.play(c_list[4].animate().shift(LEFT*2))

        #self.play(c_list[5].animate().shift(DOWN*1))
        #self.play(c_list[5].animate().shift(RIGHT*2))

        #self.play(c_list[6].animate().shift(DOWN*1))
        #self.play(c_list[6].animate().shift(RIGHT*6))

        #self.play(c_list[7].animate().shift(DOWN*2))
        #self.play(c_list[7].animate().shift(LEFT*5.8))

        #self.play(c_list[8].animate().shift(DOWN*2))
        #self.play(c_list[8].animate().shift(LEFT*4.2))
        #self.add(c_list)

        

        
        for i in [5,6]:
            if i==5:
                self.play(c_list[5].animate().shift(DOWN*1))
                self.play(c_list[5].animate().shift(RIGHT*2))
                edge_start = (c_list[2].get_center()+(-root2,-root2,0))
                edge_end = (c_list[i].get_center()+(root2,root2,0))
            if i==6:
                self.play(c_list[6].animate().shift(DOWN*1))
                self.play(c_list[6].animate().shift(RIGHT*6))
                edge_start = (c_list[2].get_center()+(root2,-root2,0))
                edge_end = (c_list[i].get_center()+(-root2,+root2,0))
            edge = Line(edge_start, edge_end, stroke_color=WHITE)
            self.play(edge.animate())
            #self.add(edge)

        for i in [7,8]:
            if i==7:
                self.play(c_list[7].animate().shift(DOWN*2))
                self.play(c_list[7].animate().shift(LEFT*5.8))
                edge_start = (c_list[3].get_center()+(-root2,-root2,0))
                edge_end = (c_list[i].get_center()+(0,root2,0))
            if i==8:
                self.play(c_list[8].animate().shift(DOWN*2))
                self.play(c_list[8].animate().shift(LEFT*4.2))
                edge_start = (c_list[3].get_center()+(root2,-root2,0))
                edge_end = (c_list[i].get_center()+(0,+root2,0))
            edge = Line(edge_start, edge_end, stroke_color=WHITE)
            #self.add(edge)
            self.play(edge.animate())
        
        score = ChangableText(str(0))
        score.scale(0.7)
        score.shift(DOWN*3)
        self.add(score)

        path = [7,3,8,1,4,0,5,2,6]
        check = True
        cnt=0
        for i in path:
            if arr[i]!=0:
                self.play(c_list[i].animate.set_color(BLUE))
            else:
                self.play(c_list[i].animate.set_color(RED))
                check = False
            if check:
                cnt+=arr[i]
                self.remove(score)
                score = ChangableText(str(cnt))
                score.scale(0.7)
                score.shift(DOWN*3)
                self.add(score)
        self.wait(0.5)

