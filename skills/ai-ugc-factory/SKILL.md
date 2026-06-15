---
name: ai-ugc-factory
description: Build enterprise AI ad asset systems and batch AI UGC video production briefs. Use when a user asks for AI UGC ads, product demo videos, ad asset factories, prompt packs, or reusable video production workflows.
category: media
symbolName: video.badge.waveform
seedVersion: 2
---

# AI UGC Factory｜AI UGC 广告工厂

Use this skill to turn a product or service into a repeatable AI UGC ad production system, not a one-off prompt.  
使用这个 skill，把一个产品或服务转成可重复运行的 AI UGC 广告生产系统，而不是一次性 prompt。

## Output｜输出内容

Produce a compact package:  
输出一个轻量生产包：

1. product brief｜产品 brief；
2. asset manifest｜素材资产清单；
3. reference breakdown｜参考视频/参考图拆解；
4. 1-3 video concepts｜1–3 个视频创意方向；
5. beat-level prompt pack｜1–2 秒级分镜提示词包；
6. generation input rules｜生成输入规则；
7. QA checklist｜质检清单；
8. batch-learning plan｜批量测试与复盘计划。

## Workflow｜工作流

### 1. Anchor product truth｜锚定产品事实

Read the product website, source files, screenshots, and user notes. Separate verified facts from assumptions. Do not invent prices, discounts, certifications, bonuses, or performance claims.  
读取产品官网、源文件、截图和用户说明。区分已验证事实和推测。不要编造价格、折扣、认证、赠品或效果承诺。

### 2. Build the asset map｜建立素材地图

Rename or label assets by visual function:  
按视觉功能重命名或标记素材：

- `hero-product-image`｜主产品图
- `packaging-detail`｜包装/细节
- `lifestyle-context`｜生活场景
- `feature-proof`｜功能证明
- `website-cta`｜网页/CTA
- `creator-reference`｜真人/创作者参考
- `style-reference`｜风格参考
- `contact-asset`｜联系/转化资产

The manifest should say which assets must be actual model inputs. A path in a prompt is not proof that the model read the image.  
素材清单必须说明哪些素材需要作为真实模型输入。只在 prompt 里写路径，不等于模型真的读取了图片。

### 3. Choose production lanes｜选择生产路线

Pick 1-3 lanes that fit the product:  
根据产品选择 1–3 条视频生产路线：

- Real-person UGC demo｜真人 UGC demo；
- hands/product tabletop demo｜手部/桌面产品演示；
- animated explainer｜动画解释视频；
- creator reaction / testimonial-style｜创作者反应/证言风格；
- founder/product walkthrough｜创始人/产品 walkthrough；
- SaaS screen + human narration｜SaaS 屏幕录制 + 真人口播。

### 4. Write beat-level prompts｜写分镜级提示词

Every 1-2 seconds should carry a job: hook, product proof, pain point, benefit, objection, credibility cue, visual reset, CTA.  
每 1–2 秒画面都应承担一个明确任务：钩子、产品证明、痛点、利益点、异议、可信度、视觉重置或 CTA。

For every segment, state:  
每个片段都要写清：

- duration｜时长；
- aspect ratio｜画幅；
- sound/voice requirements｜声音/口播要求；
- exact model input images/videos to attach｜实际要附加的模型输入图片/视频；
- visible product requirements｜产品可见性要求；
- forbidden claims｜禁止声明；
- QA risks｜质检风险。

### 5. Gate before rendering｜渲染前确认门槛

Before final video generation, confirm any user-owned style decisions: mascot/character identity, voiceover tone, rhythm, CTA/contact asset, and whether exact captions should be post-composited.  
最终生成前，确认所有用户拥有的风格决策：角色/吉祥物、口播语气、节奏、CTA/联系资产，以及精确字幕是否需要后期合成。

### 6. QA the result｜质检成片

Require per segment:  
每个片段必须检查：

- `MODEL_INPUT_IMAGES_ACTUALLY_ATTACHED`
- `PRODUCT_REFERENCE_WAS_IMAGE_INPUT`
- `PROMPT_ONLY_PRODUCT_REFERENCE_USED`
- `PRODUCT_VISIBLE_AND_MATCHES_REAL_ASSET`
- duration / resolution / audio present｜时长 / 分辨率 / 音频；
- text drift or brand-label issues｜文字漂移或品牌标签问题；
- unsupported claims｜未证实声明。

If product fidelity or text quality fails in client-facing shots, request a narrow correction pass instead of accepting the render.  
如果客户可见镜头中的产品一致性或文字质量失败，应要求窄范围返修，而不是直接接受成片。

## Example trigger｜触发示例

User: “帮我为这个产品批量生产 AI UGC 广告视频，并沉淀成可复用 workflow。”

Response shape｜响应结构：

- Confirm asset sources and style gates｜确认素材来源和风格门槛；
- Build manifest｜建立素材清单；
- Draft prompt pack｜起草提示词包；
- Send rendering work to the media/video owner｜把渲染交给媒体/视频 owner；
- QA with proof｜带证明做 QA；
- turn stable workflow into a reusable skill only after it succeeds｜流程跑通后再沉淀成可复用 skill。
