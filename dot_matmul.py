from manim import *

class MatrixDot(Scene):
    def construct(self):
        np.random.seed(42)

        A = np.random.randint(0,10,size=(2,2,2))
        A_1 = Matrix(A[0],v_buff=0.5, h_buff=0.5)
        A_2 = Matrix(A[1],v_buff=0.5, h_buff=0.5)
        B = np.random.randint(0,10,size=(2,2,2))
        B_1 = Matrix(B[0],v_buff=0.5, h_buff=0.5)
        B_2 = Matrix(B[1],v_buff=0.5, h_buff=0.5)
        C = Matrix(np.dot(A,B)[0,0,:,:])
        g1 = Group(
                A_1, B_1, A_2, B_2
        ).arrange_in_grid(buff=1)
        self.add(g1.to_edge(LEFT))
        g2 = Group(C)
        self.add(g2.to_edge(RIGHT))
        for i in range(A.shape[2]-1):
            rect1 = SurroundingRectangle(A_1.get_rows()[i])
            rect2 = SurroundingRectangle(A_2.get_rows()[i])
            for j in range(B.shape[1]):
                rect3 = SurroundingRectangle(B_1.get_columns()[j])
                rect5 = SurroundingRectangle(C.get_entries()[j+(i*B.shape[1])])
                self.play(rect1.animate())
                self.play(rect3.animate())
                self.play(rect5.animate())
                self.wait(0.5)

                self.remove(rect3)
                self.remove(rect5)
            for j in range(B.shape[1]):
                rect4 = SurroundingRectangle(B_2.get_columns()[j])
                rect5 = SurroundingRectangle(C.get_entries()[j+(i*B.shape[1])])
                self.play(rect2.animate())
                self.play(rect3.animate())
                self.play(rect4.animate())
                self.play(rect5.animate())
                self.wait(0.5)

                
                self.remove(rect3)
                self.remove(rect4)
                self.remove(rect5)
            self.remove(rect1)
            self.remove(rect2)
        
        #B_1.add(SurroundingRectangle(B_1.get_columns()[0]))
        #B_2.add(SurroundingRectangle(B_2.get_columns()[0]))
        #A_2.add(SurroundingRectangle(A_2.get_rows()[0]))

class MatrixMatmul(Scene):
    def construct(self):
        np.random.seed(42)

        A = np.random.randint(0,10,size=(2,2,2))
        A_1 = Matrix(A[0],v_buff=0.5, h_buff=0.5)
        A_2 = Matrix(A[1],v_buff=0.5, h_buff=0.5)
        B = np.random.randint(0,10,size=(2,2,2))
        B_1 = Matrix(B[0],v_buff=0.5, h_buff=0.5)
        B_2 = Matrix(B[1],v_buff=0.5, h_buff=0.5)
        C = np.matmul(A,B)
        C_1 = Matrix(C[0])
        C_2 = Matrix(C[1])
        g1 = Group(
                A_1, B_1, A_2, B_2
        ).arrange_in_grid(buff=1)
        self.add(g1.to_edge(LEFT))
        g2 = Group(
            C_1, C_2
        ).arrange_in_grid(buff=1)
        self.add(g2.to_edge(RIGHT))
        
        for i in range(A.shape[2]):
            rect1 = SurroundingRectangle(A_1.get_rows()[i],color=RED)
            rect2 = SurroundingRectangle(A_2.get_rows()[i])
            for j in range(B.shape[1]):
                rect3 = SurroundingRectangle(B_1.get_columns()[j],color=RED)
                rect4 = SurroundingRectangle(B_2.get_columns()[j])
                rect5 = SurroundingRectangle(C_1.get_entries()[j+(i*B.shape[1])],color=RED)
                rect6 = SurroundingRectangle(C_2.get_entries()[j+(i*B.shape[1])])
                self.play(rect1.animate())
                self.play(rect2.animate())
                self.play(rect3.animate())
                self.play(rect4.animate())
                self.play(rect5.animate())
                self.play(rect6.animate())
                self.wait(0.5)

                
                self.remove(rect3)
                self.remove(rect4)
                self.remove(rect5)
                self.remove(rect6)
            self.remove(rect1)
            self.remove(rect2)
        
        #B_1.add(SurroundingRectangle(B_1.get_columns()[0]))
        #B_2.add(SurroundingRectangle(B_2.get_columns()[0]))
        #A_2.add(SurroundingRectangle(A_2.get_rows()[0]))
