#### カテゴリー提案
開発

# 『GitHub Issue作成術式』 著者: 元木大介、カテゴリー: 開発

- プロンプト: 〜をしたいので、ghコマンドでいい感じにイシューを書いて、そのための実装計画を立てて、また#番号を取得してそれを内包したブランチを作成してください。そして、イシューURLを自動で開いて（lang ja）
- 魔法効果: GitHubでイシューを作成し、実装計画を立て、ブランチを作成し、イシューURLを自動で開く
- 特殊効果: ghコマンドを使用してGitHub操作を行う
- 利用前提: Open Interpreter上で実行、GPT-4を利用

# 術式の実行例:
    - オプション: Difyを用いたチャットボット開発
    - 術式は人がまず利用します。
    - 記述内容を改変せず利用すること
    - 使っている様子を、人とAIの対話で記載
    - 真面目なですます調

人: 〜をしたいので、ghコマンドでいい感じにイシューを書いて、そのための実装計画を立てて、また#番号を取得してそれを内包したブランチを作成してください。そして、イシューURLを自動で開いて（lang ja）

AI: はい、承知いたしました。Difyを用いたチャットボット開発のためのイシューを作成し、実装計画を立て、ブランチを作成し、イシューURLを開きます。

```bash
# イシューを作成
gh issue create --title "Difyを用いたチャットボット開発" --body "Difyフレームワークを使ってチャットボットを開発する。

### 要件
- 自然な対話ができること
- コンテキストを維持できること
- 知識ベースを構築できること

### タスク
- [ ] Difyのインストールと初期設定
- [ ] 対話データの収集と前処理
- [ ] 学習モデルの構築
- [ ] チャットボットインターフェースの実装
- [ ] 知識ベースの構築と統合
- [ ] テストと改善"

# 実装計画
1. Difyのインストールと初期設定
2. 対話データの収集と前処理
3. 学習モデルの構築
4. チャットボットインターフェースの実装 
5. 知識ベースの構築と統合
6. テストと改善

# ブランチ作成
git checkout -b issue-123-chatbot-dev

# イシューURLを開く
https://github.com/my-repo/issues/123
```

人: ありがとうございます。素晴らしい対応でした。

AI: ご丁寧にありがとうございます。今後もGitHubの運用をスムーズに行えるよう、ghコマンドの活用を心がけます。

# 術式を表現する画像生成プロンプトを記載する:

英語:
A software developer is using the gh command in a terminal to create a new issue on GitHub for developing a chatbot using the Dify framework. The issue contains requirements, tasks, and an implementation plan. The developer then checks out a new branch with the issue number included and opens the issue URL in a web browser.

日本語:
ソフトウェア開発者がターミナルでghコマンドを使用し、Difyフレームワークを使ったチャットボット開発のための新しいイシューをGitHubに作成している。イシューには要件、タスク、実装計画が含まれている。開発者はその後、イシュー番号を含む新しいブランチをチェックアウトし、WebブラウザでイシューのURLを開いている。