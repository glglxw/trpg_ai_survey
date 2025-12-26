# 🛒 TRPG 服务价值感知实验平台 (TRPG Value Perception Experiment)

这是一个基于 Python (Flask) 和 HTML 构建的轻量级 Web 实验平台，专为线下桌游店/跑团店设计。

该项目旨在研究 **“人工智能（AI）的参与度披露”** 对用户在服务行业（特别是 TRPG 跑团）中 **付费意愿（WTP）** 和 **价值感知** 的影响。

## 🧪 实验设计逻辑

本系统采用 **被试间设计 (Between-subjects Design)**，用户扫码进入页面后，系统会自动以 50% 的概率将其分配到以下两组之一，并记录其真实的付费决策。

### 自变量 (Independent Variable)
*   **Condition A (控制组 - 人工匠心)**：强调剧情与 NPC 对话完全由主持人（GM）依靠个人经验和即兴能力独立完成。
*   **Condition B (实验组 - AI 协作)**：强调剧情与 NPC 对话是由主持人与公开的 AI 大模型协作完成。

### 因变量 (Dependent Variables)
1.  **WTP (Willingness to Pay)**：用户在基础成本（29.9元）之上愿意支付的最终金额。
2.  **感知努力 (Perceived Effort)**：用户认为 GM 付出了多少脑力/精力。
3.  **去神秘化/复刻难度 (Demystification)**：用户认为掌握相同方法后，复刻该体验的难易程度。
4.  **公平感 (Fairness)**：用户对定价公平性的感知。

---

## 🚀 快速开始

### 1. 环境准备
确保您的电脑上已安装 [Python 3.x](https://www.python.org/downloads/)。

### 2. 安装依赖
在项目根目录下打开终端（Terminal 或 CMD），运行以下命令安装 Flask：

```bash
pip install -r requirements.txt
```
*(如果没有 requirements.txt，直接运行 `pip install Flask` 即可)*

### 3. 启动服务器
运行以下命令启动实验平台：

```bash
python app.py
```

### 4. 访问页面
*   **本机测试**：在浏览器打开 `http://127.0.0.1:5000`
*   **局域网访问（店内使用）**：
    1.  打开终端，输入 `ipconfig` (Windows) 或 `ifconfig` (Mac) 查看电脑的局域网 IP 地址（例如 `192.168.1.5`）。
    2.  让顾客手机连接店内 Wi-Fi。
    3.  顾客扫描二维码或输入地址：`http://192.168.1.5:5000`。

---

## 📊 数据说明

所有实验数据会自动追加写入项目根目录下的 `experiment_data.csv` 文件中。建议使用 Excel 或 SPSS 打开分析。

| 字段名 | 说明 | 取值范围 |
| :--- | :--- | :--- |
| **Timestamp** | 提交时间 | YYYY-MM-DD HH:MM:SS |
| **Condition** | 实验分组 | `A` (人工组) / `B` (AI组) |
| **WTP_Amount** | 支付金额 | ≥ 29.9 (浮点数) |
| **Perceived_Effort** | 感知努力程度 | 1-7 (7代表非常努力) |
| **Demystification** | 复刻难度感知 | 1-7 (7代表非常容易复刻) |
| **Fairness** | 定价公平感 | 1-7 (7代表非常公平) |
| **Quality** | 质量感知(控制变量) | 1-7 (7代表质量很高) |
| **Mani_Check** | 操纵检查 | `Human` / `AI` / `Unsure` |
| **Reason** | 开放性理由 | 文本字符串 |

> **⚠️ 数据分析提示**：在分析数据前，建议剔除 `Mani_Check` 回答错误（例如处于 B 组却选了 Human）的样本，以确保数据有效性。

---

## 📂 项目结构

```text
TRPG-Experiment/
├── app.py                # 后端核心逻辑 (数据处理、CSV写入)
├── experiment_data.csv   # 数据存储文件 (自动生成)
├── requirements.txt      # 依赖库列表
├── README.md             # 说明文档
└── templates/
    └── index.html        # 前端页面 (问卷逻辑、随机分组、样式)
```

---

## 🛠️ 自定义配置

如果您需要修改问卷文案或逻辑：

1.  **修改刺激物文案**：打开 `templates/index.html`，找到底部的 `<script>` 区域，修改 `if (condition === 'A')` 里的 HTML 内容。
2.  **修改价格底线**：在 `index.html` 中搜索 `29.9`，将其修改为您期望的底价。
3.  **修改问卷题目**：直接在 `index.html` 的 HTML 结构中修改 `<label>` 标签的内容。

---

## 📱 兼容性

*   **前端**：已针对 iOS Safari 和 Android Chrome 进行移动端适配，禁止了缩放以获得原生 App 般的体验。
*   **防重复**：使用了 `localStorage` 防止同一用户刷新页面后组别发生变化（避免穿帮）。

---

## 🔒 隐私与伦理

本系统仅收集实验所需数据，不收集用户的微信 ID、手机号等个人隐私信息。建议在实验结束后向感兴趣的玩家进行事后解释（Debriefing）。