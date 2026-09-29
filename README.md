# bio-api-tester

A minimal Streamlit app that takes a protein ID and queries three biological APIs live:

- **NCBI** E-utilities (esearch, protein database)
- **UniProt** REST API
- **InterPro** API

The returned JSON is displayed directly in the app.

All data is fetched live from the APIs. No local biological data (CSV, Excel, JSON, FASTA, etc.) is used.

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

## Example

Enter protein ID `P69905` (human hemoglobin subunit alpha) and click any of the query buttons.

The NCBI email and API key are optional; enter your own in the app. No API key is stored in the code.
