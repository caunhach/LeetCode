package leetcode_practice.ex01_Add_Two_Number;

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

public class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
      public void add_node(ListNode node){
        ListNode HeadNode = next;
        while (next != null)
            next = next.next;
        next = node;
        next = HeadNode;
      }
}

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ans = null;
        int tmp = 0;
        int remainder = 0;
        while (l1 != null || l2 != null || remainder != 0){
            if (l1 != null){
                tmp += l1.val;
                l1 = l1.next;
            }
            if (l2 != null){
                tmp += l2.val;
                l2 = l2.next;
            }
            tmp += remainder;
            remainder = tmp/10;
            tmp %= 10;
            ListNode tmpNode = new ListNode(tmp);
            if (ans == null)
                ans = tmpNode;
            else
                ans.add_node(tmpNode);
        }
        return ans;
    }
}
