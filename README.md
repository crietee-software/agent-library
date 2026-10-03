# Skills

Persoonlijke skills die Grok in elke sessie kan laden. Elke skill is een map met een `SKILL.md`.

Grok leest deze map via `~/.grok/config.toml`:

```toml
[skills]
paths = ["~/Documents/GitHub/skills"]
```

Skills die al via Claude of de agents-map geïnstalleerd zijn (`~/.claude/skills`, `~/.agents/skills`) blijven daar staan en blijven werken. Zet hier de skills die je zelf beheert.

## Nieuwe skill

Maak een map met de skillnaam. Alleen kleine letters, cijfers en koppeltekens. Begin en eindig met een letter of cijfer.

```
mijn-skill/
  SKILL.md
  references/   # optioneel, langere uitleg
  scripts/      # optioneel, helpers
```

`SKILL.md`:

```markdown
---
name: mijn-skill
description: Wat de skill doet, in een of twee zinnen. Use when de gebruiker X vraagt, of /mijn-skill gebruikt.
---

# Mijn skill

Korte procedure die de agent uitvoert.
```

Het `description`-veld bepaalt wanneer Grok de skill zelf start. Noem daarin de situatie en de slash-command.

Daarna is de skill beschikbaar als `/mijn-skill`. Grok herlaadt skills zodra de bestanden op schijf veranderen.

## Controleren

```bash
grok inspect
```

Skills uit deze map krijgen als bron `config`.
