markdown-convertor/
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── config.ini.example
├── docs/
│   ├── getting-started.md
│   └── style-guide.md
├── templates/
│   └── default.css
├── src/
│   ├── converter/
│   │   ├── __init__.py
│   │   ├── core.py       # 核心转换逻辑
│   │   ├── cli.py        # 命令行接口
│   │   └── utils.py      # 工具函数
└── tests/
    ├── test_core.py
    └── test_cli.py