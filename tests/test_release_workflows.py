import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKOUT_SHA = "3d3c42e5aac5ba805825da76410c181273ba90b1"
SETUP_PYTHON_SHA = "5fda3b95a4ea91299a34e894583c3862153e4b97"


class ReleaseWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.validate_workflow = (
            ROOT / ".github" / "workflows" / "validate.yml"
        ).read_text(encoding="utf-8")
        self.release_workflow = (
            ROOT / ".github" / "workflows" / "release.yml"
        ).read_text(encoding="utf-8")

    def test_validation_workflow_is_read_only(self):
        self.assertIn("pull_request:", self.validate_workflow)
        self.assertIn("branches: [main]", self.validate_workflow)
        self.assertIn("contents: read", self.validate_workflow)
        self.assertNotIn("contents: write", self.validate_workflow)
        self.assertIn("python3 -m unittest discover -s tests -v", self.validate_workflow)
        self.assertIn("python3 scripts/validate_release.py", self.validate_workflow)

    def test_release_workflow_is_tag_gated(self):
        self.assertIn("tags:", self.release_workflow)
        self.assertIn("'v*.*.*'", self.release_workflow)
        self.assertIn("contents: write", self.release_workflow)
        self.assertIn("--tag \"$GITHUB_REF_NAME\"", self.release_workflow)
        self.assertIn("git archive", self.release_workflow)
        self.assertIn("sha256sum", self.release_workflow)
        self.assertIn("gh release create", self.release_workflow)
        self.assertIn("--verify-tag", self.release_workflow)

    def test_workflows_pin_only_the_two_official_actions(self):
        for workflow in (self.validate_workflow, self.release_workflow):
            with self.subTest(workflow=workflow[:30]):
                self.assertIn(f"actions/checkout@{CHECKOUT_SHA}", workflow)
                self.assertIn(f"actions/setup-python@{SETUP_PYTHON_SHA}", workflow)
                uses_lines = [
                    line.strip() for line in workflow.splitlines() if "uses:" in line
                ]
                self.assertEqual(len(uses_lines), 2)
                self.assertTrue(all("uses: actions/" in line for line in uses_lines))


if __name__ == "__main__":
    unittest.main()
