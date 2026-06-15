# AI UGC Factory｜AI UGC 广告工厂

**AI UGC Factory** is an open-source operating system for building enterprise-grade AI ad assets and producing AI UGC ad videos in batches.  
**AI UGC Factory** 是一个开源工作流项目，用来搭建企业级 AI 广告资产体系，并批量生产 AI UGC 广告视频。

It is designed for founders, growth teams, agencies, and creators who want a reusable workflow instead of one-off prompts: product intake, asset mapping, reference control, UGC script design, generation prompts, QA gates, demo packaging, and performance-learning loops.  
它适合创始人、增长团队、营销机构和内容创作者：不再只依赖一次性 prompt，而是沉淀一套可复用流程，包括产品 brief、素材资产整理、参考图/视频控制、UGC 脚本、生成提示词、质检门槛、demo 包装与投放学习闭环。

> Matrix launch note: the full Matrix product link is coming soon. For early access / collaboration, scan the WeChat QR code in [`assets/contact/wechat-qr.jpg`](assets/contact/wechat-qr.jpg).  
> Matrix 即将上线：正式产品链接稍后发布。如需提前交流或合作，可查看 [`assets/contact/wechat-qr.jpg`](assets/contact/wechat-qr.jpg)。

## What this project gives you｜这个项目包含什么

- A reusable **AI UGC Factory skill** for turning product assets into production-ready ad video briefs.  
  一个可复用的 **AI UGC Factory skill**，把产品素材转成可执行的视频生产 brief。
- Asset manifest templates for real product images, webpages, references, videos, and contact assets.  
  真实产品图、网页、参考图、参考视频、联系资产的素材清单模板。
- Prompt-pack examples for UGC videos, demo reels, and ad-asset systems.  
  UGC 视频、demo reel、广告资产系统的提示词包示例。
- A lightweight project webpage you can deploy with GitHub Pages.  
  一个可用 GitHub Pages 部署的轻量项目网页。
- Demo index for multiple verticals: pet food, puzzle/Kickstarter, education/course, beauty device, and AI video SaaS.  
  多行业 demo 索引：猫粮、拼图/Kickstarter、课程教育、卷发棒、AI 视频 SaaS。

## Why it exists｜为什么需要它

Most AI ad workflows fail because they treat video generation as a prompt-writing problem. Production quality usually comes from a system:  
很多 AI 广告流程失败，是因为把视频生成误以为只是“写 prompt”。真正稳定的产出，通常来自一套系统：

1. real product assets are organized and named by function;  
   真实产品素材按功能命名和整理；
2. reference images/videos are attached as model-readable inputs, not merely described;  
   参考图片/视频作为模型可读取输入，而不是只在 prompt 里描述；
3. every 1-2 second beat has a job: hook, proof, benefit, objection, CTA;  
   每 1–2 秒画面都有明确任务：钩子、证明、利益点、异议、CTA；
4. voice, pacing, visuals, and claims are QA'd before delivery;  
   口播、节奏、画面和产品声明都经过 QA；
5. winning angles become reusable batches.  
   跑通的角度可以沉淀成批量测试模板。

This repo packages that system into a compact open-source starter.  
这个仓库把这套系统整理成一个轻量的开源 starter。

## Repository structure｜仓库结构

```text
skills/ai-ugc-factory/        # reusable Matrix/agent skill｜可复用技能
examples/briefs/              # product brief examples｜产品 brief 示例
examples/asset-manifests/     # asset inventory examples｜素材清单示例
templates/                    # reusable production templates｜生产模板
docs/                         # GitHub Pages project website｜项目网页
docs/demo-videos/             # demo video index｜demo 视频索引
assets/contact/               # WeChat contact QR / launch placeholder｜联系与上线占位资产
scripts/                      # helper scripts｜辅助脚本
```

## Quick start｜快速开始

1. Copy `templates/product-brief.md` and fill in the product, audience, claims, and offer boundaries.  
   复制 `templates/product-brief.md`，填写产品、受众、声明边界和报价/转化目标。
2. Put real assets in a stable folder and build an asset manifest from `templates/asset-manifest.csv`.  
   把真实素材放入稳定目录，并基于 `templates/asset-manifest.csv` 建立素材清单。
3. Use `skills/ai-ugc-factory/SKILL.md` as the production workflow.  
   使用 `skills/ai-ugc-factory/SKILL.md` 作为生产流程。
4. Draft a prompt pack with `templates/video-prompt-pack.md`.  
   用 `templates/video-prompt-pack.md` 起草视频提示词包。
5. Run the QA checklist before rendering or publishing.  
   渲染或发布前执行 QA 检查。

## Demo verticals included｜已包含 demo 方向

| Vertical｜方向 | Local source｜本地来源 | Use in project｜用途 |
| --- | --- | --- |
| Pet food｜猫粮 | `/Users/agent/Downloads/猫粮 AI UGC` | UGC product ad examples｜产品 UGC 广告示例 |
| Puzzle / Kickstarter｜拼图 / Kickstarter | `/Users/agent/Downloads/PieceStory \| ads Demo` | Real-person + anime ad examples｜真人 UGC + 动漫广告示例 |
| Course education｜课程教育 | `/Users/agent/Downloads/课程教育 AI UGC` | Education/service offer ads｜课程/服务广告示例 |
| Curling iron｜卷发棒 | `/Users/agent/Downloads/Feishu20260615-145610.mp4` | Beauty device demo example｜美妆工具 demo 示例 |
| AI video SaaS｜AI 视频 SaaS | `https://aivideopro.io` | SaaS/product website ad example｜SaaS/产品站广告示例 |

Large videos are intentionally not committed into the repo by default. Use `docs/demo-videos/index.md` to reference hosted demos, local proof paths, or GitHub Release assets.  
大型视频默认不直接提交进 Git 历史。请用 `docs/demo-videos/index.md` 引用托管 demo、本地证明路径或 GitHub Release 附件。

## Project webpage｜项目网页

- GitHub Pages: https://nzmax.github.io/ai-ugc-factory/
- Demo Release: https://github.com/nzmax/ai-ugc-factory/releases/tag/v0.1.0

## Contact / early access｜联系 / 提前体验

Matrix launch link is coming soon. If you want early access, collaboration, or batch custom AI UGC production support, scan the WeChat QR code:  
Matrix 正式链接即将上线。如果你希望提前交流、合作，或需要批量定制 AI UGC 广告生产支持，可以查看微信二维码：

![WeChat QR](assets/contact/wechat-qr.jpg)

## License｜许可证

MIT. Use it, fork it, adapt it — just keep claims truthful and respect product assets you do not own.  
MIT 协议。欢迎使用、fork 和改造；请保持产品声明真实，并尊重不属于你的产品素材版权。
