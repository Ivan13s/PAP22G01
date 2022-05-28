import pylint
options=["--disable=unnecessary-lambda,missing-function-docstring,missing-module-docstring", 'app1_decorator.py']
pylint.run_pylint(argv=options)