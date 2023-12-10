import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Word': ['bilbo', 'earth', 'hobbit', 'lord', 'precious', 'ring', 'walk', 'bow', 'run', 'way'],
    'The Fellowship of the Ring': [321, 39, 410, 68, 14, 392, 147, 64, 101, 296],
    'The Two Towers': [8, 45, 260, 114, 92, 98, 111, 85, 99, 332],
    'The Return of the King': [32, 31, 132, 265, 21, 105, 77, 57, 65, 192]
}

df = pd.DataFrame(data)

ax = df.plot(kind='bar', x='Word', y=['The Fellowship of the Ring', 'The Two Towers', 'The Return of the King'],
             color=['blue', 'orange', 'green'], figsize=(10, 6))

plt.title('Absolute Häufigkeiten von Wörtern in der Trilogie "Der Herr der Ringe"')
plt.xlabel('Wort')
plt.ylabel('Absolute Häufigkeit')
plt.legend(title='Trilogie')

plt.show()
