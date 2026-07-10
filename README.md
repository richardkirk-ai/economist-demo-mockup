# The Economist — Ada demo mockup

A two-page demo prop for the Ada Sales Engineering demo with **The Economist**.

| Page | File | What it is | Ada connection |
|------|------|-----------|----------------|
| **1** | [`index.html`](index.html) | Static replica of The Economist's "Save 30% today" **Premium** subscription page. Top-nav links open Page 2 (**The Economist app**) and Page 3 (**Ada Voice**). | **Real Ada widget** — embeds the live `the-economist-ai-agent-demo` bot (needs internet) |
| **2** | [`app.html`](app.html) | Mobile **in-app experience** — the Economist app home screen inside an iPhone frame, with a floating **Support** button that launches the scripted Ada support chat | **Fully scripted** — no backend, no real bot, works offline |
| **3** | [`ada-voice.html`](ada-voice.html) | **Ada Voice — Live Call Intelligence.** Plays a real recorded voice call (`call.wav`) synced to a live playbook/reasoning panel and an animated **backend-systems orchestration** (CRM → Fulfilment → Logistics → Billing → Case Mgmt → Notifications). Shows how Ada retrieves knowledge, runs playbooks and integrates with systems. | Recorded call; systems calls are illustrative. Keys: Space play · S calibrate |

## The demo sequence

1. **Page 1** — a "customer on the site" asks the **real** Ada bot signup / plan / KB questions. Then tap **"The Economist app"** in the nav to jump to Page 2.
2. **Page 2** — tap the **Support** button (bottom-right of the phone) to open the in-app support chat, which runs the headline flow:
   - **Missed delivery** → *"replacement sent + credit applied + digital access unlocked"* (a checklist card).
   - **Auto-upsell** → 2-year / 3-year Premium + Print cards → **Switch & Save** → confirmation + a green **"Plan updated"** toast in the phone.
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
