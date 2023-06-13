# Import the MaxHeap class
from heaps import MaxHeap


def test_parent():
    # Create a MaxHeap object
    heap = MaxHeap([1, 2, 3, 4, 5])

    # Test parent method for different indices
    assert heap.parent(0) is None
    assert heap.parent(1) == 0
    assert heap.parent(2) == 0
    assert heap.parent(3) == 1
    assert heap.parent(4) == 1

    print("parent method test passed")


def test_leftChild():
    # Create a MaxHeap object
    heap = MaxHeap([1, 2, 3, 4, 5])

    # Test leftChild method for different indices
    assert heap.leftChild(0) == 1
    assert heap.leftChild(1) == 3
    assert heap.leftChild(2) is None
    assert heap.leftChild(3) is None
    assert heap.leftChild(4) is None

    print("leftChild method test passed")


def test_rightChild():
    # Create a MaxHeap object
    heap = MaxHeap([1, 2, 3, 4, 5])

    # Test rightChild method for different indices
    assert heap.rightChild(0) == 2
    assert heap.rightChild(1) == 4
    assert heap.rightChild(2) is None
    assert heap.rightChild(3) is None
    assert heap.rightChild(4) is None

    print("rightChild method test passed")


# Define and call test functions for the remaining methods


def test_isLeaf():
    # Create a MaxHeap object
    heap = MaxHeap([1, 2, 3, 4, 5])

    # Test isLeaf method for different indices
    assert not heap.isLeaf(0)
    assert not heap.isLeaf(1)
    assert heap.isLeaf(2)
    assert heap.isLeaf(3)
    assert heap.isLeaf(4)

    print("isLeaf method test passed")


def test_swap():
    # Create a MaxHeap object
    heap = MaxHeap([1, 2, 3, 4, 5])

    # Test swap method
    heap.swap(1, 3)
    assert heap.heap == [5, 1, 3, 4, 2]

    print("swap method test passed")


def test_heapify():
    # Create a MaxHeap object
    heap = MaxHeap([5, 3, 1, 4, 2])

    # Test heapify method
    heap.heapify(0)
    assert heap.heap == [5, 4, 1, 3, 2]

    print("heapify method test passed")


def test_buildHeap():
    # Create a MaxHeap object
    heap = MaxHeap([5, 3, 1, 4, 2])

    # Test buildHeap method
    heap.buildHeap()
    assert heap.heap == [5, 4, 1, 3, 2]

    print("buildHeap method test passed")


def test_insert():
    # Create a MaxHeap object
    heap = MaxHeap([1, 3, 2, 4, 5])

    # Test insert method
    heap.insert(0)
    assert heap.heap == [5, 4, 2, 1, 3, 0]

    print("insert method test passed")


def test_removeMax():
    # Create a MaxHeap object
    heap = MaxHeap([1, 2, 3, 4, 5])

    # Test removeMax method
    max_val = heap.removeMax()
    assert max_val == 5
    assert heap.heap == [4, 2, 3, 1]

    print("removeMax method test passed")


def test_removeAt():
    # Create a MaxHeap object
    heap = MaxHeap([1, 2, 3, 4, 5])

    # Test removeAt method
    heap.removeAt(2)
    assert heap.heap == [5, 4, 2, 1]

    print("removeAt method test passed")


def test_removeValue():
    # Create a MaxHeap object
    heap = MaxHeap([1, 2, 3, 4, 5])

    # Test removeValue method
    heap.removeValue(3)
    assert heap.heap == [5, 4, 2, 1]

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
test_removeMax()
test_removeAt()
test_removeValue()
