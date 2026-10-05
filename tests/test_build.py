"""Run with:  python -m unittest discover tests"""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import build  # noqa: E402


def mini(css):
    """minify() without its banner line."""
    return build.minify(css).split("\n", 1)[1].strip()


class Minify(unittest.TestCase):
    def test_keeps_strings(self):
        css = 'a::before{content:"~/  home ; { }"}'
        self.assertEqual(mini(css), 'a::before{content:"~/  home ; { }"}')

    def test_drops_comments_and_space(self):
        self.assertEqual(mini("/* x */\na , b {\n  color : red ;\n}\n"), "a,b{color:red}")

    def test_keeps_space_in_selectors(self):
        self.assertEqual(mini("article p{x:1}"), "article p{x:1}")
        self.assertEqual(mini(":is(a, b) ul > li + li{x:1}"), ":is(a,b) ul>li+li{x:1}")

    def test_keeps_calc_and_variable_names(self):
        css = "a{margin:calc(var(--nss-gutter) + 18px) calc(-.5rem - 2px)}"
        self.assertEqual(mini(css), "a{margin:calc(var(--nss-gutter) + 18px) calc(-.5rem - 2px)}")

    def test_keeps_media_queries_readable(self):
        self.assertEqual(mini("@media (min-width: 40rem) and (hover: hover){a{x:1}}"),
                         "@media (min-width:40rem) and (hover:hover){a{x:1}}")


class Framework(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.css, cls.mini = build.build()

    def test_passes_its_own_checks(self):
        self.assertEqual(build.check(self.css, self.mini), [])

    def test_check_catches_a_class(self):
        self.assertTrue(build.check(self.css + ".btn{color:red}", self.mini))

    def test_check_catches_data_attribute(self):
        self.assertTrue(build.check(self.css + "[data-theme=dark]{color:red}", self.mini))

    def test_every_variable_used_is_defined(self):
        defined = set(re.findall(r"(--nss-[\w-]+)\s*:", self.css))
        used = set(re.findall(r"var\((--nss-[\w-]+)", self.css))
        self.assertEqual(used - defined, set())

    def test_themes_only_set_known_variables(self):
        defined = set(re.findall(r"(--nss-[\w-]+)\s*:", self.css))
        for theme in (ROOT / "themes").glob("*.css"):
            names = set(re.findall(r"(--nss-[\w-]+)\s*:", theme.read_text(encoding="utf-8")))
            self.assertEqual(names - defined, set(), theme.name)

    def test_demo_has_no_classes_or_scripts(self):
        html = (ROOT / "demo" / "index.html").read_text(encoding="utf-8")
        self.assertNotRegex(html, r"\sclass=|<script|\sstyle=|\son\w+=")


if __name__ == "__main__":
    unittest.main()
