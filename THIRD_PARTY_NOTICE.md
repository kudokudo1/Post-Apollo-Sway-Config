# THIRD-PARTY NOTICE // SWAY CONFIG LINEAGE

This repository contains a heavily customized Sway/SwayFX configuration.

## INHERITED SWAY CONFIGURATION

The root `config` file is recognizably derived from the default configuration template distributed with:

**Sway**  
https://github.com/swaywm/sway

The inherited structure includes the default explanatory comments, variables, workspace bindings, layout controls, resize mode, scratchpad examples, input/output examples, and other baseline configuration sections.

Sway is distributed under the **MIT License**.

## POST-APOLLO MODIFICATIONS

Post-Apollo changes include, among other things:

- Kitty/Zellij terminal integration
- Quickshell application and control-menu launch paths
- Post-Apollo window rules and floating geometry
- display placement and workspace policy
- SwayFX animation and shadow behavior
- Post-Apollo palette values
- custom gaps and borders
- custom media/audio bindings and workflow controls
- machine-specific runtime paths and integrations

The result is a substantially customized configuration, but its original template lineage remains visible.

## SWAYFX RELATIONSHIP

This repository configures a SwayFX-based compositor environment. The compositor source itself lives separately from this configuration repository.

Using SwayFX-specific configuration directives does not by itself place SwayFX source code inside this repository.

## PROVENANCE RULE

The inherited Sway template material remains subject to Sway's MIT terms.

The Post-Apollo license applies only to original Post-Apollo additions and modifications to the extent legally applicable and does not remove or narrow the rights granted by the upstream MIT license.
