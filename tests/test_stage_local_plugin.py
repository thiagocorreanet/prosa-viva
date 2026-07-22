import json
import tempfile
import unittest
from pathlib import Path


class StageLocalPluginTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)
        self.source = self.root / "checkout"
        self.destination = self.root / "staging" / "prosa-viva"

        manifest_directory = self.source / ".codex-plugin"
        manifest_directory.mkdir(parents=True)
        (manifest_directory / "plugin.json").write_text(
            json.dumps({"name": "prosa-viva", "version": "0.1.0"}),
            encoding="utf-8",
        )
        skill_directory = self.source / "skills" / "refinar-prosa"
        skill_directory.mkdir(parents=True)
        (skill_directory / "SKILL.md").write_text("skill\n", encoding="utf-8")
        (self.source / "README.md").write_text("readme\n", encoding="utf-8")
        (self.source / "LICENSE").write_text("license\n", encoding="utf-8")

        for excluded in ("docs/design.md", "evals/case.json", ".git/HEAD"):
            path = self.source / excluded
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("excluded\n", encoding="utf-8")

    def test_copies_only_distributable_allowlist(self):
        from scripts.stage_local_plugin import stage_plugin

        copied = stage_plugin(self.source, self.destination)

        self.assertEqual(
            copied,
            (".codex-plugin", "skills", "README.md", "LICENSE"),
        )
        self.assertEqual(
            sorted(
                path.relative_to(self.destination).as_posix()
                for path in self.destination.rglob("*")
                if path.is_file()
            ),
            [
                ".codex-plugin/plugin.json",
                "LICENSE",
                "README.md",
                "skills/refinar-prosa/SKILL.md",
            ],
        )

    def test_replaces_previous_staging_instead_of_merging(self):
        from scripts.stage_local_plugin import stage_plugin

        stage_plugin(self.source, self.destination)
        stale_file = self.destination / "skills" / "stale.md"
        stale_file.write_text("stale\n", encoding="utf-8")

        stage_plugin(self.source, self.destination)

        self.assertFalse(stale_file.exists())

    def test_rejects_manifest_with_another_plugin_name(self):
        from scripts.stage_local_plugin import stage_plugin

        manifest = self.source / ".codex-plugin" / "plugin.json"
        manifest.write_text(
            json.dumps({"name": "outro-plugin", "version": "0.1.0"}),
            encoding="utf-8",
        )

        with self.assertRaisesRegex(ValueError, "prosa-viva"):
            stage_plugin(self.source, self.destination)

        self.assertFalse(self.destination.exists())

    def test_rejects_source_as_destination(self):
        from scripts.stage_local_plugin import stage_plugin

        with self.assertRaisesRegex(ValueError, "different"):
            stage_plugin(self.source, self.source)

    def test_rejects_home_as_destination(self):
        from scripts.stage_local_plugin import stage_plugin

        with self.assertRaisesRegex(ValueError, "home"):
            stage_plugin(self.source, Path.home())


if __name__ == "__main__":
    unittest.main()
