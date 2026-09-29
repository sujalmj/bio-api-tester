import streamlit as st
import requests

st.title("Bio API Tester")

protein_id = st.text_input("Protein ID", value="P69905")
email = st.text_input("NCBI email")
api_key = st.text_input("NCBI API key", type="password")

if st.button("Query NCBI"):
    params = {"db": "protein", "term": protein_id, "retmode": "json"}
    if email:
        params["email"] = email
    if api_key:
        params["api_key"] = api_key
    try:
        r = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi", params=params, timeout=30)
        r.raise_for_status()
        st.json(r.json())
    except Exception as e:
        st.error(f"NCBI request failed: {e}")

if st.button("Query UniProt"):
    try:
        r = requests.get(f"https://rest.uniprot.org/uniprotkb/{protein_id}", headers={"Accept": "application/json"}, timeout=30)
        r.raise_for_status()
        st.json(r.json())
    except Exception as e:
        st.error(f"UniProt request failed: {e}")

if st.button("Query InterPro"):
    try:
        r = requests.get(f"https://www.ebi.ac.uk/interpro/api/entry/InterPro/protein/uniprot/{protein_id}/", timeout=30)
        r.raise_for_status()
        st.json(r.json())
    except Exception as e:
        st.error(f"InterPro request failed: {e}")
