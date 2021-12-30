#include <vector>
#include <memory>
#include <cassert>
#include <iostream>
#include <optional>

class MinHeap {
public:
    MinHeap() {}

    void push(const int& value) {
        internalVector_.push_back(value);
        
        size_t indexOfNewValue = internalVector_.size() - 1;
        while (indexOfNewValue > 0 && internalVector_[getParentIndex(indexOfNewValue)] > value) {
            internalVector_[indexOfNewValue] = internalVector_[getParentIndex(indexOfNewValue)];
            internalVector_[getParentIndex(indexOfNewValue)] = value;
        }
    }

    int top() const {
        return internalVector_.front();
    }

    int pop() {
        const int toReturn = internalVector_.front();
        const int valueToPushDown = internalVector_.back();

        internalVector_.front() = internalVector_.back();
        internalVector_.pop_back();

        size_t indexOfValueToPushDown = 0;
        
        while (true) {
            size_t leftChildIndex = getLeftChildIndex(indexOfValueToPushDown);
            size_t rightChildIndex = geRightChildIndex(indexOfValueToPushDown);
            size_t indexToPushDownTo = indexOfValueToPushDown;

            if (leftChildIndex >= internalVector_.size()) {
                break;
            } else if (internalVector_[leftChildIndex] < valueToPushDown) {
                indexToPushDownTo = leftChildIndex;
            }

            if (rightChildIndex < internalVector_.size() && internalVector_[rightChildIndex] < internalVector_[leftChildIndex]) {
                indexToPushDownTo = rightChildIndex;
            }

            if (indexToPushDownTo != indexOfValueToPushDown) {;
                std::swap(internalVector_[indexToPushDownTo], internalVector_[indexOfValueToPushDown]);
                indexOfValueToPushDown = indexToPushDownTo;
            } else {
                break;
            }
        }

        return toReturn;
    }

public:
    std::vector<int> internalVector_;

private:
    static size_t getLeftChildIndex(const size_t parentIndex) {
        return parentIndex * 2 + 1;
    }

    static size_t geRightChildIndex(const size_t parentIndex) {
        return getLeftChildIndex(parentIndex) + 1;
    }

    static size_t getParentIndex(const size_t childIndex) {
        return (childIndex - (childIndex % 2 != 0 ? 1 : 2)) / 2;
    }

    void pushDown(const size_t indexOfElementToPushDown) {
        size_t leftChildIndex = getLeftChildIndex(indexOfElementToPushDown);
        size_t rightChildIndex = geRightChildIndex(indexOfElementToPushDown);
        std::optional<size_t> indexToPushDownTo;

        if (leftChildIndex >= internalVector_.size()) {
            return;
        }

        if (internalVector_[indexOfElementToPushDown] > internalVector_[leftChildIndex]) {
            indexToPushDownTo = leftChildIndex;
        }

        if (rightChildIndex < internalVector_.size() && internalVector_[rightChildIndex] < internalVector_[leftChildIndex]) {
            indexToPushDownTo = rightChildIndex;
        }

        if (!indexToPushDownTo) {
            return;
        }

        std::swap(internalVector_[*indexToPushDownTo], internalVector_[indexOfElementToPushDown]);
        pushDown(*indexToPushDownTo);
    }
};

void testCorrectlyReturnsSmallestElementWithIncreasingInsertionOrder() {
    MinHeap minHeap;
    minHeap.push(1);
    minHeap.push(2);
    minHeap.push(3);
    minHeap.push(4);
    minHeap.push(5);

    assert(minHeap.pop() == 1);
    assert(minHeap.pop() == 2);
    assert(minHeap.pop() == 3);
    assert(minHeap.pop() == 4);
    assert(minHeap.pop() == 5);
}

void testCorrectlyReturnsSmallestElementWithRandomInsertionOrder() {
    MinHeap minHeap;
    minHeap.push(15);
    minHeap.push(21);
    minHeap.push(3);
    minHeap.push(10);
    minHeap.push(6);
    minHeap.push(100);
    minHeap.push(17);

    assert(minHeap.pop() == 3);
    assert(minHeap.pop() == 6);
    assert(minHeap.pop() == 10);
    assert(minHeap.pop() == 15);
    assert(minHeap.pop() == 17);
    assert(minHeap.pop() == 21);
    assert(minHeap.pop() == 100);
}

int main() {
    testCorrectlyReturnsSmallestElementWithIncreasingInsertionOrder();
    testCorrectlyReturnsSmallestElementWithRandomInsertionOrder();

    return 0;
}