# Demo Videos｜Demo 视频

This project supports a demo gallery without forcing large video files into Git history.  
本项目支持 demo 视频展示，但默认不把大视频文件直接提交进 Git 历史。

## Recommended publishing pattern｜推荐发布方式

1. Upload demo videos to GitHub Releases, object storage, or your product website.  
   将 demo 视频上传到 GitHub Releases、对象存储或产品官网。
2. Replace local source paths with public URLs.  
   用公开 URL 替换本地源路径。
3. Keep the manifest fields: vertical, format, duration, product truth, and production notes.  
   保留清单字段：行业方向、格式、时长、产品事实、制作说明。

## Public demo release｜公开 demo release

Representative demo videos are attached to the first release:  
首版 release 已附带代表性 demo 视频：

- [AI UGC Factory v0.1.0 demos](https://github.com/nzmax/ai-ugc-factory/releases/tag/v0.1.0)

## Demo slots｜Demo 展示位

| Slot｜展示位 | Public asset｜公开附件 | Notes｜说明 |
| --- | --- | --- |
| Pet food AI UGC｜猫粮 AI UGC | `pet-food-short-demo.mp4` | Short vertical product UGC sample｜短竖屏产品 UGC 示例 |
| PieceStory puzzle real-person｜PieceStory 真人 UGC | `piecestory-realperson-demo.mp4` | 30s real-person UGC demo｜30 秒真人 UGC demo |
| PieceStory puzzle anime｜PieceStory 动漫广告 | `piecestory-anime-demo.mp4` | 25s animated ad demo｜25 秒动漫广告 demo |
| Course education｜课程教育 | `course-education-demo-a.mp4` | Education/service offer sample｜课程/服务广告示例 |
| Curling iron｜卷发棒 | `curling-iron-demo.mp4` | 15s beauty device demo｜15 秒美妆工具 demo |
| AIVideoPro.io | pending｜待补充 | Add SaaS demo when public release asset is ready｜公开 SaaS demo 准备好后补充 |

## QA expectation｜QA 要求

Every public demo should state:  
每个公开视频 demo 都应说明：

- whether real product assets were used as model-readable inputs;  
  是否使用真实产品素材作为模型可读取输入；
- duration and aspect ratio;  
  时长与画幅；
- voice/audio status;  
  语音/音频状态；
- whether exact captions were model-native or post-composited;  
  精确字幕是模型原生生成还是后期合成；
- claims that were verified vs intentionally avoided.  
  哪些产品声明已验证，哪些声明被刻意避免。
