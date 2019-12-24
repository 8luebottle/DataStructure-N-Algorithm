## Linked List Cycle
#### Given a Linked List, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

**EXAMPLE 1**
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node
```

**EXAMPLE 2**
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

**EXAMPLE 3**
```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

Can you solve it using O(1) (i.e. constant) memory?
