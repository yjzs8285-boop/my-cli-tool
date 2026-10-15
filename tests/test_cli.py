"""cli 模块的基础测试。"""

import io
import unittest
from contextlib import redirect_stdout

from my_cli_tool import __version__
from my_cli_tool.cli import build_parser, main


class CliTest(unittest.TestCase):
    def test_hello_default(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = main(["hello"])
        self.assertEqual(code, 0)
        self.assertEqual(buf.getvalue().strip(), "Hello, world!")

    def test_hello_with_name(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = main(["hello", "Python"])
        self.assertEqual(code, 0)
        self.assertEqual(buf.getvalue().strip(), "Hello, Python!")

    def test_version(self):
        parser = build_parser()
        buf = io.StringIO()
        with redirect_stdout(buf), self.assertRaises(SystemExit) as cm:
            parser.parse_args(["--version"])
        self.assertEqual(cm.exception.code, 0)
        self.assertIn(__version__, buf.getvalue())


if __name__ == "__main__":
    unittest.main()
