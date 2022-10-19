import astroid
import pylint.testutils

from pylint_google_style_guide_imports_enforcing import ModuleOnlyImports


class TestAlphabeticallySortedImports(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = ModuleOnlyImports

    def test_reports_direct_imports(self):
        node = astroid.extract_node("""
            from __future__ import annotations
            """)

        with self.assertNoMessages():
            self.checker.visit_importfrom(node)
