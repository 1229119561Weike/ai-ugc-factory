---
name: ai-ugc-factory
description: Build enterprise AI ad asset systems and batch AI UGC video production briefs. Use when a user asks for AI UGC ads, product demo videos, ad asset factories, prompt packs, or reusable video production workflows.
category: media
symbolName: video.badge.waveform
seedVersion: 1
---

# AI UGC Factory

Use this skill to turn a product or service into a repeatable AI UGC ad production system, not a one-off prompt.

## Output

Produce a compact package:

1. product brief;
2. asset manifest;
3. reference breakdown;
4. 1-3 video concepts;
5. beat-level prompt pack;
6. generation input rules;
7. QA checklist;
8. batch-learning plan.

## Workflow

### 1. Anchor product truth

Read the product website, source files, screenshots, and user notes. Separate verified facts from assumptions. Do not invent prices, discounts, certifications, bonuses, or performance claims.

### 2. Build the asset map

Rename or label assets by visual function:

- `hero-product-image`
- `packaging-detail`
- `lifestyle-context`
- `feature-proof`
- `website-cta`
- `creator-reference`
- `style-reference`
- `contact-asset`

The manifest should say which assets must be actual model inputs. A path in a prompt is not proof that the model read the image.

### 3. Choose production lanes

Pick 1-3 lanes that fit the product:

- Real-person UGC demo;
- hands/product tabletop demo;
- animated explainer;
- creator reaction / testimonial-style;
- founder/product walkthrough;
- SaaS screen + human narration.

### 4. Write beat-level prompts

Every 1-2 seconds should carry a job: hook, product proof, pain point, benefit, objection, credibility cue, visual reset, CTA.

For every segment, state:

- duration;
- aspect ratio;
- sound/voice requirements;
- exact model input images/videos to attach;
- visible product requirements;
- forbidden claims;
- QA risks.

### 5. Gate before rendering

Before final video generation, confirm any user-owned style decisions: mascot/character identity, voiceover tone, rhythm, CTA/contact asset, and whether exact captions should be post-composited.

### 6. QA the result

Require per segment:

- `MODEL_INPUT_IMAGES_ACTUALLY_ATTACHED`
- `PRODUCT_REFERENCE_WAS_IMAGE_INPUT`
- `PROMPT_ONLY_PRODUCT_REFERENCE_USED`
- `PRODUCT_VISIBLE_AND_MATCHES_REAL_ASSET`
- duration / resolution / audio present;
- text drift or brand-label issues;
- unsupported claims.

If product fidelity or text quality fails in client-facing shots, request a narrow correction pass instead of accepting the render.

## Example trigger

User: “帮我为这个产品批量生产 AI UGC 广告视频，并沉淀成可复用 workflow。”

Response shape:

- Confirm asset sources and style gates;
- Build manifest;
- Draft prompt pack;
- Send rendering work to the media/video owner;
- QA with proof;
- turn stable workflow into a reusable skill only after it succeeds.
