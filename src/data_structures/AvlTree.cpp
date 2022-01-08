#include <memory>
#include <assert.h>

struct AvlTreeNode {
public:
    std::shared_ptr<AvlTreeNode> left_;
    std::shared_ptr<AvlTreeNode> right_;
    int value_;
    size_t height_;
};

class AvlTree {
public:
    void insert(const int toInsert) {
        insert(toInsert, root_);
    }

    bool contains(const int toCheck) const {
        return contains(toCheck, root_);
    }

private:
    std::shared_ptr<AvlTreeNode> root_;

private:
    

   // https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
   void insert(const int toInsert, std::shared_ptr<AvlTreeNode>& parent) {
       if (!parent) {
           parent = std::make_shared<AvlTreeNode>();
           parent->value_ = toInsert;
           parent->height = 1;
           return;
       }

       if (toInsert > parent->value_) {
           insert(toInsert, parent->right_);
       } else if (toInsert < parent->value_) {
           insert(toInsert, parent->left_);
       }

       const size_t leftHeight = parent_->left_->height_;
       const size_t rightHeight = parent_->right_->height_;

       if (max(leftHeight, rightHeight) - min(leftHeight, rightHeight) > 1) {
          if (toInsert < parent->left_->value_) {
              const auto rightChildOfLeftChild = parent->left->right_;
              const auto leftChild = parent->left_;
              
              parent->left_ = rightChildOfLeftChild;
              leftChild_->right_ = parent;
              parent = leftChild;

              parent_->height_ = max(parent_->left_->height_, parent->right_->height_) + 1;
              leftChild->height_ = max(leftChild_->left_->height_, leftChild->right_->height_) + 1;
          } else if (toInsert > parent->right_->value) {
              const auto leftChildOfRightChild = parent->right_->left_;
              const auto rightChild = parent->right_;

              parent->right_ = leftChildOfRightChild;
              rightChild->left_ = parent;
              parent = rightChild;

              parent_->height = 
          }

          if (toInsert < parent->value_) {

          }

          if (toInsert > parent->value_) {

          }
       }

       height_ = max(leftHeight, rightHeight) + 1;
   }

   bool contains(const int toCheck, const std::shared_ptr<AvlTreeNode>& parent) const {
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

void testEmptyTreeContainsNothing() {
    AvlTree tree;
    
    assert(!tree.contains(1));
    assert(!tree.contains(0));
    assert(!tree.contains(-1));
}

void testTreeContainsOnlyInsertedElements() {
    AvlTree tree;

    tree.insert(1);
    tree.insert(2);
    tree.insert(3);
    tree.insert(4);
    tree.insert(5);
    tree.insert(6);

    assert(tree.contains(1));
    assert(tree.contains(2));
    assert(tree.contains(3));
    assert(tree.contains(4));
    assert(tree.contains(5));
    assert(tree.contains(6));
    assert(!tree.contains(-1));
    assert(!tree.contains(-2));
}

int main() {
    testEmptyTreeContainsNothing();
    testTreeContainsOnlyInsertedElements();
    
    return 0;
}