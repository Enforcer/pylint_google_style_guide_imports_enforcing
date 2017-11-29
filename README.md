# How it works?
It marks importing anything but modules/packages as invalid with a message `only-importing-modules-is-allowed`. This adheres to Google's Python style guide.

# Why?
To not force people to manual check if something we imported is a module or not.

# How to use it?
After installing a package just `pylint`, appending `pylint_google_style_guide_imports_enforcing` to your `--load-plugins` option, like this: `pylint my_cool_project --load-plugins=pylint_google_style_guide_imports_enforcing`
