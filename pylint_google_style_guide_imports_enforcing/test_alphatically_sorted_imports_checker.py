import astroid
import pylint.testutils

from pylint_google_style_guide_imports_enforcing import ModuleOnlyImports


class TestAlphabeticallySortedImports(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = ModuleOnlyImports

    def test_doesnt_report_direct_imports_from_excluded_modules(self):
        importnode = astroid.extract_node("""
        from typing import Optional
        from os import path
        from typing_extensions import get_args
        from six.moves import html_parser
        """)

        with self.assertNoMessages():
            self.checker.visit_importfrom(importnode)

    def test_reports_direct_imports(self):
        node = astroid.extract_node("""
            from typing import Optional
            from json import loads
            """)

        with self.assertAddsMessages(
            pylint.testutils.MessageTest(
                msg_id="only-importing-modules-is-allowed",
                node=node,
                args=("loads",),
                line=3,
                col_offset=0,
                end_line=3,
                end_col_offset=22,
            )
        ):
            self.checker.visit_importfrom(node)
