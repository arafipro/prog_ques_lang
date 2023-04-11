import streamlit as st
import deepl, openai, os
from os.path import join, dirname
from dotenv import load_dotenv

# envファイルのパスを取得
dotenv_path = join(dirname(__file__), ".env")

# envファイルの読み込み
load_dotenv(
    dotenv_path,
    verbose=True,  # .envファイルが見つからないときにエラーを出す
)

st.title("GPT Programming Question")

st.sidebar.markdown(
    """## 使用方法
質問するプログラミング言語を選択後、質問を入力して質問するボタンを押してください。
お待ちいただくと回答が返ってきます。使用上の注意をご理解の上、使用してください。
## 使用上の注意
- 仮想環境上での使用を想定しています。はじめて使用される場合には使用手順の通りに仮想環境を作成してください。
- 使用するにはOpenAIとDeepLのAPI KEYが必要です。ご自身で取得して設定後、使用してください。取得方法はご自身でお調べください。
- API KEYの設定手順は使用手順の中で説明しています。
- OpenAIを使用して解答を出力しています。解答内容に関して当アプリは責任を負いません。ご自身の責任において使用してください。
"""
)

pg: str = st.selectbox(
    "質問するプログラミング言語を選択してください",
    (
        "HTML",
        "CSS",
        "PHP",
        "Laravel",
        "Python",
        "Flutter",
    ),
)

ques_txt_ja: str = st.text_input("質問を入力してください")

ans_btn: bool = st.button("質問する")


def deepl_trans(pre_trans_test: str, target_lang: str):
    api_key = os.environ.get("DEEPL_API_KEY")
    translator = deepl.Translator(api_key)
    post_trans_test = translator.translate_text(
        pre_trans_test,
        target_lang=target_lang,
    )
    return post_trans_test


def openai_chat_pg_question(pg: str, ques_txt_ja: str):
    user_txt = deepl_trans(ques_txt_ja, "EN-US")
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"""You are a most helpful {pg} engieer.\n
																Output in markdown format.\n
																Code and commands to be output should be enclosed in ``` and ```.""",
            },
            {
                "role": "user",
                "content": f"{user_txt}\n"
            },
        ],
    )
    ans_text = response["choices"][0]["message"]["content"]
    ans_text_ja = deepl_trans(ans_text, "JA")
    return ans_text_ja


if ans_btn and ques_txt_ja:
    st.success("解答を考えています")
    ans_txt = openai_chat_pg_question(pg, ques_txt_ja)
    st.markdown(ans_txt)
else:
    st.warning("質問を入力してください")
