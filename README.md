# NSS CSS Framework v2.0

## 🎨 Modern, Vibrant, Compact Design

A plug-and-play CSS framework for semantic HTML with no classes or JavaScript required. Built for personal websites, portfolios, and technical blogs.

---

## 📦 Files

### 1. **nss.css** (24.2 KB)
- Full version with comments
- Easy to read and customize
- Perfect for development

### 2. **nss.min.css** (15.9 KB) ⚡
- Minified version (34.1% smaller!)
- Production-ready
- Optimized for performance

---

## ✨ Key Features

### 🎨 **Vibrant Design System**
- 6 vibrant accent colors (blue, purple, pink, orange, green, cyan)
- Gradient effects on headers and buttons
- Color-coded project and note items
- Smooth animations and transitions

### 🌓 **AMOLED Dark Mode**
- Pure black (#000000) background in dark mode
- Automatic theme switching based on system preference
- Perfect contrast ratios
- Manual theme override support via `data-theme` attribute

### 📱 **Fully Responsive**
- Mobile-first approach
- Smooth breakpoints: 768px, 640px, 480px
- Perfect on all devices
- Touch-friendly interface

### 🎯 **Compact Layout**
- Single-line header on desktop
- Inline project tags with unique colors
- Inline note items with time + description
- Space-efficient design

### 🚀 **Zero Configuration**
- Works with pure semantic HTML
- No classes required
- No JavaScript needed
- Just link and go!

### ♿ **Accessibility First**
- WCAG compliant
- Keyboard navigation support
- Screen reader friendly
- Reduced motion support
- High contrast mode support

---

## 💻 Installation & Usage

### Quick Start
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Website</title>
    
    <!-- For Production -->
    <link rel="stylesheet" href="nss.min.css">
    
    <!-- OR For Development -->
    <link rel="stylesheet" href="nss.css">
</head>
<body>
    <!-- Your semantic HTML here -->
</body>
</html>
```

### Manual Theme Override (Optional)
```html
<!-- Force light mode -->
<html data-theme="light">

<!-- Force dark mode -->
<html data-theme="dark">
```

---

## 🎨 Color System

### Light Mode
- **Background:** #fafbfc (soft white)
- **Text:** #0f172a (dark slate)
- **Accents:** Blue, Purple, Pink, Orange, Green, Cyan

### Dark Mode (AMOLED)
- **Background:** #000000 (pure black)
- **Surface:** #0a0a0a (near black)
- **Text:** #f1f5f9 (bright white)
- **Accents:** Vibrant versions of light mode colors

---

## 🏗️ HTML Structure Support

### Header
```html
<header>
    <h1><a href="/">Site Name</a></h1>
    <nav>
        <a href="/">home</a>
        <a href="/about">about</a>
        <a href="/blog">blog</a>
    </nav>
</header>
```

### Projects Section (Inline Tags)
```html
<section>
    <h2>Projects</h2>
    <ul>
        <li><a href="#">Project 1</a></li>
        <li><a href="#">Project 2</a></li>
        <li><a href="#">Project 3</a></li>
    </ul>
</section>
```
*Projects display as colorful inline tags, each with unique color*

### Notes Section (with Time)
```html
<section>
    <h2>Notes</h2>
    <ul>
        <li><time>2024-01-15</time> -- <a href="#">Note Title</a></li>
        <li><time>2024-01-10</time> -- <a href="#">Another Note</a></li>
    </ul>
</section>
```
*Notes display inline with time tags, maintaining single-line layout*

### Articles
```html
<article>
    <h1>Article Title</h1>
    <p>Lead paragraph...</p>
    
    <h2>Section</h2>
    <p>Content...</p>
    
    <ul>
        <li>List item with arrow</li>
        <li>Another item</li>
    </ul>
</article>
```

### Footer
```html
<footer>
    <p>
        <nav>
            <a href="/">home</a>
            <a href="/rss.xml">rss</a>
            <a href="/privacy">privacy</a>
        </nav>
        <span>Contact: <a href="mailto:you@email.com">you@email.com</a></span>
    </p>
</footer>
```

---

## 🎨 Customization

All design tokens are defined as CSS variables in `:root`:

```css
:root {
    /* Colors */
    --accent-blue: #3b82f6;
    --accent-purple: #8b5cf6;
    --accent-pink: #ec4899;
    
    /* Spacing */
    --space-sm: 0.5rem;
    --space-md: 0.75rem;
    --space-lg: 1rem;
    
    /* Typography */
    --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    --font-mono: ui-monospace, 'SF Mono', monospace;
}
```

Simply override these variables to customize the design!

---

## 📐 Supported Elements

### Typography
- `h1` - `h6` headings
- `p` paragraphs
- `strong`, `em`, `small`
- `mark` for highlights
- `time` for dates
- `code`, `pre`, `kbd`

### Lists
- `ul` unordered lists (with arrows)
- `ol` ordered lists (with numbers)
- `dl`, `dt`, `dd` description lists

### Forms
- `input` (text, email, password, etc.)
- `textarea`
- `select`
- `button`
- `fieldset`, `legend`

### Tables
- Full table support with hover effects

### Media
- `img`, `video`, `audio`
- `figure`, `figcaption`

### Interactive
- `details`, `summary`
- `progress`

---

## 🚀 Performance

- **No JavaScript:** Pure CSS solution
- **Lightweight:** Only 15.9 KB minified
- **Fast Rendering:** GPU-accelerated animations
- **CDN Ready:** Host anywhere

---

## 🌟 Perfect For

- Personal websites
- Developer portfolios
- Technical blogs
- Documentation sites
- Project showcases
- Minimalist landing pages

---

## 📊 Browser Support

- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers
- ⚠️ IE11 not supported (uses modern CSS)

---

## 🎯 Design Philosophy

1. **Semantic HTML First:** Let HTML structure define the design
2. **No Classes Needed:** Pure element and pseudo-class selectors
3. **Vibrant Yet Professional:** Eye-catching without being overwhelming
4. **Compact & Efficient:** Maximum content, minimum chrome
5. **Accessible by Default:** WCAG compliance built-in

---

## 📝 Changelog

### v2.0 (Current)
- ✨ Complete design overhaul with vibrant colors
- 🎨 Added 6-color accent system
- 🖤 AMOLED pure black dark mode
- 📦 Compact inline layouts for projects and notes
- 🎯 Single-line header design
- 📱 Improved mobile responsiveness
- ⚡ 34% smaller when minified

### v1.1 (Previous)
- Initial brutalist cyber design
- Basic dark/light theme support
- Semantic HTML styling

---

## 📄 License

Free to use for personal and commercial projects.

---

## 🤝 Contributing

This is a personal framework, but feel free to fork and customize for your needs!

---

## 📬 Support

For questions or issues, refer to the code comments or create a discussion.

---

## 🎉 Credits

Built with ❤️ for the modern web.

Inspired by brutalist design, terminal aesthetics, and modern UI trends.

---

**NSS CSS Framework v2.0** - Making semantic HTML beautiful since 2024.