---
name: crietee-invoice
description: "Schrijf een factuur van Crietee Software met de wettelijke regels en btw, als tekst voor een document in Crietee Werkplek. Gebruik bij factuur, uren factureren of een herinnering. Niet voor offertes, contracten of weekplannen."
type: workflow
lifecycle: active
---

# Crietee factuur

Schrijf een factuur die een boekhouder kan inboeken. De huisstijl volgt [crietee-brand](../crietee-brand/SKILL.md). Wettelijke velden staan in [references/fields.md](references/fields.md).

## Wanneer

Gebruik bij: factuur, uren factureren, herinnering.

Niet bij: offerte, voorstel, contract, weekplan.

## Standaardwaarden

| Veld | Standaard |
|---|---|
| Verkoper | Crietee Software, eenmanszaak. Naam, adres, KvK en btw-id komen uit de instellingen van de werkplek |
| Tarief | Uit de offerte of uit de uren. Vraag het als het ontbreekt |
| Btw | 21%. Alleen 0% met de KOR-zin als Levi zegt dat de kleineondernemersregeling geldt |
| Betaaltermijn | 14 dagen |
| Nummer | Geeft de werkplek: INV-JJJJ-NNN. Hergebruik nooit een nummer |
| Valuta | Euro |
| Taal | Nederlands |

## Werkwijze

1. Lees de huisstijl in `crietee-brand`.
2. Factureer alleen uren die bestaan. Ontbreekt de klant, de periode of de uren, dan vraag je ernaar. Verzin geen uren.
3. Lever het document in de vorm die de werkplek vraagt:
   - **Titel:** "Factuur" met de periode of de opdracht, kort, zonder punt.
   - **Inleiding:** één zin met de periode of het project.
   - **Regels:** per regel de omschrijving, het aantal uren en het tarief per uur, excl. btw.
   - **Betaling:** het betaaltermijn en de reden, bijvoorbeeld het factuurnummer als betalingskenmerk.
4. Bedragen, btw en het totaal berekent de werkplek uit de regels.

## Niet doen

- Geen factuur zonder nummer van de werkplek.
- Geen factuur als "betaald" markeren, tenzij Levi dat zegt.
- Creditnota's maakt de werkplek nog niet. Zeg dat tegen Levi, en maak er geen losse nota van.
