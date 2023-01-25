forca = ['''
F O R C A
  +---+
  |   |
      |
      |
      |
      |''', '''
F O R C A
  +---+
  |   |
  O   |
      |
      |
      |''', '''
F O R C A
  +---+
  |   |
  O   |
  |   |
      |
      |''', '''
F O R C A
  +---+
  |   |
  O   |
 /|   |
      |
      |''', '''
F O R C A
  +---+
  |   |
  O   |
 /|\  |
      |
      |''', '''
F O R C A
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |''', '''
F O R C A
  +---+
  |   | 
  O   |
 /|\  |
 / \  |
      |''']

def forcafun(a, b, c):
    print(forca[a])
    print(f"{''.join(b)}\t\tpontuação: {c}")
