#include <vector>
#include <assert.h>

void mergeSort(std::vector<int>& toSort, const size_t start, const size_t end) {
  if (end <= start + 1) {
    return;
  }

  const size_t mid = (start + end) / 2;

  mergeSort(toSort, start, mid);
  mergeSort(toSort, mid, end);

  std::vector<int> sorted;
  size_t left = start;
  size_t right = mid;

  while (left < mid && right < end) {
    size_t& indexOfNextSmallestElement = toSort[left] < toSort[right] ? left : right;
    
    sorted.push_back(toSort[indexOfNextSmallestElement]);
    ++indexOfNextSmallestElement;
  }

  size_t indexWithElementsRemaining = left == mid ? right : left;
  size_t indexBoundWithElementsRemaining = left == mid ? end : mid;

  for (size_t i = indexWithElementsRemaining; i < indexBoundWithElementsRemaining; ++i) {
    sorted.push_back(toSort[i]);
  }

  for (int i = start; i < end; ++i) {
    toSort[i] = sorted[i - start];
  }
}

void mergeSort(std::vector<int>& toSort) {
  mergeSort(toSort, 0, toSort.size());
}

void assertSorted(const std::vector<int>& vector) {
  for (size_t i = 1; i < vector.size(); ++i) {
    assert(vector[i] >= vector[i - 1]);
  }
}

void testSortEmptyVector() {
  std::vector<int> emptyVector;
  mergeSort(emptyVector);

  assertSorted(emptyVector);
}

void testSortLengthOneVector() {
  std::vector<int> lengthOneVector = {1};
  mergeSort(lengthOneVector);

  assertSorted(lengthOneVector);
}

void testSortAlreadySortedVector() {
  std::vector<int> sortedVector = {1, 2, 3, 4, 5};
  mergeSort(sortedVector);

  assertSorted(sortedVector);
}

void testSortReverselySortedVector() {
  std::vector<int> reverselySortedVector = {5, 4, 3, 2, 1};
  mergeSort(reverselySortedVector);

  assertSorted(reverselySortedVector);
}

void testSortOddLengthVector() {
  std::vector<int> oddLengthVector = {1, 4, 3, 2, 5};
  mergeSort(oddLengthVector);

  assertSorted(oddLengthVector);
}

void testSortEvenLengthVector() {
  std::vector<int> evenLengthVector = {5, 1, 1, 2, 1, 6};
  mergeSort(evenLengthVector);

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