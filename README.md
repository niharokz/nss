# nss

**Classless CSS. Write plain HTML and get a finished website.** No classes, no JavaScript, no build step.

nss styles every HTML element, and it recognises common page structures from the HTML alone: a hero, cards, a timeline, tiles, a gallery, stat tiles, a sidebar and more. You write semantic HTML. nss does the rest.

- **About 7 KB gzipped**, one file, zero JavaScript.
- **Light and dark** follow the visitor's system setting.
- **Mobile first.** Every pattern works from 320px phones up to wide screens.
- **Themeable** through about 25 CSS variables, with three ready-made themes.
- **Accessible.** Visible focus rings, reduced motion, high-contrast mode and print styles.

It powers [nih.ar](https://nih.ar) and [home.nihars.com](https://home.nihars.com). See every element on the [demo page](https://niharokz.gitlab.io/nss/).

---

## Contents

- [Install](#install)
- [A first page](#a-first-page)
- [Elements](#elements)
- [Patterns](#patterns)
- [Forms](#forms)
- [Themes and variables](#themes-and-variables)
- [Building from source](#building-from-source)
- [Upgrading from 2.x](#upgrading-from-2x)
- [FAQ](#faq)

---

## Install

Add one line to your page's `<head>`:

```html
<link rel="stylesheet" href="https://niharokz.gitlab.io/nss/nss.min.css">
```

Or download [`dist/nss.min.css`](dist/nss.min.css), put it next to your pages, and link it with `href="nss.min.css"`. Self-hosting is faster and keeps your site free of third-party requests.

| File | Use it for |
| --- | --- |
| `dist/nss.min.css` | Production. Everything, minified |
| `dist/nss.css` | Reading or editing. Same rules, with comments |
| `dist/nss-amber.min.css`, `nss-violet.min.css`, `nss-paper.min.css` | Optional themes, loaded **after** nss |

---

## A first page

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>My site</title>
  <link rel="stylesheet" href="nss.min.css">
</head>
<body>
  <header>
    <h1><a href="/">mysite</a></h1>
    <nav><a href="/about.html">about</a> <a href="/notes.html">notes</a></nav>
  </header>

  <section>
    <p>Hi, I'm Ada. I build small, fast things.</p>
    <p>This line becomes the hero's subtitle.</p>
  </section>

  <article>
    <h2>Hello world</h2>
    <p>A normal article: readable width, good spacing, nothing to configure.</p>
  </article>

  <footer><nav><a href="/feed.xml">feed</a></nav></footer>
</body>
</html>
```

That gives you a sticky header bar with the logo `~/mysite_`, a large hero, a styled article and a footer. It is responsive and works in light and dark mode.

---

## Elements

Every element is styled. A few have extra touches:

| HTML | What you get |
| --- | --- |
| `h2` … `h6` in an `article` | Headings marked `##` and `###` in the accent colour |
| `<h3>Title <small>new</small></h3>` | A small badge next to the heading |
| `<pre><code>` | A terminal-style window with three dots |
| `<pre><samp>` | Command output: smaller, no window dots |
| `kbd`, `var`, `samp`, inline `code` | Key caps, italic mono variables, output chips |
| `blockquote` with a `footer` | A quote with its attribution |
| `ol` | Monospace numbers |
| `dl` | A two-column term list on wide screens |
| `table` with `caption`, `thead`, `tfoot` | Scrolls sideways on phones; rows highlight on hover |
| `details` / `summary` | A disclosure box; several in a row join into an accordion |
| `dialog` | A centred modal with a dimmed backdrop |
| `mark`, `abbr`, `del`, `ins`, `q`, `time`, `data`, `address`, `hr` | All styled to match |

---

## Patterns

Patterns are components that nss recognises from structure. There is nothing to add: write the HTML on the left and you get the component on the right.

| Write this | Get this |
| --- | --- |
| `header` containing `h1>a` and `nav` | A sticky, blurred header bar. The link text becomes the logo `~/name_` |
| `header` with `nav` first, then an `h1` | The bar, plus a large gradient page title below it |
| `nav>ol` of links | Breadcrumbs, with `/` separators and `aria-current="page"` support |
| The first `<p>` of the first `section` | The hero headline. A link inside it gets the gradient. The next `<p>` is the subtitle |
| A `ul` in the first `section`, before its last list | Cards in a responsive grid |
| A `section` holding two or more `article`s | Article cards; each card's `footer` becomes its meta line |
| A `ul` where every item starts with a link | Tiles: a grid of link buttons |
| A `ul` where every item starts with `<time>` | A timeline. In the first section, the newest entry is highlighted |
| `li` starting with `<strong>` | Key–value rows: the label on the left, the value on the right |
| `dl` made of `div`s (`<div><dt>…</dt><dd>…</dd></div>`) | Stat tiles |
| A `figure` holding `figure`s | An image gallery, with one caption for the whole set |
| An `aside` inside an `article` | A callout box. A leading `<strong>` or `<h4>` becomes its title |
| `main` and `aside` side by side in `body` | A sidebar layout from 64rem wide |
| A later `section` with a single `<p>` | A strip of badges; each link becomes a chip |
| An article whose last `<p>` contains a `<time>` | A quiet "last updated" line |

Here is the cards and timeline markup from the demo:

```html
<section>
  <p>Plain HTML in. A finished website out.</p>
  <h2># features</h2>
  <ul>
    <li><a href="/a">Fast</a>: about 7 KB gzipped.</li>
    <li><a href="/b">Simple</a>: nothing to learn but HTML.</li>
  </ul>
  <h2># changelog</h2>
  <ul>
    <li><time datetime="2026-10-05">2026-10-05</time> -- <a href="/v3">nss 3.0</a></li>
    <li><time datetime="2025-04-01">2025-04-01</time> -- <a href="/v2">nss 2.0</a></li>
  </ul>
</section>
```

---

## Forms

Forms need no extra markup either.

- A `form` that contains `label`s, `fieldset`s or `p`s stacks into a column. A form made only of inputs and a button sits on one line, which suits a search box.
- `type="submit"` and plain `button` are the primary button. `type="reset"` and `type="button"` are the secondary, outlined button. `disabled` dims either one.
- `<input type="checkbox" role="switch">` is drawn as a toggle switch.
- Checkboxes, radios, ranges, selects, file inputs, `progress` (including the indeterminate state with no `value`), `meter` and `output` are all styled.
- Invalid fields turn red once the visitor has touched them (`:user-invalid`), or when you set `aria-invalid="true"`.

```html
<form>
  <label>Email <input type="email" required></label>
  <label><input type="checkbox" role="switch"> Send me updates</label>
  <p><button>Subscribe</button> <button type="reset">Clear</button></p>
</form>
```

---

## Themes and variables

Load a theme after nss:

```html
<link rel="stylesheet" href="nss.min.css">
<link rel="stylesheet" href="nss-paper.min.css">
```

| Theme | Look |
| --- | --- |
| *(none)* | Teal `#3a807a` on a dark grid. Light mode follows the system |
| `amber` | Warm orange accent |
| `violet` | Violet accent |
| `paper` | Always light, serif text, no grid, no logo decoration |

Or set your own variables. Put them after nss, in a `<style>` block or your own file:

```html
<style>
  :root { --nss-accent: #c2410c; --nss-ink: #ea580c; --nss-radius: 4px; }
</style>
```

| Variable | Default | Controls |
| --- | --- | --- |
| `--nss-bg`, `--nss-surface`, `--nss-surface-2`, `--nss-line` | dark greys | Page, card and border colours |
| `--nss-fg`, `--nss-muted` | near-white, grey | Text |
| `--nss-accent` | `#3a807a` | Buttons, borders and highlights |
| `--nss-ink` | `#66bdb3` | Accent-coloured text (keep it readable on `--nss-bg`) |
| `--nss-accent-2` | `#a9b8ff` | Second accent: gradients, the third terminal dot |
| `--nss-on-accent` | `#fff` | Text on accent-filled buttons |
| `--nss-ok`, `--nss-warn`, `--nss-bad` | green, amber, red | Meters and validation |
| `--nss-grid`, `--nss-grid-size`, `--nss-glow` | faint teal | The background grid and corner glow. Set to `transparent` to turn them off |
| `--nss-sans`, `--nss-mono` | system fonts | Font stacks |
| `--nss-size`, `--nss-leading` | `16px` (`17px` on wide screens), `1.7` | Base text size and line height |
| `--nss-radius` | `12px` | Corner rounding |
| `--nss-width`, `--nss-wide` | `46rem`, `72rem` | Text column and sidebar-layout widths |
| `--nss-gutter` | `1rem` (`1.5rem` on wide screens) | Side padding |
| `--nss-logo-prefix`, `--nss-logo-suffix` | `"~/"`, `"_"` | Text around the header logo. Use `""` to remove |

To change only the light mode, wrap your overrides in `@media (prefers-color-scheme: light) { :root { … } }`.

---

## Building from source

You only need Python 3.10 or newer. There are no dependencies.

```bash
python build.py           # join src/*.css → dist/, minify, build themes
python build.py --check   # also fail on class selectors, data-* hooks, bad braces, or > 8 KB gzipped
python -m unittest discover -s tests
```

```text
src/
  00-tokens.css       variables, light and dark
  01-base.css         reset, page background, focus
  02-typography.css   text, headings, lists, quotes
  03-code.css         code, kbd, pre
  04-media.css        images, video, figures, gallery
  05-tables.css
  06-forms.css        inputs, buttons, switch, progress
  07-interactive.css  details, accordion, dialog
  08-layout.css       header bar, nav, breadcrumbs, sidebar, footer
  09-patterns.css     hero, cards, tiles, timeline, stats, callouts
  10-a11y-print.css   reduced motion, forced colours, print
themes/               one file of variables per theme
sites/                site-specific extras, e.g. nihar.css for nih.ar
demo/index.html       every element and pattern on one page
```

Edit `src/`, run `python build.py`, and commit `dist/` along with your change. CI fails if `dist/` is out of date. Pushing to `main` publishes the demo and the CSS to GitLab Pages.

**The rules:** no class selectors, no `data-*` selectors, and no JavaScript. Standard attributes such as `type`, `role`, `open`, `disabled` and `aria-*` are fine, because they carry meaning on their own.

---

## Upgrading from 2.x

- The root `nss.css` and `nss.min.css` still exist and are rebuilt from `src/`, so old links keep working. New links should point at `dist/`.
- The design is new: a teal accent, a grid background and a sticky header bar.
- The `data-theme` attribute is gone. Light and dark follow the system; use a theme file or the variables to force one look.
- The old per-project colour cycling is gone. Use `--nss-accent` instead.
- If your site relied on nih.ar's `$ whoami` label or the `~/nih.ar` logo, those now live in `sites/nihar.css`.

---

## FAQ

**Why no classes?** HTML already says what things are. A stylesheet that reads that structure keeps your markup clean, works with any Markdown generator, and lets you swap the look without touching a page.

**Can I still use classes?** Yes, in your own CSS on top of nss. nss itself never uses them.

**Does it work with Markdown generators?** Yes. It was built for [rynz](https://pypi.org/project/rynz/), and works with anything that writes plain HTML.

**Which browsers?** Current Firefox, Chrome, Edge and Safari. The patterns use `:has()`, which every major browser has supported since 2023. Older browsers still get readable, styled pages; they just miss some layout touches.

---

[Changelog](CHANGELOG.md) · MIT License · made by [Nihar](https://nih.ar)
