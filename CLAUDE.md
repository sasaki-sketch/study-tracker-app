# Claude Code ルール

## 🚨 絶対遵守ルール

### Anthropic API使用制限
- **`anthropic.Anthropic()` および `client.messages.create()` の使用は、X投稿文生成（`services/record_handler.py`内）のみ許可**
- それ以外の場所では**絶対に使用禁止**
- 理由: 従量課金APIのため、X投稿文生成以外でコストをかけないため

### 許可されているツール
- Read/Grep/Bash/Edit/Write/Glob → 常時使用OK
- Task/WebSearch/WebFetch → MAXプラン内、通常使用OK

### 禁止事項
- X投稿文生成以外で `anthropic.Anthropic()` を使う
- コード内に新しくAnthropicクライアントを作成する

---

## 📝 作業前チェックリスト
1. Anthropic APIを使おうとしていないか？
2. 使う場合、X投稿文生成か？
3. それ以外なら、Read/Grep/Task等の代替手段はないか？
