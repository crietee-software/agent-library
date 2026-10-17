# Agent library

Persoonlijke skills en agents. Grok leest deze map op deze machine.

| Map | Wat je erin zet | Hoe Grok het laadt |
| --- | --- | --- |
| `skills/` | Een map per skill, met `SKILL.md` | `~/.grok/config.toml` → `[skills] paths` |
| `agents/` | Eén `.md` per subagent | `~/.grok/agents` wijst hierheen |

Skills die al in `~/.claude/skills` of `~/.agents/skills` staan blijven daar en blijven werken.

## Skill

```text
skills/mijn-skill/SKILL.md
```

```markdown
---
name: mijn-skill
description: Wat de skill doet. Use when de gebruiker X vraagt, of /mijn-skill gebruikt.
---

# Mijn skill

Korte procedure die de agent uitvoert.
```

Aanroepen als `/mijn-skill`.

## Subagent

```text
agents/researcher.md
```

```markdown
---
name: researcher
description: Wanneer de hoofdagent deze subagent moet starten.
prompt_mode: full
---

Instructies voor de subagent. Dit is zijn hele opdrachtkader.
```

De bestandsnaam zonder `.md` is het type. Een nieuwe Grok-sessie kan hem starten als subagent `researcher`.

## Agents met een stijl

Er zijn geen aparte personas meer. Zet de stijl of werkwijze in het agentbestand zelf, onder een kop `## Persona instructions`. Eén bestand per agent, en de app en Grok lezen hetzelfde.

## Controleren

```bash
grok inspect
```
