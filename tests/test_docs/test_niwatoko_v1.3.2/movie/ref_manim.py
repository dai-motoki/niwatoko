from manim import *

class MixtureOfExperts(Scene):
    def construct(self):
        # タイトル
        title = Text("Mixture of Experts (MoE)").scale(0.8)  # タイトルテキストを作成し、サイズを0.8倍に設定
        self.play(Write(title))                              # タイトルを書く(Write)アニメーションを再生
        self.wait(1)                                         # 1秒待機
        self.play(title.animate.to_edge(UP))                 # タイトルを上端(UP)に移動するアニメーションを再生

        # 入力
        input_text = MathTex("Input \, x").scale(0.7)        # 入力テキストを数式(MathTex)として作成し、サイズを0.7倍に設定
        input_text.move_to(LEFT * 5)                         # 入力テキストを左に5単位移動
        input_text_explanation = (                           # 入力テキストの説明を作成
            Text("入力データx", font_size=24)                  #   - フォントサイズを24に設定
            .next_to(input_text, DOWN)                       #   - 入力テキストの下に配置
        )
        self.play(                                           # アニメーションを再生
            Write(input_text),                               #   - 入力テキストを書く
            Write(input_text_explanation),                   #   - 入力テキストの説明を書く
        )

        # エキスパート
        experts = VGroup(                                                                          # エキスパートを表す円を作成
             Circle(radius=0.5, color=BLUE, fill_opacity=1).set_fill(BLUE, opacity=0.5),           #   - 青い円を作成し、塗りつぶしの透明度を0.5に設定
             Circle(radius=0.5, color=GREEN, fill_opacity=1).set_fill(GREEN, opacity=0.5),         #   - 緑の円を作成し、塗りつぶしの透明度を0.5に設定
             Circle(radius=0.5, color=RED, fill_opacity=1).set_fill(RED, opacity=0.5),             #   - 赤い円を作成し、塗りつぶしの透明度を0.5に設定
        ).arrange(DOWN, buff=1)                                                                    #   - 円を縦に並べ、間隔を1に設定
        experts.next_to(input_text, RIGHT, buff=1.5)                                               # エキスパートを入力テキストの右に配置し、間隔を1.5に設定
        expert_labels = VGroup(                                                                    # エキスパートのラベルを作成
             MathTex(r"f_1(x)"),                                                                   #   - f_1(x)のラベルを作成
             MathTex(r"f_2(x)"),                                                                   #   - f_2(x)のラベルを作成
             MathTex(r"f_3(x)"),                                                                   #   - f_3(x)のラベルを作成
        ).scale(0.7).arrange(DOWN, buff=1)                                                         #   - ラベルのサイズを0.7倍に設定し、縦に並べ、間隔を1に設定
        expert_labels.next_to(experts, RIGHT)                                                      # エキスパートのラベルをエキスパートの右に配置
        expert_labels_explanation = Text(                                                          # エキスパートのラベルの説明を作成
            "エキスパートの出力関数",                                                                  #   - 説明テキストを作成
            font_size=24                                                                           #   - フォントサイズを24に設定
        ).next_to(expert_labels, DOWN * 5).shift(LEFT * 1)                                         #   - 説明テキストをラベルの下に配置し、左に1単位移動

        self.play(                                                                                 # アニメーションを再生
            *[FadeIn(expert, scale=0.5) for expert in experts],                                    #   - エキスパートを0.5倍のスケールでフェードインさせる
            *[Write(label) for label in expert_labels],                                            #   - エキスパートのラベルを書く
            Write(expert_labels_explanation)                                                       #   - エキスパートのラベルの説明を書く
        )
        # 入力からエキスパートへの矢印を作成
        input_arrows = VGroup(                                                                                 # 入力からエキスパートへの矢印のグループを作成
            Arrow(start=input_text.get_right(), end=experts[0].get_left(), buff=0.1),                          #   - 入力テキストの右端からエキスパート1の左端への矢印を作成
            Arrow(start=input_text.get_right(), end=experts[1].get_left(), buff=0.1),                          #   - 入力テキストの右端からエキスパート2の左端への矢印を作成
            Arrow(start=input_text.get_right(), end=experts[2].get_left(), buff=0.1),                          #   - 入力テキストの右端からエキスパート3の左端への矢印を作成
        )                                                                                                      # 矢印のグループ作成を終了
        # 矢印が来たタイミングで、ぴこんってなるエフェクトを追加する関数を定義🌟
        def pikon_effect(arrow, expert):                                                                       # ぴこんエフェクトの関数を定義
            self.play(GrowArrow(arrow))                                                                        #   - 矢印を伸ばすアニメーションを再生
            self.play(Flash(expert, color=YELLOW, flash_radius=0.5))                                           #   - エキスパートを黄色で光らせるアニメーションを再生
        
        # 各矢印とエキスパートに対してぴこんエフェクトを適用
        for arrow, expert in zip(input_arrows, experts):                                                       # 矢印とエキスパートを組み合わせてループ
            pikon_effect(arrow, expert)                                                                        #   - 各組み合わせに対してぴこんエフェクトを適用

        # ゲーティング関数を円で表現🔵
        gating_function = Circle(radius=0.5, color=YELLOW, fill_opacity=1).set_fill(YELLOW, opacity=0.5)       # 半径0.5の黄色い円を作成し、塗りつぶしの透明度を0.5に設定
        gating_function.next_to(experts, RIGHT, buff=1.5)                                                      # ゲーティング関数をエキスパートの右に配置し、間隔を1.5に設定
        gating_label = MathTex(r"w(x)").scale(0.7).next_to(gating_function, UP)                                # ゲーティング関数のラベルを作成し、サイズを0.7倍に設定し、ゲーティング関数の上に配置
        gating_label_explanation = Text(                                                                       # ゲーティング関数のラベルの説明テキストを作成
            "ゲーティング関数の重み",                                                                              #   - 説明テキストを設定
            font_size=24                                                                                       #   - フォントサイズを24に設定
        ).next_to(gating_label, UP * 2).shift(RIGHT * 1)                                                       #   - 説明テキストをラベルの上に配置し、右に1単位移動

        # 入力からゲーティング関数への矢印を追加し、その後消す処理を追加🚀
        input_to_gating_arrow = Arrow(                                                                         # 入力からゲーティング関数への矢印を作成
            start=input_text.get_right(),                                                                      #   - 矢印の始点を入力テキストの右端に設定
            end=gating_function.get_left(),                                                                    #   - 矢印の終点をゲーティング関数の左端に設定
            buff=0.1,                                                                                          #   - 矢印の始点と終点の間隔を0.1に設定
            color=YELLOW                                                                                       #   - 矢印の色を黄色に設定
        )                                                                                                      # 矢印の作成を終了
        self.play(GrowArrow(input_to_gating_arrow))                                                            # 入力からゲーティング関数への矢印を伸ばすアニメーションを再生
        self.remove(input_to_gating_arrow)                                                                     # 入力からゲーティング関数への矢印を削除

        self.play(                                                                                             # アニメーションを再生
            FadeIn(gating_function),                                                                           #   - ゲーティング関数をフェードインさせる
            Write(gating_label),                                                                               #   - ゲーティング関数のラベルを書く
            Write(gating_label_explanation)                                                                    #   - ゲーティング関数のラベルの説明を書く
        )                                                                                                      # アニメーションの再生を終了

        # エキスパートからゲーティング関数への矢印
        gating_arrows = VGroup(                                                                                # エキスパートからゲーティング関数への矢印のグループを作成
            Arrow(start=experts[0].get_right(), end=gating_function.get_left(), buff=0.1),                     #   - エキスパート1の右端からゲーティング関数の左端への矢印を作成
            Arrow(start=experts[1].get_right(), end=gating_function.get_left(), buff=0.1),                     #   - エキスパート2の右端からゲーティング関数の左端への矢印を作成
            Arrow(start=experts[2].get_right(), end=gating_function.get_left(), buff=0.1),                     #   - エキスパート3の右端からゲーティング関数の左端への矢印を作成
        )                                                                                                      # 矢印のグループ作成を終了
        # 矢印が来たタイミングで、ぴこんってなるエフェクトを追加しました🌟
        # f(x)を矢印が見えた瞬間に消すように変更しました🚀
        def pikon_effect_gating(arrow, expert_label):                                                          # ゲーティング関数のぴこんエフェクトの関数を定義
            self.play(                                                                                         #   - アニメーションを再生
                GrowArrow(arrow),                                                                              #     - 矢印を伸ばすアニメーションを再生
                FadeOut(expert_label)                                                                          #     - エキスパートのラベルをフェードアウトさせる
            )                                                                                                  #   - アニメーションの再生を終了
            self.play(Flash(gating_function, color=YELLOW, flash_radius=0.5))                                   #   - ゲーティング関数を黄色で光らせるアニメーションを再生
        
        for arrow, expert_label in zip(gating_arrows, expert_labels):                                          # 矢印とエキスパートのラベルを組み合わせてループ
            pikon_effect_gating(arrow, expert_label)                                                           #   - 各組み合わせに対してゲーティング関数のぴこんエフェクトを適用

        # 出力
        output_text = MathTex(r"\sum_{i=1}^{n} w(x)_i f_i(x)").scale(0.7)  # 出力テキストを作成し、サイズを0.7倍に設定
        output_text.next_to(gating_function, RIGHT, buff=1.5)             # 出力テキストをゲーティング関数の右側に配置し、間隔を1.5に設定
        output_text_explanation = Text("最終的な出力", font_size=24)      # 出力テキストの説明を作成し、フォントサイズを24に設定
        output_text_explanation.next_to(output_text, DOWN)                # 出力テキストの説明を出力テキストの下に配置
        output_arrow = Arrow(                                             # 出力への矢印を作成
            start=gating_function.get_right(),                            # 矢印の始点をゲーティング関数の右端に設定
            end=output_text.get_left(),                                   # 矢印の終点を出力テキストの左端に設定
            buff=0.1                                                      # 矢印の始点と終点の間隔を0.1に設定
        )

        self.play(                                                        # アニメーションを再生
            GrowArrow(output_arrow),                                     # 出力への矢印を伸ばすアニメーションを再生
            Write(output_text),                                          # 出力テキストを書くアニメーションを再生
            Write(output_text_explanation)                               # 出力テキストの説明を書くアニメーションを再生
        )

        self.wait(2)                                                      # 2秒間待機

        # 今までの図を消しますが、タイトルは残します🧹✨ 矢印もぴゅーんと消えますよ〜🚀✨
        # expertsの丸と矢印もちゃんと消えるように修正しました👌✨
        self.remove(input_text)                                           # 入力テキストを削除
        self.remove(experts)                                              # エキスパートの画像を削除
        self.remove(expert_labels)                                        # エキスパートのラベルを削除
        self.remove(gating_function)                                      # ゲーティング関数の画像を削除
        self.remove(gating_label)                                         # ゲーティング関数のラベルを削除
        self.remove(gating_label_explanation)                             # ゲーティング関数のラベルの説明を削除
        self.remove(input_to_gating_arrow)                                # 入力からゲーティング関数への矢印を削除
        self.remove(gating_arrows)                                        # エキスパートからゲーティング関数への矢印を削除
        self.remove(output_text)                                          # 出力テキストを削除
        self.remove(output_text_explanation)                              # 出力テキストの説明を削除
        self.remove(output_arrow)                                         # 出力への矢印を削除
        self.remove(input_arrows)                                         # 入力からエキスパートへの矢印を削除
        self.remove(*experts)                                             # エキスパートの画像を個別に削除
        self.remove(*input_arrows)                                        # 入力からエキスパートへの矢印を個別に削除
        self.remove(*gating_arrows)                                       # エキスパートからゲーティング関数への矢印を個別に削除
        # 入力データとエキスパートの出力関数を消します🧹✨
        self.remove(input_text_explanation)                               # 入力テキストの説明を削除
        self.remove(expert_labels_explanation)                            # エキスパートのラベルの説明を削除
        # すっきりしましたね！🌈✨

        input_text = Text("可愛い広告バナーを\nつくってほしい").scale(0.5)     # 新しい入力テキストを作成し、サイズを0.5倍に設定
        input_text.move_to(LEFT * 5)                                      # 入力テキストを左に5単位移動
        self.play(Write(input_text))                                      # 入力テキストを書くアニメーションを再生

        # エキスパート
        experts = Group(                                                 # エキスパートの画像をグループ化
            ImageMobject("images/marketing_character.png").scale(0.2),   #   - マーケターの画像を読み込み、サイズを0.2倍に設定
            ImageMobject("images/designer_character.png").scale(0.2),    #   - デザイナーの画像を読み込み、サイズを0.2倍に設定
            ImageMobject("images/writer_character.png").scale(0.2),      #   - ライターの画像を読み込み、サイズを0.2倍に設定
        ).arrange(DOWN, buff=0.25)                                       # エキスパートの画像を縦に並べ、間隔を0.25に設定
        experts.next_to(input_text, RIGHT, buff=1)                       # エキスパートの画像を入力テキストの右側に配置し、間隔を1に設定
        expert_labels = VGroup(                                          # エキスパートのラベルをグループ化
            Text("マーケター", font_size=30).next_to(experts[0], RIGHT, buff=0.2),  #   - マーケターのラベルを作成し、画像の右側に配置
            Text("デザイナー", font_size=30).next_to(experts[1], RIGHT, buff=0.2),  #   - デザイナーのラベルを作成し、画像の右側に配置
            Text("ライター", font_size=30).next_to(experts[2], RIGHT, buff=0.2),    #   - ライターのラベルを作成し、画像の右側に配置
        )

        self.play(                                                       # アニメーションを再生
            *[FadeIn(expert, scale=0.25) for expert in experts],         #   - エキスパートの画像をフェードインさせるアニメーションを再生
            *[Write(label) for label in expert_labels],                  #   - エキスパートのラベルを書くアニメーションを再生
        )

        # 入力からエキスパートへの矢印
        input_arrows = VGroup(                                           # 入力からエキスパートへの矢印をグループ化
            Arrow(                                                       #   - 入力テキストの右端からエキスパート1の左端への矢印を作成
                start=input_text.get_right(),                            #     - 矢印の始点を入力テキストの右端に設定
                end=experts[0].get_left(),                               #     - 矢印の終点をエキスパート1の左端に設定
                buff=0.1,                                                #     - 矢印の始点と終点の間隔を0.1に設定
            ),
            Arrow(                                                       #   - 入力テキストの右端からエキスパート2の左端への矢印を作成
                start=input_text.get_right(),                            #     - 矢印の始点を入力テキストの右端に設定
                end=experts[1].get_left(),                               #     - 矢印の終点をエキスパート2の左端に設定
                buff=0.1,                                                #     - 矢印の始点と終点の間隔を0.1に設定
            ),
            Arrow(                                                       #   - 入力テキストの右端からエキスパート3の左端への矢印を作成
                start=input_text.get_right(),                            #     - 矢印の始点を入力テキストの右端に設定
                end=experts[2].get_left(),                               #     - 矢印の終点をエキスパート3の左端に設定
                buff=0.1,                                                #     - 矢印の始点と終点の間隔を0.1に設定
            ),
        )
        for arrow, expert in zip(input_arrows, experts):                # 矢印とエキスパートを組み合わせてループ
            self.play(                                                  #   - アニメーションを再生
                GrowArrow(arrow),                                       #     - 矢印を伸ばすアニメーションを再生
                Flash(expert, color=YELLOW, flash_radius=0.25),         #     - エキスパートを黄色で光らせるアニメーションを再生
            )

        # ゲーティング関数（ディレクター）
        gating_function = ImageMobject("images/director_character.png").scale(0.25)  # ディレクターの画像を読み込み、サイズを0.25倍に設定
        gating_function.next_to(experts, RIGHT, buff=1)                              # ディレクターの画像をエキスパートの右側に配置し、間隔を1に設定
        gating_label = Text("ディレクター").scale(0.5)                                 # ディレクターのラベルを作成し、サイズを0.5倍に設定
        gating_label.next_to(gating_function, UP)                                    # ディレクターのラベルをディレクターの画像の上に配置

        self.play(                                                                    # アニメーションを再生
            FadeIn(gating_function),                                                 #   - ディレクターの画像をフェードインさせるアニメーションを再生
            Write(gating_label),                                                     #   - ディレクターのラベルを書くアニメーションを再生
        )
        # エキスパートからゲーティング関数への矢印
        gating_arrows = VGroup(                                                        # エキスパートからゲーティング関数への矢印をグループ化
            Arrow(                                                                     # エキスパート1の右端からディレクターの左端へ矢印を引く
                start=experts[0].get_right(),                                         # 矢印の始点をエキスパート1の右端に設定
                end=gating_function.get_left(),                                       # 矢印の終点をディレクターの左端に設定
                buff=0.1,                                                             # 矢印の始点と終点の間隔を0.1に設定
            ),
            Arrow(                                                                     # エキスパート2の右端からディレクターの左端へ矢印を引く
                start=experts[1].get_right(),                                         # 矢印の始点をエキスパート2の右端に設定
                end=gating_function.get_left(),                                       # 矢印の終点をディレクターの左端に設定
                buff=0.1,                                                             # 矢印の始点と終点の間隔を0.1に設定
            ),
            Arrow(                                                                     # エキスパート3の右端からディレクターの左端へ矢印を引く
                start=experts[2].get_right(),                                         # 矢印の始点をエキスパート3の右端に設定
                end=gating_function.get_left(),                                       # 矢印の終点をディレクターの左端に設定
                buff=0.1,                                                             # 矢印の始点と終点の間隔を0.1に設定
            ),
        )
        for arrow, expert_label in zip(gating_arrows, expert_labels):                 # 矢印とエキスパートのラベルを組み合わせてループ
            self.play(                                                                 # アニメーションを再生
                GrowArrow(arrow),                                                     # 矢印を伸ばすアニメーションを再生
                FadeOut(expert_label),                                                # エキスパートのラベルをフェードアウトさせるアニメーションを再生
            )
            self.play(Flash(gating_function, color=YELLOW, flash_radius=0.25))         # ディレクターを黄色で光らせるアニメーションを再生

        # 出力
        output_image = ImageMobject("images/cute_ad_banner.png").scale(0.5)           # 可愛い広告バナーの画像を読み込み、サイズを0.5倍に設定
        output_image.next_to(gating_function, RIGHT, buff=1)                          # 出力画像をディレクターの右側に配置し、間隔を1に設定
        output_text = Text("可愛い広告バナー").scale(0.5)                             # 出力テキストを作成し、サイズを0.5倍に設定
        output_text.next_to(output_image, DOWN)                                       # 出力テキストを出力画像の下に配置
        output_arrow = Arrow(                                                         # 出力への矢印を作成
            start=gating_function.get_right(),                                        # 矢印の始点をディレクターの右端に設定
            end=output_image.get_left(),                                              # 矢印の終点を出力画像の左端に設定
            buff=0.1,                                                                 # 矢印の始点と終点の間隔を0.1に設定
        )

        self.play(                                                                     # アニメーションを再生
            GrowArrow(output_arrow),                                                  # 出力への矢印を伸ばすアニメーションを再生
            FadeIn(output_image),                                                     # 出力画像をフェードインさせるアニメーションを再生
            Write(output_text),                                                       # 出力テキストを書くアニメーションを再生
        )

        self.wait(2)                                                                   # 2秒間待機
        # 最終の動画出力ファイルパスをprintする
        print(f"動画出力ファイルパス: {self.renderer.file_writer.movie_file_path}")  # 動画出力ファイルのパスを表示する
        # 入力からエキスパートへの矢印
        input_arrows = VGroup(                                                         # 入力テキストからエキスパートへの矢印をグループ化
            Arrow(                                                                     # 入力テキストの右端からエキスパート1の左端へ矢印を引く
                start=input_text.get_right(),                                         # 矢印の始点を入力テキストの右端に設定
                end=experts[0].get_left(),                                            # 矢印の終点をエキスパート1の左端に設定
                buff=0.1,                                                             # 矢印の始点と終点の間隔を0.1に設定
            ),
            Arrow(                                                                     # 入力テキストの右端からエキスパート2の左端へ矢印を引く
                start=input_text.get_right(),                                         # 矢印の始点を入力テキストの右端に設定
                end=experts[1].get_left(),                                            # 矢印の終点をエキスパート2の左端に設定
                buff=0.1,                                                             # 矢印の始点と終点の間隔を0.1に設定
            ),
            Arrow(                                                                     # 入力テキストの右端からエキスパート3の左端へ矢印を引く
                start=input_text.get_right(),                                         # 矢印の始点を入力テキストの右端に設定
                end=experts[2].get_left(),                                            # 矢印の終点をエキスパート3の左端に設定
                buff=0.1,                                                             # 矢印の始点と終点の間隔を0.1に設定
            ),
        )
        for arrow, expert in zip(input_arrows, experts):                              # 矢印とエキスパートを組み合わせてループ
            self.play(                                                                 # アニメーションを再生
                GrowArrow(arrow),                                                     # 矢印を伸ばすアニメーションを再生
                Flash(                                                                # エキスパートを光らせるアニメーションを再生
                    expert,                                                           # 光らせる対象をエキスパートに設定
                    color=YELLOW,                                                     # 光の色を黄色に設定
                    flash_radius=0.25,                                                # 光の半径を0.25に設定
                ),
            )

        # ゲーティング関数（ディレクター）
        gating_function = ImageMobject("images/director_character.png").scale(0.25)   # ディレクターの画像を読み込み、サイズを0.25倍に設定
        gating_function.next_to(experts, RIGHT, buff=1)                               # ディレクターの画像をエキスパートの右側に配置し、間隔を1に設定
        gating_label = Text("ディレクター").scale(0.5)                                # ディレクターのラベルを作成し、サイズを0.5倍に設定
        gating_label.next_to(gating_function, UP)                                     # ディレクターのラベルをディレクターの画像の上に配置

        self.play(                                                                     # アニメーションを再生
            FadeIn(gating_function),                                                  # ディレクターの画像をフェードインさせるアニメーションを再生
            Write(gating_label),                                                      # ディレクターのラベルを書くアニメーションを再生
        )

        # エキスパートからゲーティング関数への矢印
        gating_arrows = VGroup(                                                        # エキスパートからゲーティング関数への矢印をグループ化
            Arrow(                                                                     # エキスパート1の右端からディレクターの左端へ矢印を引く
                start=experts[0].get_right(),                                         # 矢印の始点をエキスパート1の右端に設定
                end=gating_function.get_left(),                                       # 矢印の終点をディレクターの左端に設定
                buff=0.1,                                                             # 矢印の始点と終点の間隔を0.1に設定
            ),
            Arrow(                                                                     # エキスパート2の右端からディレクターの左端へ矢印を引く
                start=experts[1].get_right(),                                         # 矢印の始点をエキスパート2の右端に設定
                end=gating_function.get_left(),                                       # 矢印の終点をディレクターの左端に設定
                buff=0.1,                                                             # 矢印の始点と終点の間隔を0.1に設定
            ),
            Arrow(                                                                     # エキスパート3の右端からディレクターの左端へ矢印を引く
                start=experts[2].get_right(),                                         # 矢印の始点をエキスパート3の右端に設定
                end=gating_function.get_left(),                                       # 矢印の終点をディレクターの左端に設定
                buff=0.1,                                                             # 矢印の始点と終点の間隔を0.1に設定
            ),
        )
        for arrow, expert_label in zip(gating_arrows, expert_labels):                 # 矢印とエキスパートのラベルを組み合わせてループ
            self.play(                                                                 # アニメーションを再生
                GrowArrow(arrow),                                                     # 矢印を伸ばすアニメーションを再生
                FadeOut(expert_label),                                                # エキスパートのラベルをフェードアウトさせるアニメーションを再生
            )
            self.play(                                                                 # アニメーションを再生
                Flash(                                                                # ディレクターを光らせるアニメーションを再生
                    gating_function,                                                  # 光らせる対象をディレクターに設定
                    color=YELLOW,                                                     # 光の色を黄色に設定
                    flash_radius=0.25,                                                # 光の半径を0.25に設定
                )
            )

        # 出力
        output_image = ImageMobject("images/cute_ad_banner.png").scale(0.5)           # 可愛い広告バナーの画像を読み込み、サイズを0.5倍に設定
        output_image.next_to(gating_function, RIGHT, buff=1)                          # 出力画像をディレクターの右側に配置し、間隔を1に設定
        output_text = Text("可愛い広告バナー").scale(0.5)                             # 出力テキストを作成し、サイズを0.5倍に設定
        output_text.next_to(output_image, DOWN)                                       # 出力テキストを出力画像の下に配置
        output_arrow = Arrow(                                                         # 出力への矢印を作成
            start=gating_function.get_right(),                                        # 矢印の始点をディレクターの右端に設定
            end=output_image.get_left(),                                              # 矢印の終点を出力画像の左端に設定
            buff=0.1,                                                                 # 矢印の始点と終点の間隔を0.1に設定
        )

        self.play(                                                                     # アニメーションを再生
            GrowArrow(output_arrow),                                                  # 出力への矢印を伸ばすアニメーションを再生
            FadeIn(output_image),                                                     # 出力画像をフェードインさせるアニメーションを再生
            Write(output_text),                                                       # 出力テキストを書くアニメーションを再生
        )

        self.wait(2)                                                                   # 2秒間待機

        # 最終の動画出力ファイルパスをprintする
        print(f"動画出力ファイルパス: {self.renderer.file_writer.movie_file_path}")  # 動画出力ファイルのパスを表示する
