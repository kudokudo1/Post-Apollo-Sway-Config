# Post-Apollo Sway Configuration

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
