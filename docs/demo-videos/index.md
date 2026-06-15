# Demo Videos

This project supports a demo gallery without forcing large video files into Git history.

Recommended publishing pattern:

1. Upload demo videos to GitHub Releases, object storage, or your product website.
2. Replace the local source paths below with public URLs.
3. Keep the manifest fields: vertical, format, duration, product truth, and production notes.

## Public demo release

Representative demo videos are attached to the first release:

- [AI UGC Factory v0.1.0 demos](https://github.com/nzmax/ai-ugc-factory/releases/tag/v0.1.0)

## Demo slots

| Slot | Public asset | Notes |
| --- | --- | --- |
| Pet food AI UGC | `pet-food-short-demo.mp4` | Short vertical product UGC sample. |
| PieceStory puzzle real-person | `piecestory-realperson-demo.mp4` | 30s real-person UGC demo. |
| PieceStory puzzle anime | `piecestory-anime-demo.mp4` | 25s animated ad demo. |
| Course education | `course-education-demo-a.mp4` | Education/service offer sample. |
| Curling iron | `curling-iron-demo.mp4` | 15s beauty device demo. |
| AIVideoPro.io | pending | Add SaaS demo when public release asset is ready. |

## QA expectation

Every public demo should state:

- whether real product assets were used as model-readable inputs;
- duration and aspect ratio;
- voice/audio status;
- whether exact captions were model-native or post-composited;
- claims that were verified vs intentionally avoided.
