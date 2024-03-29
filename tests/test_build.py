"""Test sphinxcontrib.termynal extension."""
import pytest
from bs4 import BeautifulSoup, formatter

# this formatting specification is build to align with prettier
# without it all your regression will be modified by commit hooks
# and fail in your CI
fmt = formatter.HTMLFormatter(indent=2, void_element_close_prefix=" /")


# explore the warnings of the build to check if the latex node is skipped
@pytest.mark.sphinx("epub", testroot="role")
def test_role_epub(app, status, warning):
    app.builder.build_all()
    assert "Unsupported output format (node skipped)" in warning.getvalue()


# use beautifulsoup to parse the html output and data_regression to save a snapshot
# of the desired output. it's the most elegant way we found to check sphinx outputs
# open an issue if you want to propose a better one.
@pytest.mark.sphinx("html", testroot="role")
def test_role_html(app, status, warning, file_regression):
    app.builder.build_all()
    html = (app.outdir / "index.html").read_text(encoding="utf8")
    html = BeautifulSoup(html, "html.parser")
    role = html.select("b.demo")[0].prettify(formatter=fmt)
    file_regression.check(role, extension=".html")


@pytest.mark.sphinx("html", testroot="directive")
def test_directive_html(app, status, warning, file_regression):
    app.builder.build_all()
    html = (app.outdir / "index.html").read_text(encoding="utf8")
    html = BeautifulSoup(html, "html.parser")
    role = html.select("div.demo-directive")[0].prettify(formatter=fmt)
    file_regression.check(role, extension=".html")
