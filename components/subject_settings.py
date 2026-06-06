"""
科目設定画面コンポーネント
"""
import streamlit as st
import pandas as pd
from services.database import DatabaseService


def show_subject_settings():
    """科目設定画面を表示"""
    st.header("⚙️ 科目設定")

    db_service = DatabaseService()

    # タブで1次試験・2次試験を切り替え
    tab1, tab2 = st.tabs(["📚 1次試験", "📝 2次試験"])

    with tab1:
        show_subject_table(db_service, '1次試験')

    with tab2:
        show_subject_table(db_service, '2次試験')


def show_subject_table(db_service: DatabaseService, category: str):
    """科目設定テーブルを表示（設定根拠を含む表形式）

    Args:
        db_service: データベースサービス
        category: 科目カテゴリ
    """
    subjects = db_service.get_subject_settings(category)

    if not subjects:
        st.info(f"{category}の科目設定がありません")
        return

    # サマリー表示
    total_standard = sum(s['standard_hours'] or 0 for s in subjects)
    total_target = sum(s['target_hours'] or 0 for s in subjects)
    total_reduction = total_standard - total_target
    reduction_rate = (total_reduction / total_standard * 100) if total_standard > 0 else 0
    total_target_score = sum(s['target_score'] or 0 for s in subjects)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "標準学習時間",
            f"{total_standard:.0f}h"
        )

    with col2:
        st.metric(
            "設定目標時間",
            f"{total_target:.0f}h",
            f"-{total_reduction:.0f}h",
            delta_color="inverse"
        )

    with col3:
        st.metric(
            "削減率",
            f"{reduction_rate:.1f}%"
        )

    with col4:
        st.metric(
            "目標合計得点",
            f"{total_target_score}点"
        )

    st.divider()

    # テーブル形式で表示（設定根拠を含む）
    table_data = []
    for subject in subjects:
        standard = subject['standard_hours'] or 0
        target = subject['target_hours'] or 0
        reduction_pct = ((standard - target) / standard * 100) if standard > 0 else 0

        table_data.append({
            '科目': subject['name'],
            '標準': f"{standard:.0f}h",
            '目標': f"{target:.0f}h",
            '削減率': f"{reduction_pct:.0f}%",
            '目標得点': f"{subject['target_score'] or 0}点",
            '設定根拠': subject['notes'] or "未設定"
        })

    # 合計行を追加
    table_data.append({
        '科目': '合計',
        '標準': f"{total_standard:.0f}h",
        '目標': f"{total_target:.0f}h",
        '削減率': f"{reduction_rate:.1f}%",
        '目標得点': f"{total_target_score}点",
        '設定根拠': ''
    })

    # DataFrameに変換
    df = pd.DataFrame(table_data)

    # テーブル表示（設定根拠も含む、横スクロール対応）
    st.dataframe(
        df,
        width=None,
        hide_index=True,
        use_container_width=True
    )
