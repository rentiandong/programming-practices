#include <unordered_map>
#include <string>
#include <assert.h>

class Node {
public:
  Node(): isTerminal_(false) {}

  void setTerminal() {
    isTerminal_ = true;
  }

  bool isTerminal() const {
    return isTerminal_;
  }

  bool hasKey(const char key) const {
    return children_.count(key);
  }

  void createKey(const char key) {
    if (children_.count(key)) {
      return;
    }

    children_[key] = std::make_shared<Node>();
  }

  std::shared_ptr<Node> getKey(const char key) const {
    if (!hasKey(key)) {
      return nullptr;
    }

    return children_.at(key);
  }

private:
  bool isTerminal_;
  std::unordered_map<char, std::shared_ptr<Node> > children_; // unique?
};

class Trie {
public:
  Trie(): root_(std::make_shared<Node>()) {}

  void insert(const std::string& string) {
    insert(string, 0, root_);
  }

  void insert(const std::string& string, const size_t index, const std::shared_ptr<Node>& node) {
    if (index >= string.size()) {
      node->setTerminal();
      return;
    }

    const char key = string[index];

    if (!node->hasKey(key)) {
      node->createKey(key);
    }

    insert(string, index + 1, node->getKey(key));
  }

  bool contains(const std::string& string) const {
    if (string == "") {
      return root_->isTerminal();
    }

    return contains(string, 0, root_);
  }

  bool contains(const std::string& string, const size_t index, const std::shared_ptr<Node>& node) const {
    if (index == string.size() - 1) {
      return node->isTerminal();
    }

    const char key = string[index];

    if (!node->hasKey(key)) {
      return false;
    }

    return contains(string, index + 1, node->getKey(key));
  }

private:
  std::shared_ptr<Node> root_;
};

void testEmptyTrieContainsNothing() {
  Trie trie;

  assert(!trie.contains(""));
  assert(!trie.contains("a"));
}

void testCorrectlyReturnsContainEmptyString() {
  Trie trie;

  trie.insert("");
  
  assert(trie.contains(""));
}

void testCorrectlyReturnsContainNonEmptyString() {
  Trie trie;

  trie.insert("apple");
  trie.insert("bob");
  trie.insert("alice");

  assert(trie.contains("alice"));
  assert(trie.contains("apple"));
  assert(trie.contains("bob"));

}

int main() {
  testEmptyTrieContainsNothing();

  return 0;
}