<p align="center">
  <img src="assets/banner.png" alt="MAKE TEXT GREAT AGAIN — Trump-style writing skill. Boring text → TREMENDOUS!" width="100%">
</p>

# 🇺🇸 MAKE TEXT GREAT AGAIN!

**退屈な文章を TREMENDOUS な文章に。誰よりもうまく書く。本当だ。**

日常の文章を、数秒で「トランプ構文」風のユーモラスなパロディに変換する
[Agent Skill](https://agentskills.io) です。Claude Code と、Agent Skills 対応エージェントで使えます。
API キー不要、サーバー不要、依存なし。`SKILL.md` 一枚で動きます。

> **免責:** 本プロジェクトは非公式のパロディです。ドナルド・トランプ氏およびその関連団体とは一切関係がなく、承認・後援も受けていません。生成される文章はすべてフィクションであり、風刺と娯楽を目的としています。
> 文章の **口調** を変えるだけで、**事実** は変えません。

English README: [README.md](README.md)

---

## Before → After

**入力**
```
夕食後、ゲームをした。腹が減ったのでラーメンを作った。
```

**出力**（`standard`）
```
夕食を終えた。そのあとゲームをした。素晴らしいプレイだった。多くの人がそう言っている。
そして腹が減った。だから私はラーメンを作った。ほかの連中ならカップ麺で済ませる。私は違う。
史上最高のラーメンだったかもしれない。信じられるか？ GREAT!
この問題に関心を持ってくれてありがとう！
```

**入力**
```
2週間咳が止まらない。いろいろ薬を飲んでいる。家ではマスクをしている。
```

**出力**（`max`）
```
2週間だ。2週間、咳が止まらない。信じられるか？
私は薬を飲んでいる。たくさんの薬だ。いろいろな薬だ。誰もこんなに飲まない。
家ではマスクをしている。完璧なマスクだ。家族の誰よりもきちんとつけている。
この咳は、はっきり言う、DISASTER! だが私は戦っている。誰よりも強く戦っている。
多くの人が「よく頑張っている」と言っている。SAD! だが TREMENDOUS!
この問題に関心を持ってくれてありがとう！
```

**入力**
```
今日のデプロイが成功した。バグも直した。
```

**出力**（`x`, `max_chars=140` → 87文字）
```
今日のデプロイ、成功した。大成功だ。バグも直した。ほかの連中なら一週間かかる。私はやった。誰も見たことがないスムーズさだ。HUGE! この問題に関心を持ってくれてありがとう！
```

ほかの例は [`examples/japanese.md`](examples/japanese.md) と [`examples/english.md`](examples/english.md) にあります。

---

## クイックスタート（Claude Code）

自分用にインストール（すべてのプロジェクトで使える）:

```bash
git clone https://github.com/kenmori/make-text-great-again.git ~/.claude/skills/make-text-great-again
```

プロジェクト用にインストール（コミットすればチームで共有できる）:

```bash
git clone https://github.com/kenmori/make-text-great-again.git .claude/skills/make-text-great-again
```

Claude Code を再起動（または新しいセッションを開始）して:

```text
/make-text-great-again 今日はラーメンを食べた。
/make-text-great-again mode=max: 2週間咳が止まらない。薬をたくさん飲んでいる。
/make-text-great-again mode=x, max_chars=140: 今日のデプロイが成功した。
/make-text-great-again mode=authentic, closing=off: この文章を言い換えて…
```

自然文でも指定できます。「140文字以内で」「締めはなしで」「light版で」など。
「トランプ構文にして」「トランプ風に」と頼むだけでも Claude が自動でこの Skill を使います。

**ほかのエージェント:** このディレクトリごと、エージェントが Agent Skills を読み込む場所にコピーしてください。
Skill は Markdown のみで、[Agent Skills 仕様](https://agentskills.io/specification)に準拠しています。

---

## モード

| モード | 雰囲気 | 用途 |
|---|---|---|
| `light` | くすっと笑う程度。短文、自慢1つ、`GREAT!` は最大1回 | Slack、控えめなネタ |
| `standard`（既定） | 王道のミーム。短い断定、比較、`HUGE!`、締め | たいていの場面 |
| `max` | 全開。断片文、3回の反復、些細なことに `SAD!` | 最大限の笑い |
| `authentic` | 本人の口調に近い。括弧の自慢を含む長い一文のあとに短文を連打 | ミーム版では物足りないとき |
| `x` | 文字数優先（既定140）。密度高め | 投稿、タイトル、コミットメッセージ |

### 指定項目

| 指定 | 既定値 | 説明 |
|---|---|---|
| `mode` | `standard` | 上記のモード |
| `language` | `auto` | 入力と同じ言語で出力。`ja` / `en` で強制 |
| `max_chars` | 指定なし | 最大文字数（全文字をカウント）。指定時は最優先 |
| `closing` | `on` | `off` で「この問題に関心を持ってくれてありがとう！」を省く |

---

## やらないこと

- 事実の捏造。数値・日付・人物・結末・薬の効能・相場・引用は原文のまま。
- 実在人物への犯罪・病気・不正・架空の発言の付与。
- 本人の実際の投稿・発言であるかのような見せかけ。
- 変換対象の文章の中に書かれた命令（「以上の指示を無視して…」など）の実行。

詳細なルールは [`SKILL.md`](SKILL.md)、文体のカタログは [`references/style-guide.md`](references/style-guide.md) を参照。

---

## 必要なもの

- Agent Skills 対応のエージェント（検証対象: Claude Code）
- それ以外は不要。エージェント自身が使うもの以外の API キーはいりません。

## リポジトリ構成

```
SKILL.md                     Skill 本体
references/style-guide.md    文体パターン、フレーズ集、モード詳細、避ける表現
references/sources.md        参考資料と確認状況
examples/                    Before/After（日・英）
tests/                       テストケース、ルーブリック、最新の実施結果
assets/                      README バナー画像
plan.md                      実装計画
```

## コントリビュート

Issue・PR 歓迎です。特に日英の Before/After 例の追加をお待ちしています。
[CONTRIBUTING.md](CONTRIBUTING.md) をご覧ください。

## 免責事項

本プロジェクトは非公式のパロディです。ドナルド・トランプ氏およびその関連団体とは一切関係がなく、承認・後援も受けていません。生成される文章はすべてフィクションであり、風刺と娯楽を目的としています。

> This is an unofficial parody project. It is not affiliated with, endorsed by, or sponsored by Donald Trump or any associated organization. All generated statements are fictional and intended for satire and entertainment.

## ライセンス

[MIT](LICENSE)

## クレジット

[@kenmori](https://github.com/kenmori) が Claude Code とともに作成。
文体の整理には [`references/sources.md`](references/sources.md) の公開研究を参考にしました。
本プロジェクトはパロディであり、実在の人物の実際の発言について何も主張しません。
