# AI UGC Factory

**AI UGC Factory** is an open-source operating system for building enterprise-grade AI ad assets and producing AI UGC ad videos in batches.

It is designed for founders, growth teams, agencies, and creators who want a reusable workflow instead of one-off prompts: product intake, asset mapping, reference control, UGC script design, generation prompts, QA gates, demo packaging, and performance-learning loops.

> Matrix launch note: the full Matrix product link is coming soon. For early access / collaboration, scan the WeChat QR code in [`assets/contact/wechat-qr.jpg`](assets/contact/wechat-qr.jpg).

## What this project gives you

- A reusable **AI UGC Factory skill** for turning product assets into production-ready ad video briefs.
- Asset manifest templates for real product images, webpages, references, videos, and contact assets.
- Prompt-pack examples for UGC videos, demo reels, and ad-asset systems.
- A lightweight project webpage you can deploy with GitHub Pages.
- Demo index for multiple verticals: pet food, puzzle/Kickstarter, education/course, beauty device, and AI video SaaS.

## Why it exists

Most AI ad workflows fail because they treat video generation as a prompt-writing problem. Production quality usually comes from a system:

1. real product assets are organized and named by function;
2. reference images/videos are attached as model-readable inputs, not merely described;
3. every 1-2 second beat has a job: hook, proof, benefit, objection, CTA;
4. voice, pacing, visuals, and claims are QA'd before delivery;
5. winning angles become reusable batches.

This repo packages that system into a compact open-source starter.

## Repository structure

```text
skills/ai-ugc-factory/        # reusable Matrix/agent skill
examples/briefs/              # product brief examples
examples/asset-manifests/     # asset inventory examples
templates/                    # reusable production templates
docs/                         # GitHub Pages project website
docs/demo-videos/             # demo video index; large files stay external/local by default
assets/contact/               # WeChat contact QR / launch placeholder
scripts/                      # helper scripts
```

## Quick start

1. Copy `templates/product-brief.md` and fill in the product, audience, claims, and offer boundaries.
2. Put real assets in a stable folder and build an asset manifest from `templates/asset-manifest.csv`.
3. Use `skills/ai-ugc-factory/SKILL.md` as the production workflow.
4. Draft a prompt pack with `templates/video-prompt-pack.md`.
5. Run the QA checklist before rendering or publishing.

## Demo verticals included

| Vertical | Local source | Use in project |
| --- | --- | --- |
| Pet food | `/Users/agent/Downloads/猫粮 AI UGC` | UGC product ad examples |
| Puzzle / Kickstarter | `/Users/agent/Downloads/PieceStory \| ads Demo` | Real-person + anime ad examples |
| Course education | `/Users/agent/Downloads/课程教育 AI UGC` | Education/service offer ads |
| Curling iron | `/Users/agent/Downloads/Feishu20260615-145610.mp4` | Beauty device demo example |
| AI video SaaS | `https://aivideopro.io` | SaaS/product website ad example |

Large videos are intentionally not committed into the repo by default. Use `docs/demo-videos/index.md` to reference hosted demos, local proof paths, or GitHub Release assets.

## Project webpage

Open `docs/index.html` locally, or publish this repo with GitHub Pages from the `docs/` folder.

## Contact / early access

Matrix launch link is coming soon. If you want early access, collaboration, or batch custom AI UGC production support, scan the WeChat QR code:

![WeChat QR](assets/contact/wechat-qr.jpg)

## License

MIT. Use it, fork it, adapt it — just keep claims truthful and respect product assets you do not own.
