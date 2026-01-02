"""
学習ロードマップコンポーネント（完全再設計版）
過去の成果を称え、現在のフェーズを明確にし、未来への道筋を示す
"""
import streamlit as st
import pandas as pd
from datetime import date, timedelta
import plotly.graph_objects as go


def show_learning_journey_summary(db_service, all_records):
    """学習の旅全体サマリー（過去の成果を含む）"""
    st.markdown("### 🏆 学習の成果")

    # データベースから過去資格を取得
    with db_service.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT s.name, s.target_hours, r.date
            FROM subjects s
            LEFT JOIN records r ON s.name = r.shindan_subject
            WHERE s.category = '関連資格' AND s.completed = 1
            ORDER BY r.date
        ''')
        past_data = cursor.fetchall()

    # 過去資格のカラー定義
    colors = ['#4169E1', '#32CD32', '#FF6347', '#FFD700', '#9370DB']

    past_achievements = []
    for idx, cert in enumerate(past_data):
        past_achievements.append({
            'name': cert['name'],
            'hours': int(cert['target_hours']),
            'date': cert['date'] if cert['date'] else '取得済み',
            'color': colors[idx % len(colors)]
        })

    total_past_hours = sum(a['hours'] for a in past_achievements)

    # 大きく目立つ総学習時間カード
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 35px; border-radius: 20px; color: white; text-align: center;
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); margin-bottom: 20px;">
        <div style="font-size: 16px; opacity: 0.95; margin-bottom: 8px; letter-spacing: 1px;">
            🎓 これまでの学習成果
        </div>
        <div style="font-size: 72px; font-weight: bold; margin: 20px 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            {total_past_hours}h
        </div>
        <div style="font-size: 20px; opacity: 0.9; margin-bottom: 15px;">
            取得資格: <strong>3つ</strong>
        </div>
        <div style="font-size: 14px; opacity: 0.85; line-height: 1.8;">
            基本情報技術者 ✅ | 簿記3級 ✅ | 簿記2級 ✅
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 過去の資格詳細（コンパクトに3列）
    st.markdown("#### 取得済み資格の詳細")
    cols = st.columns(3)

    for idx, cert in enumerate(past_achievements):
        with cols[idx]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {cert['color']} 0%, {cert['color']}DD 100%);
                        padding: 20px; border-radius: 12px; color: white; text-align: center;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
                <div style="font-size: 14px; font-weight: bold; margin-bottom: 10px;">
                    {cert['name']}
                </div>
                <div style="font-size: 32px; font-weight: bold; margin: 10px 0;">
                    {cert['hours']}h
                </div>
                <div style="font-size: 12px; opacity: 0.9;">
                    合格日: {cert['date']}
                </div>
            </div>
            """, unsafe_allow_html=True)


def show_roadmap():
    """学習ロードマップを表示（シンプル版）"""
    st.subheader("🗺️ 学習ロードマップ")

    # 重要な日付
    shindan_start = date(2026, 1, 1)      # 診断士学習開始
    toukei_exam = date(2026, 2, 1)        # 統計検定試験
    shindan_1st_exam = date(2026, 8, 5)   # 診断士1次試験
    shindan_2nd_exam = date(2026, 10, 25) # 診断士2次試験

    today = date.today()

    # フェーズ定義（1次試験まで）
    phases_1st = [
        {
            'name': '基礎固め期',
            'start': date(2026, 1, 1),
            'end': date(2026, 3, 31),
            'color': '#4ecdc4',
            'goal_hours': 240,
            'description': '全科目1周完了、基礎問題70%以上'
        },
        {
            'name': '応用力強化期',
            'start': date(2026, 4, 1),
            'end': date(2026, 5, 31),
            'color': '#ff6b6b',
            'goal_hours': 400,
            'description': '過去問3年分完了、過去問60点以上'
        },
        {
            'name': '直前追い込み期',
            'start': date(2026, 6, 1),
            'end': shindan_1st_exam,
            'color': '#ffd93d',
            'goal_hours': 570,
            'description': '模試420点以上 (×3回)、弱点完全克服'
        }
    ]

    # 2次試験フェーズ
    phase_2nd = {
        'name': '2次試験対策',
        'start': date(2026, 8, 6),
        'end': shindan_2nd_exam,
        'color': '#9370DB',
        'goal_hours': 240,
        'description': '事例演習80問完了、各事例60点以上安定'
    }

    # Plotlyでロードマップ作成
    fig = go.Figure()

    # 1次試験フェーズの背景色
    for phase in phases_1st:
        fig.add_shape(
            type="rect",
            x0=phase['start'],
            x1=phase['end'],
            y0=0,
            y1=1,
            fillcolor=phase['color'],
            opacity=0.25,
            line_width=0,
        )

        mid_date = phase['start'] + (phase['end'] - phase['start']) / 2
        fig.add_annotation(
            x=mid_date,
            y=0.5,
            text=f"<b>{phase['name']}</b>",
            showarrow=False,
            font=dict(size=14, color='white', family="Arial Black"),
            bgcolor=f'rgba({int(phase["color"][1:3], 16)}, {int(phase["color"][3:5], 16)}, {int(phase["color"][5:7], 16)}, 0.85)',
            bordercolor=phase['color'],
            borderwidth=2,
            borderpad=8
        )

    # 2次試験フェーズの背景色
    fig.add_shape(
        type="rect",
        x0=phase_2nd['start'],
        x1=phase_2nd['end'],
        y0=0,
        y1=1,
        fillcolor=phase_2nd['color'],
        opacity=0.25,
        line_width=0,
    )

    mid_date_2nd = phase_2nd['start'] + (phase_2nd['end'] - phase_2nd['start']) / 2
    fig.add_annotation(
        x=mid_date_2nd,
        y=0.5,
        text=f"<b>{phase_2nd['name']}</b>",
        showarrow=False,
        font=dict(size=14, color='white', family="Arial Black"),
        bgcolor=f'rgba({int(phase_2nd["color"][1:3], 16)}, {int(phase_2nd["color"][3:5], 16)}, {int(phase_2nd["color"][5:7], 16)}, 0.85)',
        bordercolor=phase_2nd['color'],
        borderwidth=2,
        borderpad=8
    )

    # 月末ベンチマーク (1次試験合計570h ÷ 7ヶ月 ≒ 80h/月)
    monthly_benchmarks = [
        {'date': date(2026, 1, 31), 'shindan_h': 80, 'label': '1月末\n目標80h'},
        {'date': date(2026, 2, 28), 'shindan_h': 160, 'label': '2月末\n目標160h'},
        {'date': date(2026, 3, 31), 'shindan_h': 240, 'label': '3月末\n目標240h'},
        {'date': date(2026, 4, 30), 'shindan_h': 320, 'label': '4月末\n目標320h'},
        {'date': date(2026, 5, 31), 'shindan_h': 400, 'label': '5月末\n目標400h'},
        {'date': date(2026, 6, 30), 'shindan_h': 485, 'label': '6月末\n目標485h'},
        {'date': date(2026, 7, 31), 'shindan_h': 570, 'label': '7月末\n目標570h'},
    ]

    for benchmark in monthly_benchmarks:
        fig.add_shape(
            type="line",
            x0=benchmark['date'],
            x1=benchmark['date'],
            y0=0,
            y1=1,
            line=dict(color="rgba(255, 255, 255, 0.3)", width=1, dash="dot")
        )

        fig.add_annotation(
            x=benchmark['date'],
            y=1.12,
            text=f"<b>{benchmark['label']}</b>",
            showarrow=False,
            font=dict(size=9, color='#B0B0B0'),
            bgcolor='rgba(50, 50, 50, 0.6)',
            bordercolor='rgba(255, 255, 255, 0.2)',
            borderwidth=1,
            borderpad=3
        )

    # 今日の位置
    fig.add_shape(
        type="line",
        x0=today,
        x1=today,
        y0=-0.05,
        y1=1.05,
        line=dict(color="#FF6B6B", width=4)
    )

    fig.add_annotation(
        x=today,
        y=1.25,
        text=f"<b>TODAY</b><br>{today.strftime('%m/%d')}",
        showarrow=True,
        arrowhead=3,
        arrowsize=1.5,
        arrowwidth=2,
        arrowcolor="#FF6B6B",
        ax=0,
        ay=-40,
        font=dict(size=12, color='white', family="Arial Black"),
        bgcolor="#FF6B6B",
        bordercolor="white",
        borderwidth=2,
        borderpad=6
    )

    # 試験日マーカー
    # 統計検定
    fig.add_shape(
        type="line",
        x0=toukei_exam,
        x1=toukei_exam,
        y0=0,
        y1=1,
        line=dict(color="#4169E1", width=3, dash="solid")
    )

    fig.add_annotation(
        x=toukei_exam,
        y=-0.15,
        text=f"<b>統計検定2級</b><br>{toukei_exam.strftime('%m/%d')}",
        showarrow=False,
        font=dict(size=11, color='white', family="Arial Black"),
        bgcolor="#4169E1",
        bordercolor='white',
        borderwidth=2,
        borderpad=5
    )

    # 診断士1次試験
    fig.add_shape(
        type="line",
        x0=shindan_1st_exam,
        x1=shindan_1st_exam,
        y0=0,
        y1=1,
        line=dict(color="#FFD700", width=4, dash="solid")
    )

    fig.add_annotation(
        x=shindan_1st_exam,
        y=-0.15,
        text=f"<b>診断士1次試験</b><br>{shindan_1st_exam.strftime('%m/%d')}",
        showarrow=False,
        font=dict(size=11, color='#2C2C2C', family="Arial Black"),
        bgcolor="#FFD700",
        bordercolor='white',
        borderwidth=2,
        borderpad=5
    )

    # 診断士2次試験
    fig.add_shape(
        type="line",
        x0=shindan_2nd_exam,
        x1=shindan_2nd_exam,
        y0=0,
        y1=1,
        line=dict(color="#9370DB", width=4, dash="solid")
    )

    fig.add_annotation(
        x=shindan_2nd_exam,
        y=-0.15,
        text=f"<b>診断士2次試験</b><br>{shindan_2nd_exam.strftime('%m/%d')}",
        showarrow=False,
        font=dict(size=11, color='white', family="Arial Black"),
        bgcolor="#9370DB",
        bordercolor='white',
        borderwidth=2,
        borderpad=5
    )

    # レイアウト設定
    fig.update_layout(
        xaxis=dict(
            title="<b>日付</b>",
            title_font=dict(size=14, color='#E0E0E0'),
            type='date',
            tickformat='%Y/%m/%d',
            tickangle=-45,
            showgrid=True,
            gridcolor='rgba(255, 255, 255, 0.1)',
            gridwidth=1,
            range=[shindan_start - timedelta(days=5), shindan_2nd_exam + timedelta(days=10)],
            tickfont=dict(color='#B0B0B0')
        ),
        yaxis=dict(
            showticklabels=False,
            range=[-0.25, 1.4],
            showgrid=False
        ),
        height=400,
        margin=dict(l=30, r=30, t=50, b=110),
        showlegend=False,
        plot_bgcolor='rgba(30, 30, 30, 0.5)',
        paper_bgcolor='rgba(0, 0, 0, 0)'
    )

    st.plotly_chart(fig, use_container_width=True)

    # 現在フェーズの詳細情報（コンパクトに）
    st.markdown("### 📅 現在のフェーズ")

    # 現在どのフェーズにいるか判定
    current_phase = None
    all_phases = phases_1st + [phase_2nd]

    for phase in all_phases:
        if phase['start'] <= today <= phase['end']:
            current_phase = phase
            break

    if current_phase:
        days_in_phase = (today - current_phase['start']).days + 1
        total_days = (current_phase['end'] - current_phase['start']).days + 1
        days_remaining = (current_phase['end'] - today).days
        phase_progress = (days_in_phase / total_days) * 100

        # フェーズ情報カード（1行にまとめる）
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {current_phase['color']} 0%, {current_phase['color']}DD 100%);
                    padding: 25px; border-radius: 15px; color: white;
                    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3); margin-bottom: 15px;">
            <div style="font-size: 24px; font-weight: bold; margin-bottom: 15px;">
                🔥 {current_phase['name']}
            </div>
            <div style="font-size: 14px; opacity: 0.95; margin-bottom: 10px; line-height: 1.6;">
                <strong>ゴール:</strong> {current_phase['description']}
            </div>
            <div style="display: flex; justify-content: space-between; margin-top: 15px;">
                <div>
                    <span style="font-size: 12px; opacity: 0.9;">フェーズ進捗</span><br>
                    <span style="font-size: 20px; font-weight: bold;">{phase_progress:.0f}%</span>
                </div>
                <div>
                    <span style="font-size: 12px; opacity: 0.9;">経過日数</span><br>
                    <span style="font-size: 20px; font-weight: bold;">{days_in_phase}/{total_days}日</span>
                </div>
                <div>
                    <span style="font-size: 12px; opacity: 0.9;">残り日数</span><br>
                    <span style="font-size: 20px; font-weight: bold;">{days_remaining}日</span>
                </div>
                <div>
                    <span style="font-size: 12px; opacity: 0.9;">目標時間</span><br>
                    <span style="font-size: 20px; font-weight: bold;">{current_phase['goal_hours']}h</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # フェーズ一覧（シンプルな表形式）
    st.markdown("### 📋 フェーズ別ゴール一覧")

    for phase in all_phases:
        is_current = current_phase and phase['name'] == current_phase['name']
        is_complete = today > phase['end']

        status_icon = "🔥" if is_current else ("✅" if is_complete else "⏳")
        border_color = phase['color'] if is_current else 'rgba(255,255,255,0.2)'

        st.markdown(f"""
        <div style="background: rgba(50, 50, 50, 0.4);
                    padding: 15px 20px; border-radius: 10px; margin-bottom: 10px;
                    border-left: 5px solid {border_color};">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="flex: 1;">
                    <span style="font-size: 16px; font-weight: bold; color: {phase['color']};">
                        {status_icon} {phase['name']}
                    </span>
                    <span style="font-size: 13px; color: #B0B0B0; margin-left: 15px;">
                        {phase['start'].strftime('%m/%d')} - {phase['end'].strftime('%m/%d')}
                    </span>
                </div>
                <div style="flex: 2; color: #E0E0E0; font-size: 13px;">
                    {phase['description']}
                </div>
                <div style="flex: 0 0 80px; text-align: right;">
                    <span style="font-size: 18px; font-weight: bold; color: #FFD700;">
                        {phase['goal_hours']}h
                    </span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


def get_progress_color(progress_rate):
    """進捗率に応じた色を返す"""
    if progress_rate >= 80:
        return "#4caf50", "#45a049"  # Green (順調)
    elif progress_rate >= 50:
        return "#ff9800", "#f57c00"  # Orange (注意)
    else:
        return "#f44336", "#e53935"  # Red (要注意)


def show_goal_vs_actual(stats, db_service):
    """現在の学習進捗サマリー（過去の成果含む総計）"""
    st.subheader("📈 現在の学習進捗")

    # データベースから過去資格の学習時間を計算
    with db_service.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT SUM(target_hours) as total
            FROM subjects
            WHERE category = '関連資格' AND completed = 1
        ''')
        result = cursor.fetchone()
        past_total = int(result['total']) if result['total'] else 0

    col1, col2, col3 = st.columns(3)

    with col1:
        # 診断士
        shindan_rate = (stats.shindan_total / stats.shindan_goal * 100) if stats.shindan_goal > 0 else 0
        color1, color2 = get_progress_color(shindan_rate)

        # ステータスアイコン
        if shindan_rate >= 80:
            status_icon = "✅"
            status_text = "順調"
        elif shindan_rate >= 50:
            status_icon = "⚠️"
            status_text = "注意"
        else:
            status_icon = "🚨"
            status_text = "要加速"

        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {color1} 0%, {color2} 100%);
                    padding: 25px; border-radius: 15px; color: white; text-align: center;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
                    height: 200px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-size: 18px; margin-bottom: 8px; font-weight: 600;">中小企業診断士</div>
            <div style="font-size: 42px; font-weight: bold; margin: 15px 0;">{shindan_rate:.1f}%</div>
            <div style="font-size: 16px; opacity: 0.95; margin-bottom: 10px;">{stats.shindan_total:.1f}h / {stats.shindan_goal:.0f}h</div>
            <div style="font-size: 14px; opacity: 0.9; margin-top: 8px;">{status_icon} {status_text}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # 統計
        toukei_rate = (stats.toukei_total / stats.toukei_goal * 100) if stats.toukei_goal > 0 else 0
        color1, color2 = get_progress_color(toukei_rate)

        # ステータスアイコン
        if toukei_rate >= 80:
            status_icon = "✅"
            status_text = "順調"
        elif toukei_rate >= 50:
            status_icon = "⚠️"
            status_text = "注意"
        else:
            status_icon = "🚨"
            status_text = "要加速"

        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {color1} 0%, {color2} 100%);
                    padding: 25px; border-radius: 15px; color: white; text-align: center;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
                    height: 200px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-size: 18px; margin-bottom: 8px; font-weight: 600;">統計検定2級</div>
            <div style="font-size: 42px; font-weight: bold; margin: 15px 0;">{toukei_rate:.1f}%</div>
            <div style="font-size: 16px; opacity: 0.95; margin-bottom: 10px;">{stats.toukei_total:.1f}h / {stats.toukei_goal:.0f}h</div>
            <div style="font-size: 14px; opacity: 0.9; margin-top: 8px;">{status_icon} {status_text}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        # 総学習時間（過去の成果含む）
        current_total = stats.shindan_total + stats.toukei_total
        all_time_total = past_total + current_total

        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    padding: 25px; border-radius: 15px; color: white; text-align: center;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
                    height: 200px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-size: 18px; margin-bottom: 8px; font-weight: 600;">総学習時間</div>
            <div style="font-size: 42px; font-weight: bold; margin: 15px 0;">{all_time_total:.0f}h</div>
            <div style="font-size: 14px; opacity: 0.9;">過去{past_total}h + 現在{current_total:.1f}h</div>
        </div>
        """, unsafe_allow_html=True)
