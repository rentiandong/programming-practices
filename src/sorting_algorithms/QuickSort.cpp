#include <vector>
#include <assert.h>

void quickSort(std::vector<int>& toSort, const size_t start, const size_t end) {
    if (start + 1 >= end) {
        return;
    }

    const int pivot = toSort[end - 1];
    size_t indexLastElementLessThanPivot = start;
    
    for (size_t i = start; i < end - 1; ++i) {
        if (toSort[i] < pivot) {
            const int temp = toSort[i];

            toSort[i] = toSort[indexLastElementLessThanPivot];
            toSort[indexLastElementLessThanPivot] = temp;
            ++indexLastElementLessThanPivot;
        }
    }

    toSort[end - 1] = toSort[indexLastElementLessThanPivot];
    toSort[indexLastElementLessThanPivot] = pivot;

    quickSort(toSort, start, indexLastElementLessThanPivot);
    quickSort(toSort, indexLastElementLessThanPivot + 1, end);
}

void quickSort(std::vector<int>& toSort) {
  quickSort(toSort, 0, toSort.size());  
}

void assertSorted(const std::vector<int>& vector) {
  for (size_t i = 1; i < vector.size(); ++i) {
    assert(vector[i] >= vector[i - 1]);
  }
}

void testSortEmptyVector() {
  std::vector<int> emptyVector;
  quickSort(emptyVector);

  assertSorted(emptyVector);
}

void testSortLengthOneVector() {
  std::vector<int> lengthOneVector = {1};
  quickSort(lengthOneVector);

  assertSorted(lengthOneVector);
}

void testSortAlreadySortedVector() {
  std::vector<int> sortedVector = {1, 2, 3, 4, 5};
  quickSort(sortedVector);

  assertSorted(sortedVector);
}

void testSortReverselySortedVector() {
  std::vector<int> reverselySortedVector = {5, 4, 3, 2, 1};
  quickSort(reverselySortedVector);

  assertSorted(reverselySortedVector);
}

void testSortOddLengthVector() {
  std::vector<int> oddLengthVector = {1, 4, 3, 2, 5};
  quickSort(oddLengthVector);

  assertSorted(oddLengthVector);
}

void testSortEvenLengthVector() {
  std::vector<int> evenLengthVector = {5, 1, 1, 2, 1, 6};
  quickSort(evenLengthVector);

  assertSorted(evenLengthVector);
}

int main() {
  testSortEmptyVector();
  testSortLengthOneVector();
  testSortAlreadySortedVector();
  testSortReverselySortedVector();
  testSortEvenLengthVector();
  testSortOddLengthVector();
  return 0;
}