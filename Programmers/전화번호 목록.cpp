#include <string>
#include <vector>
#include <memory>

using namespace std;

class Trie {
private:
	Trie* next[10];

public:
	Trie() {
		for (auto& n : next)
            n = nullptr;
	}

	void Insert(const string& key) {
		Trie* curTrie = this;

		for (auto letter : key) {
			int curIndex = letter - '0';

			if (curTrie->next[curIndex] == nullptr)
				curTrie->next[curIndex] = new Trie();

			curTrie = curTrie->next[curIndex];
		}
	}

	bool IsValid(const string& key) {
		Trie* curTrie = this;
		
		for (auto letter : key) {
			curTrie = curTrie->next[letter - '0'];

			if (curTrie == nullptr)
				return false;
		}

		return true;
	}
};

bool solution(vector<string> phone_book) {
	Trie trie;
	trie.Insert(phone_book[0]);

	int n = phone_book[0].length();

	for (int i = 1; i < phone_book.size(); i++) {
		if (trie.IsValid(phone_book[i].substr(0, n)))
			return false;
	}

	return true;
}