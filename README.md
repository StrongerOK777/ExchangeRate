<div align="center">

# 💰 ExchangeRate

**实时汇率监控与计算中心**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=flat-square)](LICENSE)
[![API](https://img.shields.io/badge/API-ExchangeRate--API-F59E0B?style=flat-square&logo=fastapi&logoColor=white)](https://www.exchangerate-api.com)

<br/>

> 🌐 一个基于 Streamlit 构建的优雅汇率工具 —— 支持实时转换、多币种混合计算，数据每小时自动刷新。

<br/>

![demo](https://img.shields.io/badge/🚀%20立即体验-点击预览-6366F1?style=for-the-badge)

</div>

---

## ✨ 功能亮点

| 功能 | 描述 |
|------|------|
| ⚡ **实时汇率转换** | 输入金额，即时换算，支持 CNY / USD / KRW / EUR / JPY / GBP / HKD |
| 🧮 **多币种混合计算** | 多笔不同货币的金额加减混合，自动统一换算并汇总 |
| 🔄 **智能缓存** | 汇率数据每小时自动刷新，减少 API 请求次数 |
| 🎨 **简洁 UI** | 基于 Streamlit 的响应式宽屏布局，清晰直观 |

---

## 🖼️ 界面预览

```
┌─────────────────────────────────────────────────────────┐
│  💰 实时汇率监控与计算中心                                  │
├──────────────────────────┬──────────────────────────────┤
│  实时转换                 │                              │
│  金额:  [ 1.00      ]    │                              │
│  从:    [ CNY ▼    ]    │  (汇率图表 / 信息面板)          │
│  换为:  [ JPY ▼    ]    │                              │
│                          │                              │
│  1 CNY = 21.xx JPY      │                              │
├──────────────────────────┴──────────────────────────────┤
│  多币种混合计算器                                          │
│  [+]  [ 100.00 ]  [ USD ▼ ]  🗑️                       │
│  [-]  [  50.00 ]  [ EUR ▼ ]  🗑️                       │
│  + 添加一行                    合计: ¥ x,xxx.xx CNY      │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/your-username/ExchangeRate.git
cd ExchangeRate
```

### 2. 安装依赖

```bash
pip install streamlit requests pandas numpy
```

或使用 requirements 文件（如有）：

```bash
pip install -r requirements.txt
```

### 3. 配置 API Key

在项目根目录创建 `.streamlit/secrets.toml`（此文件已被 `.gitignore` 保护，不会上传至 Git）：

```toml
# .streamlit/secrets.toml
API_KEY = "your_api_key_here"
```

> 💡 免费 API Key 申请：[https://www.exchangerate-api.com](https://www.exchangerate-api.com)，免费套餐每月 1500 次请求。

### 4. 启动应用

```bash
streamlit run main.py
```

浏览器将自动打开 `http://localhost:8501` 🎉

---

## 📁 项目结构

```
ExchangeRate/
├── main.py                  # 主应用入口
├── .streamlit/
│   ├── secrets.toml         # 🔐 API 密钥（本地，不提交 Git）
│   └── config.toml          # Streamlit 主题配置（可选）
├── .gitignore               # Git 忽略规则
└── README.md                # 项目文档
```

---

## 🛠️ 技术栈

<div align="center">

| 技术 | 版本 | 用途 |
|------|------|------|
| [Python](https://python.org) | 3.8+ | 核心语言 |
| [Streamlit](https://streamlit.io) | 1.x | Web UI 框架 |
| [Requests](https://requests.readthedocs.io) | 2.x | HTTP 请求 |
| [Pandas](https://pandas.pydata.org) | 2.x | 数据处理 |
| [NumPy](https://numpy.org) | 1.x | 数值计算 |
| [ExchangeRate-API](https://www.exchangerate-api.com) | v6 | 汇率数据源 |

</div>

---

## ⚙️ 配置说明

### 支持的货币

默认支持以下 7 种货币，可在 `main.py` 中的 `CURRENCY_LIST` 自由扩展：

```python
CURRENCY_LIST = ["CNY", "USD", "KRW", "EUR", "JPY", "GBP", "HKD"]
```

### 缓存策略

汇率数据通过 `@st.cache_data(ttl=3600)` 缓存，每 **1 小时**自动过期刷新，可按需调整 `ttl` 参数（单位：秒）。

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建新分支 `git checkout -b feat/your-feature`
3. 提交更改 `git commit -m 'feat: add some feature'`
4. 推送分支 `git push origin feat/your-feature`
5. 创建 Pull Request

---

## 🌐 在线使用

不想自己部署的同学，可以直接访问在线版本：

👉 [https://cur-converter.streamlit.app](https://cur-converter.streamlit.app)

---

## 📄 License

本项目采用 [MIT License](LICENSE) 开源协议。

---

<div align="center">

Made with ❤️ by **ExchangeRate Team**

⭐ 如果觉得有帮助，欢迎点个 Star！

</div>
