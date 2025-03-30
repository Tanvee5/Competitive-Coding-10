# Problem 2 : Peeking Iterator
# Time Complexity : 
'''
hasNext() - O(1)
next() - O(n) where n is the number of elements in the iterator
peek() - O(n) where n is the number of elements in the iterator
'''
# Space Complexity : O(n) where n is the number of elements in the iterator
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        # define and initialize iterator
        self.iterator = iterator
        # define and initialize the nextElement which store the next element in iterator
        self.nextElement = None
        # call advance function to get the value of next element of iterator
        self.advance()
    
    def advance(self):
        # set the next element to None
        self.nextElement = None
        # loop till we get the valid element and the hashNext of iterator return True
        while self.nextElement is None and self.iterator.hasNext():
            # store the next element of iterator in nextElement variable
            self.nextElement = self.iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        # check if there is any element in the iterator and if it is not then return runtime error
        if not self.hasNext():
            raise RuntimeError("Empty")
        # return the value of nextElement
        return self.nextElement
        

    def next(self):
        """
        :rtype: int
        """
        # check if there is any element in the iterator and if it is not then return runtime error
        if not self.hasNext():
            raise RuntimeError("Empty")
        # store the value of nextElement in the element
        element = self.nextElement
        # call advance function to get the value of next element in the iterator
        self.advance()
        # return the element
        return element
        

    def hasNext(self):
        """
        :rtype: bool
        """
        # return true if the nextElement is not None else return false
        return self.nextElement is not None

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].