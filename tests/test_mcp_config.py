"""Tests for MCP configuration in .mcp.json file."""

import json
import pytest
from pathlib import Path


class TestMcpServerCount:
    """Verify MCP server configuration."""

    def test_mcp_json_has_exactly_18_servers(self, plugin_root):
        """.mcp.json should have exactly 18 MCP servers."""
        mcp_json = plugin_root / ".mcp.json"
        with open(mcp_json) as f:
            data = json.load(f)

        server_count = len(data["mcpServers"])
        assert server_count == 18, (
            f"Expected 18 MCP servers, found {server_count}. "
            f"Servers: {list(data['mcpServers'].keys())}"
        )


class TestMcpServerStructure:
    """Verify each server entry has required fields and valid URLs."""

    def test_all_servers_have_type_and_url(self, plugin_root):
        """All server entries should have 'type' and 'url' keys."""
        mcp_json = plugin_root / ".mcp.json"
        with open(mcp_json) as f:
            data = json.load(f)

        servers = data["mcpServers"]
        missing_fields = []

        for server_name, server_config in servers.items():
            if "type" not in server_config:
                missing_fields.append(f"{server_name}: missing 'type'")
            if "url" not in server_config:
                missing_fields.append(f"{server_name}: missing 'url'")

        assert not missing_fields, f"Found missing fields: {missing_fields}"

    def test_all_urls_use_https(self, plugin_root):
        """All server URLs should start with https://."""
        mcp_json = plugin_root / ".mcp.json"
        with open(mcp_json) as f:
            data = json.load(f)

        servers = data["mcpServers"]
        non_https_urls = []

        for server_name, server_config in servers.items():
            url = server_config.get("url", "")
            if not url.startswith("https://"):
                non_https_urls.append(f"{server_name}: {url}")

        assert not non_https_urls, (
            f"Found non-HTTPS URLs: {non_https_urls}"
        )


class TestRequiredServers:
    """Verify required MCP servers are configured."""

    @pytest.mark.parametrize(
        "required_server",
        ["github", "slack", "notion", "figma", "tavily", "consensus"],
    )
    def test_required_server_exists(self, plugin_root, required_server):
        """Required servers should be present in .mcp.json."""
        mcp_json = plugin_root / ".mcp.json"
        with open(mcp_json) as f:
            data = json.load(f)

        servers = data["mcpServers"]
        assert required_server in servers, (
            f"Required server '{required_server}' not found in .mcp.json. "
            f"Available servers: {list(servers.keys())}"
        )


class TestMcpServerDetails:
    """Verify specific server configuration details."""

    def test_github_server_configured(self, plugin_root):
        """GitHub server should be properly configured."""
        mcp_json = plugin_root / ".mcp.json"
        with open(mcp_json) as f:
            data = json.load(f)

        github = data["mcpServers"].get("github", {})
        assert github.get("type") is not None, "GitHub server missing 'type'"
        assert github.get("url", "").startswith("https://"), "GitHub URL should use HTTPS"

    def test_slack_server_configured(self, plugin_root):
        """Slack server should be properly configured."""
        mcp_json = plugin_root / ".mcp.json"
        with open(mcp_json) as f:
            data = json.load(f)

        slack = data["mcpServers"].get("slack", {})
        assert slack.get("type") is not None, "Slack server missing 'type'"
        assert slack.get("url", "").startswith("https://"), "Slack URL should use HTTPS"

    def test_notion_server_configured(self, plugin_root):
        """Notion server should be properly configured."""
        mcp_json = plugin_root / ".mcp.json"
        with open(mcp_json) as f:
            data = json.load(f)

        notion = data["mcpServers"].get("notion", {})
        assert notion.get("type") is not None, "Notion server missing 'type'"
        assert notion.get("url", "").startswith("https://"), "Notion URL should use HTTPS"

    def test_figma_server_configured(self, plugin_root):
        """Figma server should be properly configured."""
        mcp_json = plugin_root / ".mcp.json"
        with open(mcp_json) as f:
            data = json.load(f)

        figma = data["mcpServers"].get("figma", {})
        assert figma.get("type") is not None, "Figma server missing 'type'"
        assert figma.get("url", "").startswith("https://"), "Figma URL should use HTTPS"

    def test_tavily_server_configured(self, plugin_root):
        """Tavily server should be properly configured."""
        mcp_json = plugin_root / ".mcp.json"
        with open(mcp_json) as f:
            data = json.load(f)

        tavily = data["mcpServers"].get("tavily", {})
        assert tavily.get("type") is not None, "Tavily server missing 'type'"
        assert tavily.get("url", "").startswith("https://"), "Tavily URL should use HTTPS"

    def test_consensus_server_configured(self, plugin_root):
        """Consensus server should be properly configured."""
        mcp_json = plugin_root / ".mcp.json"
        with open(mcp_json) as f:
            data = json.load(f)

        consensus = data["mcpServers"].get("consensus", {})
        assert consensus.get("type") is not None, "Consensus server missing 'type'"
        assert consensus.get("url", "").startswith("https://"), "Consensus URL should use HTTPS"
