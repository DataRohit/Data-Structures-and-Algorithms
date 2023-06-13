# Import the MinHeap class
from heaps import MinHeap


def test_parent():
    # Create a MinHeap object
    heap = MinHeap([1, 2, 3, 4, 5])

    # Test parent method for different indices
    assert heap.parent(0) is None
    assert heap.parent(1) == 0
    assert heap.parent(2) == 0
    assert heap.parent(3) == 1
    assert heap.parent(4) == 1

    print("parent method test passed")


def test_leftChild():
    # Create a MinHeap object
    heap = MinHeap([1, 2, 3, 4, 5])

    # Test leftChild method for different indices
    assert heap.leftChild(0) == 1
    assert heap.leftChild(1) == 3
    assert heap.leftChild(2) == None
    assert heap.leftChild(3) == None
    assert heap.leftChild(4) == None

    print("leftChild method test passed")


def test_rightChild():
    # Create a MinHeap object
    heap = MinHeap([1, 2, 3, 4, 5])

    # Test rightChild method for different indices
    assert heap.rightChild(0) == 2
    assert heap.rightChild(1) == 4
    assert heap.rightChild(2) == None
    assert heap.rightChild(3) == None
    assert heap.rightChild(4) == None

    print("rightChild method test passed")


# Define and call test functions for the remaining methods


def test_isLeaf():
    # Create a MinHeap object
    heap = MinHeap([1, 2, 3, 4, 5])

    # Test isLeaf method for different indices
    assert heap.isLeaf(0) == False
    assert heap.isLeaf(1) == False
    assert heap.isLeaf(2) == True
    assert heap.isLeaf(3) == True
    assert heap.isLeaf(4) == True

    print("isLeaf method test passed")


def test_swap():
    # Create a MinHeap object
    heap = MinHeap([1, 2, 3, 4, 5])

    # Test swap method
    heap.swap(1, 3)
    assert heap.heap == [1, 4, 3, 2, 5]

    print("swap method test passed")


def test_heapify():
    # Create a MinHeap object
    heap = MinHeap([5, 3, 1, 4, 2])

    # Test heapify method
    heap.heapify(0)

    assert heap.heap == [1, 2, 5, 4, 3]

    print("heapify method test passed")


def test_buildHeap():
    # Create a MinHeap object
    heap = MinHeap([5, 3, 1, 4, 2])

    # Test buildHeap method
    heap.buildHeap()
    assert heap.heap == [1, 2, 5, 4, 3]

    print("buildHeap method test passed")


def test_insert():
    # Create a MinHeap object
    heap = MinHeap([1, 3, 2, 4, 5])

    # Test insert method
    heap.insert(0)
    assert heap.heap == [0, 3, 1, 4, 5, 2]

    print("insert method test passed")


def test_removeMin():
    # Create a MinHeap object
    heap = MinHeap([1, 2, 3, 4, 5])

    # Test removeMin method
    min_val = heap.removeMin()
    assert min_val == 1
    assert heap.heap == [2, 4, 3, 5]

    print("removeMin method test passed")


def test_removeAt():
    # Create a MinHeap object
    heap = MinHeap([1, 2, 3, 4, 5])

    # Test removeAt method
    heap.removeAt(2)
    assert heap.heap == [1, 2, 5, 4]

    print("removeAt method test passed")


def test_removeValue():
    # Create a MinHeap object
    heap = MinHeap([1, 2, 3, 4, 5])

    # Test removeValue method
    heap.removeValue(3)
    assert heap.heap == [1, 2, 5, 4]

    print("removeValue method test passed")


# Call test functions
test_parent()
test_leftChild()
test_rightChild()
test_isLeaf()
test_swap()
test_heapify()
test_buildHeap()
test_insert()
test_removeMin()
test_removeAt()
test_removeValue()
