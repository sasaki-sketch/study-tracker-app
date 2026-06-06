"""
学習データ可視化ユーティリティ
"""
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime


def create_past_exam_trend_chart(db):
    """過去問正答率の推移グラフ作成

    Args:
        db: DatabaseServiceインスタンス

    Returns:
        plotly.graph_objects.Figure
    """
    # 過去問イベント取得（全件、日付昇順）
    events = db.get_events_by_type('past_exam', limit=1000)

    if not events:
        # データがない場合は空のグラフ
        fig = go.Figure()
        fig.add_annotation(
            text="まだ過去問の記録がありません",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=16, color="gray")
        )
        fig.update_layout(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            height=300
        )
        return fig

    # データ準備（日付昇順に並び替え）
    events_sorted = sorted(events, key=lambda x: x['date'])

    dates = []
    correct_rates = []
    subjects = []
    tooltips = []

    for event in events_sorted:
        details = event['details']
        if details['total_count'] > 0:
            rate = details['correct_count'] / details['total_count'] * 100
            dates.append(event['date'])
            correct_rates.append(rate)
            subjects.append(event['subject'])

            # ツールチップ用の情報
            tooltip = (
                f"日付: {event['date']}<br>"
                f"科目: {event['subject']}<br>"
                f"正答率: {rate:.1f}%<br>"
                f"正答数: {details['correct_count']}/{details['total_count']}<br>"
                f"年度: {details['exam_year']}"
            )
            tooltips.append(tooltip)

    # グラフ作成
    fig = go.Figure()

    # 合格水準ライン（70%）
    fig.add_hline(
        y=70,
        line_dash="dash",
        line_color="green",
        annotation_text="合格水準（70%）",
        annotation_position="right"
    )

    # 正答率プロット
    fig.add_trace(go.Scatter(
        x=dates,
        y=correct_rates,
        mode='lines+markers',
        name='正答率',
        line=dict(color='#3B82F6', width=2),
        marker=dict(size=8, color=correct_rates,
                   colorscale=[[0, '#EF4444'], [0.7, '#F59E0B'], [1, '#10B981']],
                   cmin=0, cmax=100,
                   showscale=False),
        text=tooltips,
        hovertemplate='%{text}<extra></extra>'
    ))

    # レイアウト設定
    fig.update_layout(
        title="過去問正答率の推移",
        xaxis_title="日付",
        yaxis_title="正答率（%）",
        yaxis=dict(range=[0, 100]),
        height=400,
        hovermode='closest',
        showlegend=False
    )

    return fig


def create_subject_performance_chart(db):
    """科目別パフォーマンスチャート作成

    Args:
        db: DatabaseServiceインスタンス

    Returns:
        plotly.graph_objects.Figure
    """
    # 過去問イベント取得
    events = db.get_events_by_type('past_exam', limit=1000)

    if not events:
        fig = go.Figure()
        fig.add_annotation(
            text="まだ過去問の記録がありません",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=16, color="gray")
        )
        fig.update_layout(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            height=300
        )
        return fig

    # 科目別に集計
    subject_stats = {}

    for event in events:
        subject = event['subject']
        details = event['details']

        if details['total_count'] > 0:
            rate = details['correct_count'] / details['total_count'] * 100

            if subject not in subject_stats:
                subject_stats[subject] = {
                    'rates': [],
                    'count': 0
                }

            subject_stats[subject]['rates'].append(rate)
            subject_stats[subject]['count'] += 1

    # 平均正答率計算
    subjects = []
    avg_rates = []
    counts = []

    for subject, stats in subject_stats.items():
        subjects.append(subject)
        avg_rate = sum(stats['rates']) / len(stats['rates'])
        avg_rates.append(avg_rate)
        counts.append(stats['count'])

    # 色分け（正答率に応じて）
    colors = ['#10B981' if rate >= 70 else '#F59E0B' if rate >= 60 else '#EF4444'
              for rate in avg_rates]

    # バーチャート作成
    fig = go.Figure(data=[
        go.Bar(
            x=subjects,
            y=avg_rates,
            marker_color=colors,
            text=[f"{rate:.1f}%<br>({count}回)" for rate, count in zip(avg_rates, counts)],
            textposition='outside',
            hovertemplate='科目: %{x}<br>平均正答率: %{y:.1f}%<extra></extra>'
        )
    ])

    # 合格水準ライン
    fig.add_hline(
        y=70,
        line_dash="dash",
        line_color="green",
        annotation_text="合格水準",
        annotation_position="right"
    )

    # レイアウト設定
    fig.update_layout(
        title="科目別平均正答率",
        xaxis_title="科目",
        yaxis_title="平均正答率（%）",
        yaxis=dict(range=[0, 100]),
        height=400,
        showlegend=False
    )

    return fig


def create_study_time_heatmap(db):
    """学習時間ヒートマップ（カレンダー形式）

    Args:
        db: DatabaseServiceインスタンス

    Returns:
        plotly.graph_objects.Figure
    """
    from datetime import date, timedelta

    # 全記録取得
    all_records = db.get_all_records()

    if not all_records:
        fig = go.Figure()
        fig.add_annotation(
            text="まだ学習記録がありません",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=16, color="gray")
        )
        fig.update_layout(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            height=200
        )
        return fig

    # 日付別に学習時間を集計
    date_times = {}
    for record in all_records:
        total_time = record.shindan_time + record.toukei_time
        date_times[record.date] = total_time

    # 最近90日間のデータを準備
    today = date.today()
    start_date = today - timedelta(days=89)

    dates = []
    times = []
    weekdays = []
    weeks = []

    for i in range(90):
        current_date = start_date + timedelta(days=i)
        dates.append(current_date.isoformat())
        times.append(date_times.get(current_date, 0))
        weekdays.append(current_date.strftime('%a'))
        weeks.append(i // 7)

    # ヒートマップ作成
    # 簡易版: 時系列バーチャート
    fig = go.Figure(data=[
        go.Bar(
            x=dates,
            y=times,
            marker=dict(
                color=times,
                colorscale='Greens',
                showscale=True,
                colorbar=dict(title="学習時間(h)")
            ),
            hovertemplate='日付: %{x}<br>学習時間: %{y:.1f}h<extra></extra>'
        )
    ])

    fig.update_layout(
        title="学習時間カレンダー（最近90日）",
        xaxis_title="日付",
        yaxis_title="学習時間（h）",
        height=250,
        showlegend=False
    )

    return fig
