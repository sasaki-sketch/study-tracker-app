"""
イベント入力フォームコンポーネント
"""
import streamlit as st
from datetime import date
from models.event import PastExamEvent
from services.database import DatabaseService

db = DatabaseService()


def render_past_exam_form():
    """過去問演習記録フォーム"""
    st.markdown("### 📖 過去問演習を記録")

    with st.form("past_exam_form", clear_on_submit=True):
        # 日付
        exam_date = st.date_input(
            "日付 *",
            value=date.today(),
            format="YYYY-MM-DD"
        )

        # 科目
        subjects = db.get_subjects()
        subject = st.selectbox(
            "科目 *",
            options=[s[0] for s in subjects]
        )

        # 年度(最近3年を優先表示)
        current_year = date.today().year
        recent_years = [f"令和{y-2018}年度({y}年)" for y in range(current_year, current_year-3, -1)]
        older_years = [f"令和{y-2018}年度({y}年)" for y in range(current_year-3, current_year-10, -1)]

        # グループ化された選択肢
        year_options = ["━━ 最近の年度 ━━"] + recent_years + ["━━ 過去の年度 ━━"] + older_years
        exam_year = st.selectbox("年度・回 *", options=year_options, index=1)

        # セパレーター選択時は最初の実年度にフォールバック
        if "━━" in exam_year:
            exam_year = recent_years[0]

        # 問題範囲
        question_range = st.text_input(
            "問題範囲",
            placeholder="例: 第1問〜第5問"
        )

        # 正答数/総問題数
        col1, col2 = st.columns(2)
        with col1:
            correct_count = st.number_input(
                "正答数 *",
                min_value=0,
                value=0,
                step=1
            )
        with col2:
            total_count = st.number_input(
                "総問題数 *",
                min_value=1,
                value=25,
                step=1
            )

        # 正答率表示
        if total_count > 0:
            correct_rate = round(correct_count / total_count * 100, 1)
            if correct_rate >= 70:
                st.success(f"✓ 正答率: {correct_rate}% - 目標達成!")
            elif correct_rate >= 50:
                st.warning(f"⚠ 正答率: {correct_rate}% - もう一歩!")
            else:
                st.error(f"✗ 正答率: {correct_rate}% - 復習必要")

        # 所要時間
        time_spent = st.number_input(
            "所要時間(分)",
            min_value=0,
            value=60,
            step=5
        )

        # メモ
        memo = st.text_area(
            "苦手論点・復習メモ",
            placeholder="例: 資本コスト計算でミス、CVP分析要復習",
            height=100
        )

        # 送信ボタン
        submitted = st.form_submit_button("💾 記録する", width="stretch")

        if submitted:
            # イベント作成
            event = PastExamEvent(
                date=exam_date,
                subject=subject,
                exam_year=exam_year,
                question_range=question_range,
                correct_count=correct_count,
                total_count=total_count,
                time_spent=time_spent if time_spent > 0 else None,
                memo=memo if memo else None
            )

            # バリデーション
            valid, error_msg = event.validate()
            if not valid:
                st.error(f"❌ {error_msg}")
                return

            # 保存
            try:
                event_id = db.save_event(event)
                st.success("✅ 過去問記録を保存しました!")
                st.balloons()  # お祝いアニメーション

                # セッション状態更新(ダッシュボード再読み込み用)
                if 'events_updated' not in st.session_state:
                    st.session_state.events_updated = 0
                st.session_state.events_updated += 1

            except Exception as e:
                st.error(f"❌ 保存に失敗しました: {str(e)}")


def show_recent_past_exams(limit=5):
    """最近の過去問演習記録を表示"""
    st.markdown("### 📋 最近の過去問演習")

    events = db.get_events_by_type('past_exam', limit=limit)

    if not events:
        st.info("まだ過去問演習の記録がありません")
        return

    for event in events:
        details = event['details']

        # 正答率計算
        if details['total_count'] > 0:
            correct_rate = round(details['correct_count'] / details['total_count'] * 100, 1)
        else:
            correct_rate = 0.0

        with st.container():
            st.markdown(f"""
            📅 **{event['date']}**
            **{event['subject']}** | {details['exam_year']}

            正答率: **{correct_rate}%** ({details['correct_count']}/{details['total_count']}問)
            """)

            # プログレスバー
            if correct_rate >= 70:
                st.progress(correct_rate / 100, text=f"{correct_rate}% ✓")
            elif correct_rate >= 50:
                st.progress(correct_rate / 100, text=f"{correct_rate}% ⚠")
            else:
                st.progress(correct_rate / 100, text=f"{correct_rate}% ✗")

            if event['memo']:
                st.caption(f"💭 {event['memo'][:100]}{'...' if len(event['memo']) > 100 else ''}")

            st.divider()


def render_material_lap_form():
    """教材周回記録フォーム"""
    from models.event import MaterialLapEvent, Material

    st.markdown("### 📚 教材周回を記録")

    # 教材選択: 新規 or 既存
    material_mode = st.radio(
        "教材の選択",
        options=["既存の教材", "新規教材を登録"],
        horizontal=True
    )

    if material_mode == "新規教材を登録":
        # 新規教材登録フォーム
        with st.form("new_material_form", clear_on_submit=True):
            st.markdown("#### ✨ 新規教材を登録")

            col1, col2 = st.columns(2)
            with col1:
                material_name = st.text_input(
                    "教材名 *",
                    placeholder="例: スピードテキスト 財務会計"
                )
            with col2:
                subjects = db.get_subjects()
                material_subject = st.selectbox(
                    "科目 *",
                    options=[s[0] for s in subjects]
                )

            col3, col4 = st.columns(2)
            with col3:
                material_type = st.selectbox(
                    "教材タイプ *",
                    options=["テキスト", "問題集", "講義動画", "その他"]
                )
            with col4:
                target_laps = st.number_input(
                    "目標周回数 *",
                    min_value=1,
                    value=3,
                    step=1
                )

            submitted = st.form_submit_button("📝 教材を登録", width="stretch")

            if submitted:
                # 教材作成
                material = Material(
                    name=material_name,
                    subject=material_subject,
                    material_type=material_type,
                    target_laps=target_laps
                )

                # バリデーション
                valid, error_msg = material.validate()
                if not valid:
                    st.error(f"❌ {error_msg}")
                else:
                    try:
                        material_id = db.save_material(material)
                        st.success(f"✅ 教材「{material_name}」を登録しました!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ 保存に失敗しました: {str(e)}")

    else:
        # 既存教材への周回記録
        materials = db.get_all_materials()

        if not materials:
            st.warning("⚠️ まだ教材が登録されていません。先に新規教材を登録してください。")
            return

        with st.form("material_lap_form", clear_on_submit=True):
            st.markdown("#### 📖 周回を記録")

            # 教材選択
            material_options = {f"{m['name']} ({m['subject']})": m['id'] for m in materials}
            selected_material_label = st.selectbox(
                "教材 *",
                options=list(material_options.keys())
            )
            material_id = material_options[selected_material_label]

            # 選択した教材の情報表示
            selected_material = next(m for m in materials if m['id'] == material_id)
            st.caption(f"📊 現在の進捗: {selected_material['current_lap']}/{selected_material['target_laps']}周 ({round(selected_material['current_lap']/selected_material['target_laps']*100, 1) if selected_material['target_laps'] > 0 else 0}%)")

            # 日付
            lap_date = st.date_input(
                "日付 *",
                value=date.today(),
                format="YYYY-MM-DD"
            )

            # ページ範囲
            col1, col2 = st.columns(2)
            with col1:
                start_page = st.number_input(
                    "開始ページ",
                    min_value=1,
                    value=None,
                    step=1
                )
            with col2:
                end_page = st.number_input(
                    "終了ページ",
                    min_value=1,
                    value=None,
                    step=1
                )

            # 所要時間
            time_spent = st.number_input(
                "所要時間(分) *",
                min_value=0,
                value=60,
                step=5
            )

            # 理解度
            understanding = st.select_slider(
                "理解度 *",
                options=[1, 2, 3, 4, 5],
                value=3,
                format_func=lambda x: "⭐" * x
            )

            st.caption("1: 全く理解できなかった / 3: だいたい理解できた / 5: 完璧に理解できた")

            # メモ
            memo = st.text_area(
                "メモ",
                placeholder="例: 第3章が難しかった、例題の解法を復習する",
                height=80
            )

            # 送信ボタン
            submitted = st.form_submit_button("💾 記録する", width="stretch")

            if submitted:
                # イベント作成
                event = MaterialLapEvent(
                    date=lap_date,
                    subject=selected_material['subject'],
                    material_id=material_id,
                    start_page=start_page,
                    end_page=end_page,
                    time_spent=time_spent,
                    understanding=understanding,
                    memo=memo if memo else None
                )

                # バリデーション
                valid, error_msg = event.validate()
                if not valid:
                    st.error(f"❌ {error_msg}")
                    return

                # 保存
                try:
                    event_id = db.save_event(event)
                    # 教材進捗を更新
                    db.update_material_progress(material_id)

                    st.success("✅ 教材周回を記録しました!")
                    st.balloons()

                    # セッション状態更新
                    if 'events_updated' not in st.session_state:
                        st.session_state.events_updated = 0
                    st.session_state.events_updated += 1

                except Exception as e:
                    st.error(f"❌ 保存に失敗しました: {str(e)}")


def show_materials_list():
    """教材一覧と進捗を表示"""
    st.markdown("### 📚 教材一覧")

    materials = db.get_all_materials()

    if not materials:
        st.info("まだ教材が登録されていません")
        return

    for material in materials:
        # 進捗率計算
        if material['target_laps'] > 0:
            progress_rate = material['current_lap'] / material['target_laps']
        else:
            progress_rate = 0.0

        with st.container():
            st.markdown(f"**📖 {material['name']}** ({material['subject']})")

            # プログレスバー
            if progress_rate >= 1.0:
                st.progress(min(progress_rate, 1.0), text=f"{material['current_lap']}/{material['target_laps']}周 完了! ✓")
            else:
                st.progress(progress_rate, text=f"{material['current_lap']}/{material['target_laps']}周 ({round(progress_rate*100, 1)}%)")

            # 統計情報
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("総学習時間", f"{material['total_time']:.1f}分")
            with col2:
                st.metric("平均理解度", f"{'⭐' * int(material['avg_understanding'])}" if material['avg_understanding'] > 0 else "-")
            with col3:
                st.metric("最終学習日", material['last_study_date'] if material['last_study_date'] else "-")

            st.divider()


def render_mock_exam_form():
    """模試・答練記録フォーム"""
    from models.event import MockExamEvent

    st.markdown("### 📊 模試・答練を記録")

    with st.form("mock_exam_form", clear_on_submit=True):
        # 基本情報
        col1, col2 = st.columns(2)
        with col1:
            exam_date = st.date_input(
                "日付 *",
                value=date.today(),
                format="YYYY-MM-DD"
            )
        with col2:
            exam_type = st.selectbox(
                "試験区分 *",
                options=["1次試験", "2次試験"]
            )

        # 試験名
        exam_name = st.text_input(
            "試験名 *",
            placeholder="例: TAC 第1回全国模試, LEC 合格答練 第3回"
        )

        # 科目選択
        subjects = db.get_subjects()
        subject = st.selectbox(
            "科目 *",
            options=[s[0] for s in subjects]
        )

        # 1次試験の場合: 得点入力
        if exam_type == "1次試験":
            st.markdown("#### 📝 得点入力")
            col1, col2 = st.columns(2)
            with col1:
                total_score = st.number_input(
                    "総合得点 *",
                    min_value=0,
                    value=0,
                    step=1
                )
            with col2:
                max_score = st.number_input(
                    "配点 *",
                    min_value=1,
                    value=100,
                    step=1
                )

            # 得点率表示
            if max_score > 0:
                score_rate = round(total_score / max_score * 100, 1)
                if score_rate >= 60:
                    st.success(f"✓ 得点率: {score_rate}% - 合格水準!")
                elif score_rate >= 40:
                    st.warning(f"⚠ 得点率: {score_rate}% - もう少し!")
                else:
                    st.error(f"✗ 得点率: {score_rate}% - 要復習")

            subject_scores = None
            case_grades = None

        # 2次試験の場合: 事例別評価
        else:
            st.markdown("#### 📝 事例別評価")
            col1, col2 = st.columns(2)
            with col1:
                case1_grade = st.selectbox("事例I (組織・人事)", options=["A", "B", "C", "D"])
                case2_grade = st.selectbox("事例II (マーケティング)", options=["A", "B", "C", "D"])
            with col2:
                case3_grade = st.selectbox("事例III (生産・技術)", options=["A", "B", "C", "D"])
                case4_grade = st.selectbox("事例IV (財務)", options=["A", "B", "C", "D"])

            case_grades = {
                "事例I": case1_grade,
                "事例II": case2_grade,
                "事例III": case3_grade,
                "事例IV": case4_grade
            }

            # 合格判定表示
            grade_values = {"A": 4, "B": 3, "C": 2, "D": 1}
            grades_list = [grade_values[g] for g in case_grades.values()]
            a_count = sum(1 for g in grades_list if g >= 4)
            has_low_grade = min(grades_list) < 2

            if a_count >= 2 and not has_low_grade:
                st.success("✓ 合格水準! (A評価2科目以上 かつ C以下なし)")
            else:
                st.warning("⚠ 合格水準に届いていません")

            total_score = None
            max_score = None
            subject_scores = None

        # メモ
        memo = st.text_area(
            "振り返りメモ",
            placeholder="例: 財務分析で時間が足りなかった、事例IIの市場分析が弱い",
            height=100
        )

        # 送信ボタン
        submitted = st.form_submit_button("💾 記録する", width="stretch")

        if submitted:
            # イベント作成
            event = MockExamEvent(
                date=exam_date,
                subject=subject,
                exam_name=exam_name,
                exam_type=exam_type,
                total_score=total_score,
                max_score=max_score,
                subject_scores=subject_scores,
                case_grades=case_grades,
                memo=memo if memo else None
            )

            # バリデーション
            valid, error_msg = event.validate()
            if not valid:
                st.error(f"❌ {error_msg}")
                return

            # 保存
            try:
                event_id = db.save_event(event)
                st.success("✅ 模試・答練の記録を保存しました!")
                st.balloons()

                # セッション状態更新
                if 'events_updated' not in st.session_state:
                    st.session_state.events_updated = 0
                st.session_state.events_updated += 1

            except Exception as e:
                st.error(f"❌ 保存に失敗しました: {str(e)}")


def show_recent_mock_exams(limit=5):
    """最近の模試・答練記録を表示"""
    st.markdown("### 📋 最近の模試・答練")

    events = db.get_events_by_type('mock_exam', limit=limit)

    if not events:
        st.info("まだ模試・答練の記録がありません")
        return

    for event in events:
        details = event['details']

        with st.container():
            st.markdown(f"📅 **{event['date']}**")
            st.markdown(f"**{details['exam_name']}** ({event['subject']})")

            if details['exam_type'] == "1次試験":
                # 1次試験の表示
                score_rate = round(details['total_score'] / details['max_score'] * 100, 1)
                st.markdown(f"得点率: **{score_rate}%** ({details['total_score']}/{details['max_score']}点)")

                if score_rate >= 60:
                    st.progress(score_rate / 100, text=f"{score_rate}% ✓")
                elif score_rate >= 40:
                    st.progress(score_rate / 100, text=f"{score_rate}% ⚠")
                else:
                    st.progress(score_rate / 100, text=f"{score_rate}% ✗")

            else:
                # 2次試験の表示
                case_grades = details['case_grades']
                grade_display = " | ".join([f"{k}: {v}" for k, v in case_grades.items()])
                st.markdown(f"評価: **{grade_display}**")

                # 色分け表示
                cols = st.columns(4)
                for i, (case_name, grade) in enumerate(case_grades.items()):
                    with cols[i]:
                        if grade == "A":
                            st.success(f"{case_name}: {grade}")
                        elif grade == "B":
                            st.info(f"{case_name}: {grade}")
                        elif grade == "C":
                            st.warning(f"{case_name}: {grade}")
                        else:
                            st.error(f"{case_name}: {grade}")

            if event['memo']:
                st.caption(f"💭 {event['memo'][:100]}{'...' if len(event['memo']) > 100 else ''}")

            st.divider()
