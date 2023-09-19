from zkmarek.video.slides.common.tex_slide import TexSlide

class ScalarMultiplication(TexSlide):

    def __init__(self):
        super().__init__("Scalar multiplication", "data/ec/multiplication1.tex")


    def animate_in(self, scene):
        self.new_subsection(scene, "Scalar multiplication",
            sound="data/sound/episode/s19-1.m4a")
        super().animate_in(scene)



        self.new_subsection(scene, "Scalar multiplication - zero and one",
            sound="data/sound/episode/s19-2.wav")
        scene.wait(2)
        self.animate_replace_tex(scene, "data/ec/multiplication2.tex")
        scene.wait(8)
        self.animate_replace_tex(scene, "data/ec/multiplication3.tex")

        self.new_subsection(scene, "Scalar multiplication - doubling",
            sound="data/sound/episode/s19-3.wav")
        scene.wait(3)
        self.animate_replace_tex(scene, "data/ec/multiplication4.tex")
        scene.wait(4)
