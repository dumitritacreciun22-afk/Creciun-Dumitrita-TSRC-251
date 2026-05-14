import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import seaborn as sns
import matplotlib.pyplot as plt

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


np.random.seed(42)

nr_inregistrari = 1000

produse = {
    "Laptop": "Electronice",
    "Telefon": "Electronice",
    "Mouse": "Electronice",
    "Birou": "Mobilier",
    "Scaun": "Mobilier",
    "Carte": "Carti",
    "Casti": "Electronice",
    "Monitor": "Electronice"
}

orase = ["Bucuresti", "Cluj", "Iasi", "Timisoara", "Brasov"]

data_start = datetime(2025, 1, 1)

date = []

for i in range(nr_inregistrari):

    produs = random.choice(list(produse.keys()))
    categorie = produse[produs]

    pret = np.random.randint(50, 5000)
    cantitate = np.random.randint(1, 5)

    data_comanda = data_start + timedelta(days=np.random.randint(0, 90))

    date.append([
        i + 1,
        data_comanda,
        produs,
        categorie,
        pret,
        cantitate,
        random.choice(orase)
    ])

df = pd.DataFrame(date, columns=[
    "id_comanda",
    "data",
    "produs",
    "categorie",
    "pret",
    "cantitate",
    "oras"
])

df["valoare_totala"] = df["pret"] * df["cantitate"]

print(df.head())


vanzari_pe_zi = df.groupby("data")["valoare_totala"].sum().reset_index()

vanzari_pe_categorie = df.groupby("categorie")["valoare_totala"].sum().reset_index()

media_comenzi = df["valoare_totala"].mean()
print("Media valorii comenzilor:", media_comenzi)

top_produse = df.groupby("produs")["cantitate"].sum().sort_values(ascending=False).head(5)
print(top_produse)


es = Elasticsearch("http://localhost:9200")

index_name = "vanzari_index"

mapping = {
    "mappings": {
        "properties": {
            "id_comanda": {"type": "integer"},
            "data": {"type": "date"},
            "produs": {"type": "keyword"},
            "categorie": {"type": "keyword"},
            "pret": {"type": "float"},
            "cantitate": {"type": "integer"},
            "oras": {"type": "keyword"},
            "valoare_totala": {"type": "float"}
        }
    }
}

if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body=mapping)


def generator_date(df):

    for _, row in df.iterrows():

        yield {
            "_index": index_name,
            "_source": row.to_dict()
        }


bulk(es, generator_date(df))


query = {
    "size": 0,
    "aggs": {
        "vanzari_categorie": {
            "terms": {"field": "categorie"},
            "aggs": {
                "total_vanzari": {
                    "sum": {"field": "valoare_totala"}
                }
            }
        }
    }
}

response = es.search(index=index_name, body=query)

print(response)


fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# 1. Evolutia zilnica a vanzarilor
sns.lineplot(data=vanzari_pe_zi, x="data", y="valoare_totala", ax=axs[0, 0])
axs[0, 0].set_title("Evolutia zilnica a vanzarilor")
axs[0, 0].tick_params(axis='x', rotation=45)

# 2. Vanzari pe categorie
sns.barplot(data=vanzari_pe_categorie, x="categorie", y="valoare_totala", ax=axs[0, 1])
axs[0, 1].set_title("Total vanzari pe categorie")

# 3. Distributia valorii comenzilor
sns.boxplot(data=df, y="valoare_totala", ax=axs[1, 0])
axs[1, 0].set_title("Distributia valorii comenzilor")

# 4. Corelatii
sns.heatmap(
    df[["pret", "cantitate", "valoare_totala"]].corr(),
    annot=True,
    cmap="coolwarm",
    ax=axs[1, 1]
)
axs[1, 1].set_title("Corelatii intre variabile")

plt.tight_layout()
plt.show()