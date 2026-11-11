"""Check Post-Apollo optional keyboard startup include without changing Sway."""
from pathlib import Path
import re
import unittest

CONFIG = Path(__file__).resolve().parents[1] / "config"
INCLUDE = "include ~/.config/sway/post-apollo-keyboard-locks.conf"


class KeyboardStartupInclude(unittest.TestCase):
    def test_single_post_apollo_include_after_system_includes(self):
        data = CONFIG.read_text(encoding="utf-8")
        active = [line.strip() for line in data.splitlines()
                  if line.strip() and not line.lstrip().startswith("#")]
        self.assertEqual(active.count(INCLUDE), 1)
        self.assertIn("include /etc/sway/config.d/*", active)
        self.assertGreater(active.index(INCLUDE),
                           active.index("include /etc/sway/config.d/*"))

    def test_no_direct_lock_overrides_or_restart_churn(self):
        data = CONFIG.read_text(encoding="utf-8")
        active = [line.strip() for line in data.splitlines()
                  if line.strip() and not line.lstrip().startswith("#")]
        self.assertFalse(any(re.search(r"\bxkb_(?:numlock|capslock)\b", x)
                             for x in active))
        self.assertEqual(len([x for x in active if "post-apollo-keyboard-locks.conf" in x]), 1)
        self.assertNotIn("reload", active[-1])
        self.assertTrue(data.endswith("\n"))


if __name__ == "__main__":
    unittest.main()
