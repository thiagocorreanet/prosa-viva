import unittest
from pathlib import Path


README = Path(__file__).resolve().parents[1] / "README.md"


class LocalInstallationDocumentationTests(unittest.TestCase):
    def test_documents_each_supported_local_lifecycle(self):
        content = README.read_text(encoding="utf-8")

        for heading in (
            "## Instalação local como plugin",
            "### Atualização e reinstalação",
            "### Remoção",
            "## Instalação somente como skill",
        ):
            with self.subTest(heading=heading):
                self.assertIn(heading, content)

    def test_documents_the_public_commands_and_official_helpers(self):
        content = README.read_text(encoding="utf-8")

        for command in (
            "scripts/stage_local_plugin.py",
            "update_plugin_cachebuster.py",
            "read_marketplace_name.py",
            "codex plugin add",
            "codex plugin list",
            "codex plugin remove",
            "npx skills add",
        ):
            with self.subTest(command=command):
                self.assertIn(command, content)

    def test_explains_cache_and_session_boundaries(self):
        content = README.read_text(encoding="utf-8")

        self.assertIn("0.1.0+codex.local-", content)
        self.assertIn("conversa nova", content)
        self.assertIn("aplicativo desktop", content)
        self.assertNotIn("Claude", content)


if __name__ == "__main__":
    unittest.main()
