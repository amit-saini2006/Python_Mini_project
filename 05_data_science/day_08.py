import pandas as pd

data = [
  {
    "title": "The Silent Lake",
    "author": "Mira Desai",
    "genre": "Mystery",
    "description": "A detective unravels a hidden past after a body is found near a quiet lakeside town."
  },
  {
    "title": "Code of Tomorrow",
    "author": "Raj Malhotra",
    "genre": "Science Fiction",
    "description": "In a world run by AI, a young hacker discovers the code that could save or destroy humanity."
  },
  {
    "title": "Threads of Time",
    "author": "Elena Roy",
    "genre": "Fantasy",
    "description": "A girl discovers a magical loom that weaves the destinies of people across centuries."
  },
  {
    "title": "Whispers of the Desert",
    "author": "Arun Patel",
    "genre": "Adventure",
    "description": "An archaeologist embarks on a dangerous journey to uncover a lost civilization beneath the dunes."
  },
  {
    "title": "City of Echoes",
    "author": "Lina Fernandes",
    "genre": "Thriller",
    "description": "A journalist uncovers a powerful conspiracy linking missing persons to secret experiments in the city."
  },
  {
    "title": "Midnight Blossoms",
    "author": "Haruki Aoyama",
    "genre": "Romance",
    "description": "Two souls meet under the cherry blossoms each year, bound by a promise made long ago."
  },
  {
    "title": "Quantum Truth",
    "author": "Ananya Sen",
    "genre": "Philosophical Fiction",
    "description": "A physicist questions reality after a quantum experiment shows the universe reacting to human thoughts."
  },
  {
    "title": "Iron Shadows",
    "author": "Leo Grant",
    "genre": "Historical Fiction",
    "description": "Set in 18th century Europe, a blacksmith becomes an unlikely hero in a war of rebellion."
  },
  {
    "title": "Digital Mirage",
    "author": "Tara Mehta",
    "genre": "Cyberpunk",
    "description": "In a neon-filled megacity, a rogue programmer battles corporate control over people's dreams."
  },
  {
    "title": "Echoes from the Sky",
    "author": "Karan Dutta",
    "genre": "Drama",
    "description": "After a tragic plane crash, a survivor struggles to rebuild his life while uncovering the truth behind it."
  }
]

df = pd.DataFrame(data)
df.to_csv("books.csv", index=False)
print("✅ Books datasheet created")