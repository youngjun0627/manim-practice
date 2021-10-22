from manim import *


class Uchan(Scene):
    def Client(self):
        codes = ["""
        async def get_or_create(
        cls,
        ...
        ...,
    ) -> ComputeSession:

        ...

        rqst = Request('POST', f'/{prefix}')
        params: Dict[str, Any] = {
            'tag': tag,
            get_naming(api_session.get().api_version, 'name_arg'): name,
            'config': {
                ...
            },
        }
        if api_session.get().api_version >= (6, '20200815'):
            params['clusterSize'] = cluster_size
            params['clusterMode'] = cluster_mode
        …

        rqst.set_json(params)
                async with rqst.fetch() as resp:
                    data = await resp.json()
                    o = cls(name, owner_access_key)  # type: ignore
                    if api_session.get().api_version[0] >= 5:
                        o.id = UUID(data['sessionId'])
                ...
                    return o


"""]
        text="".join(codes)
        text=Text(text)
        text.scale(0.3)
        text.shift(LEFT*3)
        return text

    def construct(self):
        def get_shift_loc(step=0, is_text=0):
            step *= 0.5
            return LEFT * 6 + UP * 2.8 + DOWN * step*0.8 + RIGHT * is_text*5 

        client_code = self.Client()
        self.add(client_code)
        manager = Square(side_length=4).add(Text('Manager')).move_to(RIGHT*3)
        
        self.play(FadeIn(manager))
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
        
        