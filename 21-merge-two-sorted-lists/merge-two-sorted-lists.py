# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution(object):

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        st = ListNode()
        head = ListNode()
        
        if not list1 or not list2:
            if list1:
                head = list1
            else:
                head = list2
     
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    print(list1.val)
                    if head.val == 0:
                        st = ListNode(list1.val)
                        head = st
                        print(head)
                        if st.next != None:
                            st = st.next
                    else:
                        st.next = ListNode(list1.val)
                        if st.next != None:
                            st = st.next
                    
                    
                    list1 = list1.next
                elif list2.val < list1.val:    
                    if head.val == 0:
                        st = ListNode(list2.val)
                        head = st
                        if st.next != None:
                            st = st.next
                    else:
                        st.next = ListNode(list2.val)
                        if st.next != None:
                            st = st.next
                    
                    list2 = list2.next
                elif list2.val == list1.val:

                
                    if head.val == 0:
                        st = ListNode(list1.val)
                        head = st
                        if st.next != None:
                            st = st.next
                        
                    else:
                        st.next = ListNode(list1.val)
                        if st.next != None:
                            st = st.next
                    list1 = list1.next
                    st.next =  ListNode(list2.val)
                    if st.next != None:
                            st = st.next
                    list2 = list2.next
            else:
                if list1:
                    if head.val == 0:
                        st = ListNode(list1.val)
                        head = st
                        if st.next != None:
                            st = st.next
                    else:
                        st.next = ListNode(list1.val)
                        if st.next != None:
                            st = st.next
                    
                    
                    list1 = list1.next
                elif list2:    
                    if head.val == 0:
                        st = ListNode(list2.val)
                        head = st
                        if st.next != None:
                            st = st.next
                    else:
                        st.next = ListNode(list2.val)
                        if st.next != None:
                            st = st.next
                    
                    list2 = list2.next
                
            #print(st)
                
        return head
            
            
            