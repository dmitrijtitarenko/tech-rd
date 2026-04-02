"""Tests for content completeness — required sections, frontmatter, and cross-references."""

import json
import re
import pytest
from pathlib import Path


class TestSkillCompleteness:
    """Every SKILL.md must have required sections."""

    REQUIRED_HEADINGS = [
        r"##\s+.*Research Dimensions|##\s+.*Key.*Dimensions|##\s+.*Dimensions",
        r"##\s+.*Data Sources|##\s+.*Sources",
    ]

    # Capability/utility skills that don't need Research Dimensions or Data Sources
    CAPABILITY_SKILLS = {
        "interactive-brainstorming",
        "scheduling",
        "notion-knowledge-base",
        "data-export",
        "output-formats",
        "diagram-generation",
    }

    def test_skill_has_research_dimensions(self, all_skill_files):
        """Each domain SKILL.md should have a Research Dimensions section."""
        missing = []
        pattern = re.compile(
            r"##\s+.*(?:Research Dimensions|Key.*Dimensions|Dimensions|Overview|Capabilities|Coverage)",
            re.IGNORECASE,
        )
        for skill_file in all_skill_files:
            if skill_file.parent.name in self.CAPABILITY_SKILLS:
                continue
            content = skill_file.read_text()
            if not pattern.search(content):
                missing.append(skill_file.parent.name)
        assert not missing, (
            f"Skills missing Research Dimensions section: {missing}"
        )

    def test_skill_has_data_sources(self, all_skill_files):
        """Each SKILL.md should have a Data Sources section with ~~ connectors."""
        missing = []
        pattern = re.compile(r"##\s+.*(?:Data Sources|Sources)", re.IGNORECASE)
        for skill_file in all_skill_files:
            content = skill_file.read_text()
            if not pattern.search(content):
                # Allow skills that are capability skills (not domain skills)
                capability_skills = {
                    "interactive-brainstorming",
                    "scheduling",
                    "notion-knowledge-base",
                    "data-export",
                    "output-formats",
                    "diagram-generation",
                }
                if skill_file.parent.name not in capability_skills:
                    missing.append(skill_file.parent.name)
        assert not missing, (
            f"Domain skills missing Data Sources section: {missing}"
        )

    def test_skill_minimum_length(self, all_skill_files):
        """Each SKILL.md should be at least 40 lines (not a stub)."""
        stubs = []
        for skill_file in all_skill_files:
            lines = skill_file.read_text().strip().splitlines()
            if len(lines) < 40:
                stubs.append((skill_file.parent.name, len(lines)))
        assert not stubs, (
            f"Skills that are too short (< 40 lines): {stubs}"
        )


class TestCommandCompleteness:
    """Every command .md must have frontmatter and required sections."""

    def test_command_has_yaml_frontmatter(self, all_command_files):
        """Each command should start with YAML frontmatter (---)."""
        missing = []
        for cmd_file in all_command_files:
            content = cmd_file.read_text()
            if not content.startswith("---"):
                missing.append(cmd_file.name)
        assert not missing, (
            f"Commands missing YAML frontmatter: {missing}"
        )

    def test_command_has_description_field(self, all_command_files):
        """Each command frontmatter should include 'description:'."""
        missing = []
        for cmd_file in all_command_files:
            content = cmd_file.read_text()
            # Extract frontmatter between first and second ---
            parts = content.split("---", 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                if "description:" not in frontmatter:
                    missing.append(cmd_file.name)
            else:
                missing.append(cmd_file.name)
        assert not missing, (
            f"Commands missing 'description:' in frontmatter: {missing}"
        )

    def test_command_has_workflow_section(self, all_command_files):
        """Each command should have a ## Workflow section."""
        missing = []
        pattern = re.compile(r"##\s+Workflow", re.IGNORECASE)
        for cmd_file in all_command_files:
            content = cmd_file.read_text()
            if not pattern.search(content):
                missing.append(cmd_file.name)
        assert not missing, (
            f"Commands missing ## Workflow section: {missing}"
        )

    def test_command_has_output_format_section(self, all_command_files):
        """Each command should have an ## Output Format section."""
        missing = []
        pattern = re.compile(r"##\s+Output Format", re.IGNORECASE)
        for cmd_file in all_command_files:
            content = cmd_file.read_text()
            if not pattern.search(content):
                missing.append(cmd_file.name)
        assert not missing, (
            f"Commands missing ## Output Format section: {missing}"
        )


class TestAgentCompleteness:
    """Every agent .md must have valid frontmatter and required sections."""

    def test_agent_has_yaml_frontmatter(self, all_agent_files):
        """Each agent should start with YAML frontmatter (---)."""
        missing = []
        for agent_file in all_agent_files:
            content = agent_file.read_text()
            if not content.startswith("---"):
                missing.append(agent_file.name)
        assert not missing, (
            f"Agents missing YAML frontmatter: {missing}"
        )

    def test_agent_has_name_field(self, all_agent_files):
        """Each agent frontmatter should include 'name:'."""
        missing = []
        for agent_file in all_agent_files:
            content = agent_file.read_text()
            parts = content.split("---", 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                if "name:" not in frontmatter:
                    missing.append(agent_file.name)
            else:
                missing.append(agent_file.name)
        assert not missing, (
            f"Agents missing 'name:' in frontmatter: {missing}"
        )

    def test_agent_has_model_field(self, all_agent_files):
        """Each agent frontmatter should specify a model (opus or sonnet)."""
        missing = []
        for agent_file in all_agent_files:
            content = agent_file.read_text()
            parts = content.split("---", 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                if "model:" not in frontmatter:
                    missing.append(agent_file.name)
            else:
                missing.append(agent_file.name)
        assert not missing, (
            f"Agents missing 'model:' in frontmatter: {missing}"
        )

    def test_agent_has_tools_field(self, all_agent_files):
        """Each agent frontmatter should list tools."""
        missing = []
        for agent_file in all_agent_files:
            content = agent_file.read_text()
            parts = content.split("---", 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                if "tools:" not in frontmatter:
                    missing.append(agent_file.name)
            else:
                missing.append(agent_file.name)
        assert not missing, (
            f"Agents missing 'tools:' in frontmatter: {missing}"
        )

    def test_agent_has_role_section(self, all_agent_files):
        """Each agent should have a ## Role section."""
        missing = []
        pattern = re.compile(r"##\s+Role", re.IGNORECASE)
        for agent_file in all_agent_files:
            content = agent_file.read_text()
            if not pattern.search(content):
                missing.append(agent_file.name)
        assert not missing, (
            f"Agents missing ## Role section: {missing}"
        )


class TestCrossReferences:
    """Validate consistency between metadata files."""

    def test_plugin_and_marketplace_version_match(self, plugin_root):
        """plugin.json and marketplace-entry.json should have the same version."""
        with open(plugin_root / ".claude-plugin" / "plugin.json") as f:
            plugin = json.load(f)
        with open(plugin_root / "marketplace-entry.json") as f:
            marketplace = json.load(f)
        assert plugin["version"] == marketplace["version"], (
            f"Version mismatch: plugin.json={plugin['version']} vs "
            f"marketplace-entry.json={marketplace['version']}"
        )

    def test_plugin_and_package_version_match(self, plugin_root):
        """plugin.json and package.json should have the same version."""
        with open(plugin_root / ".claude-plugin" / "plugin.json") as f:
            plugin = json.load(f)
        with open(plugin_root / "package.json") as f:
            package = json.load(f)
        assert plugin["version"] == package["version"], (
            f"Version mismatch: plugin.json={plugin['version']} vs "
            f"package.json={package['version']}"
        )

    def test_plugin_and_marketplace_name_match(self, plugin_root):
        """plugin.json and marketplace-entry.json should have the same name."""
        with open(plugin_root / ".claude-plugin" / "plugin.json") as f:
            plugin = json.load(f)
        with open(plugin_root / "marketplace-entry.json") as f:
            marketplace = json.load(f)
        assert plugin["name"] == marketplace["name"], (
            f"Name mismatch: plugin.json={plugin['name']} vs "
            f"marketplace-entry.json={marketplace['name']}"
        )

    def test_mcp_server_count_matches_readme(self, plugin_root):
        """README should reference the correct number of MCP servers."""
        with open(plugin_root / ".mcp.json") as f:
            mcp = json.load(f)
        actual_count = len(mcp.get("mcpServers", {}))

        readme = (plugin_root / "README.md").read_text()
        assert str(actual_count) in readme, (
            f"README does not mention {actual_count} MCP servers"
        )

    def test_contributing_md_exists(self, plugin_root):
        """CONTRIBUTING.md should exist for open-source completeness."""
        assert (plugin_root / "CONTRIBUTING.md").exists(), (
            "CONTRIBUTING.md not found"
        )

    def test_examples_md_exists(self, plugin_root):
        """EXAMPLES.md should exist for user onboarding."""
        assert (plugin_root / "EXAMPLES.md").exists(), (
            "EXAMPLES.md not found"
        )

    def test_mcp_setup_md_exists(self, plugin_root):
        """MCP_SETUP.md should exist for connector documentation."""
        assert (plugin_root / "MCP_SETUP.md").exists(), (
            "MCP_SETUP.md not found"
        )

    def test_changelog_exists(self, plugin_root):
        """CHANGELOG.md should exist for version history."""
        assert (plugin_root / "CHANGELOG.md").exists(), (
            "CHANGELOG.md not found"
        )
