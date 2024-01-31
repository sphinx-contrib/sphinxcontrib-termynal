"""The init file of the extension.

This is where the extension is loaded and the sphinx builder is extended.
"""
from __future__ import annotations

from typing import Any, Dict

from sphinx.application import Sphinx

from .demo_directive import DemoDirective
from .demo_role import _NODE_VISITORS, DemoRole, demo_node

__version__ = "0.0.0"
__author__ = "Pierrick Rambaud"
__email__ = "pierrick.rambaud49@gmail.com"


def setup(app: Sphinx) -> Dict[str, Any]:
    """Add icon node to the sphinx builder."""
    # add the node and role to the sphinx builder
    app.add_node(demo_node, **_NODE_VISITORS)  # type: ignore
    app.add_role("demo-role", DemoRole())

    # add the directive to the sphinx builder
    app.add_directive("demo-directive", DemoDirective)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
