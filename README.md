# Wagtail PYPI Template

A good starting point for a wagtail pypi package.

Replace `yourapp` in these files with what you intend to build

Circle ci config example is added, once it fully configured add a badge to the readme to indicate passing:

```
[![CircleCI](https://circleci.com/gh/yourname/yourapp.svg?style=shield&circle)](https://circleci.com/gh/yourname/yourapp)
```

## Tests and coverage

The ci will run coverage and  upload a report to http://codecov.io/ if you configure the token in circle/config.yml or .github/workflows/main.yml

Add a github secret for your coverage token secrets.CODE_COV_KEY

## Publishing to PYPI

To package your app for pypi you will need twine:
```
pip install twine
```
Then run the following:

```
python setup.py sdist bdist_wheel
```

You should now have a dist/ directory:

```
twine check dist/*
```

Watch out for:

```
Checking distribution dist/PACKAGE-NAME-VERSION.tar.gz: warning: `long_description_content_type` missing.  defaulting to `text/x-rst`.
Failed

The project's long_description has invalid markup which will not be rendered on PyPI. The following syntax errors were detected:
line 18: Warning: Inline literal start-string without end-string.
```
That's ok. twine has an issue with markdown

Get an account on https://test.pypi.org and https://pypi.org

Then run

```
twine upload --repository-url https://test.pypi.org/legacy/ dist/* * to safely check your package twine upload dist/* -- when ready to publish
```
or

``` twine upload dist/*```

:tada: