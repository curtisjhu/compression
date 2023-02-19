#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <utility>
#include <limits>
#include <exception>
#include <array>
using namespace std;

#define INPUT_FILE "input.txt"
#define OUTPUT_FILE "output.txt"

map<char, int> create_frequency_map(string file)
{
	ifstream input;
	input.open(file);

	map<char, int> frequency_map;

	char temp;
	while (input.get(temp))
	{
		frequency_map[temp]++;
	}
	input.close();

	return frequency_map;
}

pair<int, int> get_two_lowest_frequencies(array<pair<int, int>, 190> tree)
{
	// (index (not root node), freq)
	int outOfBounds = '~' + 1;
	pair<int, int> lowest = make_pair(outOfBounds, INT_MAX);
	pair<int, int> second_lowest = make_pair(outOfBounds, INT_MAX);

	for (int i = 0; i < tree.size(); i++)
	{
		int freq = tree[i].second; // current frequency
		if (freq != 0 && freq < second_lowest.second)
		{
			if (freq < lowest.second)
			{
				second_lowest = lowest;
				lowest = make_pair(i, freq);
			}
			else
			{
				second_lowest = make_pair(i, freq);
			}
		}

	}
	return make_pair(lowest.first, second_lowest.first);
}

array<pair<int, int>, 190> create_frequency_tree(map<char, int> &freq_map)
{
	if (freq_map.size() < 2)
		throw std::invalid_argument("frequency map should be at least 2+ size");

	// 32 - 126
	// [char: (node, freq)] < - either frequency or points to a new node???
	array<pair<int, int>, 190> tree;
	for (int i = 0; i < tree.size(); i++)
		tree[i] = make_pair(-1, 0);

	// just put the frequencies into the tree;
	map<char, int>::iterator it = freq_map.begin();
	for (; it != freq_map.end(); it++)
	{
		int index = it->first - ' ';
		tree[index].second = it->second;
	}

	int next_root = '~' - ' ';

	
	// new tree to keep track of frequencies already used;
	array<pair<int, int>, 190> fakeTree(tree);

	pair<int, int> ll = get_two_lowest_frequencies(fakeTree);
	int index1 = ll.first;
	int index2 = ll.second;

	//assign nodes/ leafs
	while (index1 < 95 || index2 < 95)
	{
		//assign parent
		tree[index1].first = next_root;
		tree[index2].first = next_root;

		// combine their frequencies
		tree[next_root].second = tree[index1].second + tree[index2].second;

		next_root++;

		// erase these two nodes
		fakeTree[index1].second = INT_MAX;
		fakeTree[index2].second = INT_MAX;

		ll = get_two_lowest_frequencies(fakeTree);
		index1 = ll.first;
		index2 = ll.second;
	}

	return tree;
}

map<char, string> create_code_table(array<pair<int, int>, 190> tree)
{
	int maxFreq = 0;
	int root = -1;
	for (int i = 0; i < tree.size(); i++) {
		if (maxFreq < tree[i].second) {
			maxFreq = tree[i].second;
			root = i;
		}
	}

	vector<int> v;
	


}

int main()
{
	map<char, int> m = create_frequency_map(INPUT_FILE);

	map<char, int>::iterator c = m.begin();
	for (; c != m.end(); c++)
		cout << c->first << ": " << c->second << endl;

	array<pair<int, int>, 190> tree = create_frequency_tree(m);
	for (int i = 0; i < tree.size(); i++)
		cout<<tree[i].first<<" "<<tree[i].second<<", ";
	


	return 0;
}