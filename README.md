# プログラミング言語別質問アプリ - programming_questions_language

## 使用方法

質問するプログラミング言語を選択後、質問を入力して質問するボタンを押してください。お待ちいただくと回答が返ってきます。
使用上の注意をご理解の上、使用してください。

## 使用上の注意

- 仮想環境上での使用を想定しています。はじめて使用される場合には使用手順の通りに仮想環境を作成してください。
- 使用するにはOpenAIとDeepLのAPIキーが必要です。ご自身で取得して設定後、使用してください。取得方法はご自身でお調べください。
- APIキーの設定手順は使用手順の中で説明しています。
- OpenAIを使用して解答を出力しています。解答内容に関して当アプリは責任を負いません。ご自身の責任において使用してください。

## 対応プログラミング言語

- HTML
- CSS
- PHP
- Laravel
- Python
- Flutter

## 使用手順

### Python 仮想環境を作成

以下のコマンドを実行して仮想環境を作成します。

```bash
python3 -m venv .venv
```

### Python 仮想環境を起動

以下のコマンドを実行して仮想環境を起動します。

```bash
source .venv/bin/activate.fish
```

### Python 仮想環境にパッケージをインストール

以下のコマンドを実行して`requirements.txt`にリストされているすべてのパッケージが仮想環境にインストールします。

```bash
pip3 install -r requirements.txt
```

### 環境変数を設定

`.env.example`に取得したOPENAI_API_KEYとDEEPL_API_KEYを入力して、ファイル名を`.env`に変更します。

```env
OPENAI_API_KEY=取得したOPENAI_API_KEY
DEEPL_API_KEY=取得したDEEPL_API_KEY
```

### 起動

以下のコマンドを実行してアプリを起動します。

```bash
streamlit run app.py
```

## OpenAI と DeepL の API KEY の取得方法

### OpenAI

「OpenAI APIキー 登録方法」で検索してください。

### DeepL

「DeepL APIキー 登録方法」で検索してください。

## プログラムの実行フロー

1. 日本語の質問を入力
2. 日本語の質問をDeepLで英語に翻訳
3. 英語に翻訳した質問をOpenAIに渡す
4. OpenAIからの解答を取得
5. DeepLで英語の解答を日本語に変換

## プログラムの構造

- UIはStreamlitを使用
- DeepLは日本語→英語と英語→日本語の2回使用するので、翻訳するテキストと言語を引数にして関数を作成
- OpenAIも管理しやすいように関数を作成し内部でDeepLの関数を使用して質問と解答の中間での受け渡しは英語、入力と出力は日本語になるように作成
