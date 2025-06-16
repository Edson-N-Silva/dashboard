# tests/test_data_loading.py
import pandas as pd

def test_carregamento_dados():
    df = pd.read_csv('acidentes2025_todas_causas_tipos.csv', delimiter=';', encoding='latin1')
    assert not df.empty
