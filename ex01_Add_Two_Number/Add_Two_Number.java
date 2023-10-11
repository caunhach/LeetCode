package leetcode_practice.ex01_Add_Two_Number;

class list_node{
	int value;
	list_node next = null;
	public list_node(){
	}
	public list_node(int value){
		this.value = value;
	}
}

class linked_list{
	list_node Node;
	public linked_list(){
	}
	public void add_node(int val){
		list_node tmp = new list_node(val);
		if (Node == null)
		{
			Node = tmp;
			return ;
		}
		list_node head = Node;
		tmp.value = val;
		while (Node.next != null)
			Node = Node.next;
		Node.next = tmp;
		Node = head;
	}
	public void print_node(){
		while(Node != null){
			System.out.println(Node.value);
			Node = Node.next;
		}
	}
}

public class Add_Two_Number {
	public static void main (String[] args){
		linked_list a = new linked_list();
		linked_list b = new linked_list();
		a.add_node(9);
		a.add_node(9);
		a.add_node(9);
		a.add_node(9);
		a.add_node(9);
		a.add_node(9);
		a.add_node(9);
		b.add_node(9);
		b.add_node(9);
		b.add_node(9);
		b.add_node(9);
		linked_list ans = new linked_list();
		int tmp = 0;
		int remain = 0;
		while (a.Node != null || b.Node!= null || remain!= 0){
			tmp = 0;
			if (a.Node != null)
			{
				tmp += a.Node.value;
				a.Node = a.Node.next;
			}
			if (b.Node != null)
			{
				tmp += b.Node.value;
				b.Node = b.Node.next;
			}
			tmp += remain;
			remain = tmp / 10;
			tmp = tmp % 10;
			ans.add_node(tmp);
		}
		ans.print_node();
	}
}
