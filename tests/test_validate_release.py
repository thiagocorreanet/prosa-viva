import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class ReleaseValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name) / "prosa-viva"

        self._write_json(
            ".codex-plugin/plugin.json",
            {
                "name": "prosa-viva",
                "version": "0.1.0",
                "description": "Revisa prosa em pt-BR.",
                "author": {
                    "name": "Thiago Corrêa",
                    "url": "https://github.com/thiagocorreanet",
                },
                "homepage": "https://github.com/thiagocorreanet/prosa-viva",
                "repository": "https://github.com/thiagocorreanet/prosa-viva",
                "license": "MIT",
                "skills": "./skills/",
                "interface": {
                    "displayName": "Prosa Viva",
                    "shortDescription": "Refina prosa em pt-BR",
                    "longDescription": "Revisa prosa sem alterar os fatos.",
                    "developerName": "Thiago Corrêa",
                    "category": "Productivity",
                    "capabilities": ["Write"],
                    "websiteURL": "https://github.com/thiagocorreanet/prosa-viva",
                    "defaultPrompt": ["Use $refinar-prosa para revisar este texto."],
                },
            },
        )
        self._write_json(
            ".agents/plugins/marketplace.json",
            {
                "name": "prosa-viva",
                "interface": {"displayName": "Prosa Viva"},
                "plugins": [
                    {
                        "name": "prosa-viva",
                        "source": {
                            "source": "url",
                            "url": "https://github.com/thiagocorreanet/prosa-viva.git",
                            "ref": "v0.1.0",
                        },
                        "policy": {
                            "installation": "AVAILABLE",
                            "authentication": "ON_INSTALL",
                        },
                        "category": "Productivity",
                    }
                ],
            },
        )
        self._write(
            "LICENSE",
            "MIT License\n\nCopyright (c) 2026 Thiago Corrêa\n",
        )
        self._write("README.md", "# Prosa Viva\n")
        self._write(
            "skills/refinar-prosa/SKILL.md",
            "---\nname: refinar-prosa\ndescription: Revisa prosa.\n---\n",
        )
        self._write(
            "skills/refinar-prosa/agents/openai.yaml",
            'interface:\n  display_name: "Refinar prosa"\n',
        )
        self._write("docs/releases/v0.1.0.md", "# Prosa Viva v0.1.0\n")

    def _write(self, relative_path: str, content: str) -> None:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def _write_json(self, relative_path: str, payload: object) -> None:
        self._write(relative_path, json.dumps(payload, ensure_ascii=False, indent=2))

    def _read_json(self, relative_path: str) -> dict:
        return json.loads((self.root / relative_path).read_text(encoding="utf-8"))

    def test_accepts_a_complete_public_release(self):
        from scripts.validate_release import validate_release

        self.assertEqual(
            validate_release(self.root, "v0.1.0"),
            ("plugin=prosa-viva", "version=0.1.0", "release=v0.1.0"),
        )

    def test_rejects_tag_that_differs_from_manifest_version(self):
        from scripts.validate_release import validate_release

        with self.assertRaisesRegex(ValueError, "tag"):
            validate_release(self.root, "v0.1.1")

    def test_rejects_public_version_with_cachebuster(self):
        from scripts.validate_release import validate_release

        manifest = self._read_json(".codex-plugin/plugin.json")
        manifest["version"] = "0.1.0+codex.local-test"
        self._write_json(".codex-plugin/plugin.json", manifest)

        with self.assertRaisesRegex(ValueError, "cachebuster"):
            validate_release(self.root)

    def test_rejects_marketplace_ref_that_differs_from_version(self):
        from scripts.validate_release import validate_release

        marketplace = self._read_json(".agents/plugins/marketplace.json")
        marketplace["plugins"][0]["source"]["ref"] = "v0.1.1"
        self._write_json(".agents/plugins/marketplace.json", marketplace)

        with self.assertRaisesRegex(ValueError, "marketplace"):
            validate_release(self.root)

    def test_rejects_missing_license(self):
        from scripts.validate_release import validate_release

        (self.root / "LICENSE").unlink()

        with self.assertRaisesRegex(ValueError, "LICENSE"):
            validate_release(self.root)

    def test_rejects_claude_manifest(self):
        from scripts.validate_release import validate_release

        self._write(".claude-plugin/plugin.json", "{}")

        with self.assertRaisesRegex(ValueError, "Claude"):
            validate_release(self.root)

    def test_rejects_placeholder_in_distributable_content(self):
        from scripts.validate_release import validate_release

        self._write("README.md", "[TODO: release]\n")

        with self.assertRaisesRegex(ValueError, "placeholder"):
            validate_release(self.root)

    def test_rejects_declared_path_outside_plugin(self):
        from scripts.validate_release import validate_release

        manifest = self._read_json(".codex-plugin/plugin.json")
        manifest["skills"] = "../skills/"
        self._write_json(".codex-plugin/plugin.json", manifest)

        with self.assertRaisesRegex(ValueError, "inside"):
            validate_release(self.root)

    def test_cli_reports_validation_errors(self):
        result = subprocess.run(
            [
                sys.executable,
                str(REPOSITORY_ROOT / "scripts" / "validate_release.py"),
                "--root",
                str(self.root),
                "--tag",
                "v0.1.1",
            ],
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(result.returncode, 1)
        self.assertIn("tag", result.stderr)


if __name__ == "__main__":
    unittest.main()
