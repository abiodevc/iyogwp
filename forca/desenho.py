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

def forcafun(a, b):
    print(forca[a])
    print(''.join(b))
