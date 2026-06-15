# Webcattus Labs — Website

Hugo-based static site deployed via GitHub Pages. Zero hosting cost.

---

## Quick Start

### 1. Install Hugo (Extended)

```bash
# macOS
brew install hugo

# Windows (Chocolatey)
choco install hugo-extended

# Linux — see hugo.yml workflow for deb install
```

Verify: `hugo version` — must show `extended`.

### 2. Clone and run locally

```bash
git clone https://github.com/YOUR_USERNAME/webcattus-labs.git
cd webcattus-labs
hugo server -D
```

Open `http://localhost:1313`

---

## Deploy to GitHub Pages

### Step 1 — Create GitHub repo
Create a new repo named `webcattus-labs` (or any name) on GitHub.

### Step 2 — Push your code
```bash
git init
git add .
git commit -m "Initial site"
git remote add origin https://github.com/YOUR_USERNAME/webcattus-labs.git
git push -u origin main
```

### Step 3 — Enable GitHub Pages
1. Go to **Settings → Pages**
2. Under **Source**, select **GitHub Actions**
3. The workflow in `.github/workflows/hugo.yml` runs automatically on every push

### Step 4 — Connect your Squarespace domain
In Squarespace → **Domains → Manage → DNS Settings**, add:

| Type  | Host | Value |
|-------|------|-------|
| A     | @    | 185.199.108.153 |
| A     | @    | 185.199.109.153 |
| A     | @    | 185.199.110.153 |
| A     | @    | 185.199.111.153 |
| CNAME | www  | YOUR_USERNAME.github.io |

Then in GitHub → **Settings → Pages → Custom Domain** — enter your domain.

---

## Connect the Contact Form

1. Go to [formspree.io](https://formspree.io) and create a free account
2. Create a new form and copy your Form ID
3. In `layouts/contact/single.html`, replace `YOUR_FORM_ID` with your actual ID:
   ```html
   <form action="https://formspree.io/f/YOUR_ACTUAL_ID" method="POST">
   ```
4. Free tier: 50 submissions/month

---

## Update Content

| What to change | Where |
|---|---|
| Site title / email | `config.toml` |
| Homepage hero copy | `layouts/index.html` |
| Services content | `layouts/services/list.html` |
| About copy | `layouts/about/single.html` |
| Contact form | `layouts/contact/single.html` |
| Colors / fonts | `static/css/style.css` |
| Nav links | `config.toml` → `[menu]` |
| Footer links | `layouts/partials/footer.html` |

---

## Add a Blog (Optional but great for SEO)

```bash
# Create a new post
hugo new content/blog/my-first-post.md
```

Add to `config.toml`:
```toml
[[menu.main]]
  name = "Blog"
  url = "/blog/"
  weight = 4
```

---

## File Structure

```
webcattus-labs/
├── config.toml               # Site config, nav, params
├── .github/workflows/
│   └── hugo.yml              # Auto-deploy to GitHub Pages
├── content/
│   ├── _index.md             # Homepage
│   ├── about.md
│   ├── contact.md
│   └── services/_index.md
├── layouts/
│   ├── index.html            # Homepage template
│   ├── _default/
│   │   ├── baseof.html       # Base wrapper
│   │   └── single.html       # Generic page
│   ├── partials/
│   │   ├── head.html
│   │   ├── header.html
│   │   └── footer.html
│   ├── services/list.html
│   ├── about/single.html
│   └── contact/single.html
└── static/
    └── css/style.css
```
