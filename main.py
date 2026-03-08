import streamlit as st
import requests
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="全球汇率计算大师", page_icon="💰", layout="wide")

# --- 1. 稳健获取 API Key ---
def get_api_key():
    for i in range(100):
        key = st.secrets.get("API_KEY")
        if key:
            return key
        time.sleep(0.5)
    return None

API_KEY = get_api_key()

# --- 2. 核心逻辑判断 ---
if not API_KEY:
    # 如果真的拿不到 Key，只显示警告，不执行任何下方代码
    st.warning("🔄 正在等待云端 Secrets 加载，请在 5 秒后手动刷新页面...")
    st.info("如果你已经配置了 Secrets 但仍看到此提示，请点击右侧的 'Reboot App'")
    st.stop() # 这里用 stop 是安全的，因为已经在 warning 之后了
else:
    # 所有的函数定义和 UI 必须全部缩进在 else 里面！！
    @st.cache_data(ttl=3600)
    def get_rates(base_currency):
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"
        try:
            response = requests.get(url, timeout=10)
            data = response.json()
            if data.get("result") == "success":
                return data["conversion_rates"]
            return None
        except Exception as e:
            return None

    # --- 以下是 UI 界面 ---
    st.title("💰 实时汇率监控与计算中心")
    CURRENCY_LIST = ["CNY", "USD", "KRW", "EUR", "JPY", "GBP", "HKD"]
    
    col_left, col_right = st.columns([2, 1.2], gap="large")
    
    with col_left:
        st.subheader("实时转换")
        input_amount = st.number_input("请输入金额", value=1.0, step=0.01, format="%.2f")
        c1, c2 = st.columns(2)
        with c1:
            from_curr = st.selectbox("从", CURRENCY_LIST, index=0)
        with c2:
            to_curr = st.selectbox("转换为", CURRENCY_LIST, index=4)
        
        rates = get_rates(from_curr)
        if rates:
            current_rate = rates[to_curr]
            converted_result = input_amount * current_rate
            st.markdown(f"### {input_amount} {from_curr} 等于")
            st.markdown(f"<h1 style='color: #1a73e8;'>{converted_result:,.2f} {to_curr}</h1>", unsafe_allow_html=True)
        else:
            st.error("数据加载失败，请检查 API Key 状态。")

    st.divider()

    st.subheader("多币种混合计算器")
    st.info("可以在下方添加多笔不同货币的金额，系统会自动统一换算并求和。")

    # 初始化 session_state 存储计算行
    if 'calc_rows' not in st.session_state:
        st.session_state.calc_rows = [{'amount': 0.0, 'currency': 'USD', 'op': '+'}]

    # 最终汇总货币选择
    final_target = st.select_slider("选择最终汇总货币", options=CURRENCY_LIST, value="CNY")

    total_sum = 0.0

    # 遍历渲染每一行
    for i, row in enumerate(st.session_state.calc_rows):
        r1, r2, r3, r4 = st.columns([1, 2, 2, 1])
        
        with r1:
            op = st.selectbox("符号", ["+", "-"], key=f"op_{i}", index=0 if row.get('op') == '+' else 1)
        with r2:
            amt = st.number_input("金额", value=float(row['amount']), key=f"amt_{i}", step=10.0)
        with r3:
            curr = st.selectbox("货币", CURRENCY_LIST, key=f"curr_{i}", index=CURRENCY_LIST.index(row['currency']))
        with r4:
            if st.button("🗑️", key=f"del_{i}"):
                st.session_state.calc_rows.pop(i)
                st.rerun()
        
        # 更新数据到 session_state
        st.session_state.calc_rows[i] = {'amount': amt, 'currency': curr, 'op': op}
        
        # 实时计算当前行的汇率贡献
        row_rates = get_rates(curr)
        if row_rates:
            rate_to_final = row_rates[final_target]
            contribution = amt * rate_to_final
            if op == "+":
                total_sum += contribution
            else:
                total_sum -= contribution

    # 添加行按钮
    if st.button("➕ 添加一笔金额"):
        st.session_state.calc_rows.append({'amount': 0.0, 'currency': 'USD', 'op': '+'})
        st.rerun()

    # 显示合计结果
    st.divider()
    st.markdown(f"### 💰 合计")
    st.markdown(f"<h1 style='color: #1a73e8;'>{total_sum:,.2f} {final_target}</h1>", unsafe_allow_html=True)

    st.divider()
    # 最终统计结果
    st.markdown(f"### 🏁 所有项汇总结果 ({final_target})")
    st.markdown(f"<h2 style='background-color: #f1f3f4; padding: 20px; border-radius: 10px; text-align: center;'>{total_sum:,.2f} {final_target}</h2>", unsafe_allow_html=True)