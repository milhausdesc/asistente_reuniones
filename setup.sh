#!/bin/bash
pip install -r requirements.txt
streamlit run app.py --server.port=$PORT --server.enableCORS=false
