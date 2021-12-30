// using test cases from https://leetcode.com/problems/implement-queue-using-stacks/

#include <cstddef>
#include <iostream>
#include <vector>
#include <string>

class QueueWithArray {
public:
    QueueWithArray(): internalArray_(std::vector<int>(kInitialSize)), start_(0), end_(0) {}
    
    void push(int x) {
        internalArray_[end_] = x;
        end_ = (end_ + 1) % internalArray_.size();
        
        if (end_ == start_) {
            const std::size_t previousSizeOfInternalArray = internalArray_.size();        
            internalArray_.resize(internalArray_.size() * kExtensionRatioWhenInternalArrayIsFull);
            
            for (std::size_t i = start_; i < previousSizeOfInternalArray; ++i) {
                internalArray_[i + previousSizeOfInternalArray] = internalArray_[i];
            }
            
            start_ += previousSizeOfInternalArray;
        }
    }
    
    int pop() {
        const int toReturn = internalArray_[start_];
        start_++;
        
        return toReturn;
    }
    
    int peek() {
        return internalArray_[start_];
    }
    
    bool empty() {
        return start_ == end_;
    }

private:
    static constexpr std::size_t kInitialSize = 10;
    static constexpr std::size_t kExtensionRatioWhenInternalArrayIsFull = 2;

    std::vector<int> internalArray_;
    std::size_t start_;
    std::size_t end_;
};

int main()  { 
    return 0; 
}