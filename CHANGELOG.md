# Changelog

## 3.0.0 — 2026-10-05

A rewrite. nss is now a complete classless framework: every element is styled, and common components are recognised from plain HTML structure.

### Added
- **Patterns** recognised from structure, with no classes: hero, cards, article cards, tiles, timeline, key–value rows, stat tiles, gallery, callout, badge strip, "last updated" line, breadcrumbs, sidebar layout and accordion.
- **Full form kit:** stacked or inline layout chosen automatically, primary and secondary buttons, a toggle switch (`role="switch"`), custom select arrow, range, file and colour inputs, indeterminate `progress`, `meter` colours, and validation styles (`:user-invalid`, `aria-invalid`).
- **More elements:** `dialog` with backdrop, `menu`, `search`, `hgroup`, `output`, `data`, `var`, `samp`, `pre>samp` output blocks, table `caption` and `tfoot`, and blockquote attribution.
- **Variables:** about 25 `--nss-*` custom properties for colours, fonts, sizes, radius, widths, the background grid and the header logo text.
- **Themes:** `amber`, `violet` and `paper`.
- **Accessibility:** focus rings, `prefers-reduced-motion`, `forced-colors` and print styles.
- **Source and build:** the source is split into `src/` modules. `build.py` (Python, no dependencies) builds `dist/` and checks that no class or `data-*` selectors exist, that braces balance, and that the gzipped size stays under 8 KB.
- **Demo:** `demo/index.html` shows every element and pattern, and is published to GitLab Pages.
- **Tests:** `tests/` covers the minifier and the framework's own rules.

### Changed
- New default look: teal `#3a807a`, a square grid background, a sticky blurred header bar and a mobile-first layout. Light and dark follow the system.
- Site-specific details (nih.ar's `$ whoami` label and `~/nih.ar` logo) moved out of the framework into `sites/nihar.css`.
- The CSS now lives in `dist/`. The root `nss.css` and `nss.min.css` are still built so that old links keep working.
- CI runs the build check and tests, then publishes to Pages. It no longer commits from CI with a push token.

### Removed
- The `data-theme` attribute and the per-item colour cycling from 2.0.
- `QuickStart.txt`; the README covers it.

## 2.0.0

- The "vibrant" redesign: gradient accents, AMOLED dark mode and compact layouts.

## 1.x

- The first versions, used by nih.ar.
