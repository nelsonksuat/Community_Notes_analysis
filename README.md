# European Fact-Checkers within Community Notes on X

This repository contains the data processing scripts, source lists, and analysis for the project *European Fact-Checkers within Community Notes on X* (Tausk, 2025).

## Overview

This project investigates the presence and role of European fact-checking organisations in Community Notes on X (formerly Twitter). It analyzes how often these sources are cited, why they are cited, how they are perceived, and whether their contributions are more or less likely to be published by X.

## Methodology

### Step 1: Data Collection and Preparation

We use publicly available `.tsv` datasets from X’s Community Notes project. Three datasets are used:

- **Notes**: Contains the community-contributed notes with summary text, source URLs, and annotation reasons.
- **Note Status History**: Indicates whether each note is rated as helpful, unhelpful, or still needs more ratings.
- **Ratings**: Contains user-level ratings of individual notes.

All datasets are merged using the unique `noteId`. Participant IDs are removed to preserve privacy. Column selections and modifications are documented in the appendices.

### Step 2: Identifying Fact-Checker Sources

Two manually curated lists of European fact-checkers are used:

- EFCSN (European Fact-Checking Standards Network)
- EDMO (European Digital Media Observatory)

These lists are saved in `.txt` format and matched against the `sourceURL` column in the Notes dataset.

### Step 3: URL Extraction

We use `tldextract` to extract base domains from the `summary` field and match them against the EFCSN and EDMO lists. To validate our matching method, 100 notes are manually checked; the match accuracy was 100%. This information is stored in the `verificationSource` column.

### Step 4: Motives Behind Citations

We compare the distribution of contributor-provided reasons for submitting notes between:

- Notes citing European fact-checkers
- All other notes

This reveals whether European sources are invoked for specific topics or similar to other sources.

### Step 5: Perception of Notes

Using the Ratings dataset, we compare how helpful notes citing European fact-checkers are perceived to be versus other notes. Variables analyzed include `helpfulnessLevel` and `helpfulGoodSources`.

### Step 6: Publication on X

We examine whether notes citing European fact-checkers are more or less likely to be rated as helpful and published on X, using the `currentStatus` column from the Note Status History.

### Methodological Justification

This methodology draws on approaches used by Borenstein et al. (2025) and Maldita.es (2025), who developed procedures for working with Community Notes and domain-level classification. The validation step (Step 3) ensures precision. Comparative analyses across all notes increase the robustness of the findings.

## Data Summary

- Total collected notes: **805,975** (from Jan 1, 2024 to May 5, 2025)
- Notes citing European fact-checkers: **5,380** (≈ 0.67%)

## Repository Structure

