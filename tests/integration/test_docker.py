import subprocess
import unittest

class TestDockerBuild(unittest.TestCase):
    def test_build(self):
        result = subprocess.run(
            ["docker", "build", "-t", "mechbot-test", "."],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0)
