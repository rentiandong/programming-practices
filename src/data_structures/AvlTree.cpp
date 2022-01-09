#include <assert.h>
#include <memory>
#include <vector>

struct AvlTreeNode {
public:
  std::shared_ptr<AvlTreeNode> left_;
  std::shared_ptr<AvlTreeNode> right_;
  int value_;
  size_t height_;
};

class AvlTree {
public:
  void insert(const int toInsert) { insert(toInsert, root_); }

  void erase(const int toErase) { erase(toErase, root_); }

  bool contains(const int toCheck) const { return contains(toCheck, root_); }

  size_t getTotalHeight() const { return getHeight(root_); }

  std::vector<int> inOrderTraversal() const {
    std::vector<int> result;

    inOrderTraversal(result, root_);

    return result;
  }

private:
  std::shared_ptr<AvlTreeNode> root_;

private:
  static void inOrderTraversal(std::vector<int> &result,
                               const std::shared_ptr<AvlTreeNode> &node) {
    if (!node) {
      return;
    }

    inOrderTraversal(result, node->left_);
    result.push_back(node->value_);
    inOrderTraversal(result, node->right_);
  }

  static size_t getHeight(const std::shared_ptr<AvlTreeNode> &node) {
    return node ? node->height_ : 0;
  }

  static void updateHeight(std::shared_ptr<AvlTreeNode> &node) {
    if (!node) {
      return;
    }

    node->height_ =
        std::max(getHeight(node->left_), getHeight(node->right_)) + 1;
  }

  static std::shared_ptr<AvlTreeNode> &
  findInOrderPredecessor(const std::shared_ptr<AvlTreeNode> &parent) {
    if (!parent->left_->right_) {
      return parent->left_;
    }

    auto predecessor = parent->left_;

    if (predecessor->right_ && !predecessor->right_->right_) {
      return predecessor->right_;
    }

    while (predecessor->right_->right_) {
      predecessor = predecessor->right_;
    }

    return predecessor->right_;
  }

  static void rotateRight(std::shared_ptr<AvlTreeNode> &parent) {
    auto rightChildOfLeftChild = parent->left_->right_;
    auto leftChild = parent->left_;

    parent->left_ = rightChildOfLeftChild;
    leftChild->right_ = parent;
    parent = leftChild;

    updateHeight(parent->right_);
    updateHeight(parent);
  }

  static void rotateLeft(std::shared_ptr<AvlTreeNode> &parent) {
    auto leftChildOfRightChild = parent->right_->left_;
    auto rightChild = parent->right_;

    parent->right_ = leftChildOfRightChild;
    rightChild->left_ = parent;
    parent = rightChild;

    updateHeight(parent->left_);
    updateHeight(parent);
  }

  static void rebalance(std::shared_ptr<AvlTreeNode> &parent) {
    if (!parent) {
      return;
    }

    const size_t leftHeight = getHeight(parent->left_);
    const size_t rightHeight = getHeight(parent->right_);

    if (std::max(leftHeight, rightHeight) - std::min(leftHeight, rightHeight) <=
        1) {
      return;
    }

    if (leftHeight > rightHeight) {
      if (getHeight(parent->left_->left_) >
          getHeight(parent->left_->right_)) { // left left
        rotateRight(parent);
      } else { // left right
        rotateLeft(parent->left_);
        rotateRight(parent);
      }
    } else {
      if (getHeight(parent->right_->right_) >
          getHeight(parent->right_->left_)) { // right right
        rotateLeft(parent);
      } else { // right left
        rotateRight(parent->right_);
        rotateLeft(parent);
      }
    }
  }

  // https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
  void insert(const int toInsert, std::shared_ptr<AvlTreeNode> &parent) {
    if (!parent) {
      parent = std::make_shared<AvlTreeNode>();
      parent->value_ = toInsert;
      parent->height_ = 1;
      return;
    }

    if (toInsert > parent->value_) {
      insert(toInsert, parent->right_);
    } else {
      insert(toInsert, parent->left_);
    }

    rebalance(parent);
    updateHeight(parent);
  }

  void erase(const int toErase, std::shared_ptr<AvlTreeNode> &parent) {
    if (!parent) {
      return;
    }

    if (toErase > parent->value_) {
      erase(toErase, parent->right_);
    } else if (toErase < parent->value_) {
      erase(toErase, parent->left_);
    } else {
      if (!parent->left_ && !parent->right_) {
        parent = nullptr;
      } else if (parent->left_ && parent->right_) {
        auto &inOrderPredecessor = findInOrderPredecessor(parent);

        parent->value_ = inOrderPredecessor->value_;
        erase(inOrderPredecessor->value_, inOrderPredecessor);
      } else {
        parent = parent->left_ ? parent->left_ : parent->right_;
      }
    }

    rebalance(parent);
    updateHeight(parent);
  }

  bool contains(const int toCheck,
                const std::shared_ptr<AvlTreeNode> &parent) const {
    if (!parent) {
      return false;
    }

    if (toCheck < parent->value_) {
      return contains(toCheck, parent->left_);
    }

    if (toCheck > parent->value_) {
      return contains(toCheck, parent->right_);
    }

    return true;
  }
};

void assertSearchTree(const AvlTree &avlTree) {
  std::vector<int> inOrderTraversalResult = avlTree.inOrderTraversal();

  for (size_t i = 0; i < inOrderTraversalResult.size() - 1; ++i) {
    assert(inOrderTraversalResult[i] <= inOrderTraversalResult[i + 1]);
  }
}

void testEmptyTreeContainsNothing() {
  AvlTree tree;

  assert(!tree.contains(1));
  assert(!tree.contains(0));
  assert(!tree.contains(-1));
}

void testBalancingWhenInsertedValueIsRightChildOfRightChildOfUnblancedNode() {
  AvlTree tree;

  tree.insert(1);
  assert(tree.getTotalHeight() == 1);
  assertSearchTree(tree);

  tree.insert(2);
  assert(tree.getTotalHeight() == 2);
  assertSearchTree(tree);

  tree.insert(3);
  assert(tree.getTotalHeight() == 2);
  assertSearchTree(tree);

  tree.insert(4);
  assert(tree.getTotalHeight() == 3);
  assertSearchTree(tree);

  tree.insert(5);
  assert(tree.getTotalHeight() == 3);
  assertSearchTree(tree);

  tree.insert(6);
  assert(tree.getTotalHeight() == 3);
  assertSearchTree(tree);

  assert(tree.contains(1));
  assert(tree.contains(2));
  assert(tree.contains(3));
  assert(tree.contains(4));
  assert(tree.contains(5));
  assert(tree.contains(6));
  assert(!tree.contains(-1));
  assert(!tree.contains(-2));
}

void testBalancingWhenInsertedValueIsLeftChildOfLeftChildOfUnblancedNode() {
  AvlTree tree;

  tree.insert(6);
  assert(tree.getTotalHeight() == 1);
  assertSearchTree(tree);

  tree.insert(5);
  assert(tree.getTotalHeight() == 2);
  assertSearchTree(tree);

  tree.insert(4);
  assert(tree.getTotalHeight() == 2);
  assertSearchTree(tree);

  tree.insert(3);
  assert(tree.getTotalHeight() == 3);
  assertSearchTree(tree);

  tree.insert(2);
  assert(tree.getTotalHeight() == 3);
  assertSearchTree(tree);

  tree.insert(1);
  assert(tree.getTotalHeight() == 3);
  assertSearchTree(tree);

  assert(tree.contains(1));
  assert(tree.contains(2));
  assert(tree.contains(3));
  assert(tree.contains(4));
  assert(tree.contains(5));
  assert(tree.contains(6));
  assert(!tree.contains(-1));
  assert(!tree.contains(-2));
}

void testBalancingWhenInsertedValueIsRightChildOfLeftChildOfUnblancedNode() {
  AvlTree tree;

  tree.insert(6);
  assert(tree.getTotalHeight() == 1);
  assertSearchTree(tree);

  tree.insert(3);
  assert(tree.getTotalHeight() == 2);
  assertSearchTree(tree);

  tree.insert(5);
  assert(tree.getTotalHeight() == 2);
  assertSearchTree(tree);

  tree.insert(4);
  assert(tree.getTotalHeight() == 3);
  assertSearchTree(tree);

  tree.insert(1);
  assert(tree.getTotalHeight() == 3);
  assertSearchTree(tree);

  tree.insert(2);
  assert(tree.getTotalHeight() == 3);
  assertSearchTree(tree);

  assert(tree.contains(1));
  assert(tree.contains(2));
  assert(tree.contains(3));
  assert(tree.contains(4));
  assert(tree.contains(5));
  assert(tree.contains(6));
  assert(!tree.contains(-1));
  assert(!tree.contains(-2));
}

void testBalancingWhenInsertedValueIsLeftChildOfRightChildOfUnblancedNode() {
  AvlTree tree;

  tree.insert(1);
  assert(tree.getTotalHeight() == 1);
  assertSearchTree(tree);

  tree.insert(6);
  assert(tree.getTotalHeight() == 2);
  assertSearchTree(tree);

  tree.insert(3);
  assert(tree.getTotalHeight() == 2);
  assertSearchTree(tree);

  tree.insert(2);
  assert(tree.getTotalHeight() == 3);
  assertSearchTree(tree);

  tree.insert(5);
  assert(tree.getTotalHeight() == 3);
  assertSearchTree(tree);

  tree.insert(4);
  assert(tree.getTotalHeight() == 3);
  assertSearchTree(tree);

  assert(tree.contains(1));
  assert(tree.contains(2));
  assert(tree.contains(3));
  assert(tree.contains(4));
  assert(tree.contains(5));
  assert(tree.contains(6));
  assert(!tree.contains(-1));
  assert(!tree.contains(-2));
}

void testRemoveFromEmptyTree() {
  AvlTree tree;

  tree.erase(0);
}

void testRemoveRootOfTree() {
  AvlTree tree;

  tree.insert(1);
  tree.erase(1);

  assert(!tree.contains(1));
}

void testRemoveNodeWithOnlyOneChildren() {
  AvlTree tree;

  tree.insert(1);
  tree.insert(2);
  tree.erase(1);

  assert(!tree.contains(1));
  assert(tree.contains(2));
}

void testRemoveNodeWithTwoChildren() {
  AvlTree tree;

  tree.insert(2);
  tree.insert(1);
  tree.insert(3);
  tree.erase(2);

  assert(tree.contains(1));
  assert(tree.contains(3));
  assert(!tree.contains(2));

  assert(tree.getTotalHeight() == 2);
}

void testInsertingAndDeletingDuplicatedElements() {
  AvlTree tree;

  tree.insert(1);
  tree.insert(1);
  tree.insert(1);

  tree.erase(1);
  tree.erase(1);

  assertSearchTree(tree);
  assert(tree.contains(1));
}

void testBalancingWhenAfterDeletionUnbalancedNodeIsLeftChildOfLeftChild() {
  AvlTree tree;

  tree.insert(3);
  tree.insert(2);
  tree.insert(4);
  tree.insert(1);

  tree.erase(4);

  assertSearchTree(tree);
  assert(tree.getTotalHeight() == 2);
}

void testBalancingWhenAfterDeletionUnbalancedNodeIsRightChildOfRightChild() {
  AvlTree tree;

  tree.insert(2);
  tree.insert(3);
  tree.insert(1);
  tree.insert(4);

  tree.erase(1);

  assertSearchTree(tree);
  assert(tree.getTotalHeight() == 2);
}

void testBalancingWhenAfterDeletionUnbalancedNodeIsRightChildOfLeftChild() {
  AvlTree tree;

  tree.insert(5);
  tree.insert(7);
  tree.insert(3);
  tree.insert(4);

  tree.erase(7);

  assertSearchTree(tree);
  assert(tree.getTotalHeight() == 2);
}

void testBalancingWhenAfterDeletionUnbalancedNodeIsLeftChildOfRightChild() {
  AvlTree tree;

  tree.insert(5);
  tree.insert(7);
  tree.insert(3);
  tree.insert(6);

  tree.erase(3);

  assertSearchTree(tree);
  assert(tree.getTotalHeight() == 2);
}

int main() {
  testEmptyTreeContainsNothing();

  testBalancingWhenInsertedValueIsRightChildOfRightChildOfUnblancedNode();
  testBalancingWhenInsertedValueIsLeftChildOfLeftChildOfUnblancedNode();
  testBalancingWhenInsertedValueIsRightChildOfLeftChildOfUnblancedNode();
  testBalancingWhenInsertedValueIsLeftChildOfRightChildOfUnblancedNode();

  testRemoveFromEmptyTree();
  testRemoveNodeWithOnlyOneChildren();
  testRemoveNodeWithTwoChildren();

  testBalancingWhenAfterDeletionUnbalancedNodeIsLeftChildOfLeftChild();
  testBalancingWhenAfterDeletionUnbalancedNodeIsRightChildOfRightChild();
  testBalancingWhenAfterDeletionUnbalancedNodeIsRightChildOfLeftChild();

  return 0;
}