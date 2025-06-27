import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


dados = pd.DataFrame({
    "classe": ['Cubozoa', 'Scyphozoa', 'Hydrozoa', 'Anthozoa'],
    "espécies": ['50',  '200', '3.700', '6.000']
})


dados['espécies'] = dados['espécies'].str.replace('.', '', regex=False).str.strip().astype(int)


plt.figure(figsize=(8, 6))
ax = sns.barplot(x="classe", y="espécies", data=dados, palette="coolwarm", ci=None)


for i, row in dados.iterrows():
    ax.text(i, row['espécies'] + 100, f"{row['espécies']}", 
            ha='center', va='bottom', fontsize=10, fontweight='bold')


plt.title("Quantidade de espécies por classe dos cnidários")
plt.xlabel("Classe de Cnidários")
plt.ylabel("Quantidade de Espécies")

plt.tight_layout()
plt.savefig("cnidarios/static/grafico_cnidario.png")
plt.close()