import math

from manim import *
from manim.utils.color.XKCD import AQUAMARINE


class Main(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        self.camera.frame.set(width=16*2, height=9*2)

        plane = NumberPlane(
            x_range=[-100, 100, 1],
            y_range=[-50, 50, 1],
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 1,
                "stroke_opacity": 0
            }
        )

        self.play(Create(plane))

        focus1 = Dot(point=(5, 0, 0), color=AQUAMARINE)
        focus2 = Dot(point=(-5, 0, 0), color=AQUAMARINE)
        focus_label1 = MathTex("F(c, 0)", font_size=40).next_to(focus1, UP)
        focus_label2 = MathTex("F'(-c, 0)", font_size=40).next_to(focus2, UP)

        ellipse = Ellipse(width=14, height=4 * math.sqrt(6), color=BLUE)
        ellipse.move_to((0, 0, 0))

        tex1 = Tex(r"초점이 \(F(c, 0), F'(-c, 0)\)인 타원 \(C\)", tex_template=TexTemplate(preamble=r"\usepackage{kotex}"), font_size=40)
        tex1.to_edge(UP)

        # 애니메이션 재생
        self.play(Create(focus1), Create(focus2))
        self.play(Write(focus_label1), Write(focus_label2))
        self.play(Create(ellipse), Write(tex1).set_run_time(1))
        self.wait(1)

        dot_p = Dot(point=(7/5, 24/5, 0), color=PINK)
        dot_p_label = MathTex("P", font_size=40).next_to(dot_p, UP)
        dot_p_label1 = Tex(r"1사분면 위의 점", tex_template=TexTemplate(preamble=r"\usepackage{kotex}"), font_size=40).next_to(dot_p_label, LEFT)
        self.play(Create(dot_p), Write(dot_p_label), Write(dot_p_label1).set_run_time(1))
        self.wait()
        self.play(FadeOut(dot_p_label1).set_run_time(0.2), FadeOut(tex1).set_run_time(0.2))
        self.wait()

        line_pf = Line(start=dot_p.get_center(), end=focus1.get_center(), color=AQUAMARINE)

        line_l = plane.plot(lambda x: 3 * x / 4 + 15 / 4, color=WHITE)
        line_l_2 = Line(start=dot_p.get_center(), end=focus2.get_center())
        line_l_label = Tex(r"\(l\)", font_size=40).next_to((3,6,0), LEFT*2)
        line_l_label2 = Tex(r"접선", tex_template=TexTemplate(preamble=r"\usepackage{kotex}"), font_size=40).next_to(line_l_label, LEFT)
        line_l_label3 = Tex(r"\(F'\)을 지나는 ", tex_template=TexTemplate(preamble=r"\usepackage{kotex}"), font_size=40).next_to(line_l_label2, LEFT)
        self.play(Create(line_pf).set_run_time(0.8))
        angle_pf_pf2 = RightAngle(line_l_2, line_pf, length=0.3, quadrant=(1, 1))
        self.play(Create(line_l).set_run_time(1), Write(line_l_label3), Write(line_l_label2), Write(line_l_label), Create(angle_pf_pf2))
        self.wait()

        circle_1 = Circle(radius=6, color=AQUAMARINE).move_to((5, 0, 0))
        circle_1_label = Tex(r"반지름이 \( \overline{PF} \)인 원", tex_template=TexTemplate(preamble=r"\usepackage{kotex}"), font_size=40).move_to((5, 2, 0))
        self.play(Create(circle_1), Write(circle_1_label))
        self.wait()
        self.play(FadeOut(circle_1_label).set_run_time(0.2), FadeOut(line_l_label3).set_run_time(0.2))
        self.wait()

        line_m = plane.plot(lambda x: (35 - x) / 7, color=WHITE)
        line_m_label = Tex(r"\(m\)", font_size=40).next_to((-10.5,6.5,0), UP*1)
        line_m_label2 = Tex(r"접선", tex_template=TexTemplate(preamble=r"\usepackage{kotex}"), font_size=40).next_to(line_m_label, LEFT)

        self.play(
            Create(line_m).set_run_time(0.4),
            Write(line_m_label),
            Write(line_m_label2)
                # self.camera.frame.animate.move_to((8,0,0)).set(width=16*4, height=9*4)
        )
        self.wait()

        dot_q = Dot(point=(-1, 0, 0), color=AQUAMARINE)
        dot_q_label = MathTex("Q", font_size=40).next_to(dot_q, np.array((-1.0, 1.0, 0.0)))
        self.play(Create(dot_q), Write(dot_q_label))
        # self.wait()

        self.play(self.camera.frame.animate.move_to((8,0,0)))

        text1 = Tex(r"\( \overline{FQ} : \overline{F'Q} = 3 : 2 \)이므로 \( \overline{FQ}=3k,\) \(\overline{F'Q}=2k\) \((k > 0)\)라고 하자", tex_template=TexTemplate(preamble=r"\usepackage{kotex}"), font_size=40)
        text1.move_to((17, 6, 0))
        self.play(Write(text1))

        line_f2q = Line(start=focus2.get_center(), end=dot_q.get_center())
        # brace_f2q = Brace(line_f2q, DOWN, stroke_width=0.05)
        brace_f2q = DashedVMobject(
            ArcBetweenPoints(line_f2q.get_start(), line_f2q.get_end(), angle=PI/3)
        )
        # brace_f2q_label = brace_f2q.get_tex("2k")
        brace_f2q_label = MathTex("2k").next_to(brace_f2q, DOWN)
        line_fq = Line(start=dot_q.get_center(), end=focus1.get_center())
        # brace_fq = Brace(line_fq, DOWN, stroke_width=0.05)
        brace_fq = DashedVMobject(
            ArcBetweenPoints(line_fq.get_start(), line_fq.get_end(), angle=PI/3)
        )
        # brace_fq_label = brace_fq.get_tex("3k")
        brace_fq_label = MathTex("3k").next_to(brace_fq, DOWN)
        self.play(Create(brace_fq), Create(brace_f2q))
        self.play(Write(brace_fq_label), Write(brace_f2q_label))
        self.wait()
        self.play(FadeOut(text1))

        line_ff2 = Line(start=focus1.get_center(), end=focus2.get_center())
        # brace_ff2 = Brace(line_ff2, DOWN, stroke_width=0.05)
        brace_ff2 = DashedVMobject(
            ArcBetweenPoints(line_ff2.get_end(), line_ff2.get_start(), angle=PI/4)
        )
        # brace_ff2_label = brace_ff2.get_tex("5k")
        brace_ff2_label = MathTex("5k").next_to(brace_ff2, DOWN)

        # brace_fq_label.generate_target().move_to(brace_ff2_label.get_center())
        # brace_f2q_label.generate_target().move_to(brace_ff2_label.get_center())
        self.play(
            FadeOut(brace_fq), FadeOut(brace_f2q), FadeTransform(brace_fq_label, brace_ff2_label), FadeTransform(brace_f2q_label, brace_ff2_label), Create(brace_ff2)
        )

        lines1 = VGroup(
            brace_ff2_label,
            MathTex("{5}", "k", "=", "{2}", "c").move_to((17, 6, 0)),
            MathTex("c", "=", r"\frac{5}{2}", "k").move_to((17, 6, 0))
        )
        self.play(
            TransformMatchingTex(
                lines1[0].copy(), lines1[1]
            ),
        )
        self.wait()
        self.play(
            TransformMatchingTex(lines1[1].copy(), lines1[2]),
            FadeOut(lines1[1])
        )
        self.wait()
        self.play(
            lines1[2].animate.shift((6, 1, 0))
        )
        self.wait()

        # brace_pf = BraceBetweenPoints(line_pf.get_end(), line_pf.get_start(), stroke_width=0.05)
        brace_pf = DashedVMobject(
            ArcBetweenPoints(line_pf.get_end(), line_pf.get_start(), angle=PI/3)
        )
        # brace_pf_label = brace_pf.get_tex("3k")
        brace_pf_label = MathTex("3k").move_to(brace_pf).shift(RIGHT + UP)

        # brace_fq = BraceBetweenPoints(line_fq.get_end(), line_fq.get_start(), stroke_width=0.05)
        brace_fq = DashedVMobject(
            ArcBetweenPoints(line_fq.get_end(), line_fq.get_start(), angle=PI/3)
        )
        # brace_fq_label = brace_fq.get_tex("3k")
        brace_fq_label = MathTex("3k").next_to(brace_fq, UP)

        self.play(Create(brace_fq), Write(brace_fq_label).set_run_time(0.5))
        self.wait()

        self.play(
            Transform(
                brace_fq, brace_pf
            ),
            TransformMatchingTex(
                brace_fq_label, brace_pf_label
            )
        )
        self.wait(0.2)

        lines2 = VGroup(
            MathTex(r"\overline{PF'}^{2}", "=", r"\overline{FF'}^{2}", "-", r"\overline{PF}^{2}"),
            MathTex(r"\overline{PF'}^{2}", "=", "(5k)^{2}", "-", "(3k)^{2}"),
            MathTex(r"\overline{PF'}^{2}", "=", "16k^{2}"),
            MathTex(r"\overline{PF'}", "=", r"\sqrt{16k^{2}}"),
            MathTex(r"\overline{PF'}", "=", "4k")
        )
        for e in lines2:
            e.move_to((17, 5, 0))

        self.play(
            Write(
                lines2[0]
            )
        )
        self.wait(0.2)

        self.play(
            TransformMatchingTex(
                VGroup(brace_pf_label.copy(), brace_ff2_label.copy()), lines2[1],
                key_map={
                    "3k": "(3k)^{2}",
                    "5k": "(5k)^{2}",
                }
            ).set_run_time(0.5),
            FadeOut(lines2[0]).set_run_time(0.5)
        )
        self.play(
            TransformMatchingTex(
                lines2[1].copy(), lines2[2],
                transform_mismatches=True
            ).set_run_time(0.5),
            FadeOut(lines2[1]).set_run_time(0.5)
        )
        self.wait(0.2)
        lines2_2_new = MathTex(r"\overline{PF'}^{2}", "=", "16k^{2}", substrings_to_isolate=[r"\overline{PF'}", "16k^{2}"])
        lines2_2_new.replace(lines2[2])
        lines2_2_new.match_style(lines2[2])

        self.play(
            TransformMatchingTex(
                lines2_2_new, lines2[3],
                transform_mismatches=True
            ),
            FadeOut(lines2[2]).set_run_time(0.5)
        )
        self.wait(0.2)
        self.play(
            TransformMatchingTex(
                lines2[3].copy(), lines2[4],
                transform_mismatches=True
            ).set_run_time(0.5),
            FadeOut(lines2[3]).set_run_time(0.5)
        )
        self.wait(0.2)

        # brace_pf2 = BraceBetweenPoints(dot_p.get_center(), focus2.get_center(), stroke_width=0.05)
        brace_pf2 = DashedVMobject(
            ArcBetweenPoints(dot_p.get_center(), focus2.get_center(), angle=PI/3)
        )
        # brace_pf2_label = brace_pf2.get_tex("4k")
        brace_pf2_label = MathTex("4k").move_to(brace_pf2).shift(LEFT*1.2 + UP)

        self.play(
            Create(brace_pf2),
            Transform(
                lines2[4], brace_pf2_label
            )
        )
        self.wait()

        dot_h = Dot((7/5, 0, 0), color=BLUE_C)
        dot_h_label = MathTex("H", font_size=40).next_to(dot_h, DOWN)
        dot_h_label2 = Tex(r"\(P\)에서의 수선의 발", tex_template=TexTemplate(preamble=r"\usepackage{kotex}"), font_size=40).next_to(dot_h_label, LEFT).shift(DOWN * 0.02, RIGHT * 0.1)
        line_ph = Line(dot_p.get_center(), dot_h.get_center(), color=BLUE_C)
        rightangle_ph = RightAngle(line_ph, Line((0, 0, 0), (10, 0, 0)), length=0.3, quadrant=(-1, 1))

        self.play(Create(dot_h), Write(dot_h_label), Write(dot_h_label2), Create(line_ph), Create(rightangle_ph))
        self.wait()
        
        self.play(FadeOut(dot_h_label2).set_run_time(0.2))
        self.wait()

        tri_pff2 = Polygon(dot_p.get_center(), focus1.get_center(), focus2.get_center(), color=BLUE).set_fill(color=BLUE, opacity=0.5)
        tri_phf = Polygon(dot_p.get_center(), focus1.get_center(), dot_h.get_center(), color=GREEN).set_fill(color=GREEN, opacity=0.5)

        # self.play(Create(tri_pff2))
        # self.wait()
        tex2 = MathTex(r"\Delta", "F'", "P", "F").move_to((14, 7, 0))
        tex3 = MathTex(r"\sim", r"\Delta", "P", "H", "F").next_to(tex2, RIGHT)
        # tri_pff2.generate_target()
        # tri_pff2.target.move_to((14, 5, 0))
        # tri_pff2.target.rotate(-math.asin(3/5)-PI/2)
        # tri_pff2.target.scale(0.1)

        # tri_phf.generate_target()
        # tri_phf.target.shift(obj2.get_center() - tri_phf.get_center())
        # tri_phf.target.scale(0.1)
        # self.play(
            # MoveToTarget(tri_pff2),
            # FadeOut(tri_pff2)
        # )
        self.play(
            FadeIn(tri_pff2),
            Write(tex2)
        )
        self.play(FadeOut(tri_pff2))
        # self.wait()
        self.play(
            FadeIn(tri_phf),
            Write(tex3)
        )
        self.play(FadeOut(tri_phf))
        # tri_pff2_c = tri_pff2.copy().set_fill(color=GREEN, opacity=0.5)
        # self.remove(tri_pff2_c)
        # self.play(
        #     Write(obj1),
        #     Transform(
        #         tri_phf, tri_pff2_c,
                # path_arc=90*DEGREES
            # ),
            # Write(obj2),
            # FadeOut(tri_phf)
        # )
        self.wait()

        lines3 = VGroup(
            MathTex(r"\overline{FP}", ":", r"\overline{F'P}", ":", r"\overline{F'F}", "=", r"\overline{FH}", ":", r"\overline{PH}", ":", r"\overline{PF}"),
            MathTex("3k", ":", "4k", ":", "5k", "=", r"\overline{FH}", ":", r"\overline{PH}", ":", "3k"),
            MathTex("3k", ":", "5k", "=", r"\overline{FH}", ":", "3k"),
            MathTex("3k", r"\times", "3k", "=", "5k", r"\times", r"\overline{FH}"),
            MathTex(r"\frac{9k^2}{5k}", "=", r"\overline{FH}"),
            MathTex(r"\overline{FH}", "=", r"\frac{9k}{5}")
        ).next_to(tex2, DOWN).shift(np.array((2, 0, 0)))
        # for e in lines3:
            # e.arrange(center=False, aligned_edge=LEFT)
        lines3.arrange(DOWN, center=False, aligned_edge=LEFT)
        lines4 = VGroup(
            MathTex(r"\overline{FP}", ":", r"\overline{F'P}", ":", r"\overline{F'F}", "=", r"\overline{FH}", ":", r"\overline{PH}", ":", r"\overline{PF}"),
            MathTex("3k", ":", "4k", ":", "5k", "=", r"\overline{FH}", ":", r"\overline{PH}", ":", "3k"),
            MathTex("4k", ":", "5k", "=", r"\overline{PH}", ":", "3k"),
            MathTex("4k", r"\times", "3k", "=", "5k", r"\times", r"\overline{PH}"),
            MathTex(r"\frac{12k^2}{5k}", "=", r"\overline{PH}"),
            MathTex(r"\overline{PH}", "=", r"\frac{12k}{5}")
        ).next_to(tex2, DOWN).shift(np.array((2, 0, 0)))
        # for e in lines4:
        #     e.arrange(center=False, aligned_edge=LEFT)
        lines4.arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Write(lines3[0]))
        for i in range(len(lines3)-1):
            self.play(
                TransformMatchingTex(
                    lines3[i].copy(), lines3[i+1],
                    transform_mismatches=True,
                    fade_transform_mismatches=True
                )
            )
            self.wait()

        brace_fh = DashedVMobject(
            ArcBetweenPoints(focus1.get_center(), dot_h.get_center(), angle=PI/4)
        )
        brace_fh_label = MathTex(r"\frac{9k}{5}").scale(0.7).next_to(brace_fh, UP)
        self.play(
            Create(brace_fh),
            TransformMatchingTex(
                lines3[5].copy(), brace_fh_label
            )
        )
        self.wait()

        self.play(FadeOut(lines3[1:]))
        self.wait()

        # self.play(Write(lines4[0]))
        # self.wait()
        for i in range(len(lines4)-1):
            if i == 0:
                self.play(
                    TransformMatchingTex(
                        lines3[0].copy(), lines4[1],
                        transform_mismatches=True,
                        fade_transform_mismatches=True
                    )
                )
            else:
                self.play(
                    TransformMatchingTex(
                        lines4[i].copy(), lines4[i+1],
                        transform_mismatches=True,
                        fade_transform_mismatches=True
                    )
                )
            self.wait()

        brace_ph = DashedVMobject(
            ArcBetweenPoints(dot_h.get_center(), dot_p.get_center(), angle=PI/4)
        )
        brace_ph_label = MathTex(r"\frac{12}{5}k").scale(0.8).next_to(brace_ph, RIGHT)
        self.play(
            Create(brace_ph),
            TransformMatchingTex(
                lines4[5].copy(), brace_ph_label
            )
        )
        self.wait()

        self.play(FadeOut(lines4), FadeOut(tex2), FadeOut(tex3), FadeOut(lines3[0]))
        self.wait()

        brace_of = DashedVMobject(
            ArcBetweenPoints((0,0,0), focus1.get_center(), angle=PI/4)
        )
        brace_of_label = MathTex(r"\frac{5}{2}k").next_to(brace_of, DOWN).scale(0.7)

        brace_oh = DashedVMobject(
            ArcBetweenPoints(dot_h.get_center(), (0,0,0), angle=PI/4)
        )
        brace_oh_label = MathTex(r"\frac{7}{10}k").next_to(brace_oh, UP).scale(0.7)

        self.play(
            Create(brace_of),
            Create(brace_of_label)
        )
        self.wait()
        self.play(
            FadeOut(brace_of),
            FadeOut(brace_fh),
            FadeTransform(brace_of_label, brace_oh_label),
            FadeTransform(brace_fh_label, brace_oh_label),
            Create(brace_oh)
        )
        self.wait()

        dot_p_label2 = Tex(r"$\left(\frac{7}{10}k, \frac{12}{5}k\right)$", tex_template=TexTemplate(preamble=r"\usepackage{kotex}")).scale(1.2).next_to(dot_p_label, RIGHT)

        self.play(
            FadeOut(brace_ph),
            FadeOut(brace_oh),
            TransformMatchingTex(brace_ph_label, dot_p_label2),
            TransformMatchingTex(brace_oh_label, dot_p_label2)
        )
        self.wait()

        # 타원의 방정식
        ellipse_labels = VGroup(
            Tex(r"타원 \(C:\)", tex_template=TexTemplate(preamble=r"\usepackage{kotex}")).scale(1.2),
            Tex(r"\(\frac{x^2}{a^2}\)\(+\)\(\frac{y^2}{b^2}\)\(=\)\(1\)").scale(1.5),
            Tex(r"\((a > 0, b > 0)\)").scale(1.2)
        ).move_to((12, 7, 0)).arrange(center=False)
        self.play(
            Write(ellipse_labels)
        )
        self.wait()

        a_labels = VGroup(
            MathTex("2a", "=", "4k", "+", "3k"),
            MathTex("2a", "=", "7k"),
            MathTex("a", "=", r"\frac{7}{2}", "k")
        ).next_to(ellipse_labels, DOWN).arrange(DOWN, center=False, aligned_edge=LEFT)

        self.play(
            TransformMatchingTex(
                VGroup(brace_pf2_label.copy(), brace_pf_label.copy()), a_labels[0],
                transform_mismatches=True
            )
        )
        self.wait()
        self.play(
            TransformMatchingTex(
                a_labels[0].copy(), a_labels[1],
                transform_mismatches=True
            )
        )
        self.wait()
        self.play(
            TransformMatchingTex(
                a_labels[1].copy(), a_labels[2],
                transform_mismatches=True
            )
        )
        self.wait()
        self.play(
            a_labels[2].animate.next_to(lines1[2], DOWN)
        )
        self.play(
            FadeOut(a_labels[:-1])
        )
        self.wait()

        b_labels = VGroup(
            MathTex("b^2", "=", "a^2", "-", "c^2"),
            MathTex("b^2", "=", r"\left(\frac{7}{2}k\right)^2", "-", r"\left(\frac{5}{2}k\right)^2"),
            MathTex("b^2", "=", "6k^2"),
            MathTex("b", "=", r"\sqrt{6}k")
        ).next_to(ellipse_labels, DOWN).arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(
            Write(b_labels[0])
        )
        self.wait()
        self.play(
            TransformMatchingTex(
                VGroup(b_labels[0].copy(), a_labels[2].copy()), b_labels[1],
                transform_mismatches=True
            )
        )
        self.wait()
        self.play(
            TransformMatchingTex(
                b_labels[1].copy(), b_labels[2],
                transform_mismatches=True
            )
        )
        self.wait()
        self.play(
            TransformMatchingTex(
                b_labels[2].copy(), b_labels[3],
                transform_mismatches=True
            )
        )
        self.wait()
        self.play(
            b_labels[3].animate.next_to(a_labels[2], DOWN).shift((0, -0.25, 0))
        )
        self.play(FadeOut(b_labels[:-1]))
        self.wait()
        self.play(self.camera.frame.animate.move_to((0, 0, 0)))
        self.play(self.camera.frame.animate.set(width=16*3, height=9*3))
        self.wait()

        ellipse_labels_new = VGroup(
            Tex(r"타원 \(C:\) ", tex_template=TexTemplate(preamble=r"\usepackage{kotex}")).scale(1.5),
            Tex(r"\(\frac{x^2}{\left(\frac{7}{2}k\right)^2}\)\(+\)\(\frac{y^2}{\left(\sqrt{6}k\right)^2}\)\(=\)\(1\)").scale(2),
        ).move_to((-10, 10, 0)).arrange(center=False)

        line_m_label12 = VGroup(line_m_label, line_m_label2)

        self.play(
            FadeTransform(
                VGroup(ellipse_labels, lines1[2], a_labels[2], b_labels[3]).move_to(ellipse_labels.get_center()), ellipse_labels_new,
                # transform_mismatches=True,
                # key_map={
                #     r"\frac{7}{2}k": "a^2",
                #     r"\sqrt{6}k": "b^2",
                #     r"a" : "a^2",
                #     r"b" : "b^2"
                # }
            ),
            line_m_label12.animate.scale(2)
        )
        self.wait()
        line_m_label22 = MathTex(":").scale(2).next_to(line_m_label12, RIGHT)
        line_m_label3 = MathTex(r"\frac{\frac{7}{10}kx}{\left(\frac{7}{2}k\right)^2}", "+", r"\frac{\frac{12}{5}ky}{\left(\sqrt{6}k\right)^2}", "=", "1").scale(1.5).next_to(line_m_label22, RIGHT)
        line_m_label4 = MathTex("2x", "+", "14y", "=", "35k").scale(1.5).next_to(line_m_label3, DOWN)

        self.play(
            FadeIn(line_m_label22),
            FadeTransform(
                VGroup(ellipse_labels_new.copy(), dot_p_label2.copy()).scale(0.8), line_m_label3
            )
        )
        self.wait()
        self.play(
            FadeTransform(
                line_m_label3.copy(), line_m_label4
            )
        )
        self.wait()
        self.play(line_m_label4.animate.move_to(line_m_label3), FadeOut(line_m_label3))
        self.wait()

        line_m_label4_new = line_m_label4.copy()
        self.play(self.camera.frame.animate.move_to((15, 0, 0)))
        self.play(line_m_label4_new.animate.move_to((35, 10, 0)))
        self.play(Write(lines1[2].scale(1.5).next_to(line_m_label4_new, DOWN)))

        dot_r = Dot((35, 0, 0)).scale(1.5)
        dot_r_label = MathTex("R").scale(1.5).next_to(dot_r, UP)
        dot_r_label2 = MathTex(r"\left(\frac{35}{2}k,\,0\right)").scale(1.5).next_to(dot_r_label, RIGHT)

        self.play(
            Create(dot_r),
            Write(dot_r_label)
        )
        self.wait()

        self.play(
            FadeTransform(
                line_m_label4_new, dot_r_label2
            )
        )
        self.wait()

        brace_f2o = DashedVMobject(
            ArcBetweenPoints((0,0,0), focus2.get_center(), angle=PI/4)
        )
        brace_f2o_label = MathTex(r"\frac{5}{2}k").next_to(brace_f2o, UP)

        brace_or = DashedVMobject(
            ArcBetweenPoints(dot_r.get_center(), (0,0,0), angle=PI/20), num_dashes=40
        )
        brace_or_label = MathTex(r"\frac{35}{2}k").next_to(brace_or, UP)

        self.play(
            Create(brace_f2o),
            FadeTransform(
                lines1[2], brace_f2o_label
            )
        )
        self.play(
            Create(brace_or),
            FadeTransform(
                dot_r_label2.copy(), brace_or_label
            )
        )
        self.wait()

        lines5 = VGroup(
            MathTex(r"\overline{F'R}", "=", "40"),
            MathTex(r"\frac{5}{2}k", "+", r"\frac{35}{2}k", "=", "40"),
            MathTex(r"20k", "=", "40"),
            MathTex(r"k", "=", "2"),
        ).move_to((20, 7, 0)).scale(1.5).arrange(DOWN, center=False, aligned_edge=LEFT)

        self.play(
            Write(lines5[0])
        )
        self.wait()
        self.play(
            TransformMatchingTex(
                VGroup(lines5[0].copy(), brace_or_label, brace_f2o_label), lines5[1],
                transform_mismatches=True,
                fade_transform_mismatches=True
            ),
            FadeOut(brace_f2o), FadeOut(brace_or)
        )
        self.wait()

        for i in range(len(lines5)-2):
            self.play(
                TransformMatchingTex(
                    lines5[i+1].copy(), lines5[i+2],
                    transform_mismatches=True,
                    fade_transform_mismatches=True
                )
            )
            self.wait()

        self.play(
            FadeOut(lines5[:-1]),
            lines5[-1].animate.move_to(lines5[0])
        )


        self.play(
            Write(MathTex(r"\therefore", "\overline{PF}", "+", "\overline{PF'}", "=", "7k", "=", "7", r"\times", "2", "=", "14").scale(1.5).next_to(lines5[-1], DOWN))
        )
        self.wait(4)
        # line_m_labels = VGroup(
        #
        # )
        # self.play(
        #     TransformMatchingTex(
        # )


class TexTest(Scene):
    def construct(self):
        lines = VGroup(
            MathTex(r"\overline{PF'}^{2}", "=", r"\overline{FF'}^{2}", "-", r"\overline{PF}^{2}"),
            MathTex(r"\overline{PF'}^{2}", "=", "(5k)^{2}", "-", "(3k)^{2}"),
            MathTex(r"\overline{PF'}^{2}", "=", "16k^{2}"),
            MathTex(r"\overline{PF'}", "=", r"\sqrt{16k^{2}}", substrings_to_isolate=[r"\overline{PF'}", "16k^{2}"]),
            MathTex(r"\overline{PF'}", "=", "4k")
        )
        lines.arrange(np.array((0, 0, 0)), buff=LARGE_BUFF)
        t1 = MathTex("3k").move_to(UP*3, LEFT*3)
        t2 = MathTex("5k").move_to(UP*3, RIGHT*3)
        self.add(t1, t2, lines[0])

        self.play(
            TransformMatchingTex(
                VGroup(t1, t2, lines[0].copy()), lines[1],
                key_map={
                    "5k": "(5k)^{2}",
                    "3k": "(3k)^{2}",
                }
            ),
            FadeOut(lines[0])
        )
        self.wait()
        self.play(
            TransformMatchingTex(
                lines[1].copy(), lines[2],
                transform_mismatches=True
            ),
            FadeOut(lines[1])
        )
        self.wait()
        lines2_2_new = MathTex(r"\overline{PF'}^{2}", "=", "16k^{2}", substrings_to_isolate=[r"\overline{PF'}", "16k^{2}"])
        lines2_2_new.replace(lines[2])
        lines2_2_new.match_style(lines[2])

        self.play(
            TransformMatchingTex(
                lines2_2_new, lines[3],
                transform_mismatches=True
            ),
            FadeOut(lines[2])
        )
        self.wait()
        self.play(
            TransformMatchingTex(
                lines[3].copy(), lines[4],
                transform_mismatches=True
            ),
            FadeOut(lines[3])
        )
        self.wait()

        # to_isolate = ["B", "C", "=", "(", ")"]
        # lines = VGroup(
        #     # Passing in muliple arguments to Tex will result
        #     # in the same expression as if those arguments had
        #     # been joined together, except that the submobject
        #     # hierarchy of the resulting mobject ensure that the
        #     # Tex mobject has a subject corresponding to
        #     # each of these strings.  For example, the Tex mobject
        #     # below will have 5 subjects, corresponding to the
        #     # expressions [A^2, +, B^2, =, C^2]
        #     MathTex("A^2", "+", "B^2", "=", "C^2"),
        #     # Likewise here
        #     MathTex("A^2", "=", "C^2", "-", "B^2"),
        #     # Alternatively, you can pass in the keyword argument
        #     # "isolate" with a list of strings that should be out as
        #     # their own submobject.  So the line below is equivalent
        #     # to the commented out line below it.
        #     MathTex("A^2 = (C + B)(C - B)", substrings_to_isolate=["A^2", *to_isolate]),
        #     # OldTex("A^2", "=", "(", "C", "+", "B", ")", "(", "C", "-", "B", ")"),
        #     MathTex("A = \\sqrt{(C + B)(C - B)}", substrings_to_isolate=["A", *to_isolate])
        # )
        # lines.arrange(DOWN, buff=LARGE_BUFF)
        # for line in lines:
        #     line.set_color_by_tex_to_color_map({
        #         "A": BLUE,
        #         "B": TEAL,
        #         "C": GREEN,
        #     })
        #
        # play_kw = {"run_time": 2}
        # self.add(lines[0])
        # # The animation TransformMatchingTex will line up parts
        # # of the source and target which have matching tex strings.
        # # Here, giving it a little path_arc makes each part sort of
        # # rotate into their final positions, which feels appropriate
        # # for the idea of rearranging an equation
        # self.play(
        #     TransformMatchingTex(
        #         lines[0].copy(), lines[1],
        #         path_arc=90 * DEGREES,
        #     ),
        #     **play_kw
        # )
        # self.wait()
        #
        # # Now, we could try this again on the next line...
        # self.play(
        #     TransformMatchingTex(lines[1].copy(), lines[2]),
        #     **play_kw
        # )
        # self.wait()
        # # ...and this looks nice enough, but since there's no tex
        # # in lines[2] which matches "C^2" or "B^2", those terms fade
        # # out to nothing while the C and B terms fade in from nothing.
        # # If, however, we want the C^2 to go to C, and B^2 to go to B,
        # # we can specify that with a key map.
        # self.play(FadeOut(lines[2]))
        # self.play(
        #     TransformMatchingTex(
        #         lines[1].copy(), lines[2],
        #         key_map={
        #             "C^2": "C",
        #             "B^2": "B",
        #         }
        #     ),
        #     **play_kw
        # )
        # self.wait()
        #
        # # And to finish off, a simple TransformMatchingShapes would work
        # # just fine.  But perhaps we want that exponent on A^2 to transform into
        # # the square root symbol.  At the moment, lines[2] treats the expression
        # # A^2 as a unit, so we might create a new version of the same line which
        # # separates out just the A.  This way, when TransformMatchingTex lines up
        # # all matching parts, the only mismatch will be between the "^2" from
        # # new_line2 and the "\sqrt" from the final line.  By passing in,
        # # transform_mismatches=True, it will transform this "^2" part into
        # # the "\sqrt" part.
        # new_line2 = MathTex("A^2 = (C + B)(C - B)", substrings_to_isolate=["A", *to_isolate])
        # new_line2.replace(lines[2])
        # new_line2.match_style(lines[2])
        #
        # self.play(
        #     TransformMatchingTex(
        #         new_line2, lines[3],
        #         transform_mismatches=True,
        #     ),
        #     **play_kw
        # )
        # self.wait(3)
        # self.play(
        #     FadeOut(lines)
        # )


class ArcTest(Scene):
    def construct(self):
        dot_a = Dot((4, 0, 0))
        dot_b = Dot((-4, 0, 0))
        dashed_curve = DashedVMobject(
            ArcBetweenPoints(
                start=dot_a.get_center(),
                end=dot_b.get_center(),
                angle=PI / 3  # 위로 휘어진 곡선
            ),
            dashed_ratio=0.2,  # 점선 길이
        )
        self.add(dot_a, dot_b)
        self.play(Create(dashed_curve))
        self.wait(3)

class TriangleTransformTest(Scene):
    def construct(self):
        tri = Polygon((-4,0,0), (1,0,0), (-4/5, 12/5, 0))
        self.add(tri)
        obj1 = Dot((4, 3, 0))
        self.add(obj1)
        tri.generate_target()
        tri.target.shift(obj1.get_center() - tri.get_center())
        tri.target.scale(0.1)
        tri.target.rotate(-math.asin(3/5) - PI/2)
        self.play(
            Transform(tri, tri.target)
        )
        self.wait(2)
