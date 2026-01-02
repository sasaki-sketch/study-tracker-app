"""
古典名言ユーティリティ
論語、孟子などの中国古典と日本の古典を中心に、学習・努力に関する名言を提供
"""
import random
from datetime import date


def get_daily_quote():
    """日付ベースで古典名言を取得

    Returns:
        dict: {'original': 書き下し文, 'translation': 現代語訳, 'source': 出典}
    """
    # 論語・孟子などの中国古典
    chinese_classics = [
        {
            'original': '学びて時に之を習う、亦説ばしからずや',
            'translation': '学んだことを時々復習する、なんと喜ばしいことだろうか',
            'source': '論語・学而第一'
        },
        {
            'original': '学びて思わざれば則ち罔し、思いて学ばざれば則ち殆し',
            'translation': '学ぶだけで考えなければ本当の理解には至らず、考えるだけで学ばなければ独りよがりになって危険である',
            'source': '論語・為政第二'
        },
        {
            'original': '之を知る者は之を好む者に如かず、之を好む者は之を楽しむ者に如かず',
            'translation': '物事を知っている者は、それを好む者には及ばない。好む者は、それを楽しむ者には及ばない',
            'source': '論語・雍也第六'
        },
        {
            'original': '学びて已まざれば聖と為る可し',
            'translation': '学び続けて止まなければ、聖人になることができる',
            'source': '荀子・勧学篇'
        },
        {
            'original': '天将に大任を斯の人に降さんとするや、必ず先ず其の心志を苦しめ、其の筋骨を労せしむ',
            'translation': '天が人に大任を与えようとする時は、必ずまずその人の心を苦しめ、体を鍛える',
            'source': '孟子・告子下'
        },
        {
            'original': '鍥して捨てざれば、金石も鏤む可し',
            'translation': '刻み続けて諦めなければ、金属や石でさえも彫ることができる',
            'source': '荀子・勧学篇'
        },
        {
            'original': '君子は器ならず',
            'translation': '優れた人物は一つの技能に限定されず、広く学び様々な場面に対応できる',
            'source': '論語・為政第二'
        },
        {
            'original': '過ちて改めざる、是を過ちと謂う',
            'translation': '過ちを犯しながら改めないこと、これこそが本当の過ちである',
            'source': '論語・衛霊公第十五'
        },
    ]

    # 日本の古典・先人の言葉
    japanese_classics = [
        {
            'original': '至誠にして動かざる者は未だ之れ有らざるなり',
            'translation': '真心を尽くして行動すれば、動かせないものなど存在しない',
            'source': '吉田松陰・講孟箚記'
        },
        {
            'original': '志を立てて以て万事の源と為す',
            'translation': '志を立てることが、すべての物事の源である',
            'source': '吉田松陰'
        },
        {
            'original': '学問は、ただ年月長く倦まずおこたらずして、はげみつとむるぞ肝要にて候',
            'translation': '学問は、ただ長い年月飽きずに怠けずに、励み努めることが肝心である',
            'source': '上杉鷹山'
        },
        {
            'original': '天は人の上に人を造らず人の下に人を造らず',
            'translation': '天は人間を平等に創造した。違いは学ぶか学ばないかである',
            'source': '福澤諭吉・学問のすゝめ'
        },
        {
            'original': '独立の気力なき者は必ず人に依頼す、人に依頼する者は必ず人を恐る',
            'translation': '独立した気概のない者は必ず人に頼る。人に頼る者は必ず人を恐れる',
            'source': '福澤諭吉・学問のすゝめ'
        },
        {
            'original': '読書は学問の術なり、学問は事をなすの術なり',
            'translation': '読書は学問のための手段であり、学問は事を成し遂げるための手段である',
            'source': '福澤諭吉'
        },
    ]

    # 西洋の名言（少数）
    western_quotes = [
        {
            'original': '我思う、故に我あり',
            'translation': '考えるということこそが、自分が存在する証明である',
            'source': 'デカルト'
        },
        {
            'original': '知識は力なり',
            'translation': '知識を持つことは、力を持つことと同じである',
            'source': 'フランシス・ベーコン'
        },
    ]

    # 中国古典と日本古典を多めに（8:6:1の比率）
    all_quotes = (chinese_classics * 8) + (japanese_classics * 6) + (western_quotes * 1)

    # 日付を元にシードを設定（同じ日は同じ名言）
    today = date.today()
    seed = today.year * 10000 + today.month * 100 + today.day
    random.seed(seed)

    return random.choice(all_quotes)
