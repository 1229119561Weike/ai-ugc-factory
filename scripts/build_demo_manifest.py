#!/usr/bin/env python3
"""Create or refresh a demo asset manifest from local video paths.

This script intentionally avoids third-party dependencies. It can be extended to
parse MP4 metadata if needed; the starter manifest is kept human-editable.
"""
from pathlib import Path

ROOTS = [
    Path('/Users/agent/Downloads/猫粮 AI UGC'),
    Path('/Users/agent/Downloads/PieceStory | ads Demo'),
    Path('/Users/agent/Downloads/课程教育 AI UGC'),
]

for root in ROOTS:
    if not root.exists():
        continue
    print(f'## {root}')
    for path in sorted(root.glob('*.mp4')):
        print(f'- {path.name} ({path.stat().st_size / 1024 / 1024:.2f} MB)')
