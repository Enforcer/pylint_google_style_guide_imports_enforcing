How it works?
===============
It marks importing anything but modules/packages as invalid with a message `only-importing-modules-is-allowed`. This adheres to Google's Python style guide.

An example::

    from functools import partial  # invalid
    import functools  # valid
    from some_module.some_subomdule import SomeClass  # invalid
    from some_module import some_subomdule  # valid

Why?
===============
To not force people to manual check if something we imported is a module or not.

How to use it?
===============
After installing a package just run `pylint`, appending `pylint_google_style_guide_imports_enforcing` to your `--load-plugins` option.

An example::
    pylint my_cool_project --load-plugins=pylint_google_style_guide_imports_enforcing

or append it to your `pylintrc` file::
    [MASTER]
    load-plugins=pylint_google_style_guide_imports_enforcing
