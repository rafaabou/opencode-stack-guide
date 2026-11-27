# OpenCode Stack — Field Guide: OpenCode, oh-my-opencode-slim, OpenSpec, Ponytail, OpenWolf, Herdr, Engram, Persona, Graphify, skills and commands

A practical guide to running the whole stack — nine tools, 47 skills and six custom commands — as one workflow:

| Tool | Role |
|------|------|
| [OpenCode](https://github.com/anomalyco/opencode) | The host: chat, agents, tools, models |
| [oh-my-opencode-slim](https://github.com/alvinunreal/oh-my-opencode-slim) | Agent team (orchestrator, explorer, oracle, fixer, ...) |
| [OpenSpec](https://github.com/Fission-AI/OpenSpec) | Decides what to build |
| [Ponytail](https://github.com/DietrichGebert/ponytail) | Decides how little to build |
| [OpenWolf](https://github.com/cytostack/openwolf) | Remembers what was learned |
| [Herdr](https://github.com/herdrdev/herdr) | Terminals, worktrees, parallel agents |
| [Engram](https://engram.tools/) | Persistent memory across sessions (MCP + plugin) |
| [Persona](https://github.com/RuloGB/opencode-persona) | Role, language, detail level, project conventions |

Optional add-on: [Graphify](https://github.com/Graphify-Labs/graphify) builds a local,
queryable knowledge graph of the codebase as an OpenCode skill and plugin hook.

This machine also runs Engram 3.7.2 and Persona 3.0.0, and defines six custom
slash commands. Section 20 is a beginner-to-expert run from an empty folder to a
reviewed, remembered change. Section 22 walks a real project end to end;
section 21 inventories every installed tool, skill, agent, plugin, MCP server
and custom command.

The model is not the hard part. The handoffs are: what gets built, by whom,
how much code, and what we remember afterwards. This guide covers install,
commands, file locations, security, templates, and four real workflows.

Versions re-checked 2026-11-27 against official releases.

## Read it

- [Full guide (Markdown)](guide.md)
- [Full guide (PDF)](opencode-stack-user-guide.pdf)

![The stack: Herdr isolates the work, Persona and memory load context, OpenSpec scopes the change, Graphify maps the code, agents implement, Ponytail keeps the diff small, and git ships the result.](diagram.png)

## What's inside

1. The stack at a glance
2. Install from zero
3. Where everything lives
4. OpenCode: the host
5. oh-my-opencode-slim: the agent team
6. OpenSpec: decide what to build
7. Ponytail: decide how little to build
8. OpenWolf: project memory
9. Herdr: terminal workspace manager
10. Persona: role, language and conventions
11. Engram: the memory layer
12. Security and permissions
13. When not to use the stack
14. Working with the whole stack together
15. Cheat sheet
16. Troubleshooting
17. Appendix A: templates
18. Appendix B: glossary
19. Appendix C: versions, licenses and sources
20. Beginner to expert: a complete project run
21. Complete inventory: tools, skills, agents and commands
22. Real project walkthrough: every tool in its place

## Note

OpenCode, OpenSpec, Ponytail and Herdr are third-party projects. This guide
documents how I use them together. Each tool is governed by its own license.