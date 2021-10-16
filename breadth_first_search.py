from collections import deque

graph = {
	"you": ["alice", "bob", "claire"],
	"bob": ["anuj", "peggy"],
	"alice": ["peggy"],
	"claire": ["thom", "jonny"],
	"anuj": [],
	"peggy": [],
	"thom": [],
	"jonny": []
}

def search(name):
	search_queue = deque()
	search_queue += graph["you"]
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person_is_seller(person):
				print(person + " is a seller!")
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	return False



def person_is_seller(person):
	return person[-1] == 'm'

print(search("you"))