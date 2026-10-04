✦︎✦︎✦︎ Meta Apollo Logos //

# 🖳 SWAYFX // POST-APOLLO CONFIG

![](BUILD/assets/design/chassis/focus-rail.svg)

![SwayFX // Post-Apollo Config](./BUILD/assets/design/sway-config-banner.svg)

> **STATE //** active \~\~ **VIEW //** desktop compositor/session configuration

The desktop behavior and session layer of the Post-Apollo Family — enhancing the relationship between operator, input, applications, workspaces, displays, and environment, turning compositor capabilities into a lived set of rules for how the desktop launches, moves, focuses, arranges, and responds during everyday use.

**FAMILY //** [META APOLLO LOGOS](https://github.com/kudokudo1/Meta-Apollo-Logos) · [DEV EXP](https://github.com/kudokudo1/The-Post-Apollo-Dev-Exp) · [FOREST](https://github.com/kudokudo1/The-Post-Apollo-Forest-Project) · [TASKBARS](https://github.com/kudokudo1/taskbars-post-apollo)

### 🧭 MAP // REPOSITORY

![](BUILD/assets/design/chassis/nav-rail.svg)

// [🧭 ATLAS](./ATLAS/) \~\~ // [✮˙๋࣭⭑ MODEL](./MODEL/) \~\~ // [🖨 BUILD](./BUILD/) \~\~ // [⚒ DEV](./DEV/) \~\~ // [🖳 OPERATE](./OPERATE/) \~\~ // [⊹ ࣪ℼ˖ EVIDENCE](./EVIDENCE/) \~\~ // [࣪⋅˚🕮‧₊˚ ARCHIVE](./ARCHIVE/)

---

### ★⋆˙ CORE // RUNTIME LAYOUT

The live `config` file stays where Sway expects it. Meta Apollo rooms provide documentation and semantic organization without relocating the runtime configuration.

---

Live Sway/SwayFX configuration for the Post-Apollo desktop.

This repository contains the user/session configuration layer and is separate
from the custom SwayFX compositor source repository.

## Current compositor

The running compositor is the custom SwayFX build located at:

    ~/.local/opt/swayfx/bin/sway

The compositor source itself is maintained separately in the animate-swayfx
repository.

## Purpose

This repository preserves the known-working desktop configuration including:

- displays
- workspaces
- gaps
- window rules
- keybindings
- Quickshell startup
- terminal/file-manager commands
- audio/media controls
- external helper dependencies

## Portability

The initial baseline intentionally preserves machine-specific paths and output
names exactly as they exist on the working system.

These may be generalized in later commits.
