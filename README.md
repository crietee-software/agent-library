# Agent library

Persoonlijke skills en subagent-bestanden. Grok leest deze map op deze machine.

| Map | Wat je erin zet | Hoe Grok het laadt |
| --- | --- | --- |
| `skills/` | Een map per skill, met `SKILL.md` | `~/.grok/config.toml` → `[skills] paths` |
| `agents/` | Eén `.md` per subagent | `~/.grok/agents` wijst hierheen |
| `personas/` | Eén `.toml` per persona | `~/.grok/personas` wijst hierheen |

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

## Persona

Een persona is een gedragslaag bovenop een subagent. Het type, het model en de tools veranderen niet.

```text
personas/concise.toml
```

```toml
description = "Korte antwoorden, zonder omhaal."
instructions = """
Wees kort. Geen inleiding, geen herhaling van de vraag.
"""
```

De bestandsnaam zonder `.toml` is de personanaam.

## Controleren

```bash
grok inspect
```
