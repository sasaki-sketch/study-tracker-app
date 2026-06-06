"""
分析グラフコンポーネント
Plotlyベースのインタラクティブグラフ
"""
import plotly.graph_objects as go
import plotly.express as px
from typing import List, Dict
from services.analytics import DailySummary, SubjectStats, WeeklyStats
from utils.subjects import SUBJECT_EMOJI_MAP


# カラーパレット（ブランド統一）
COLORS = {
    'shindan': '#667eea',  # 紫
    'toukei': '#4ecdc4',   # ターコイズ
    'total': '#ff6b6b',    # 赤
    'primary': '#667eea',
    'secondary': '#764ba2',
    'accent': '#f093fb'
}


def render_time_series_chart(summaries: List[DailySummary], height: int = 400):
    """学習時間推移グラフ（Plotly版）

    Args:
        summaries: 日次サマリーリスト
        height: グラフの高さ（ピクセル）

    Returns:
        Plotly Figureオブジェクト
    """
    if not summaries:
        return None

    dates = [s.date for s in summaries]
    shindan_hours = [s.shindan_hours for s in summaries]
    toukei_hours = [s.toukei_hours for s in summaries]
    total_hours = [s.total_hours for s in summaries]

    fig = go.Figure()

    # 診断士
    fig.add_trace(go.Scatter(
        x=dates,
        y=shindan_hours,
        name='🏢 中小企業診断士',
        mode='lines+markers',
        line=dict(color=COLORS['shindan'], width=3),
        marker=dict(size=8),
        hovertemplate='<b>%{x}</b><br>診断士: %{y}h<extra></extra>'
    ))

    # 統計検定
    fig.add_trace(go.Scatter(
        x=dates,
        y=toukei_hours,
        name='📈 統計検定2級',
        mode='lines+markers',
        line=dict(color=COLORS['toukei'], width=3),
        marker=dict(size=8),
        hovertemplate='<b>%{x}</b><br>統計: %{y}h<extra></extra>'
    ))

    # 合計（薄い線）
    fig.add_trace(go.Scatter(
        x=dates,
        y=total_hours,
        name='📊 合計',
        mode='lines',
        line=dict(color=COLORS['total'], width=2, dash='dot'),
        hovertemplate='<b>%{x}</b><br>合計: %{y}h<extra></extra>'
    ))

    fig.update_layout(
        title='📈 学習時間の推移',
        xaxis_title='日付',
        yaxis_title='学習時間（h）',
        hovermode='x unified',
        height=height,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12),
        margin=dict(l=50, r=50, t=80, b=50)
    )

    # グリッド線
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')

    return fig


def render_subject_bar_chart(
    subject_stats: Dict[str, SubjectStats],
    show_emoji: bool = True,
    height: int = 400
):
    """科目別学習時間バーチャート（Plotly版）

    Args:
        subject_stats: 科目別統計辞書
        show_emoji: 絵文字表示フラグ
        height: グラフの高さ

    Returns:
        Plotly Figureオブジェクト
    """
    if not subject_stats:
        return None

    # データ準備
    subjects = []
    hours = []
    colors = []
    hover_texts = []

    for subject_name, stats in sorted(
        subject_stats.items(),
        key=lambda x: x[1].total_hours,
        reverse=True
    ):
        # 絵文字付き表示名
        emoji = SUBJECT_EMOJI_MAP.get(subject_name, "📚") if show_emoji else ""
        display_name = f"{emoji} {subject_name}" if emoji else subject_name

        subjects.append(display_name)
        hours.append(stats.total_hours)

        # 色分け（資格別）
        if stats.qualification in ('shindan_1ji', 'shindan_2ji'):
            colors.append(COLORS['shindan'])
        else:
            colors.append(COLORS['toukei'])

        # ホバーテキスト
        hover_text = (
            f"<b>{subject_name}</b><br>"
            f"累計: {stats.total_hours}h<br>"
            f"学習回数: {stats.session_count}回<br>"
            f"平均: {stats.avg_hours_per_session}h/回<br>"
            f"最終学習日: {stats.last_studied}"
        )
        hover_texts.append(hover_text)

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=hours,
        y=subjects,
        orientation='h',
        marker=dict(
            color=colors,
            line=dict(color='rgba(0,0,0,0.1)', width=1)
        ),
        hovertemplate='%{customdata}<extra></extra>',
        customdata=hover_texts
    ))

    fig.update_layout(
        title='📚 科目別学習時間',
        xaxis_title='学習時間（h）',
        yaxis_title='',
        height=height,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12),
        margin=dict(l=150, r=50, t=80, b=50),
        showlegend=False
    )

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
    fig.update_yaxes(showgrid=False)

    return fig


def render_weekly_comparison_chart(
    weekly_stats: List[WeeklyStats],
    height: int = 400
):
    """週次比較バーチャート（Plotly版）

    Args:
        weekly_stats: 週次統計リスト
        height: グラフの高さ

    Returns:
        Plotly Figureオブジェクト
    """
    if not weekly_stats:
        return None

    # データ準備（新しい週から古い週の順）
    weeks = []
    shindan_hours = []
    toukei_hours = []
    hover_texts = []

    for w in reversed(weekly_stats):  # 逆順（最新が右）
        week_label = f"{w.week_start.strftime('%m/%d')}"
        weeks.append(week_label)
        shindan_hours.append(w.shindan_hours)
        toukei_hours.append(w.toukei_hours)

        hover_text = (
            f"<b>{w.week_start} 〜 {w.week_end}</b><br>"
            f"診断士: {w.shindan_hours}h<br>"
            f"統計: {w.toukei_hours}h<br>"
            f"合計: {w.total_hours}h<br>"
            f"学習日数: {w.study_days}日"
        )
        hover_texts.append(hover_text)

    fig = go.Figure()

    # 積み上げバーチャート
    fig.add_trace(go.Bar(
        name='🏢 診断士',
        x=weeks,
        y=shindan_hours,
        marker=dict(color=COLORS['shindan']),
        hovertemplate='診断士: %{y}h<extra></extra>'
    ))

    fig.add_trace(go.Bar(
        name='📈 統計',
        x=weeks,
        y=toukei_hours,
        marker=dict(color=COLORS['toukei']),
        hovertemplate='統計: %{y}h<extra></extra>'
    ))

    fig.update_layout(
        title='📊 週次学習時間の比較',
        xaxis_title='週（開始日）',
        yaxis_title='学習時間（h）',
        barmode='stack',
        height=height,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        margin=dict(l=50, r=50, t=80, b=50)
    )

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')

    return fig


def render_progress_gauge(
    current: float,
    goal: float,
    title: str,
    color: str = COLORS['primary']
):
    """進捗ゲージチャート

    Args:
        current: 現在値
        goal: 目標値
        title: タイトル
        color: メインカラー

    Returns:
        Plotly Figureオブジェクト
    """
    progress_pct = (current / goal * 100) if goal > 0 else 0

    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=progress_pct,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title, 'font': {'size': 16}},
        delta={'reference': 100, 'suffix': '%'},
        number={'suffix': '%', 'font': {'size': 32}},
        gauge={
            'axis': {'range': [None, 100], 'ticksuffix': '%'},
            'bar': {'color': color},
            'steps': [
                {'range': [0, 50], 'color': 'rgba(128,128,128,0.1)'},
                {'range': [50, 75], 'color': 'rgba(128,128,128,0.15)'},
                {'range': [75, 100], 'color': 'rgba(128,128,128,0.2)'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 100
            }
        }
    ))

    fig.update_layout(
        height=250,
        margin=dict(l=20, r=20, t=50, b=20),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )

    return fig
