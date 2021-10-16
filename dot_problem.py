
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
        A = np.random.randint(1,6,size=(2,3))
        B = np.random.randint(1,6,size=(3,2))
        C = np.dot(A,B)
        
        A_boxes = VGroup(*[Square().add(Text(str(A[i,j])) for j in range(3) for i in range(2))])
        B_boxes = VGroup(*[Square().add(Text(str(A[i,j])) for j in range(3) for i in range(2))])
        C_boxes = VGroup(*[Square().add(Text(str(A[i,j])) for j in range(3) for i in range(2))])
        A_boxes.arrange_in_grid(rows=2, buff=0.1)
        B_boxes.arrange_in_grid(rows=3, buff=0.1)
        C_boxes.arrange_in_grid(rows=2, buff=0.1)
        A_boxes.scale(0.4)
        B_boxes.scale(0.4)
        C_boxes.scale(0.4)
        