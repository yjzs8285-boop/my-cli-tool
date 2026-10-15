# my-cli-tool

一个 Python 命令行工具。

## 功能特性

- TODO: 在此描述核心功能
- 基于 Python 标准库 `argparse`，零第三方依赖即可运行
- 通过 `pyproject.toml` 打包，安装后提供 `my-cli-tool` 命令

## 环境要求

- Python 3.9+

## 安装

### 从源码安装（开发模式）

```bash
# 克隆仓库
git clone https://github.com/yjzs8285-boop/my-cli-tool.git
cd my-cli-tool

# 创建并激活虚拟环境
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 以可编辑模式安装
pip install -e .
```

## 使用

安装后即可使用命令：

```bash
my-cli-tool --version
my-cli-tool --help
my-cli-tool hello
my-cli-tool hello Python
```

未安装时也可以直接运行模块：

```bash
python -m my_cli_tool hello
```

## 开发

```bash
# 运行测试
python -m unittest discover -s tests
```

## 项目结构

```
my-cli-tool/
├── pyproject.toml          # 打包配置与命令入口
├── README.md
├── LICENSE
├── src/
│   └── my_cli_tool/
│       ├── __init__.py
│       ├── __main__.py     # 支持 python -m my_cli_tool
│       └── cli.py          # 命令行入口
└── tests/
    └── test_cli.py
```

## 许可证

[MIT](LICENSE)
