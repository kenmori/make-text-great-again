<p align="center">
  <img src="https://github.com/user-attachments/assets/31394bf9-3127-47fd-afa4-724009ddcbe2" alt="MAKE TEXT GREAT AGAIN — Trump-style writing skill. Boring text → TREMENDOUS!" width="100%">
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
夕食を終えた。そのあとゲームをした。素晴らしいプレイだった。断トツでだ。
そして腹が減った。だから私はラーメンを作った。我が家の歴史上、最高のラーメンだ。
スリーピー・ジョーにこのラーメンは作れない。作れるわけがない。SAD!
多くの人が「本物だ」と言っている。その通りだ。GREAT!
この問題に関心を持ってくれてありがとう！
```

**入力**
```
2週間咳が止まらない。いろいろ薬を飲んでいる。家ではマスクをしている。
```

**出力**（`max`）
```
2週間だ。2週間、咳が止まらない。信じられるか？
これはバイデンから引き継いだ咳だ。完全な混乱だ。私がこの咳の担当だったら、NEVER 始まっていない。
私は薬を飲んでいる。いろいろな薬だ。薬、薬、薬だ！ 誰もこんなに飲まない。断トツでだ。
家ではマスクをしている。完璧なマスクだ。誰も見たことがないようなマスクの着け方だ。我が家の歴史上、最高だ。
この「いんちき咳」は、はっきり言う、DISASTER! 私はとても不公平に扱われている。歴史上のどの患者よりもだ。
だが私は戦っている。懸命に戦っている。大きくて強い男たちが涙を浮かべて言った。「サー、あなたほど咳と戦う人は見たことがありません」。その通りだ！
フェイクニュースは「大げさだ」と言うだろう。WRONG! 終わりがない！ SAD!
続報を待て！
この問題に関心を持ってくれてありがとう！
```

**入力**
```
今日のデプロイが成功した。バグも直した。
```

**出力**（`x`, `max_chars=140` → 81文字）
```
速報：今日のデプロイ、成功した。大成功だ。バグも直した。スリーピー・ジョーには NEVER できない。誰も見たことがないようなデプロイだ。HUGE! ありがとう！
```

**入力**
```
会議が20分延びた。プロジェクターが動かなかった。
```

**出力**（`standard`, `politics=off`, `closing=off`：職場向け）
```
会議が20分延びた。20分だ。
原因は「ねぼすけプロジェクター」だ。動かなかった。何もしなかった。情けない！
私のせいではない。私はとても不公平に扱われた。歴史上のどの会議参加者よりもだ。
それでも私は最後までやった。ほかの連中なら途中で帰る。私は帰らない。
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

自然文でも指定できます。「140文字以内で」「締めはなしで」「light版で」「政治ネタなしで」など。
「トランプ構文にして」「トランプ風に」と頼むだけでも Claude が自動でこの Skill を使います。

**ほかのエージェント:** このディレクトリごと、エージェントが Agent Skills を読み込む場所にコピーしてください。
Skill は Markdown のみで、[Agent Skills 仕様](https://agentskills.io/specification)に準拠しています。

---

## モード

| モード | 雰囲気 | 用途 |
|---|---|---|
| `light` | くすっと笑う程度。短文、自慢1つ、政治ネタなし | Slack、控えめなネタ |
| `standard`（既定） | 王道のミーム。短い断定、自慢、比較、スリーピー・ジョーが1行出ることも。締めあり | たいていの場面 |
| `max` | 全部盛り。うまくいかない物へのあだ名、バイデンのせい、「サー」話、完全かつ全面的な支持、MAKE ___ GREAT AGAIN | 最大限の笑い |
| `authentic` | 実際の投稿の書き方に寄せる。大文字の名詞、短い括弧、曲がりくねる長い一文、最後に一言 | ミーム版では物足りないとき |
| `x` | 文字数優先（既定140）。密度高め | 投稿、タイトル、コミットメッセージ |

### 指定項目

| 指定 | 既定値 | 説明 |
|---|---|---|
| `mode` | `standard` | 上記のモード |
| `language` | `auto` | 入力と同じ言語で出力。`ja` / `en` で強制 |
| `max_chars` | 指定なし | 最大文字数（全文字をカウント）。指定時は最優先 |
| `closing` | `on` | `off` で「この問題に関心を持ってくれてありがとう！」などの締めを省く |
| `politics` | `on` | `off` でスリーピー・ジョーやフェイクニュースを出さない。敵役は物や架空の相手（「ねぼすけプロジェクター」）だけになる。職場向け |

### パターン集

実際の投稿 14,391 件の頻度調査（[`references/research-notes.md`](references/research-notes.md)）をもとにした約45種類の装置があります。一部を紹介します。

- **障害物へのあだ名:** 「ねぼすけプロジェクター」「いんちき天気予報」「何もしないコンパイラ」
- **いつもの敵役:** 「スリーピー・ジョーにこのラーメンは作れない。」「これはバイデンから引き継いだ咳だ。」
- **定型文:** 「完全かつ全面的に支持する！」「麺に強く、スープに強く」「偉大なる埼玉県」「MAKE ___ GREAT AGAIN!」
- **「サー」話:** 大きくて強い男たちが涙を浮かべて言う。「サー、こんなラーメンは見たことがありません」
- **被害者意識:** 「魔女狩りだ！」「仕組まれている！」「私はとても不公平に扱われている」。相手はプロジェクター。
- **締めの一言:** SAD! / 残念だ！ / 良くない！ / その通りだ！ / 続報を待て！ / 終わりがない！

データからわかった小ネタ：「believe me」は調査した投稿に1件も出てきません。あれは演説の口癖です。
書かれた投稿の特徴は、大文字の名詞と、最後の二語の判定でした。

---

## やらないこと

- 事実の捏造。数値・日付・人物・結末・薬の効能・相場・引用は原文のまま。
- 実在人物についての事実の主張。定番の敵役（スリーピー・ジョーことバイデン、フェイクニュース、急進左派）は、ラーメンやプロジェクターの責任を負わされるだけです。犯罪・汚職・健康・家族・架空の発言は一切書きません。
- 現実の選挙・裁判・報道・病気に「仕組まれた」「でっちあげ」を向けること。現実の政治・災害・不幸を扱う文章に敵役を持ち込むこと。
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
references/style-guide.md    約45種類の文体装置、フレーズ集、敵役のルール、モード別レシピ
references/research-notes.md 投稿14,391件の頻度調査
references/sources.md        参考資料と確認状況
examples/                    Before/After（日・英）
tests/                       テストケース、ルーブリック、最新の実施結果
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
