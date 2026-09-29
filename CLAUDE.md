# tomkwon.com — working notes for Claude

Tom Kwon's academic website (Assistant Professor of Strategy & Entrepreneurship, UCL School of Management).
Live at https://www.tomkwon.com, served by GitHub Pages from `main` of `tomhykwon/tomkwon.com`.
Tom talks in Korean — reply in Korean.

## How the site is built

- `_src/*.html` — **edit content here** (page bodies only: `index.html` = Home, `research.html`, `teaching.html`).
- `build.py` — wraps each page in the shared header, nav and left sidebar (photo, links, UCL logo). Sidebar/nav/`<head>` live here; the CV link is the `CV` constant.
- Run `python3 build.py` → writes the root `index.html`, `research.html`, `teaching.html`. **Never edit the root HTML files by hand**; they are overwritten.
- `style.css` — all styling. Colour tokens at the top (`--bg` warm paper white, `--accent` deep UCL purple `#3b2159`).
- `assets/` — `tom-kwon.jpg`, `ucl-som-logo.png`, favicons (UCL portico mark recoloured `#7a2ce0`), `Tom_Kwon_CV.pdf`.
- `home.html`, `cv.html` — redirects for old Google Sites URLs (`/home`, `/cv`). `CNAME` = `www.tomkwon.com`.
- `_config.yml` excludes build files from Jekyll; `_src/` is ignored by Jekyll because of the underscore.

## Workflow

1. Preview locally: `python3 -m http.server 4000 --directory ~/code/tomkwon.com` (in the Claude app, add a `launch.json` entry and use preview_start). The server caches aggressively — reload with `?v=<timestamp>`.
2. Edit `_src/` or `style.css` / `build.py`, run `python3 build.py`, check the preview.
3. Commit and `git push` — GitHub Pages redeploys in ~1–2 min. Tom has approved pushing directly once he's happy with a change.
4. To update the CV: copy the new PDF over `assets/Tom_Kwon_CV.pdf` (same filename so links never change). Read the PDF before publishing.

DNS (Squarespace Domains, for reference): `www` CNAME → `tomhykwon.github.io`; apex `tomkwon.com` uses a Squarespace forwarding rule to `www` (cannot be deleted; works fine). HTTPS enforced in Pages settings.

## Design principles (Tom's feedback)

- Clean, professional, academic. Nothing that "튀어" (stands out) or looks AI-generated: no cards, gradients, big stat blocks, loud badges.
- Emphasis should be subtle — small uppercase purple labels, a slightly bolder number, thin rules.
- Left sidebar layout inspired by hyokang.com; single-column content ≤ 700px.
- Collapsible `<details>` for abstracts and course descriptions.
- Don't copy his old Google Sites formatting.

## Content rules

- **Don't invent facts.** Source from Tom's CV / files or ask him. Latest CV: OneDrive `13_Curriculum Vitae/CV_tk_ucl_*.pdf`; papers under OneDrive `# Working Papers/` and `# Submission/`.
- Papers under review must **not** use their submitted titles (blind review):
  - "Spillover Effect of Technology Failure: Camera vs. LiDAR in the Autonomous Vehicle Industry" — with Hyo Kang and Violina Rindova (Hyo first). Under review, Management Science.
  - "To Focus or Explore: Experimentation, Failure, and the Adapting of Knowledge Development Strategies in Nascent Industries" — with Violina Rindova and Milan Miric. Under review, SMJ. SMS 2026 Best Paper nominations (conference-wide + Knowledge & Innovation IG) — "Nominated", never "finalist".
  - Tom chose to keep the abstracts as they are.
- "On the Radar? When Prior Experience Becomes an Advantage in Technological Change" (solo) is listed first under Working papers.
- Work in progress: "From Hardware to Code: Software and AI Specialists and the Direction of Innovation in Robotics" (with Hyo Kang); "Temporal Focus and Innovation Trajectories…" (with Rindova & Miric).
- Keep camera/LiDAR detail out of bios and the Home intro.
- Teaching: MSIN0020 Strategy by Design (Fall 2025, Fall 2026; rating 4.93), BUAD 497 (Summer 2023; rating 4.74; "USC Marshall Outstanding Teaching Award" — no "PhD Student"), ITM 613 SeoulTech (2019). Use "Fall", not "Autumn".
- Sidebar location reads "London, UK" (Tom preferred this over the full office address).

## Ideas Tom hasn't decided on yet

- Presentations (invited talks & conferences from the CV) and Service (AOM Industry Emergence symposium organiser 2022–2026; Strategy Witan 2027 co-organiser with Anil Doshi) sections on the Research page.
- Status lines on papers ("Under review, …") — they're in his CV but not yet on the site.
