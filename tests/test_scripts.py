"""Tests for Python scripts in scripts/ directory."""

import pytest
import py_compile
import importlib.util
from pathlib import Path


class TestScriptSyntax:
    """Verify all Python scripts compile without syntax errors."""

    def get_script_files(self, plugin_root):
        """Get all .py files from scripts/ directory."""
        scripts_dir = plugin_root / "scripts"
        return sorted(scripts_dir.glob("*.py"))

    def test_scripts_directory_exists(self, plugin_root):
        """scripts/ directory should exist."""
        scripts_dir = plugin_root / "scripts"
        assert scripts_dir.is_dir(), "scripts/ directory not found"

    @pytest.mark.parametrize(
        "script_file",
        [
            pytest.param(f, id=f.name)
            for f in (Path(__file__).parent.parent / "scripts").glob("*.py")
        ],
    )
    def test_script_compiles(self, script_file):
        """Each .py file should compile without syntax errors."""
        try:
            py_compile.compile(str(script_file), doraise=True)
        except py_compile.PyCompileError as e:
            pytest.fail(f"{script_file.name} has syntax errors: {e}")


class TestScriptDocstrings:
    """Verify all Python scripts have module docstrings."""

    @pytest.mark.parametrize(
        "script_file",
        [
            pytest.param(f, id=f.name)
            for f in (Path(__file__).parent.parent / "scripts").glob("*.py")
        ],
    )
    def test_script_has_docstring(self, script_file):
        """Each .py file should have a module docstring."""
        with open(script_file, encoding="utf-8") as f:
            content = f.read()

        # Check for docstring (triple quotes at beginning or after shebang)
        lines = content.split("\n")
        in_shebang_or_encoding = True
        found_docstring = False

        for line in lines:
            stripped = line.strip()

            # Skip shebang and encoding declarations
            if in_shebang_or_encoding:
                if stripped.startswith("#!") or stripped.startswith("# -*-") or stripped.startswith("# coding"):
                    continue
                else:
                    in_shebang_or_encoding = False

            # Look for docstring (triple quotes)
            if '"""' in stripped or "'''" in stripped:
                found_docstring = True
                break

        assert found_docstring, f"{script_file.name} missing module docstring"


class TestScriptMainBlock:
    """Verify all Python scripts have if __name__ == '__main__' block."""

    @pytest.mark.parametrize(
        "script_file",
        [
            pytest.param(f, id=f.name)
            for f in (Path(__file__).parent.parent / "scripts").glob("*.py")
        ],
    )
    def test_script_has_main_block(self, script_file):
        """Each .py file should have if __name__ == '__main__' block."""
        with open(script_file, encoding="utf-8") as f:
            content = f.read()

        assert 'if __name__ == "__main__"' in content, (
            f"{script_file.name} missing main block"
        )


class TestScriptImports:
    """Verify all Python scripts can be imported without errors."""

    @pytest.mark.parametrize(
        "script_file",
        [
            pytest.param(f, id=f.name)
            for f in (Path(__file__).parent.parent / "scripts").glob("*.py")
        ],
    )
    def test_script_imports_successfully(self, script_file):
        """Each .py file should import without errors."""
        spec = importlib.util.spec_from_file_location(script_file.stem, script_file)
        module = importlib.util.module_from_spec(spec)

        try:
            spec.loader.exec_module(module)
        except Exception as e:
            pytest.fail(f"{script_file.name} failed to import: {e}")
