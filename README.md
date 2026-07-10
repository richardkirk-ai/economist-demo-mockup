# The Economist — Ada demo mockup

A two-page demo prop for the Ada Sales Engineering demo with **The Economist**.

| Page | File | What it is | Ada connection |
|------|------|-----------|----------------|
| **1** | [`index.html`](index.html) | Static replica of The Economist's "Save 30% today" **Premium** subscription page | **Real Ada widget** — embeds the live `the-economist-ai-agent-demo` bot (needs internet) |
| **2** | [`app.html`](app.html) | Mocked **My Account** page (Premium + Print) with a **scripted** Ada-purple chat widget | **Fully scripted** — no backend, no real bot, works offline |

## The demo sequence

1. **Page 1** — a "customer on the site" asks the **real** Ada bot signup / plan / KB questions.
2. **Page 2** — the scripted widget runs the headline flow:
   - **Missed delivery** → *"replacement sent + credit applied + digital access unlocked"* (a checklist card).
   - **Auto-upsell** → 2-year / 3-year Premium + Print cards → **Switch & Save** → the confirmation *live-updates the account header* on the page and pops a green **"Plan updated"** toast.
   - Trigger via the suggested-prompt chips (reliable on stage) or by typing (substring matching). Anything unrecognised falls back gracefully. **"Reset demo"** (bottom-left) restarts it.
3. **Phone call** — you then call the **real voice bot** (+44 7898 116652) and report a missed delivery **again**. Because the same subscriber (Richard Kirk / `ECON-77213`) now shows a repeat pattern, the bot **escalates to a human immediately** instead of reshipping. *(This lives on the real bot, not in this app.)*

> The Page-1 hero image is a lightweight CSS approximation of the Economist red collage — swap in the real asset later if wanted.

## Run locally

Just open `index.html` in a browser. Or, for a local server:

```bash
python3 serve.py        # serves http://127.0.0.1:8123
```

## Host on GitHub Pages

```bash
cd ~/Documents/GitHub/economist-demo-mockup
# create the repo on your GitHub account and push (needs the gh CLI, logged in):
gh repo create economist-demo-mockup --public --source=. --remote=origin --push
```

Or manually: create an empty repo on github.com, then:

```bash
git remote add origin https://github.com/<your-username>/economist-demo-mockup.git
git branch -M main
git push -u origin main
```

Then in the repo on github.com: **Settings → Pages → Build from branch → `main` / root → Save**.
Your demo will be live at:

- Page 1: `https://<your-username>.github.io/economist-demo-mockup/`
- Page 2: `https://<your-username>.github.io/economist-demo-mockup/app.html`

*(The `.nojekyll` file ensures GitHub Pages serves the files as-is.)*
