import csv
import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 数据存储文件
DATA_FILE = 'data/experiment_data.csv'

# 初始化 CSV 文件头（如果文件不存在）
def init_db():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow([
                'Timestamp', 
                'Condition',        # A=人工, B=AI
                'WTP_Amount',       # 支付金额
                'Perceived_Effort', # 感知努力 (1-7)
                'Demystification',  # 门槛/替代感 (1-7)
                'Fairness',         # 公平感 (1-7)
                'Quality',          # 质量感知 (1-7)
                'Mani_Check',       # 操纵检查 (A/B/Unsure)
                'Reason'            # 开放性理由
            ])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.json
        
        # 获取当前时间
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 写入 CSV
        with open(DATA_FILE, mode='a', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow([
                timestamp,
                data.get('condition'),
                data.get('wtp'),
                data.get('q_effort'),
                data.get('q_demystification'),
                data.get('q_fairness'),
                data.get('q_quality'),
                data.get('manipulation_check'),
                data.get('reason')
            ])
            
        return jsonify({"status": "success", "message": "Data saved"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    init_db()
    # 启动服务，端口 5000
    app.run(host='0.0.0.0', port=5000, debug=True)