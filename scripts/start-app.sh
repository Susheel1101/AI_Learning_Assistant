#!/bin/bash
cd "$(dirname "$0")/../app"
streamlit run app.py --server.port 8502