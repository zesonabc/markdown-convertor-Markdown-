# Markdown Convertor 📄↔️📝

[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue)](https://pandoc.org/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)]()

专业Markdown文档格式转换工具，支持多平台运行和批量处理。

## 功能亮点 ✨
- 一键转换HTML/PDF/DOCX格式
- 自动生成可交互目录
- 支持自定义CSS模板
- 批量文件处理模式
- 详细的转换日志记录

## 安装指南 📦

### 前置条件
安装 [Pandoc](https://pandoc.org/installing.html)

### 各平台安装
```bash
# Windows (PowerShell)
pip install -r requirements.txt

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 使用示例 🚀
```bash
# 转换单个文件
md-convert report.md -f pdf

# 批量转换目录
md-convert ./docs -f docx -t academic.css

# 生成详细日志
md-convert chapter.md -v
```

## 开发指南 🛠️
```bash
# 运行测试
pytest tests/

# 构建安装包
python setup.py sdist bdist_wheel
```

## 贡献流程 🤝
请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)