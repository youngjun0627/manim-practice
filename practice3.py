
import manim as M
from manim import Square, VGroup, Scene, Text
from manim.animation.creation import Create
from manim.utils import rate_functions
from numpy.core.fromnumeric import size
import numpy as np

'''
if __name__=='__main__':
    n=20
    omr_cards = np.random.randint(1,6,size=(n,10,10))
    print(omr_cards.tolist())
    text="".join(omr_cards.tolist())
    print(text)
'''

class _Array(Scene):
    def construct(self):
        n=20
        omr_cards = np.random.randint(1,6,size=(n,10,10)).tolist()
        boxes=VGroup(*[Square().add(Text(str(omr_cards[0][i][j])).scale(1.2)) for i in range(10) for j in range(10)])
        boxes.arrange_in_grid(rows=10, buff=0.1)
        boxes.scale(0.4)
        for i in range(10):
            for j in range(10):
                if i==j:
                    if i==0:
                        boxes[0] = boxes[99]
                        boxes[0]
                    else:
                        boxes[10*i+j] = boxes[10*(i-1)+(j-1)]
        boxes[0]
        self.add(boxes)