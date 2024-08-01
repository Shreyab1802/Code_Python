def cutLinkedList(self, head: Optional[ListNode], length: int) -> Optional[ListNode]:
    current = head
    count = 0
    while current and count < length - 1:
        current = current.next
        count += 1

    if current:
        current.next = None

    return head