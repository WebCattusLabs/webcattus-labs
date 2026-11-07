# Webcattus Labs website

## Deploy (GitHub Pages)
Copy everything in `site/` into the root of your webcattus-labs repo (it replaces index.html and adds
services, industries, use-cases, about, faq, contact, assets/ and the Spanish site in es/). Push to main. Your existing workflow publishes it.
Also delete the old `public/` folder and `.hugo_build.lock` from the repo.

## Before going live, edit
- `site/assets/site.js` → `calendlyUrl` (your Calendly or Google Calendar booking link)
- Prices on services.html (and the FAQ "starts at $750" line) if you want different numbers
- The founder portrait placeholder on about.html: swap the "J" block for a real photo

## Editing copy later
English text lives in `source/pages_content.py`, Spanish in `source/pages_content_es.py`
(shared header/footer strings for both are in the STR table in `source/build.py`). Run `python3 build.py` inside `source/`, then copy `dist/` to the repo.
The contact form posts to Lead Router; leads arrive in Slack like before.
