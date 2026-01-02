"""
科目別進捗コンポーネント
"""
import streamlit as st
from typing import List, Dict
import pandas as pd


def show_subject_progress_by_category(db_service, all_records):
    """カテゴリ別（1次/2次）科目進捗を表示"""
    st.subheader("📚 科目別進捗")

    # 全科目情報を取得（関連資格を除外）
    with db_service.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT name, abbreviation, category, target_hours, baseline_hours
            FROM subjects
            WHERE category IN ('1次試験', '2次試験')
            ORDER BY id
        ''')
        subjects_data = cursor.fetchall()

    # 科目別の学習時間を集計
    subject_hours = {}
    for record in all_records:
        if record.shindan_subject and record.shindan_time > 0:
            if record.shindan_subject not in subject_hours:
                subject_hours[record.shindan_subject] = 0
            subject_hours[record.shindan_subject] += record.shindan_time

    # カテゴリ別に分類
    first_exam_subjects = []
    second_exam_subjects = []

    for subject_info in subjects_data:
        name = subject_info['name']
        abbr = subject_info['abbreviation']
        category = subject_info['category']
        target = float(subject_info['target_hours'])
        baseline = float(subject_info['baseline_hours'])

        # 実績時間（基礎学習時間 + 記録された学習時間）
        recorded_hours = subject_hours.get(name, 0.0)
        total_hours = baseline + recorded_hours

        # 進捗率計算
        progress = (total_hours / target * 100) if target > 0 else 0

        subject_data = {
            'name': name,
            'abbr': abbr,
            'target': target,
            'baseline': baseline,
            'recorded': recorded_hours,
            'total': total_hours,
            'progress': progress
        }

        if category == '1次試験':
            first_exam_subjects.append(subject_data)
        else:
            second_exam_subjects.append(subject_data)

    # 1次試験科目を表示
    with st.container():
        st.markdown("### 1次試験科目")

        # 2列表示
        cols = st.columns(2)

        for idx, subject in enumerate(first_exam_subjects):
            col_idx = idx % 2
            with cols[col_idx]:
                # 進捗率に応じた色分け
                if subject['progress'] >= 100:
                    st.success(f"**{subject['name']}** ✅")
                    progress_color = "normal"
                elif subject['progress'] >= 75:
                    st.info(f"**{subject['name']}**")
                    progress_color = "normal"
                elif subject['progress'] >= 50:
                    st.warning(f"**{subject['name']}**")
                    progress_color = "normal"
                else:
                    st.error(f"**{subject['name']}**")
                    progress_color = "normal"

                # プログレスバー
                st.progress(min(subject['progress'] / 100, 1.0))

                # 詳細情報
                st.caption(
                    f"📊 実績: **{subject['total']:.1f}h** / 目標: {subject['target']}h (**{subject['progress']:.1f}%**)\n\n"
                    f"📚 基礎学習: {subject['baseline']}h + 記録学習: {subject['recorded']:.1f}h"
                )

    st.divider()

    # 2次試験科目を表示
    with st.container():
        st.markdown("### 2次試験科目")

        cols = st.columns(2)

        for idx, subject in enumerate(second_exam_subjects):
            col_idx = idx % 2
            with cols[col_idx]:
                # 進捗率に応じた色分け
                if subject['progress'] >= 100:
                    st.success(f"**{subject['name']}** ✅")
                elif subject['progress'] >= 75:
                    st.info(f"**{subject['name']}**")
                elif subject['progress'] >= 50:
                    st.warning(f"**{subject['name']}**")
                else:
                    st.error(f"**{subject['name']}**")

                # プログレスバー
                st.progress(min(subject['progress'] / 100, 1.0))

                # 詳細情報
                st.caption(
                    f"📊 実績: **{subject['total']:.1f}h** / 目標: {subject['target']}h (**{subject['progress']:.1f}%**)\n\n"
                    f"📚 記録学習: {subject['recorded']:.1f}h"
                )

    # サマリー統計
    st.divider()
    st.markdown("### サマリー")

    # 関連資格の学習時間を取得
    with db_service.get_connection() as conn2:
        cursor2 = conn2.cursor()
        cursor2.execute('''
            SELECT SUM(target_hours) as total
            FROM subjects
            WHERE category = '関連資格' AND completed = 1
        ''')
        related_result = cursor2.fetchone()
        related_total = related_result['total'] if related_result['total'] else 0

    col1, col2, col3, col4 = st.columns(4)

    # 1次試験合計
    first_total = sum(s['total'] for s in first_exam_subjects)
    first_target = sum(s['target'] for s in first_exam_subjects)
    first_progress = (first_total / first_target * 100) if first_target > 0 else 0

    with col1:
        st.metric(
            "1次試験合計",
            f"{first_total:.1f}h",
            delta=f"{first_progress:.1f}%"
        )

    # 2次試験合計
    second_total = sum(s['total'] for s in second_exam_subjects)
    second_target = sum(s['target'] for s in second_exam_subjects)
    second_progress = (second_total / second_target * 100) if second_target > 0 else 0

    with col2:
        st.metric(
            "2次試験合計",
            f"{second_total:.1f}h",
            delta=f"{second_progress:.1f}%"
        )

    # 関連資格
    with col3:
        st.metric(
            "関連資格",
            f"{related_total:.0f}h",
            delta="完了済み ✅"
        )

    # 診断士全体合計
    total_all = first_total + second_total
    target_all = first_target + second_target
    progress_all = (total_all / target_all * 100) if target_all > 0 else 0

    with col4:
        st.metric(
            "診断士合計",
            f"{total_all:.1f}h",
            delta=f"{progress_all:.1f}%"
        )
