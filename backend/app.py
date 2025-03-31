from flask import Flask, jsonify
from flask_cors import CORS
from data.nav_data import *

app = Flask(__name__)
# 允许所有来源访问
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

@app.route('/api/nav-links')
def get_nav_links():
    try:
        data = [
            {"name": "AI工具", "links": AI_TOOLS},
            {"name": "技术社区", "links": TECH_COMMUNITY},
            {"name": "学习平台", "links": LEARNING_PLATFORMS},
            {"name": "开发工具", "links": DEV_TOOLS},
            {"name": "设计资源", "links": DESIGN_RESOURCES},
            {"name": "云服务平台", "links": CLOUD_SERVICES},
            {"name": "前端框架", "links": FRONTEND_FRAMEWORKS},
            {"name": "效率工具", "links": PRODUCTIVITY_TOOLS}
        ]
        return jsonify(data)
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "数据加载失败"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)