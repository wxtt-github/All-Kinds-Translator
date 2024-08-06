import streamlit as st
from utils import generate_translate_text

st.title("多语言翻译器")

with st.sidebar:
    # 换行需要在\n前面加两个空格
    openai_api_key = st.text_input("请输入OpenAI API密钥：  \n(使用系统环境变量输os即可)", type="password")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/api-keys)")
    openai_base_url = st.text_input("请输入第三方base_url，  \n若为OpenAI API密钥则留空", type="default")
    st.markdown("```https://api.aigc369.com/v1```  \n~~方便我复制base_url~~")

source_lang = st.text_input("请输入源语言", value="中文")
target_lang = st.text_input("请输入目标语言", value="英文")
# st.text_area更适合输入长段文本
text = st.text_area("请输入待翻译文本")

submit = st.button("生成翻译")

if submit and not openai_api_key:
    st.info("请输入你的OpenAI API密钥")
    st.stop()
if submit and not source_lang:
    st.info("请输入源语言")
    st.stop()
if submit and not target_lang:
    st.info("请输入目标语言")
    st.stop()
if submit:
    with st.spinner(("正在生成中，请稍后")):
        translate_text = generate_translate_text(source_lang, target_lang, text, openai_api_key, openai_base_url)
    st.success("文本翻译已生成！")
    st.subheader("👇翻译：")
    st.write(translate_text)

# 测试文本
# 在今天的全球化时代，跨文化交流变得越来越重要。
# 无论是商业、教育还是个人交流，语言都扮演着关键的角色。
# 掌握多种语言不仅可以帮助我们更好地理解和尊重不同文化，还能为我们的职业生涯带来更多机会。
# 因此，学习和使用翻译工具对于每个人来说都是非常有益的。


