import sys
from stats import get_num_words, counting_characters, sorting_characters

def get_book_text(path):
	with open(path) as f:
		return f.read()

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	path = sys.argv[1]
	text = get_book_text(path)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	word_count = get_num_words(text)
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	counts = counting_characters(text)
	sorted_chars = sorting_characters(counts)
	for item in sorted_chars:
		ch = item["char"]
		if ch.isalpha():
			print(f"{ch}: {item['num']}")
	print("============= END ===============")

if __name__ == "__main__":
    main()
