/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
     
        ListNode dummy = new ListNode(),
        previous_pointer = dummy;
        int carry = 0;
        
        while(l1 != null || l2 != null){
            int v1 = l1 != null ? l1.val : 0;
            int v2 = l2 != null ? l2.val : 0;
            int sum = v1 + v2 + carry;
            // reset the carry to 0 after use 
            carry = 0;
            if(sum > 9){
                carry++;
            }
            ListNode curNode = new ListNode(sum%10);
            
            previous_pointer.next = curNode;
            previous_pointer = curNode;
            
            l1 = l1 != null ? l1.next : null;
            
             l2 = l2 != null ? l2.next : null; 
        }
        
        if(carry != 0){
            ListNode cur = new ListNode(1);
            previous_pointer.next = cur;
            
        }
        return dummy.next;
        
        
        
        
    }
}