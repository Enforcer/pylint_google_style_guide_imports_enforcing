import astroid
from astroid import scoped_nodes

from pylint.interfaces import IAstroidChecker
from pylint.checkers import BaseChecker


class AlphabeticallySortedImports(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'check-if-we-import-only-modules'

    ONLY_IMPORTING_MODULES_IS_ALLOWED = 'only-importing-modules-is-allowed'

    msgs = {
        'C5101': ('"%s" shouldn\'t be imported directly.',
                  ONLY_IMPORTING_MODULES_IS_ALLOWED,
                  ''),
    }
    options = ()

    priority = -1

    excluded_modules = ['typing', 'typing_extensions', 'six.moves']

    def visit_importfrom(self, node):
        imported = node.do_import_module()

        if imported.name in self.excluded_modules:
            return

        for name, _ in node.names:
            _, result = imported.lookup(name)
            if not result:
                # it's not there, so probably this is another module - fine.
                continue
            imported_node, *_ = result
            if isinstance(imported_node, scoped_nodes.Module):
                continue

            # maybe a submodule?
            try:
                imported.import_module(name, relative_only=True)
            except astroid.AstroidImportError:
                self.add_message(
                    self.ONLY_IMPORTING_MODULES_IS_ALLOWED,
                    node=node,
                    args=(name, )
                )

def register(linter):
    linter.register_checker(AlphabeticallySortedImports(linter))
