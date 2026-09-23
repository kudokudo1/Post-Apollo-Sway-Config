# Post-Apollo Sway Dependencies

## Compositor

Custom SwayFX / Animate-SwayFX build:

    ~/.local/opt/swayfx/bin/sway

## Quickshell

Quickshell is restarted at session startup.

Current behavior:

    pkill -x quickshell
    quickshell

The Quickshell source is maintained separately in:

    taskbars-post-apollo

## Autotiling

Current implementation uses the external `autotiling` package.

Version:

    autotiling 1.9.3

Installation:

    pipx

Python used by current installation:

    Python 3.14.7

Current executable resolves to:

    ~/.local/share/pipx/venvs/autotiling/bin/autotiling

The Sway config currently calls:

    ~/.local/bin/autotiling

Future plan:

Native autotiling may eventually be implemented directly in the custom
Animate-SwayFX / Post-Apollo compositor fork.

## Terminal

Current effective terminal variable:

    kitty zellij

Note: the config currently contains two `$term` assignments. The later
assignment wins.

## File manager

    kitty yazi

## Audio

    pactl

## Screenshots

    grim

## Wallpaper

Current configured wallpaper:

    ~/Downloads/Wallpapers/nightsky1.png

SHA-256:

    ed0038e0b39284f5f72887ae2f7c18481f77ec6f17cfdffc2793e9fb089de020

The wallpaper is intentionally not stored in this repository.

## Displays

Current machine-specific output configuration includes:

    DP-3
    HDMI-A-1

These output names are intentionally preserved in the initial baseline.
