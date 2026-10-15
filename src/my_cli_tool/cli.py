"""my-cli-tool 的命令行入口。

使用标准库 argparse 实现，无需安装第三方依赖。
"""

import argparse
import sys

from my_cli_tool import __version__


def build_parser() -> argparse.ArgumentParser:
    """构造命令行参数解析器。"""
    parser = argparse.ArgumentParser(
        prog="my-cli-tool",
        description="一个 Python 命令行工具",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command")

    # 示例：hello 子命令
    hello_parser = subparsers.add_parser("hello", help="打印问候语")
    hello_parser.add_argument(
        "name",
        nargs="?",
        default="world",
        help="要问候的名字（默认：world）",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    """命令行主函数，返回进程退出码。"""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "hello":
        print(f"Hello, {args.name}!")
        return 0

    # 未指定子命令时打印帮助信息
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
