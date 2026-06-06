"""
Anki Card CSS Template - Dark Mode Support
統計検定2級 Ankiカード用共通CSSテンプレート

Anki's night mode uses the .night_mode class.
This template provides proper contrast in both light and dark modes.

作成日: 2026-01-25
更新日: 2026-01-25 (MathJax dark mode fix improved)
"""

# Shared CSS with dark mode support (includes table and mnemonic styles)
CARD_CSS = '''
/* Base styles (Light Mode) */
.card {
    font-family: "Hiragino Sans", "Yu Gothic", sans-serif;
    font-size: 18px;
    text-align: left;
    color: #333;
    background-color: #fff;
    padding: 20px;
    line-height: 1.6;
}

.question { font-size: 20px; margin-bottom: 15px; }
.answer { font-size: 18px; margin-top: 15px; }
.source { font-size: 12px; color: #888; margin-top: 20px; padding-top: 10px; border-top: 1px solid #eee; }

.formula {
    background-color: #f0f4f8;
    padding: 15px;
    border-radius: 8px;
    margin: 10px 0;
    border: 1px solid #d0d7de;
    color: #1a1a1a;
}

.important { color: #dc3545; font-weight: bold; }

.example {
    background-color: #d4edda;
    padding: 12px;
    border-radius: 8px;
    margin: 10px 0;
    border: 1px solid #28a745;
    color: #155724;
}

.mnemonic {
    background-color: #fff3cd;
    padding: 10px;
    border-radius: 5px;
    margin: 10px 0;
    border: 1px solid #ffc107;
    color: #856404;
}

table {
    border-collapse: collapse;
    margin: 10px 0;
    width: 100%;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: center;
}

th {
    background-color: #f0f0f0;
    color: #333;
}

/* Dark Mode / Night Mode Support */
.night_mode .card { background-color: #1e1e1e; color: #e0e0e0; }
.night_mode .source { color: #a0aec0; border-top-color: #4a5568; }
.night_mode .formula { background-color: #2d3748; border: 1px solid #4a5568; color: #f7fafc; }
.night_mode .important { color: #fc8181; }
.night_mode .example { background-color: #1a4731; border: 1px solid #2f855a; color: #c6f6d5; }
.night_mode .mnemonic { background-color: #744210; border: 1px solid #d69e2e; color: #fefcbf; }

.night_mode table { border-color: #4a5568; }
.night_mode th { background-color: #2d3748; color: #e0e0e0; border-color: #4a5568; }
.night_mode td { border-color: #4a5568; color: #e0e0e0; }

/* MathJax dark mode fix */
.night_mode mjx-container, .night_mode .MathJax { color: #f7fafc !important; }
.night_mode .formula mjx-container, .night_mode .formula .MathJax { color: #f7fafc !important; }
.night_mode .example mjx-container, .night_mode .example .MathJax { color: #c6f6d5 !important; }
'''

# CSS without table styles (for cards that don't use tables)
CARD_CSS_NO_TABLE = '''
/* Base styles (Light Mode) */
.card {
    font-family: "Hiragino Sans", "Yu Gothic", sans-serif;
    font-size: 18px;
    text-align: left;
    color: #333;
    background-color: #fff;
    padding: 20px;
    line-height: 1.6;
}

.question { font-size: 20px; margin-bottom: 15px; }
.answer { font-size: 18px; margin-top: 15px; }
.source { font-size: 12px; color: #888; margin-top: 20px; padding-top: 10px; border-top: 1px solid #eee; }

.formula {
    background-color: #f0f4f8;
    padding: 15px;
    border-radius: 8px;
    margin: 10px 0;
    border: 1px solid #d0d7de;
    color: #1a1a1a;
}

.important { color: #dc3545; font-weight: bold; }

.example {
    background-color: #d4edda;
    padding: 12px;
    border-radius: 8px;
    margin: 10px 0;
    border: 1px solid #28a745;
    color: #155724;
}

/* Dark Mode / Night Mode Support */
.night_mode .card { background-color: #1e1e1e; color: #e0e0e0; }
.night_mode .source { color: #a0aec0; border-top-color: #4a5568; }
.night_mode .formula { background-color: #2d3748; border: 1px solid #4a5568; color: #f7fafc; }
.night_mode .important { color: #fc8181; }
.night_mode .example { background-color: #1a4731; border: 1px solid #2f855a; color: #c6f6d5; }

/* MathJax dark mode fix */
.night_mode mjx-container, .night_mode .MathJax { color: #f7fafc !important; }
.night_mode .formula mjx-container, .night_mode .formula .MathJax { color: #f7fafc !important; }
.night_mode .example mjx-container, .night_mode .example .MathJax { color: #c6f6d5 !important; }
'''
