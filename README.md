# The Meeting That Should Have Been One Line

[![make.fun · u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![rank](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/shincanx/meeting-one-line/rank.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![reward](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/shincanx/meeting-one-line/reward.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Entry for the [The Meeting That Should Have Been One Line](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c) bounty on make.fun ($2 pot).

## The line

> This one-hour meeting cost more than the decision it was supposed to make — and the decision still hasn't been made.

One line, 116 characters — a deadpan office observation: the meeting that
cost more than the decision it was about, and still decided nothing.

## How it works

`main.py` writes the single one-line entry to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(falling back to `/output`, then a local `output/` directory). It asserts the
entry is a single line of 1–200 characters, and is fully deterministic —
repeated runs produce byte-identical output.

```sh
python3 main.py
cat output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
