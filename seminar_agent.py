from manim import *

class Agent(Scene):
    def construct(self):
        agent = Square(side_length=2).add(Text('Agent')).move_to(LEFT*4+DOWN*2)
        docker = Rectangle(height=3, width = 5).add(Text('AGENT DOCKER').scale(0.6)).move_to(RIGHT*4.4)
        kernel = Rectangle(height=1, width = 2, color='YELLOW').add(Text('container').scale(0.4)).move_to(RIGHT*4+DOWN)
        manager = Square(side_length=2).add(Text('Manager').scale(0.7)).move_to(LEFT*4+UP*2)
        self.add(agent)
        self.add(docker)
        #agent_to_docker_arrow = Arrow()
        agent_to_docker_arrow = Arrow(start=agent.get_center(), end=docker.get_center()).shift(LEFT*0.7).scale(0.4)
        agent_to_manager_arrow = Arrow(start=agent.get_center(), end=manager.get_center()).scale(0.4)
        start_event = Circle(0.5).add(Text('start event').scale(0.4)).move_to(LEFT*3+DOWN)

        self.play(FadeIn(agent_to_docker_arrow))
        _str = Text('create').scale(0.7).move_to(DOWN*0.3+LEFT*0.5)
        self.add(_str)
        self.wait(2)
        self.remove(_str)
        self.play(FadeOut(agent_to_docker_arrow))
        self.play(FadeIn(kernel))
        #self.play(FadeIn(docker_to_agent_arrow))
        _str = Text('container start').scale(0.5).move_to(UP*2 + RIGHT*4.4)
        self.add(_str)
        self.wait(2)
        self.remove(_str)
        #self.play(FadeOut(docker_to_agent_arrow))
        self.play(FadeIn(manager))
        self.play(FadeIn(agent_to_manager_arrow))
        self.wait(1)
        self.play(FadeIn(start_event))
        self.play(start_event.animate().shift(UP*2))
        self.play(FadeOut(start_event))
        self.wait(1)



