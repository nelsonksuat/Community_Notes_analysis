# European Fact-Checkers within Community Notes on X

This repository contains the code used in the study *European Fact-Checkers within Community Notes on X* (Tausk, 2025).

## Overview
This project analyzes how often European fact-checking organisations are cited in Community Notes on X (formerly Twitter), their reasons for being cited, how they are rated by other contributors, and how often such notes get published.

## Data Availability
All data used in this project comes from X's [Community Notes public datasets](https://communitynotes.x.com/guide/nl/under-the-hood/download-data). The datasets are available as regularly updated `.tsv` files and include detailed documentation on structure and fields.

### Datasets Used:
- `notes-*.tsv`: contains the content of the note, source URLs, and contributor justifications.
- `noteStatusHistory-*.tsv`: captures the visibility status of each note (e.g., helpful or not helpful).
- `ratings-*.tsv`: includes individual rating feedback on Community Notes.

These files are imported into pandas DataFrames, cleaned, and linked using the shared `noteId` column.

## NOTEBOOK navigation

### Step 1: Data Preparation (`NOTEBOOK 1 Preparing data.ipynb`)
All unnecessary columns are dropped, and participant identifiers are removed to ensure contributor anonymity. The notes, status history, and ratings datasets are cleaned and saved in a simplified format. Domains are extracted from the note summaries.

### Step 2: Verification of Source Matching (`NOTEBOOK 2 Manual annotation verification.py`)
To validate that domain-based matching to EFCSN and EDMO sources is accurate, 100 Community Notes identified as citing European fact-checkers are manually verified. This verification is stored in the `verificationSource` column. The matching for my particular study achieved 100% accuracy.

### Step 3: Reasoning Behind Citations (`NOTEBOOK 3 Reasoning of a Note.ipynb`)
This notebook analyzes the reasons contributors provide when proposing Community Notes, especially comparing notes that cite European fact-checkers versus all other notes. This reveals potential differences in citation motives.

### Step 4: Perception of Notes (`NOTEBOOK 4 Perception of Notes citing European fact-checkers.ipynb`)
This step evaluates how notes citing European fact-checkers are rated in terms of `helpfulnessLevel` and `helpfulGoodSources`. These ratings are compared against those of notes citing other sources.

### Step 5: Publication Likelihood (`NOTEBOOK 5 Notes published on X.ipynb`)
Using the `noteStatusHistory` dataset, this analysis compares whether notes citing European fact-checkers are more or less likely to be published on X. It focuses on the `currentStatus` column.

### Methodological Justification
This methodology is adapted from Borenstein et al. (2025) and Maldita.es (2025), with added validation steps to ensure accuracy. All comparisons are made relative to the full Community Notes dataset.

## Data Summary for specific case-study

- Timeframe: January 1, 2024 – May 5, 2025
- Notes collected: 805,975
- Notes citing European fact-checkers: 5,380 (~0.67%)

## Citation
If you use this work, please cite it as:

Tausk, N. (2025). *European fact-checkers within Community Notes on X Analysis*. GitHub. https://github.com/nelsonksuat/community_notes_analysis
