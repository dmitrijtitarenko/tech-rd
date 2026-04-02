"""Shared pytest fixtures for tech-rd plugin tests."""

import pytest
from pathlib import Path


@pytest.fixture
def plugin_root():
    """Path to the tech-rd plugin root directory."""
    return Path(__file__).parent.parent


@pytest.fixture
def all_md_files(plugin_root):
    """List of all .md files in the plugin (excluding node_modules)."""
    return sorted(
        p for p in plugin_root.rglob("*.md")
        if "node_modules" not in p.parts
    )


@pytest.fixture
def all_skill_files(plugin_root):
    """List of all SKILL.md files in skills/."""
    return sorted((plugin_root / "skills").rglob("SKILL.md"))


@pytest.fixture
def all_command_files(plugin_root):
    """List of all command .md files in commands/."""
    return sorted((plugin_root / "commands").glob("*.md"))


@pytest.fixture
def all_agent_files(plugin_root):
    """List of all agent .md files in agents/."""
    return sorted((plugin_root / "agents").glob("*.md"))
