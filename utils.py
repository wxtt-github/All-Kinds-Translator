import os
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper

def generate_translate_text(source_lang, target_lang, text, api_key, base_url):
    translate_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """你的任务是将{source_lang}翻译成{target_lang}，请给出{text}翻译后的结果
             """)
        ]
    )

    if api_key == "os":
        api_key = os.environ.get("OPENAI_API_KEY")

    if base_url != "":
        model = ChatOpenAI(openai_api_key=api_key, base_url=base_url)
    else:
        model = ChatOpenAI(openai_api_key=api_key)

    translate_chain = translate_template | model

    translate_text = translate_chain.invoke({"source_lang": source_lang, "target_lang": target_lang, "text": text}).content

    return translate_text