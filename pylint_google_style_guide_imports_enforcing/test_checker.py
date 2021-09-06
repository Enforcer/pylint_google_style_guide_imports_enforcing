import astroid
import pylint.testutils

from pylint_google_style_guide_imports_enforcing import AlphabeticallySortedImports


class TestAlphabeticallySortedImports(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = AlphabeticallySortedImports

    def test_import_exceptions_with_proper_imports(self):
        importnode = astroid.extract_node("""
        from typing import Optional
        from os import path
        from typing_extensions import get_args
        from six.moves import html_parser
        """)

        with self.assertNoMessages():
            self.checker.visit_importfrom(importnode)

    def test_import_exceptions_with_improper_imports(self):
        node = astroid.extract_node("""
            from typing import Optional
            from json import loads
            """)

        with self.assertAddsMessages(
            pylint.testutils.Message(
                msg_id="only-importing-modules-is-allowed",
                node=node,
                args=("loads",)
            )
        ):
            self.checker.visit_importfrom(node)
