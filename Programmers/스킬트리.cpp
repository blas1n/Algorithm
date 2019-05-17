#include <string>
#include <vector>

using namespace std;

int solution(string skill, vector<string> skill_trees) {
	int answer = 0;

	int skillIndex, treeIndex;
	int skillLen, treeLen;

	for (const auto& skill_tree : skill_trees) {
		skillIndex = treeIndex = 0;

		skillLen = skill.length();
		treeLen = skill_tree.length();

		while (true) {
			if (skillIndex >= skillLen || treeIndex >= treeLen) {
				answer++;
				break;
			}

			if (skill.find(skill_tree[treeIndex]) == string::npos) {
				treeIndex++;
				continue;
			}

			if (skill[skillIndex] != skill_tree[treeIndex])
				break;

			skillIndex++;
			treeIndex++;
		}
	}

	return answer;
}