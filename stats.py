def get_num_words(text: str) -> int:
    return len(text.split())


def counting_characters(text):
	t = text.lower()
	total = {}
	for i in t:
		if i not in total:
			total[i] = 1
		else:
			total[i] += 1
	return total

def sort_on(item):
        return item["num"]

def sorting_characters(counts):
	total = []
	for ch, num in counts.items():
		dict = {"char": ch, "num": num}
		total.append(dict)
	total.sort(reverse=True, key=sort_on)
	return total
