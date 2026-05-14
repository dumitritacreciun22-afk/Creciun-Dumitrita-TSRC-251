import pandas as pd
import numpy as np

# Exercițiul 1: Crearea unui Series din numerele 1-10
s1 = pd.Series(range(1, 11))
print("Ex 1 - Series 1-10:\n", s1, "\n")

# Exercițiul 2: Indexare și selectare din Series
lista_fructe = ['apple', 'banana', 'cherry', 'date']
s2 = pd.Series(lista_fructe)
# Selectăm al doilea (index 1) și al patrulea (index 3) element
print("Ex 2 - Elemente selectate:", s2[1], "și", s2[3], "\n")

# Exercițiul 3: Crearea unui DataFrame dintr-un dicționar
data = { 
    'Name': ['Alice', 'Bob', 'Charlie', 'David'], 
    'Age': [24, 27, 22, 32], 
    'City': ['New York', 'Los Angeles', 'Chicago', 'Miami'] 
}
df = pd.DataFrame(data)
print("Ex 3 - DataFrame creat:\n", df, "\n")

# Exercițiul 4: Obținerea informațiilor statistice
df_numeric = pd.DataFrame({
    'Points': [10, 20, 15, 30, 45],
    'Score': [88, 92, 80, 75, 95],
    'Rank': [5, 3, 4, 1, 2]
})
print("Ex 4 - Statistice descriptive:\n", df_numeric.describe(), "\n")

# Exercițiul 5: Indexare și filtrare (vârsta > 25)
# Folosim df de la exercițiul 3
filtered_df = df[df['Age'] > 25]
print("Ex 5 - Persoane cu vârsta > 25:\n", filtered_df, "\n")

# Exercițiul 6: Adăugarea unei coloane noi (Salary)
df['Salary'] = [5000, 6000, 4500, 7000]
print("Ex 6 - DataFrame cu coloana Salary:\n", df, "\n")

# Exercițiul 7: Gruparea datelor după City și media vârstei
# (Notă: în datele noastre fiecare oraș e unic, deci media va fi vârsta însăși)
grouped_city = df.groupby('City')['Age'].mean()
print("Ex 7 - Vârsta medie pe orașe:\n", grouped_city, "\n")

# Exercițiul 8: Îmbinarea (merge) a două DataFrame-uri
df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'ID': [101, 102]})
df2 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Department': ['IT', 'HR']})
merged_df = pd.merge(df1, df2, on='Name')
print("Ex 8 - DataFrame îmbinat:\n", merged_df, "\n")

# Exercițiul 9: Completarea valorilor lipsă (fillna)
df_missing = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [np.nan, 5, 6]
})
df_filled = df_missing.fillna(0)
print("Ex 9 - Valori lipsă înlocuite cu 0:\n", df_filled, "\n")

# Exercițiul 10: Ștergerea rândurilor cu valori lipsă (dropna)
df_dropped = df_missing.dropna()
print("Ex 10 - Rânduri rămase după dropna:\n", df_dropped, "\n")

# Exercițiul 11: Citirea și scrierea CSV
df_random = pd.DataFrame(np.random.randint(0, 100, size=(5, 3)), columns=['A', 'B', 'C'])
df_random.to_csv('date_test.csv', index=False)
df_read = pd.read_csv('date_test.csv')
print("Ex 11 - Date citite din CSV-ul nou creat:\n", df_read, "\n")

# Exercițiul 12: Transformarea datelor (pătratul unei coloane)
df['Age_Squared'] = df['Age'] ** 2
print("Ex 12 - DataFrame cu coloana Age la pătrat:\n", df)