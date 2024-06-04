import os
from manim import *

class MixtureOfExperts(Scene):
    def construct(self):
        # タイトル
        title = Text("魔法ゾルトーラーク").scale(0.8)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # 入力
        input_text = Text("複数の魔法使いの力を組み合わせた").scale(0.7)
        input_text.move_to(LEFT * 5)
        input_text_explanation = Text("強力な魔法のアーキテクチャです。", font_size=24).next_to(input_text, DOWN)
        self.play(Write(input_text), Write(input_text_explanation))

        # エキスパート
        experts = VGroup(
            Circle(radius=0.5, color=BLUE, fill_opacity=1).set_fill(BLUE, opacity=0.5),
            Circle(radius=0.5, color=GREEN, fill_opacity=1).set_fill(GREEN, opacity=0.5),
            Circle(radius=0.5, color=RED, fill_opacity=1).set_fill(RED, opacity=0.5),
        ).arrange(DOWN, buff=1)
        experts.next_to(input_text, RIGHT, buff=1.5)
        expert_labels = VGroup(
            Text("炎"),
            Text("氷"),
            Text("雷"),
        ).scale(0.7).arrange(DOWN, buff=1)
        expert_labels.next_to(experts, RIGHT)
        expert_labels_explanation = Text("各魔法使いの力", font_size=24).next_to(expert_labels, DOWN * 5).shift(LEFT * 1)

        self.play(
            *[FadeIn(expert, scale=0.5) for expert in experts],
            *[Write(label) for label in expert_labels],
            Write(expert_labels_explanation)
        )

        input_arrows = VGroup(
            Arrow(start=input_text.get_right(), end=experts[0].get_left(), buff=0.1),
            Arrow(start=input_text.get_right(), end=experts[1].get_left(), buff=0.1),
            Arrow(start=input_text.get_right(), end=experts[2].get_left(), buff=0.1),
        )

        def pikon_effect(arrow, expert):
            self.play(GrowArrow(arrow))
            self.play(Flash(expert, color=YELLOW, flash_radius=0.5))

        for arrow, expert in zip(input_arrows, experts):
            pikon_effect(arrow, expert)

        gating_function = Circle(radius=0.5, color=YELLOW, fill_opacity=1).set_fill(YELLOW, opacity=0.5)
        gating_function.next_to(experts, RIGHT, buff=1.5)
        gating_label = Text("最高位の魔導師").scale(0.7).next_to(gating_function, UP)
        gating_label_explanation = Text("魔法の威力と効果を調整", font_size=24).next_to(gating_label, UP * 2).shift(RIGHT * 1)

        input_to_gating_arrow = Arrow(start=input_text.get_right(), end=gating_function.get_left(), buff=0.1, color=YELLOW)
        self.play(GrowArrow(input_to_gating_arrow))
        self.remove(input_to_gating_arrow)

        self.play(FadeIn(gating_function), Write(gating_label), Write(gating_label_explanation))

        gating_arrows = VGroup(
            Arrow(start=experts[0].get_right(), end=gating_function.get_left(), buff=0.1),
            Arrow(start=experts[1].get_right(), end=gating_function.get_left(), buff=0.1),
            Arrow(start=experts[2].get_right(), end=gating_function.get_left(), buff=0.1),
        )

        def pikon_effect_gating(arrow, expert_label):
            self.play(GrowArrow(arrow), FadeOut(expert_label))
            self.play(Flash(gating_function, color=YELLOW, flash_radius=0.5))

        for arrow, expert_label in zip(gating_arrows, expert_labels):
            pikon_effect_gating(arrow, expert_label)

        output_text = Text("最終的な魔法").scale(0.7)
        output_text.next_to(gating_function, RIGHT, buff=1.5)
        output_text_explanation = Text("魔法の威力と効果", font_size=24).next_to(output_text, DOWN)
        output_arrow = Arrow(start=gating_function.get_right(), end=output_text.get_left(), buff=0.1)

        self.play(GrowArrow(output_arrow), Write(output_text), Write(output_text_explanation))

        self.wait(2)

        self.remove(input_text, experts, expert_labels, gating_function, gating_label, gating_label_explanation, input_to_gating_arrow, gating_arrows, output_text, output_text_explanation, output_arrow, input_arrows, *experts, *input_arrows, *gating_arrows, input_text_explanation, expert_labels_explanation)

        self.wait(2)
        print(f"動画出力ファイルパス: {self.renderer.file_writer.movie_file_path}")

if __name__ == "__main__":
    if not os.path.exists("ディレクトリ"):
        os.makedirs("ディレクトリ")
    os.system("manim -pql exe_mov.py MixtureOfExperts")
    os.system('ffmpeg -i ディレクトリ/MixtureOfExperts.mp4 -vf subtitles=./ref.srt ディレクトリ/output_with_subtitles.mp4')
