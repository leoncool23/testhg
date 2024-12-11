import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 设置页面标题和描述
st.title("Streamlit 演示程序")
st.write("这是一个简单的 Streamlit 应用示例，展示了文件上传、文本输入和图表生成功能。")

# 文件上传功能
st.header("1. 文件上传")
uploaded_file = st.file_uploader("上传一个 CSV 文件", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("上传的文件内容：")
    st.dataframe(data)

# 文本输入功能
st.header("2. 文本输入")
user_input = st.text_input("请输入一些文本：")
if user_input:
    st.write(f"您输入的内容是：{user_input}")

# 图表生成功能
st.header("3. 随机数据图表生成")
generate_chart = st.button("生成随机图表")
if generate_chart:
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.random.normal(0, 0.1, size=x.shape)
    fig, ax = plt.subplots()
    ax.plot(x, y, label="随机数据")
    ax.set_title("随机图表示例")
    ax.set_xlabel("X 轴")
    ax.set_ylabel("Y 轴")
    ax.legend()
    st.pyplot(fig)

# Footer 信息
st.write("\n---\n")
st.write("作者：您的名字 | 联系方式：example@example.com")
