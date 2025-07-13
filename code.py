import random

# Function to generate a random grid of letters
def generate_grid(size):
    grid = []
    for _ in range(size):
        row = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(size)]
        grid.append(row)
    return grid

# Function to display the grid
def display_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()

# Function to create a word list
def create_word_list():
    words = ["PYTHON", "JAVA", "CPLUSPLUS", "JAVASCRIPT", "RUBY", "HTML", "CSS","KARAN"]
    return words

# Function to hide words in the grid
def hide_words(grid, words):
    for word in words:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            row = random.randint(0, len(grid) - 1)
            col = random.randint(0, len(grid) - len(word))
            for i in range(len(word)):
                grid[row][col + i] = word[i]
        else:
            row = random.randint(0, len(grid) - len(word))
            col = random.randint(0, len(grid) - 1)
            for i in range(len(word)):
                grid[row + i][col] = word[i]

# Function to play the word search game
def play_word_search():
    grid_size = 10
    grid = generate_grid(grid_size)
    words = create_word_list()
    hide_words(grid, words)
    print("Welcome to Word Search Game!")
    print("Find the following words in the grid:")
    for word in words:
        print(word)
    print()
    display_grid(grid)

    found_words = []
    while len(found_words) < len(words):
        guess = input("Enter a word (or 'quit' to exit): ").upper()
        if guess == 'QUIT':
            break
        if guess in words and guess not in found_words:
            found_words.append(guess)
            print(f"Found '{guess}'!")
        else:
            print("Word not found. Try again.")
    
    print("Game over!")
    print("Words found:")
    print(', '.join(found_words))

if __name__ == "__main__":
    play_word_search()
