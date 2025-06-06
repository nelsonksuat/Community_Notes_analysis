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

### NOTEBOOK navigation

(Make sure to first install all the [requirements](https://github.com/nelsonksuat/Community_Notes_analysis/blob/main/requirements.txt); this notebook is tested in Python 3.11)

### Step 1: Data Preparation (`NOTEBOOK 1 Preparing data.ipynb`)
All unnecessary columns are dropped, and participant identifiers are removed to ensure contributor anonymity. The notes, status history, and ratings datasets are cleaned and saved in a simplified format. Domains are extracted from the note summaries.

### Step 2: Verification of Source Matching (`NOTEBOOK 2 Manual annotation verification.py`)
To validate that domain-based matching to EFCSN and EDMO sources is accurate, 100 Community Notes identified as citing European fact-checkers are manually verified. This verification is stored in the `verificationSource` column. The matching for my particular study achieved 100% accuracy.

After the first two notebooks, your datasets should be organised as the following tables:

## Notes dataset structure 

| Index | Column Name                               | Description                                                                                       |
|-------|-------------------------------------------|---------------------------------------------------------------------------------------------------|
| 0     | `noteId`                                   | Unique ID of Community Note                                                                       |
| 1     | `createdAtMillis`                          | Time of Note creation                                                                             |
| 2     | `classification`                           | Reason why the Note is added: `"NOT MISLEADING"`, `"MISINFORMED"`, `"POTENTIALLY_MISLEADING"`    |
| 3     | `misleadingOther`                          | 1 if “Other” is selected as misleading reason, else 0                                             |
| 4     | `misleadingFactualError`                   | 1 if “It contains a factual error” is selected, else 0                                            |
| 5     | `misleadingManipulatedMedia`               | 1 if “It contains a digitally altered photo or video” is selected, else 0                         |
| 6     | `misleadingOutdatedInformation`            | 1 if “It contains outdated information that may be misleading” is selected, else 0                |
| 7     | `misleadingMissingImportantContext`        | 1 if “It is a misrepresentation or missing important context” is selected, else 0                 |
| 8     | `misleadingUnverifiedClaimAsFact`          | 1 if “It presents an unverified claim as a fact” is selected, else 0                              |
| 9     | `misleadingSatire`                         | 1 if “It is a joke or satire that might be misinterpreted as a fact” is selected, else 0          |
| 10    | `notMisleadingOther`                       | 1 if “Other” is selected as a reason why it's not misleading, else 0                              |
| 11    | `notMisleadingFactuallyCorrect`            | 1 if “It expresses a factually correct claim” is selected, else 0                                 |
| 12    | `notMisleadingOutdatedButNotWhenWritten`   | 1 if “This post was correct when written, but is out of date now” is selected, else 0             |
| 13    | `notMisleadingClearlySatire`               | 1 if “It is clearly satirical/joking” is selected, else 0                                         |
| 14    | `notMisleadingPersonalOpinion`             | 1 if “It expresses a personal opinion” is selected, else 0                                        |
| 15    | `trustworthySources`                       | 1 if trustworthy sources are linked, 0 if not                                                     |
| 16    | `summary`                                  | Community Note text including original URL                                                        |
| 17    | `sourceURL`                                | Extracted URL from `summary`                                                                      |
| 18    | `domainExtract`                            | Domain name extracted using `tldextract`                                                          |
| 19    | `noteFromEFCSN`                            | 1 if Note uses EFCSN fact-checker, 0 otherwise                                                    |
| 20    | `noteFromEDMO`                             | 1 if Note uses EDMO fact-checker, 0 otherwise                                                     |
| 21    | `noteFromOtherSource`                      | 1 if Note uses another source, 0 otherwise                                                        |
| 22    | `verificationSource`                       | 1 if automatic identification was correct, 0 if incorrect                                         |

## Note Status History dataset structure

| Index | Column Name                        | Description                                                                                      |
|-------|------------------------------------|--------------------------------------------------------------------------------------------------|
| 0     | `noteId`                           | Unique ID of Community Note                                                                      |
| 1     | `createdAtMillis`                  | Time of Note creation (in milliseconds)                                                          |
| 2     | `currentStatus`                    | Current status of the note: `"NEEDS_MORE_RATINGS"`, `"CURRENTLY_RATED_HELPFUL"`, `"CURRENTLY_RATED_NOT_HELPFUL"` |
| 3     | `currentStatusHelpful`            | 1 if the note is currently rated as helpful, 0 otherwise                                         |
| 4     | `currentStatusNotHelpful`         | 1 if the note is currently rated as not helpful, 0 otherwise                                     |
| 5     | `currentStatusNeedsMoreRatings`   | 1 if the note needs more ratings, 0 otherwise                                                    |
| 6     | `noteFromEFCSN`                   | 1 if the note uses an EFCSN fact-checker, 0 otherwise                                            |
| 7     | `noteFromEDMO`                    | 1 if the note uses an EDMO fact-checker, 0 otherwise                                             |
| 8     | `noteFromOtherSource`            | 1 if the note uses another source, 0 otherwise                                                   |

## Ratings Dataset Structure

| Index | Column Name                             | Description                                                                                      |
|-------|------------------------------------------|--------------------------------------------------------------------------------------------------|
| 0     | `noteId`                                 | Unique ID of Community Note                                                                      |
| 1     | `createdAtMillis`                        | Time of Note creation (in milliseconds)                                                          |
| 2     | `agree`                                  | 1 if the contributor agrees with the note, 0 otherwise                                           |
| 3     | `disagree`                               | 1 if the contributor disagrees with the note, 0 otherwise                                        |
| 4     | `helpfulnessLevel`                       | Overall helpfulness of the note: `"NOT_HELPFUL"`, `"SOMEWHAT_HELPFUL"`, `"HELPFUL"`             |
| 5     | `helpfulGoodSources`                     | 1 if “Cites high-quality sources” is selected, 0 otherwise                                       |
| 6     | `helpfulImportantContext`                | 1 if “Provides important context” is selected, 0 otherwise                                       |
| 7     | `notHelpfulSourcesMissingOrUnreliable`   | 1 if “Sources missing or unreliable” is selected, 0 otherwise                                    |
| 8     | `NotHelpfulOpinionSpeculationOrBias`     | 1 if “Opinion, speculation, or bias” is selected, 0 otherwise                                    |
| 9     | `notHelpfulHardToUnderstand`             | 1 if “Hard to understand” is selected, 0 otherwise                                               |
| 10    | `noteFromEFCSN`                          | 1 if the note uses an EFCSN fact-checker, 0 otherwise                                            |
| 11    | `noteFromEDMO`                           | 1 if the note uses an EDMO fact-checker, 0 otherwise                                             |
| 12    | `noteFromOtherSource`                    | 1 if the note uses another source, 0 otherwise                                                   |




### Step 3: Reasoning Behind Citations (`NOTEBOOK 3 Reasoning of a Note.ipynb`)
This notebook analyzes the reasons contributors provide when proposing Community Notes, especially comparing notes that cite European fact-checkers versus all other notes. This reveals potential differences in citation motives.

### Step 4: Perception of Notes (`NOTEBOOK 4 Perception of Notes citing European fact-checkers.ipynb`)
This step evaluates how notes citing European fact-checkers are rated in terms of `helpfulnessLevel` and `helpfulGoodSources`. These ratings are compared against those of notes citing other sources.

### Step 5: Publication Likelihood (`NOTEBOOK 5 Notes published on X.ipynb`)
Using the `noteStatusHistory` dataset, this analysis compares whether notes citing European fact-checkers are more or less likely to be published on X. It focuses on the `currentStatus` column.

### Methodological Justification
This methodology is adapted from Borenstein et al. (2025) and Maldita.es (2025), with added validation steps to ensure accuracy. All comparisons are made relative to the full Community Notes dataset.

## Data Summary for specific case study

- Timeframe: January 1, 2024 – May 5, 2025
- Notes collected: 805,975
- Notes citing European fact-checkers: 5,380 (~0.67%)


## Results
![Figure 1](https://github.com/nelsonksuat/Community_Notes_analysis/blob/main/Graphs/Figure%201.png)

![Figure 2](https://github.com/nelsonksuat/Community_Notes_analysis/blob/main/Graphs/Figure%202.png)

![Figure 3](https://github.com/nelsonksuat/Community_Notes_analysis/blob/main/Graphs/Figure%203.png)

![Figure 4](https://github.com/nelsonksuat/Community_Notes_analysis/blob/main/Graphs/Figure%204.png)



## Citation
If you use this work, please cite it as:

Tausk, N. (2025). *European fact-checkers within Community Notes on X Analysis*. GitHub. https://github.com/nelsonksuat/community_notes_analysis
