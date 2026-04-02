"""Tests for content quality rules: no emojis, frontmatter, required sections."""

import pytest
import re
from pathlib import Path


def has_emoji(text):
    """Check if text contains emoji characters."""
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002702-\U000027B0"  # dingbats
        "\U000024C2-\U0001F251"  # enclosed characters
        "\U0001f926-\U0001f937"  # hand gestures
        "\U00010000-\U0010ffff"  # other unicode
        "\u2640-\u2642"  # gender
        "\u2600-\u2B55"  # emoticons
        "\u200d"  # zero-width joiner
        "\u23cf"  # display symbols
        "\u23e9"  # display symbols
        "\u231a"  # display symbols
        "\ufe0f"  # dingbats
        "\u3030"  # dingbats
        "]+"
    )
    return bool(emoji_pattern.search(text))


class TestNoEmojisInFiles:
    """Verify no emoji characters in markdown, JSON, or Python files."""

    def test_no_emojis_in_md_files(self, all_md_files, plugin_root):
        """No .md files should contain emoji characters (excluding examples/)."""
        files_with_emojis = []
        for md_file in all_md_files:
            # Skip example files as they demonstrate output format
            if "examples" in md_file.parts:
                continue
            with open(md_file, encoding="utf-8") as f:
                content = f.read()
            if has_emoji(content):
                files_with_emojis.append(md_file.relative_to(plugin_root))

        assert not files_with_emojis, (
            f"Found emojis in {len(files_with_emojis)} .md files: {files_with_emojis}"
        )

    def test_no_emojis_in_json_files(self, plugin_root):
        """No .json files should contain emoji characters (excluding node_modules)."""
        json_files = [
            p for p in plugin_root.rglob("*.json")
            if "node_modules" not in p.parts
        ]
        files_with_emojis = []

        for json_file in json_files:
            with open(json_file, encoding="utf-8") as f:
                content = f.read()
            if has_emoji(content):
                files_with_emojis.append(json_file.relative_to(plugin_root))

        assert not files_with_emojis, (
            f"Found emojis in {len(files_with_emojis)} .json files: {files_with_emojis}"
        )

    def test_no_emojis_in_python_files(self, plugin_root):
        """No .py files should contain emoji characters (excluding node_modules)."""
        py_files = [p for p in plugin_root.rglob("*.py") if "node_modules" not in p.parts]
        files_with_emojis = []

        for py_file in py_files:
            with open(py_file, encoding="utf-8") as f:
                content = f.read()
            if has_emoji(content):
                files_with_emojis.append(py_file.relative_to(plugin_root))

        assert not files_with_emojis, (
            f"Found emojis in {len(files_with_emojis)} .py files: {files_with_emojis}"
        )


class TestYamlFrontmatter:
    """Verify all content files have proper YAML frontmatter."""

    def test_skill_files_have_frontmatter(self, all_skill_files):
        """All SKILL.md files should start with YAML frontmatter (---)."""
        files_without_frontmatter = []

        for skill_file in all_skill_files:
            with open(skill_file, encoding="utf-8") as f:
                content = f.read()
            if not content.strip().startswith("---"):
                files_without_frontmatter.append(skill_file.name)

        assert not files_without_frontmatter, (
            f"SKILL.md files missing frontmatter: {files_without_frontmatter}"
        )

    def test_command_files_have_frontmatter(self, all_command_files):
        """All command .md files should start with YAML frontmatter (---)."""
        files_without_frontmatter = []

        for cmd_file in all_command_files:
            with open(cmd_file, encoding="utf-8") as f:
                content = f.read()
            if not content.strip().startswith("---"):
                files_without_frontmatter.append(cmd_file.name)

        assert not files_without_frontmatter, (
            f"Command files missing frontmatter: {files_without_frontmatter}"
        )

    def test_agent_files_have_frontmatter(self, all_agent_files):
        """All agent .md files should start with YAML frontmatter (---)."""
        files_without_frontmatter = []

        for agent_file in all_agent_files:
            with open(agent_file, encoding="utf-8") as f:
                content = f.read()
            if not content.strip().startswith("---"):
                files_without_frontmatter.append(agent_file.name)

        assert not files_without_frontmatter, (
            f"Agent files missing frontmatter: {files_without_frontmatter}"
        )


class TestRequiredSections:
    """Verify required sections in content files."""

    def test_all_commands_have_output_format(self, all_command_files):
        """All 12 command files must contain '## Output Format' section."""
        files_missing_section = []

        for cmd_file in all_command_files:
            with open(cmd_file, encoding="utf-8") as f:
                content = f.read()
            if "## Output Format" not in content:
                files_missing_section.append(cmd_file.name)

        assert not files_missing_section, (
            f"Command files missing '## Output Format': {files_missing_section}"
        )

    def test_computational_workflows_in_skills(self, all_skill_files):
        """At least 25 SKILL.md files should contain '## Computational Workflows'."""
        files_with_section = []

        for skill_file in all_skill_files:
            with open(skill_file, encoding="utf-8") as f:
                content = f.read()
            if "## Computational Workflows" in content:
                files_with_section.append(skill_file.parent.name)

        assert len(files_with_section) >= 25, (
            f"Expected at least 25 skills with '## Computational Workflows', "
            f"found {len(files_with_section)}: {files_with_section}"
        )


class TestSpecialFiles:
    """Verify special template and style guide files."""

    def test_scientific_style_guide_exists(self, plugin_root):
        """scientific-style-guide.md should exist."""
        file_path = plugin_root / "skills" / "output-formats" / "references" / "scientific-style-guide.md"
        assert file_path.exists(), f"scientific-style-guide.md not found at {file_path}"

    def test_scientific_style_guide_has_content(self, plugin_root):
        """scientific-style-guide.md should have content."""
        file_path = plugin_root / "skills" / "output-formats" / "references" / "scientific-style-guide.md"
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
        assert len(content.strip()) > 100, "scientific-style-guide.md is too short"

    def test_web_output_template_exists(self, plugin_root):
        """web-output-template.jsx should exist."""
        file_path = plugin_root / "skills" / "output-formats" / "references" / "web-output-template.jsx"
        assert file_path.exists(), f"web-output-template.jsx not found at {file_path}"

    def test_web_output_template_has_content(self, plugin_root):
        """web-output-template.jsx should have content."""
        file_path = plugin_root / "skills" / "output-formats" / "references" / "web-output-template.jsx"
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
        assert len(content.strip()) > 100, "web-output-template.jsx is too short"
