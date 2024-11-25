import csv

def read_books(file_name):
    books = []
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books

# Function to write books to the corresponding genre file
def write_books_to_file(genre, books):
    file_name = f'books_{genre.lower()}.txt'
    with open(file_name, mode='w') as file:
        for book in books:
            file.write(f"{book['Title']} by {book['Author']} ({book['Year']})\n")

# Function to filter books by genre
def filter_books_by_genre(books, genre):
    filtered_books = [book for book in books if book['Genre'].lower() == genre.lower()]
    return filtered_books

# Main function to process books
def process_books():
    # Read all books from the CSV file
    books = read_books('books.csv')
    
    # Define the list of genres we want to process
    genres = ['Fiction', 'Dystopian', 'Classic', 'Romance', 'Adventure', 'Historical', 'Modernist', 'Epic', 'Gothic', 'Psychological', 'Fantasy', 'Philosophical', 'Literary', 'Southern Gothic', 'Magic Realism', 'Gothic Horror', 'Novella', 'Science Fiction', 'Post-apocalyptic', 'Horror', 'Satire']
    
    # Process each genre
    for genre in genres:
        # Filter books for the current genre
        genre_books = filter_books_by_genre(books, genre)
        
        # If there are books for this genre, write them to a file
        if genre_books:
            write_books_to_file(genre, genre_books)
            print(f"Books in the {genre} genre have been written to books_{genre.lower()}.txt")
        else:
            print(f"No books found for the {genre} genre")

process_books()