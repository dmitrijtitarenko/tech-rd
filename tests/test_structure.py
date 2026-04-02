"""Tests for tech-rd plugin file structure and required files."""

import json
import pytest
from pathlib import Path


class TestPluginJsonStructure:
    """Validate plugin.json file structure and required fields."""

    def test_plugin_json_exists_in_claude_plugin(self, plugin_root):
        """plugin.json should exist in .claude-plugin/."""
        plugin_json = plugin_root / ".claude-plugin" / "plugin.json"
        assert plugin_json.exists(), "plugin.json not found in .claude-plugin/"

    def test_plugin_json_valid_json(self, plugin_root):
        """plugin.json should be valid JSON."""
        plugin_json = plugin_root / ".claude-plugin" / "plugin.json"
        with open(plugin_json) as f:
            data = json.load(f)
        assert isinstance(data, dict), "plugin.json should be a JSON object"

    def test_plugin_json_required_fields(self, plugin_root):
        """plugin.json should have all required fields."""
        plugin_json = plugin_root / ".claude-plugin" / "plugin.json"
        with open(plugin_json) as f:
            data = json.load(f)

        required_fields = {"name", "version", "description", "author", "license"}
        missing = required_fields - set(data.keys())
        assert not missing, f"Missing required fields: {missing}"


class TestMcpJsonStructure:
    """Validate .mcp.json file structure."""

    def test_mcp_json_exists(self, plugin_root):
        """`.mcp.json should exist at plugin root."""
        mcp_json = plugin_root / ".mcp.json"
        assert mcp_json.exists(), ".mcp.json not found at plugin root"

    def test_mcp_json_valid_json(self, plugin_root):
        """.mcp.json should be valid JSON."""
        mcp_json = plugin_root / ".mcp.json"
        with open(mcp_json) as f:
            data = json.load(f)
        assert isinstance(data, dict), ".mcp.json should be a JSON object"

    def test_mcp_json_has_mcp_servers(self, plugin_root):
        """.mcp.json should have mcpServers key."""
        mcp_json = plugin_root / ".mcp.json"
        with open(mcp_json) as f:
            data = json.load(f)
        assert "mcpServers" in data, ".mcp.json missing 'mcpServers' key"


class TestDirectoryStructure:
    """Validate required directories and their contents."""

    def test_agents_directory_exists(self, plugin_root):
        """agents/ directory should exist."""
        agents_dir = plugin_root / "agents"
        assert agents_dir.is_dir(), "agents/ directory not found"

    def test_five_agent_files_exist(self, all_agent_files):
        """Exactly 5 agent files should exist in agents/."""
        assert len(all_agent_files) == 5, (
            f"Expected 5 agent files, found {len(all_agent_files)}: "
            f"{[f.name for f in all_agent_files]}"
        )

    def test_commands_directory_exists(self, plugin_root):
        """commands/ directory should exist."""
        commands_dir = plugin_root / "commands"
        assert commands_dir.is_dir(), "commands/ directory not found"

    def test_twelve_command_files_exist(self, all_command_files):
        """Exactly 12 command files should exist in commands/."""
        assert len(all_command_files) == 12, (
            f"Expected 12 command files, found {len(all_command_files)}: "
            f"{[f.name for f in all_command_files]}"
        )

    def test_skills_directory_exists(self, plugin_root):
        """skills/ directory should exist."""
        skills_dir = plugin_root / "skills"
        assert skills_dir.is_dir(), "skills/ directory not found"

    def test_skill_md_files_exist(self, all_skill_files):
        """All SKILL.md files should exist (37 total)."""
        expected_count = 37
        assert len(all_skill_files) == expected_count, (
            f"Expected {expected_count} SKILL.md files, found {len(all_skill_files)}"
        )

    def test_examples_directory_exists(self, plugin_root):
        """examples/ directory should exist."""
        examples_dir = plugin_root / "examples"
        assert examples_dir.is_dir(), "examples/ directory not found"

    def test_examples_has_minimum_files(self, plugin_root):
        """examples/ should have at least 10 files."""
        examples_dir = plugin_root / "examples"
        example_files = list(examples_dir.glob("*"))
        assert len(example_files) >= 10, (
            f"Expected at least 10 files in examples/, found {len(example_files)}"
        )


class TestRequiredFiles:
    """Validate required standalone files."""

    def test_marketplace_entry_json_exists(self, plugin_root):
        """marketplace-entry.json should exist at root."""
        file_path = plugin_root / "marketplace-entry.json"
        assert file_path.exists(), "marketplace-entry.json not found"

    def test_marketplace_entry_valid_json(self, plugin_root):
        """marketplace-entry.json should be valid JSON with required fields."""
        file_path = plugin_root / "marketplace-entry.json"
        with open(file_path) as f:
            data = json.load(f)

        required_fields = {"name", "version", "description", "author", "license"}
        missing = required_fields - set(data.keys())
        assert not missing, f"marketplace-entry.json missing: {missing}"

    def test_readme_exists(self, plugin_root):
        """README.md should exist at root."""
        readme = plugin_root / "README.md"
        assert readme.exists(), "README.md not found"

    def test_readme_nonempty(self, plugin_root):
        """README.md should be non-empty."""
        readme = plugin_root / "README.md"
        with open(readme) as f:
            content = f.read()
        assert len(content.strip()) > 0, "README.md is empty"

    def test_license_exists(self, plugin_root):
        """LICENSE file should exist at root."""
        license_file = plugin_root / "LICENSE"
        assert license_file.exists(), "LICENSE file not found"

    def test_connectors_md_exists(self, plugin_root):
        """CONNECTORS.md should exist at root."""
        connectors = plugin_root / "CONNECTORS.md"
        assert connectors.exists(), "CONNECTORS.md not found"


class TestSkillNames:
    """Verify all expected skill directories and SKILL.md files exist."""

    @pytest.mark.parametrize(
        "skill_name",
        [
            "ai-ml-research",
            "api-ecosystem",
            "architecture-patterns",
            "biotech-healthtech",
            "blockchain-web3",
            "cloud-infrastructure",
            "competitive-intelligence",
            "cost-optimization",
            "cybersecurity",
            "data-engineering",
            "data-export",
            "database-technologies",
            "developer-experience",
            "devops-sre",
            "diagram-generation",
            "edtech",
            "fintech",
            "graphics-3d-xr",
            "hardware-iot-robotics",
            "interactive-brainstorming",
            "lowcode-nocode",
            "miltech-govtech",
            "networking-telecom",
            "notion-knowledge-base",
            "observability",
            "oss-intelligence",
            "output-formats",
            "patent-landscape",
            "programming-languages",
            "quantum-computing",
            "regtech-compliance",
            "scheduling",
            "software-engineering",
            "standards-tracker",
            "tech-due-diligence",
            "tech-radar",
            "tech-trend-synthesis",
        ],
    )
    def test_skill_directories_and_files(self, plugin_root, skill_name):
        """Each skill should have a directory with SKILL.md file."""
        skill_dir = plugin_root / "skills" / skill_name
        assert skill_dir.is_dir(), f"Skill directory not found: {skill_name}"

        skill_file = skill_dir / "SKILL.md"
        assert skill_file.exists(), f"SKILL.md not found for skill: {skill_name}"
