
import manim as M
from manim.animation.creation import Create
from manim.utils import rate_functions
from numpy.core.fromnumeric import size
import numpy as np

class ChangableText(M.Text):
    def change_text(self, s: str):
        self.target = ChangableText(s,size=0.7)
        self.target.move_to(self)
        return M.MoveToTarget(self)


class step (M.Scene):
    def construct(self):

        codes = ["a = [21, 1, 12, 34, 56, 19, 55, 66, 17, 9, 84]\n", "\n", "count = 0\n", "\n", "for i in a:\n",
                 "    if i >= 20:\n", "        count = count + 1\n", "\n", "print(\"20이상 수의 개수:\",count)"]
        text="".join(codes)
        text=M.Text(text)
        text.scale(0.7)
        
        # texts = []
        

        def get_shift_loc(step=0, is_text=0):
            step *= 0.5
            return M.LEFT * 4.6 + M.UP * 1.55 + M.DOWN * step*0.9 + M.RIGHT * is_text*5 

        def get_grid_loc(i, is_arrow=0):
            return M.UP * 3 + M.LEFT * 3.7 + M.RIGHT * i * 0.7 + M.UP *0.5 * is_arrow

        # for i in range(len(texts)):
        #     texts[i].shift(get_shift_loc(step=i, is_text=1))

        text.shift(M.DOWN *0.28 + M.RIGHT *0.15)
        self.add(text)
        self.wait(1)

        arrow = M.Arrow()
        arrow.scale(0.4, scale_tips=True)
        arrow.shift(get_shift_loc(step=0))
        self.add(arrow)
        self.wait(1)

        grid = [M.Square(side_length=0.7) for _ in range(11)]

        for i in range(len(grid)):
            grid[i].shift(get_grid_loc(i))
            self.add(grid[i])

        

        numbers = [21, 1, 12, 34, 56, 19, 55, 66, 17, 9, 84]

        for i in range(11):
            numbers[i] = M.Text(str(numbers[i]))
            numbers[i].scale(0.7)
            numbers[i].shift(get_grid_loc(i))
        self.add(*numbers)

        # move_list = []

        arrow2 = M.Arrow(start=M.UP, end=M.DOWN)
        arrow2.scale(0.4)
        arrow2.shift(get_grid_loc(0,1))
        i=0
        idx=0
        a = [21, 1, 12, 34, 56, 19, 55, 66, 17, 9, 84]
        count = 0
        while True:
            self.wait(0.5)
            if codes[i] != '\n':
                self.play(arrow.animate().move_to(get_shift_loc(step=i)))
                if i==4 and idx == 0:
                    self.play(Create(arrow2))
                elif i==4 :
                    self.play(arrow2.animate().move_to(get_grid_loc(idx,is_arrow=1)))
                if i==6 and idx<11:
                    if idx<10:
                        i=3
                    if a[idx]>=20:
                        count+=1
                        self.play(count_text.change_text(f"count : {count}"))
                    idx+=1
                if i==5:
                    if a[idx]>=20:
                        grid[idx].set_color(M.BLUE)
                    else:
                        i=3
                        idx+=1


                if i==2:
                    count_text = ChangableText(f"count : {count}")
                    count_text.scale(0.7)
                    count_text.shift(M.UP*2.2)
                    self.add(count_text)

            i+=1
            if i==len(codes):
                result_text= ChangableText(f"20이상 수의 개수: {count}")
                result_text.shift(M.DOWN*3.3)
                self.play(M.Create(result_text))
                break
        
        self.wait(2)
