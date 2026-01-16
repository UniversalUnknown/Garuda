from manim import *

class DoubleSlit(Scene):
    def construct(self):
        # Create the slits
        slit1 = Rectangle(width=0.1, height=1, fill_color=BLUE, fill_opacity=1).shift(LEFT * 1)
        slit2 = Rectangle(width=0.1, height=1, fill_color=BLUE, fill_opacity=1).shift(RIGHT * 1)

        # Create the screen
        screen = Rectangle(width=6, height=4, fill_color=WHITE, fill_opacity=1).shift(DOWN * 2)

        # Create the wavefronts
        wavefronts = VGroup()
        for i in range(-3, 4):
            wavefront = Line(start=LEFT * 3, end=RIGHT * 3, stroke_width=2, color=YELLOW)
            wavefront.move_to(UP * (i * 0.5))
            wavefronts.add(wavefront)

        # Create the interference pattern
        interference_pattern = VGroup()
        for i in range(-3, 4):
            if i % 2 == 0:
                line = Line(start=LEFT * 3, end=RIGHT * 3, stroke_width=2, color=RED)
                line.move_to(UP * (i * 0.5))
                interference_pattern.add(line)

        # Add the slits and screen to the scene
        self.play(Create(slit1), Create(slit2))
        self.wait(1)
        self.play(Create(screen))
        self.wait(1)

        # Show wavefronts
        self.play(Create(wavefronts))
        self.wait(1)

        # Show interference pattern
        self.play(Create(interference_pattern))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(slit1), FadeOut(slit2), FadeOut(screen), FadeOut(wavefronts), FadeOut(interference_pattern))
        self.wait(1)

# To run this scene, use the following command in your terminal:
# manim -pql your_script_name.py DoubleSlit