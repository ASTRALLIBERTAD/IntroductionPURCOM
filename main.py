from typing_extensions import runtime
from manim import (
    BOLD,
    PURE_BLUE,
    PURPLE,
    RED,
    YELLOW,
    Arrow,
    GrowArrow,
    ImageMobject,
    Paragraph,
    Scene,
    Transform,
    Write,
    Text,
    Rectangle,
    RIGHT,
    TypeWithCursor,
    Blink,
    DOWN,
    LEFT,
    FadeOut,
    UL,
    UP,
    GREY_A,
    FadeIn,
    BLUE,
    WHITE,
    GREEN,
    config,
)


class IntroScene(Scene):
    def construct(self):
        font_term = "Consolas"

        # 1. Prompt
        prompt = Text("C:\\Users\\Prince> ", font=font_term, font_size=24).to_edge(UL)
        self.add(prompt)

        # 2. Full text to type
        full_text = Text("run introduction.exe", font="Consolas", font_size=24)
        full_text.next_to(prompt, RIGHT)

        cursor = Rectangle(
            color=GREY_A, fill_color=GREY_A, fill_opacity=1.0, height=0.5, width=0
        ).move_to(full_text[0])

        self.play(TypeWithCursor(full_text, cursor), runtime=0.5)

        # 6. Blink cursor at the end
        self.play(Blink(cursor, blinks=2))

        # 7. Execution text
        exec_text = Text("Executing...", font=font_term, font_size=20, color=GREEN)
        exec_text.next_to(prompt, DOWN, aligned_edge=LEFT)
        self.play(Write(exec_text))
        self.wait(1)

        # 8. Fade out everything
        self.play(FadeOut(prompt, cursor, exec_text, full_text))

        name = Text("Prince Gabrielle Jhon M. Libertad", gradient=(BLUE, WHITE)).scale(
            1.2
        )
        subtitle = Text("Computer Engineering Student", font_size=24).next_to(
            name, DOWN
        )

        self.play(FadeIn(subtitle, shift=UP), Write(name))
        self.wait(1)

        img = ImageMobject("me.png")
        img.scale(0.5)
        self.play(FadeIn(img, scale=0.5))
        self.play(img.animate.to_edge(UP))

        arrow = Arrow(2 * RIGHT, 2 * LEFT)
        arrow.next_to(img)

        self.play(img.animate.to_edge(UL), GrowArrow(arrow, point_color=RED))

        me = Text("This is me", gradient=(YELLOW, RED)).scale(1.2)
        self.play(arrow.animate.next_to(img))
        me.next_to(arrow)

        self.play(FadeIn(me))

        details = Paragraph(
            "18 years old",
            "Location: Sta. Mesa, Manila",
            alignment="left",
            font="sans-serif",
            weight=BOLD,
            font_size=18,
        )
        details.next_to(me, DOWN)

        self.play(FadeIn(details))
        self.wait(2)

        intro_sub = Paragraph(
            "As a Computer Engineering student,",
            "I created this entire video using code.",
            t2c={"code": GREEN, "Computer Engineering": BLUE},
            font_size=28,
        ).to_edge(DOWN)

        self.play(Write(intro_sub, run_time=2))
        self.wait(3)

        curios_sub = Paragraph(
            "If you are curios, you can scan this QR code",
            "to view the source code behind this video",
            t2c={"curios": RED, "QR": PURPLE, "view": YELLOW},
        )

        self.play(Transform(intro_sub, curios_sub), FadeOut(name, subtitle))

        self.wait(3)
