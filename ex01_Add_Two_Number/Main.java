package leetcode_practice.ex01_Add_Two_Number;

public class Main {
	public static void main(String[] args){
        ListNode a = new ListNode(9);
        a.add_node(new ListNode(9));
        a.add_node(new ListNode(9));
        a.add_node(new ListNode(9));
        a.add_node(new ListNode(9));
        a.add_node(new ListNode(9));
        a.add_node(new ListNode(9));
        ListNode b = new ListNode(9);
        b.add_node(new ListNode(9));
        b.add_node(new ListNode(9));
        b.add_node(new ListNode(9));
        ListNode ans;
        Solution s = new Solution();
		ans = s.addTwoNumbers(a, b);
		while (ans.next != null){
			System.out.println(ans.val);
			ans = ans.next;
		}
		System.out.println(ans.val);
    }
}
