"""Demonstration of a custom directive for sphinx.

This directive should be deleted when starting a new extension but it gives an overview
of the different steps to follow to create a new directive. It is also used to demonstrate the
documentation/test workflows.

.. note::

    We only coded a html output for this directive.
"""
from __future__ import annotations

from typing import List

from docutils import nodes
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective

logger = logging.getLogger(__name__)


class DemoDirective(SphinxDirective):
    """A demo directive simply setting the text in bold."""

    arguments = 1
    final_argument_whitespace = False
    has_content = True

    def run(self) -> List[nodes.Node]:
        """Create the demo directive output."""
        text = self.content[0].strip()
        out = f'<div class="demo-directive"><b>{text}</b></div>'
        return [nodes.raw("", out, format="html")]
