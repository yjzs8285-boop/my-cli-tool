"""支持通过 python -m my_cli_tool 方式运行。"""

import sys

from my_cli_tool.cli import main

if __name__ == "__main__":
    sys.exit(main())
