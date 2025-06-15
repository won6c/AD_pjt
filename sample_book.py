from library.models import Book
from datetime import date, timedelta
import random

titles = [
    "Return of the Dragon", "Legacy of the Sorcerer", "Conqueror of the Universe", "End of Time", "Beyond the Galaxy",
    "Abyss of Monsters", "Portal of Dimensions", "Last Day of Humanity", "Guardians of Eden", "War with AI",
    "Walker of the Abyss", "The Immortal", "Forgotten Continent", "Knight of Twilight", "Data Utopia",
    "Revenge of Superintelligence", "Corridor of Memory", "The Third Intelligence", "Soma's Diary", "Code Breaker",
    "Quantum Phantom", "Hive Network", "Chronicles of Future City", "Cryptonic War", "Transferred God",
    "Digital Veil", "Border of Hallucination", "Cyber Spirit", "Metaverse Destroyer", "Soul Hacker",
    "Crack of Spacetime", "Mechanical Myth", "Price of Consciousness", "Network Wraith", "Memory Manipulator",
    "AI Prophet", "Revenge of Alpha", "Digital Babel", "Bit Dragon", "Key of Transcendence",
    "Deep Interface", "Lost Code", "Consciousness Simulation", "Neo Human", "Genetic Secret",
    "Time Loop Boy", "Zero Utopia", "Empire of Errors", "Virtual Warrior", "Mystic Routine",
    "End of the Matrix", "Fragmented Soul", "Coding Crusade", "Memory Eraser", "Digital Shaman",
    "Chrono the Infowarrior", "Shards of the Future", "Gods of Logic", "Liberator of Mind", "Prompt Phantom"
]

authors = ["Alex Kim", "Sophie Lee", "Daniel Park", "John Jung", "Emily Choi", "David Kang", "Jin Yoon", "Sumin Oh", "Jiwoo Han", "Aram Cho"]
keywords = ["Sci-Fi Action", "Fantasy Adventure", "Thriller Mystery", "AI Philosophy", "Dystopia", "Time Travel", "Virtual Reality", "Cyberpunk"]

books = []

for i in range(60):
    title = titles[i]
    author = random.choice(authors)
    keyword = random.choice(keywords)
    description = f"{title} is a story in the {keyword} genre, filled with engaging plots and deep messages."
    published_date = date(2010, 1, 1) + timedelta(days=random.randint(0, 5000))
    books.append(Book(title=title,author=author,keyword=keyword,description=description,published_date=published_date))

Book.objects.bulk_create(books)
