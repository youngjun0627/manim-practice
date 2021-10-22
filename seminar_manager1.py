from manim import *


class Uchan(Scene):

    def construct(self):
        def get_shift_loc(step=0, is_text=0):
            step *= 0.5
            return LEFT * 6 + UP * 2.8 + DOWN * step*0.8 + RIGHT * is_text*5 

        #manager_code = self.Manager()
        #self.add(manager_code)
        #image_ref = Square(side_length=4).add(Text('image ref')).move_to(RIGHT*3)
        
        rqst = Square(side_length=2).add(Text('Request')).move_to(UP*3 + LEFT*4)
        manager = Square(side_length=2).add(Text('Manager')).move_to(LEFT*4)
        agent = Rectangle(color=WHITE, height=4,width=2).add(Text('Agent')).move_to(RIGHT*4)
        kernel = Square(side_length=1).add(Text('kernel')).move_to(UP*3+RIGHT*4)
        key = [Text('session_name'), Text('status'), Text('kernel_id'),Text('...')]
        value = [Text('psdk-1a..'), Text('PENDING'), Text('a8411..'), Text('...')]
        key = ['session_name', 'status', 'kernel_id','...']
        value = ['psdk-1a..', 'PENDING', 'a8411..', '...']
        db = Table(
            [key,value]
        )
        key2 = ['session_name', 'status', 'kernel_id','...']
        value2 = ['psdk-1a..', 'RUNNING', 'a8411..', '...']
        db2 = Table(
            [key2,value2]
        )
        db.add_highlighted_cell((2,2), color=YELLOW)
        db.scale(0.5).move_to(DOWN*3 + LEFT*2)
        db2.add_highlighted_cell((2,2), color=GREEN)
        db2.scale(0.5).move_to(DOWN*3 + LEFT*2)
        #db.add_highlighted_cell((2,2), color=GREEN)
        
        self.add(manager)
        self.add(agent)
        
        

        self.play(FadeIn(rqst))
        self.play(rqst.animate().shift(DOWN*3))
        self.play(FadeOut(rqst))
        manager_to_agent_arrow = Arrow()
        manager_to_db_arrow = Arrow(start=ORIGIN, end=config.bottom).move_to(LEFT*4+DOWN*1.7).scale(0.4)
        agent_to_manager_arrow = Arrow(start=ORIGIN, end=config.left_side).move_to(0).scale(0.4)
        manager_process_arrow = ArcBetweenPoints(LEFT*3+DOWN, LEFT*3+UP, radius=1)
        manager_process_arrow.add_tip()
        self.play(FadeIn(manager_process_arrow))
        text = Text('check params from the request').scale(0.4)
        self.add(text)
        self.wait(2)
        self.remove(text)
        text = Text('set the kernel-config & enqueue').scale(0.4)
        self.add(text)
        self.wait(2)
        self.remove(text)
        self.play(FadeOut(manager_process_arrow))
        self.play(FadeIn(manager_to_db_arrow))
        self.play(FadeIn(db))
        text = Text('insert kernel-config to kernels table').move_to(LEFT*2+DOWN*1.6).scale(0.4)
        self.add(text)
        self.wait(2)
        self.remove(text)
        self.play(FadeOut(manager_to_db_arrow))
        self.play(FadeIn(manager_to_agent_arrow))
        text = Text('call agent to create kernel').scale(0.4).move_to(UP)
        self.add(text)
        self.wait(2)
        self.remove(text)
        self.play(FadeOut(manager_to_agent_arrow))
        self.play(FadeIn(kernel))
        self.play(kernel.animate().shift(DOWN*2))
        self.play(FadeOut(kernel))
        self.play(FadeIn(agent_to_manager_arrow))
        text = Text('we have finished to create kernel').scale(0.4).move_to(UP)
        self.add(text)
        self.wait(1)
        self.remove(text)
        self.play(FadeOut(agent_to_manager_arrow))
        self.play(FadeIn(manager_to_db_arrow))
        text = Text('update status').move_to(LEFT*2.7+DOWN*1.6).scale(0.4)
        self.add(text)
        self.wait(2)
        self.remove(text)
        self.play(FadeOut(db))
        self.play(FadeIn(db2))
        self.play(FadeOut(manager_to_db_arrow))
        
        
        '''
        self.play(FadeIn(image_ref))
        arrow = Arrow()
        arrow.scale(0.4, scale_tips=True)
        arrow.shift(get_shift_loc(step=0))
        self.play(FadeIn(arrow))
        self.play(arrow.animate().move_to(get_shift_loc(step=11)))
        self.wait(1)
        rqst = Rectangle(color=YELLOW, height=1, width=3).add(Text('Request')).move_to(LEFT)
        self.play(FadeIn(rqst))
        self.play(rqst.animate().shift(RIGHT*4))
        self.play(FadeOut(rqst))
        self.wait(1)
        '''
        