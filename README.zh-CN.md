# AI UGC 广告工厂

[English README](README.md) · [English website](https://1229119561weike.github.io/ai-ugc-factory/en/) · [中文网站](https://1229119561weike.github.io/ai-ugc-factory/zh/) · [Demo Release](https://github.com/1229119561Weike/ai-ugc-factory/releases/tag/v0.1.0)

**AI UGC Factory** 是一个开源工作流项目，用来搭建企业级 AI 广告资产体系，并批量生产 AI UGC 广告视频。

它适合创始人、增长团队、营销机构和内容创作者：不再只依赖一次性 prompt，而是沉淀一套可复用生产线，包括产品 brief、素材资产整理、参考控制、UGC 脚本设计、生成提示词包、质检门槛、demo 包装与投放学习闭环。

> Matrix 即将上线：正式产品链接稍后发布。如需提前交流或合作，可查看 [`assets/contact/wechat-qr.jpg`](assets/contact/wechat-qr.jpg)。

## 这个项目包含什么

- 一个可复用的 **AI UGC Factory skill**，把产品素材转成可执行的视频生产 brief。
- 真实产品图、网页、参考图、参考视频、联系资产的素材清单模板。
- UGC 视频、demo reel、广告资产系统的提示词包示例。
- 独立英文页面和独立中文页面。
- 托管在 GitHub Release 的可直接播放 demo 视频。

## 为什么需要它

很多 AI 广告流程失败，是因为把视频生成误以为只是“写 prompt”。真正稳定的产出，通常来自一套系统：

1. 真实产品素材按功能命名和整理；
2. 参考图片/视频作为模型可读取输入，而不是只在 prompt 里描述；
3. 每 1–2 秒画面都有明确任务：钩子、证明、利益点、异议、CTA；
4. 口播、节奏、画面和产品声明都经过 QA；
5. 跑通的角度可以沉淀成批量测试模板。

这个仓库把这套系统整理成一个轻量的开源 starter。

## 仓库结构

```text
skills/ai-ugc-factory/        # 可复用 Matrix/agent skill
examples/briefs/              # 产品 brief 示例
examples/asset-manifests/     # 素材清单示例
examples/prompt-packs/        # 提示词包示例
templates/                    # 可复用生产模板
docs/                         # GitHub Pages 项目网站
assets/contact/               # 提前体验联系资产
scripts/                      # 辅助脚本
```

## 快速开始

1. 复制 `templates/product-brief.md`，填写产品、受众、声明边界和报价/转化目标。
2. 把真实素材放入稳定目录，并基于 `templates/asset-manifest.csv` 建立素材清单。
3. 使用 `skills/ai-ugc-factory/SKILL.md` 作为生产流程。
4. 用 `templates/video-prompt-pack.md` 起草视频提示词包。
5. 渲染或发布前执行 QA 检查。

## Demo 视频

Demo 视频可以在 README 里直接播放，也可以在项目页面或 Release 页面查看：

- 英文页面：https://1229119561weike.github.io/ai-ugc-factory/en/
- 中文页面：https://1229119561weike.github.io/ai-ugc-factory/zh/
- Release：https://github.com/1229119561Weike/ai-ugc-factory/releases/tag/v0.1.0

大型视频不直接提交进 git 历史，而是作为 GitHub Release 附件托管。

### 猫粮短版 UGC

<video controls width="260" src="https://github.com/1229119561Weike/ai-ugc-factory/releases/download/v0.1.0/Feishu20260615-145618.mp4"></video>

[下载 MP4](https://github.com/1229119561Weike/ai-ugc-factory/releases/download/v0.1.0/Feishu20260615-145618.mp4)

### 猫粮长版 UGC

<video controls width="260" src="https://github.com/1229119561Weike/ai-ugc-factory/releases/download/v0.1.0/Feishu20260615-145621.mp4"></video>

[下载 MP4](https://github.com/1229119561Weike/ai-ugc-factory/releases/download/v0.1.0/Feishu20260615-145621.mp4)

### 猫粮产品 Demo A

<video controls width="260" src="https://github.com/1229119561Weike/ai-ugc-factory/releases/download/v0.1.0/Feishu20260615-145625.mp4"></video>

[下载 MP4](https://github.com/1229119561Weike/ai-ugc-factory/releases/download/v0.1.0/Feishu20260615-145625.mp4)

### 猫粮产品 Demo B

<video controls width="260" src="https://github.com/1229119561Weike/ai-ugc-factory/releases/download/v0.1.0/Feishu20260615-145628.mp4"></video>

[下载 MP4](https://github.com/1229119561Weike/ai-ugc-factory/releases/download/v0.1.0/Feishu20260615-145628.mp4)

### PieceStory 真人 Demo

<video controls width="260" src="https://github.com/1229119561Weike/ai-ugc-factory/releases/download/v0.1.0/PieceStory_DemoA_realperson_30s_9x16.mp4"></video>

[下载 MP4](https://github.com/1229119561Weike/ai-ugc-factory/releases/download/v0.1.0/PieceStory_DemoA_realperson_30s_9x16.mp4)

### PieceStory 动漫 Demo

<video controls width="260" src="https://github.com/1229119561Weike/ai-ugc-factory/releases/download/v0.1.0/PieceStory_DemoB_anime_25s_9x16.mp4"></video>

[下载 MP4](https://github.com/1229119561Weike/ai-ugc-factory/releases/download/v0.1.0/PieceStory_DemoB_anime_25s_9x16.mp4)

### 课程教育 Demo A

<video controls width="260" src="https://github.com/1229119561Weike/ai-ugc-factory/releases/download/v0.1.0/Feishu20260615-145558.mp4"></video>

[下载 MP4](https://github.com/1229119561Weike/ai-ugc-factory/releases/download/v0.1.0/Feishu20260615-145558.mp4)

### 课程教育 Demo B

<video controls width="260" src="https://github.com/1229119561Weike/ai-ugc-factory/releases/download/v0.1.0/Feishu20260615-145604.mp4"></video>

[下载 MP4](https://github.com/1229119561Weike/ai-ugc-factory/releases/download/v0.1.0/Feishu20260615-145604.mp4)

### 卷发棒 Demo

<video controls width="260" src="https://github.com/1229119561Weike/ai-ugc-factory/releases/download/v0.1.0/Feishu20260615-145610.mp4"></video>

[下载 MP4](https://github.com/1229119561Weike/ai-ugc-factory/releases/download/v0.1.0/Feishu20260615-145610.mp4)

## 联系 / 提前体验

Matrix 正式链接即将上线。如果你希望提前交流、合作，或需要批量定制 AI UGC 广告生产支持，可以查看联系资产：

![WeChat QR](assets/contact/wechat-qr.jpg)

## 许可证

MIT 协议。欢迎使用、fork 和改造；请保持产品声明真实，并尊重不属于你的产品素材版权。
