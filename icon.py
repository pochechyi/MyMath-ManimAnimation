from manim import*

class AxesAttributes(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-6.5, 6.5],
            y_range=[-2.5, 2.5],
            x_length=13,
            y_length=5,
            axis_config={
                "include_tip": True,
                "color": GREY,
                "stroke_width": 2,
                "font_size": 24,
                "tick_size": 0.07,
                "longer_tick_multiple": 1.5,
                "line_to_number_buff": 0.15,
                "decimal_number_config": {
                    "color": ORANGE,
                    "num_decimal_places": 0
                },
            },
            x_axis_config={
                "tip_width": 0.15,
                "tip_height": 0.15,
                "numbers_to_include": np.arange(-6, 7, 1),
                "numbers_with_elongated_ticks": [-3, 3],
            },
            y_axis_config={
                "tip_width": 0.15,
                "tip_height": 0.15,
                "numbers_to_include": [-2, -1, 1, 2],
                "tick_size": 0.08,
                "font_size": 25,
                "numbers_with_elongated_ticks": [-1, 1],
            }
        )
        x_lab = axes.get_x_axis_label("x", direction=DOWN, buff=0.2)
        y_lab = axes.get_y_axis_label("y", direction=LEFT, buff=0.2)
        labels = VGroup(x_lab.scale(0.6), y_lab.scale(0.6))

        # В v0.15.01 размеры стрелок (tip) не работают,
        # но разработчики знают о проблеме, планируют исправить.
        # Вы можете самостоятельно изменить значение
        # DEFAULT_ARROW_TIP_LENGTH в файле constants.py.

        cos = axes.plot(lambda x: 1.5 * np.cos(x), color=TEAL, x_range=[-6, 6])
        self.play(Write(axes, run_time=5), lag_ratio=0.2)
        self.play(Write(labels))
        self.play(Create(cos), run_time=3)
        self.wait(3)