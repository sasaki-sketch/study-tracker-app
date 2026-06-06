"""
KPIダッシュボードコンポーネント
重要指標の視覚的表示
"""
import streamlit as st
from services.analytics import KPIMetrics


def render_kpi_cards(metrics: KPIMetrics):
    """KPI指標カードを表示

    Args:
        metrics: KPI指標データ
    """
    st.markdown("### 📊 学習状況サマリー")

    # 第1行: 主要指標
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="🎯 総学習時間",
            value=f"{metrics.total_study_hours}h",
            delta=None
        )

    with col2:
        st.metric(
            label="📅 学習日数",
            value=f"{metrics.total_study_days}日",
            delta=None
        )

    with col3:
        # 連続日数の絵文字
        if metrics.current_streak >= 7:
            streak_emoji = "🔥"
        elif metrics.current_streak >= 3:
            streak_emoji = "⭐"
        else:
            streak_emoji = "📈"

        st.metric(
            label=f"{streak_emoji} 連続学習",
            value=f"{metrics.current_streak}日",
            delta=f"最長{metrics.longest_streak}日"
        )

    with col4:
        st.metric(
            label="⏱️ 平均/日",
            value=f"{metrics.avg_daily_hours}h",
            delta=None
        )

    st.divider()

    # 第2行: 週次比較
    col1, col2 = st.columns(2)

    with col1:
        week_delta = metrics.this_week_hours - metrics.last_week_hours
        week_delta_pct = (week_delta / metrics.last_week_hours * 100) if metrics.last_week_hours > 0 else 0

        st.metric(
            label="📆 今週の学習時間",
            value=f"{metrics.this_week_hours}h",
            delta=f"{week_delta:+.1f}h ({week_delta_pct:+.0f}%)",
            delta_color="normal"
        )

    with col2:
        st.metric(
            label="📆 先週の学習時間",
            value=f"{metrics.last_week_hours}h",
            delta=None
        )

    st.divider()

    # 第3行: 進捗状況
    st.markdown("### 🎯 目標進捗")

    # 2列表示：一次試験、二次試験
    col1, col2 = st.columns(2)

    with col1:
        # 診断士一次試験の進捗バー
        st.markdown("**🏢 診断士(一次試験)**")

        progress_color = _get_progress_color(metrics.shindan_1ji_progress_pct)

        st.progress(
            min(metrics.shindan_1ji_progress_pct / 100, 1.0),
            text=None
        )

        st.markdown(
            f"<div style='text-align: center; font-size: 18px; font-weight: bold; color: {progress_color};'>"
            f"{metrics.shindan_1ji_progress_pct}%"
            f"</div>",
            unsafe_allow_html=True
        )

        st.caption(f"累計: {metrics.shindan_1ji_total}h / 目標: {metrics.shindan_1ji_goal}h")

        # 残り時間の計算
        remaining = metrics.shindan_1ji_goal - metrics.shindan_1ji_total
        if remaining > 0:
            st.info(f"💡 あと **{remaining:.1f}h**")
        else:
            st.success("✅ 目標達成！")

    with col2:
        # 診断士二次試験の進捗バー
        st.markdown("**🏢 診断士(二次試験)**")

        progress_color = _get_progress_color(metrics.shindan_2ji_progress_pct)

        st.progress(
            min(metrics.shindan_2ji_progress_pct / 100, 1.0),
            text=None
        )

        st.markdown(
            f"<div style='text-align: center; font-size: 18px; font-weight: bold; color: {progress_color};'>"
            f"{metrics.shindan_2ji_progress_pct}%"
            f"</div>",
            unsafe_allow_html=True
        )

        st.caption(f"累計: {metrics.shindan_2ji_total}h / 目標: {metrics.shindan_2ji_goal}h")

        # 残り時間の計算
        remaining = metrics.shindan_2ji_goal - metrics.shindan_2ji_total
        if remaining > 0:
            st.info(f"💡 あと **{remaining:.1f}h**")
        else:
            st.success("✅ 目標達成！")

    st.divider()


def _get_progress_color(progress_pct: float) -> str:
    """進捗率に応じた色を返す

    Args:
        progress_pct: 進捗率（0-100）

    Returns:
        カラーコード
    """
    if progress_pct >= 100:
        return "#00c853"  # 緑（達成）
    elif progress_pct >= 75:
        return "#4ecdc4"  # ターコイズ（順調）
    elif progress_pct >= 50:
        return "#667eea"  # 紫（中間）
    elif progress_pct >= 25:
        return "#ffa726"  # オレンジ（遅れ気味）
    else:
        return "#ef5350"  # 赤（要注意）


def render_motivational_message(metrics: KPIMetrics):
    """モチベーションメッセージを表示

    Args:
        metrics: KPI指標データ
    """
    messages = []

    # 連続学習日数
    if metrics.current_streak >= 7:
        messages.append("🔥 素晴らしい！1週間連続学習を達成しています！")
    elif metrics.current_streak >= 3:
        messages.append("⭐ 良いペースです！この調子で継続しましょう！")

    # 今週の学習時間
    if metrics.this_week_hours > metrics.last_week_hours:
        improvement = metrics.this_week_hours - metrics.last_week_hours
        messages.append(f"📈 今週は先週より{improvement:.1f}h多く学習できています！")

    # 進捗状況（診断士1次・2次の平均）
    total_progress = (metrics.shindan_1ji_progress_pct + metrics.shindan_2ji_progress_pct) / 2
    if total_progress >= 50:
        messages.append("🎯 目標の半分を突破しました！順調です！")

    # メッセージ表示
    if messages:
        st.success("\n\n".join(messages))


def render_insights(metrics: KPIMetrics, subject_stats: dict):
    """学習インサイト（気づき）を表示

    Args:
        metrics: KPI指標データ
        subject_stats: 科目別統計
    """
    st.markdown("### 💡 学習インサイト")

    insights = []

    # 【優先1】週次トレンド（最新トレンド優先）
    if metrics.this_week_hours < metrics.last_week_hours * 0.7:
        insights.append({
            'type': 'warning',
            'message': "⚠️ 今週の学習時間が先週より大幅に減少しています。ペースを戻しましょう。"
        })
    elif metrics.this_week_hours > metrics.last_week_hours * 1.2:
        insights.append({
            'type': 'success',
            'message': f"📈 今週は先週より{metrics.this_week_hours - metrics.last_week_hours:.1f}h多く学習できています！"
        })

    # 【優先2】学習ペースの分析（全体傾向）
    if metrics.avg_daily_hours < 1.0:
        insights.append({
            'type': 'warning',
            'message': f"⚠️ 平均学習時間が{metrics.avg_daily_hours}h/日です。目標達成には学習時間を増やす必要があります。"
        })
    elif metrics.avg_daily_hours >= 3.0:
        insights.append({
            'type': 'success',
            'message': f"🎉 素晴らしい学習ペース（{metrics.avg_daily_hours}h/日）です！"
        })

    # 【優先3】科目バランスの分析（診断士科目内のみ）
    if subject_stats:
        shindan_subjects = [s for s in subject_stats.values() if s.qualification in ('shindan_1ji', 'shindan_2ji')]
        if len(shindan_subjects) >= 2:
            # 最も学習時間が少ない科目を検出
            min_subject = min(shindan_subjects, key=lambda x: x.total_hours)
            max_subject = max(shindan_subjects, key=lambda x: x.total_hours)

            if max_subject.total_hours > min_subject.total_hours * 3:
                insights.append({
                    'type': 'info',
                    'message': f"📚 科目バランスに偏りがあります。「{min_subject.subject}」の学習時間を増やすことを検討してください。"
                })

    # インサイト表示
    if insights:
        for insight in insights:
            if insight['type'] == 'success':
                st.success(insight['message'])
            elif insight['type'] == 'warning':
                st.warning(insight['message'])
            elif insight['type'] == 'info':
                st.info(insight['message'])
    else:
        st.info("💪 この調子で学習を継続してください！")
