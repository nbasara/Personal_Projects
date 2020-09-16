public class List{
	
	Node Front;
	Node Tail;
	Node cur;
	int ListLength = 0;
	int index = -1;
	Node Temp;
	
	public List() {}
	
	void MyList() {
		Front = Tail = null;
	}
	
	
	static class Node{
		int index;
		int data;
		Node next;
		Node prev;
		
		Node(int a) {
			data = a;
			next = null;
			prev = null;
			index = 0;
			}
	}
	
	
	boolean empty() {
		if (ListLength > 0) {
			return false;
		}
		else {
			return true;
		}
	}
	boolean equals(List L) {
		int j = 0;
		moveFront();
		L.moveFront();
		for (int i = 1; i<=length();i++) {
			if(L.get() != get()) {
				j++;
			}
			moveNext();
			L.moveNext();
		}
		if(L.length() != length()) {
			return false;
		}
		else if (j == 0){
			return true;
		}
		else {
			return false;
		}
	}

	
	
	void moveNext() {
		if (cur == null) {
			cur = null;
		}
		else if (cur.next == null) {
			cur = null;
		}
		else {
			Temp = cur;
			cur = Temp.next;
			cur.next = Temp.next.next;
			cur.prev = Temp;
		}
	}
	
	void movePrev() {
		if (cur.prev == null) {
			cur = null;
		}
		else {
			Temp = cur;
			cur = Temp.prev;
			cur.prev = Temp.prev.prev;
			cur.next = Temp;
		}
	}
	void moveFront() {
		if (length() == 0) {
			cur = null;
		}
		else {
			cur = Front;
		}
	}
	
	void moveBack() {
		if (length() == 0) {
			cur = null;
		}
		else {
			cur = Tail;
		}
	}
	
	void prepend(int data){
		Node N =  new Node(data);
		if(empty()) {
			Front = cur = Tail = N;
			N.index = 0;
		}
		else {
			int i = index();
			moveFront();
			while(cur!= null)
			{
				cur.index = cur.index + 1;
				moveNext();
			}
			moveFront();
			Front.prev = N;
			N.prev = null;
			N.next = Front;
			Front = N;
			Front.index = 0;
			moveFront();
			while(i+1 != index()) {
				moveNext();
			}
		}
		ListLength++;
	}
	
	void append(int data){
		Node N =  new Node(data);
		if(empty()) {
			Front = cur = Tail = N;
			Front.index = 0;
		}
		else {
			Tail.next = N;
			N.next = null;
			N.prev = Tail;
			Tail = N;
			Tail.index = ListLength;
		}
		ListLength++;
	}
	
	void insertBefore(int data) {
		if (empty()) {
			cur = null;
		}
		else if ( cur.data == Front.data) {
			Node N =  new Node(data);
			moveFront();
			while(!(cur == null))
			{
				cur.index++;
				moveNext();
			}
			moveFront();
			cur.prev = N;
			N.next = cur;
			N.prev = null;
			Front = N;
			Front.index =0;
			ListLength++;
		}
		else {
			Node N =  new Node(data);
			Temp = cur.prev;
			Temp.next = N;
			cur.prev = N;
			N.next = cur;
			N.prev = Temp;
			N.index = cur.index;
			cur = N.next;
			while(!(cur == null)) {
				cur.index = cur.index+1;
				moveNext();
			}
			cur = N.next;
			ListLength++;
		}
	}
	void insertAfter(int data) {
		if (empty()) {
			cur = null;
		}
		else if ( cur.data == Tail.data) {
			Node N =  new Node(data);
			cur.next = N;
			N.next = null;
			N.prev = cur;
			Tail = N;
			Tail.index = ListLength;
			ListLength++;
		}
		else {
			Node N =  new Node(data);
			Temp = cur.next;
			Temp.prev = N;
			N.next = Temp;
			cur.next = N;
			N.prev = cur;
			N.index = cur.index +1;
			while(!(cur == null)) {
				cur.index = cur.index+1;
				moveNext();
			}
			cur = N.prev;
			ListLength++;
		}
	}
	
	void deleteFront() {
		if (length() > 1){
			int i = cur.index;
			Temp = Front.next;
			Temp.prev = null;
			if(front() == get()) {
				Front  = Temp;
				moveFront();
				while(!(cur == null)) {
					cur.index = cur.index -1;
					moveNext();
				}	
			}
			else{
				Front  = Temp;
				moveFront();
				while(!(cur == null)) {
					cur.index = cur.index -1;
					moveNext();
				}
				moveFront();
				while(i-1 != index()) {
					moveNext();
			}	
			}
			ListLength--;
		}
		else if (length() == 1){
			Front = cur = Tail = null;
			ListLength--;
		}
		else{
			Front = cur = Tail = null;
		}
	}
	void deleteBack() {
		if (length() > 1){
			
			Temp = Tail.prev;
			Temp.next = null;
			if(back() == get()) {
				cur = null;
			}
			Tail = Temp;
			ListLength--;
		}
		else if (length() == 1){
			Front = cur = Tail = null;
			ListLength--;
		}
		else{
			Front = cur = Tail = null;
		}
	}
	void delete() {
		if ( get() == back()) {
			cur.prev.next = null;
			Tail = cur.prev;
			cur = null;
			ListLength--;
		}
		else if ( cur == null){
			cur = null;
		}
		else if ( cur.data == Front.data){
			cur.next.prev = null;
			Front = cur.next;
			moveFront();
			while(!(cur == null)) {
				cur.index = cur.index -1;
				moveNext();
			}
			ListLength--;
		}
		else {
			Temp = cur.next;
			cur.prev.next = cur.next;
			cur.next.prev = cur.prev;
			moveFront();
			while(!(cur == null)) {
				cur.index = cur.index -1;
				moveNext();
			}
			ListLength--;
		}
	}
	
	int index() {
		if(cur == null){
			return -1;
		}
		else {
			return cur.index;
		}
	}
	
	int get() {
		if (cur == null) {
			return -1;
		}
		else {
			return cur.data;
		}
		
	}
	
	int front() {
		if (length()==0) {
			return -1;
		}
		else {
			return Front.data;
		}
	}
	int back() {
		if (length()==0) {
			return -1;
		}
		else {
			return Tail.data;
		}
	}

	void PrintLength() {
		System.out.println(ListLength);
	}
	
	int length() { 
		return ListLength;
		}
	
	void printTheList(){
		moveFront();
		for(int i =0; i < length();i++){
		    System.out.print(get()+" ");
		    moveNext();
		   }
	}
	
	void printTheListRev(){
		Node n = Tail;
		while (n != null){
			System.out.println(n.index+" ");
			n = n.prev;
		}
		System.out.println("\n\n");
	}
	
	List copy() {
		List myList  = new List();
		moveFront();
		while(cur != null){
			myList.append(get());
			moveNext();
		}
		moveFront();
		return myList;
	}
	
	void clear(){
		Front = Tail = cur = null;
		ListLength = 0;
	}
	
	public String toString() {
		
		String temp1 = "";
		moveFront();
		for (int i= 0;i<length();i++) {
			temp1 = temp1 +get()+ " ";
			moveNext();
		}
		return temp1;
	}
	
	
}
