from typing import cast
from typing_extensions import runtime
from manim import (
    BOLD,
    PURPLE,
    RED,
    YELLOW,
    Arrow,
    GrowArrow,
    ImageMobject,
    Paragraph,
    ReplacementTransform,
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
    FadeTransform,
)


class IntroScene(Scene):
    def construct(self):
        font_term = "Consolas"

        prompt = Text("C:\\Users\\Prince> ", font=font_term, font_size=24).to_edge(UL)
        self.add(prompt)

        full_text = Text("run introduction.exe", font="Consolas", font_size=24)
        full_text.next_to(prompt, RIGHT)

        cursor = Rectangle(
            color=GREY_A, fill_color=GREY_A, fill_opacity=1.0, height=0.5, width=0
        ).move_to(full_text[0])

        self.play(TypeWithCursor(full_text, cursor), runtime=0.5)

        self.play(Blink(cursor, blinks=2))

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

        me_img = ImageMobject("me.png")
        me_img.scale(0.5)
        self.play(FadeIn(me_img, scale=0.5))
        self.play(me_img.animate.to_edge(UP))

        arrow = Arrow(2 * RIGHT, 2 * LEFT)
        arrow.next_to(me_img)

        self.play(me_img.animate.to_edge(UL), GrowArrow(arrow, point_color=RED))

        me = Text("This is me", gradient=(YELLOW, RED)).scale(1.2)
        self.play(arrow.animate.next_to(me_img))
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

        qr = ImageMobject("qr.png").scale(0.5)
        qr.to_edge(UP)
        self.play(
            Transform(intro_sub, curios_sub),
            FadeOut(name, subtitle, details, arrow, me),
            FadeTransform(me_img, qr),
        )

        self.wait(5)

        interest = Text("Interests", gradient=(BLUE, RED)).scale(1.3)

        iter_sub = Paragraph(
            "Some of my interests include programming, game development",
            t2c={"programming": RED, "game development": YELLOW},
            font_size=28,
        ).to_edge(DOWN)

        self.play(
            FadeTransform(qr, interest), ReplacementTransform(intro_sub, iter_sub)
        )

        rust_img = ImageMobject("rust.png")
        rust_txt = Text("Certified Rustaceans", color=RED).scale(0.5)
        rust_txt.next_to(rust_img, DOWN)

        line = iter_sub[0]

        self.play(interest.animate.to_edge(UP))
        self.play(
            iter_sub.animate.set_opacity(0.3),
            line[24:35].animate.scale(1.5).set_opacity(1).set_color(RED),
            FadeIn(rust_img),
            Write(rust_txt),
        )

        godot_img = ImageMobject("godot.png").scale(0.5)

        self.play(
            rust_img.animate.to_edge(LEFT),
            rust_txt.animate.to_edge(LEFT),
            line[24:35].animate.scale(1 / 1.5).set_opacity(0.3).set_color(RED),
            line[36:56].animate.scale(1.5).set_opacity(1),
            FadeIn(godot_img),
        )

        self.play(
            godot_img.animate.scale(0.5),
            line[36:56].animate.scale(1 / 1.5).set_opacity(0.3),
        )

        lainst_sub = Text(
            "and learning about Kernel and operating systems.",
            t2c=cast(dict[str, str], {"Kernel": GREEN, "operating systems": GREEN}),
            font_size=28,
        ).to_edge(DOWN)

        self.play(FadeOut(intro_sub, iter_sub))

        self.play(Write(lainst_sub))
        ker_part = lainst_sub[16:22]
        os_part = lainst_sub[25:41]

        linux_img = ImageMobject("linux.png").scale(0.8)
        Windows_img = ImageMobject("Windows.png").scale(0.5)

        Windows_img.next_to(linux_img)

        self.play(
            lainst_sub.animate.set_opacity(0.3),
            ker_part.animate.scale(1.4),
            os_part.animate.scale(1.4),
            FadeIn(linux_img, Windows_img),
        )

        self.play(
            Windows_img.animate.to_edge(RIGHT),
        )
        self.play(
            linux_img.animate.next_to(Windows_img, LEFT),
            ker_part.animate.scale(1 / 1.5).set_opacity(0.3),
            os_part.animate.scale(1 / 1.5).set_opacity(0.3),
        )

        self.play(
            FadeOut(lainst_sub, rust_img, rust_txt, godot_img, linux_img, Windows_img)
        )

        about_me = Text("About Me", gradient=(RED, BLUE)).scale(1.3)
        about_me.to_edge(UP)

        hobby = Text(
            "In my spare time, I enjoy building my own projects, playing Minecraft,",
            t2c=cast(
                dict[str, str], {"building my own projects": GREEN, "Minecraft": GREEN}
            ),
            font_size=28,
        ).to_edge(DOWN)

        cursor = Rectangle(
            color=GREY_A, fill_color=GREY_A, fill_opacity=1.0, height=0.5, width=0
        ).move_to(hobby[0])

        self.play(TypeWithCursor(hobby[:41], cursor))

        self.play(hobby[20:41].animate.scale(1.5).set_color(GREEN))

        self.play(
            TypeWithCursor(hobby[41:60], cursor), hobby[20:41].animate.scale(1 / 1.5)
        )

        self.play(hobby[49:58].animate.scale(1.5).set_color(GREEN))
        self.play(Blink(cursor, blinks=2))
