//Nathaniel Basara
//nbasara@ucsc.edu
//pa3
//
//
//

public class List{
	
	Node Front;
	Node Tail;
	Node cur;
	int ListLength = 0;
	int index = -1;
	Node Temp;
	
	public List() {}
	

	static class Node{
		Object data;
		Node next;
		Node prev;
		
		Node(Object a) {
			data = a;
			next = null;
			prev = null;
			}
    
    //Points to Entry Equals
    public boolean equals(Object x){
      Node N = (Node) x;
      if(!(data.equals(x))){
        return false;
      }
      return true;
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
  
  //calls node equals
	public boolean equals(Object x) {
    List L = (List) x;
		moveFront();
		L.moveFront();
    if(L.length() != length()) {
			return false;
		}
		while (index() != -1 ) {
			if(!(cur.data.equals(L.cur.data))) {
				return false;
			}
			moveNext();
			L.moveNext();
		}
		return true;
	}

	
	
	void moveNext() {
		if (cur == null) {
			cur = null;
      index = -1;
		}
		else if (cur.next == null) {
			cur = null;
      index = -1;
		}
		else {
			Temp = cur;
			cur = Temp.next;
			cur.next = Temp.next.next;
			cur.prev = Temp;
      index++;
		}
	}
	
	void movePrev() {
		if (cur.prev == null) {
			cur = null;
      index = -1;
		}
		else {
			Temp = cur;
			cur = Temp.prev;
			cur.prev = Temp.prev.prev;
			cur.next = Temp;
      index--;
		}
	}
	void moveFront() {
		if (length() == 0) {
			cur = null;
		}
		else {
			cur = Front;
      index = 0;
		}
	}
	
	void moveBack() {
		if (length() == 0) {
			cur = null;
		}
		else {
			cur = Tail;
      index = ListLength - 1;
		}
	}
	
	void prepend(Object data){
		Node N =  new Node(data);
		if(empty()) {
			Front = cur = Tail = N;
		}
		else {
			Front.prev = N;
			N.prev = null;
			N.next = Front;
			Front = N;
      index++;
		}
		ListLength++;
	}
	
	void append(Object data){
		Node N =  new Node(data);
		if(empty()) {
			Front = cur = Tail = N;
		}
		else {
			Tail.next = N;
			N.next = null;
			N.prev = Tail;
			Tail = N;
		}
		ListLength++;
	}
	
	void insertBefore(Object data) {
		if (empty()) {
			cur = null;
		}
		else if ( cur.data == Front.data) {
			Node N =  new Node(data);
			cur.prev = N;
			N.next = cur;
			N.prev = null;
			Front = N;
			index++;
			ListLength++;
		}
		else {
			Node N =  new Node(data);
			Temp = cur.prev;
			Temp.next = N;
			cur.prev = N;
			N.next = cur;
			N.prev = Temp;
			index++;
			ListLength++;
		}
	}
	void insertAfter(Object data) {
		if (empty()) {
			cur = null;
		}
		else if ( cur.data == Tail.data) {
			Node N =  new Node(data);
			cur.next = N;
			N.next = null;
			N.prev = cur;
			Tail = N;
			ListLength++;
		}
		else {
			Node N =  new Node(data);
			Temp = cur.next;
			Temp.prev = N;
			N.next = Temp;
			cur.next = N;
			N.prev = cur;
			ListLength++;
		}
	}
	
	void deleteFront() {
		if (length() > 1){
			Temp = Front.next;
			Temp.prev = null;
			if(index() == 0) {
        cur = null;
        index = -1;
			}
			Front  = Temp;
			ListLength--;
      index--;
		}
		else if (length() == 1){
			Front = cur = Tail = null;
      index = -1;
			ListLength--;
		}
		else{
			Front = cur = Tail = null;
      index = -1;
		}
	}
	void deleteBack() {
		if (length() > 1){
			Temp = Tail.prev;
			Temp.next = null;
			if(index() == ListLength - 1) {
				cur = null;
        index = -1;
			}
			Tail = Temp;
			ListLength--;
		}
		else if (length() == 1){
			Front = cur = Tail = null;
      index = -1;
			ListLength--;
		}
		else{
			Front = cur = Tail = null;
      index = -1;
		}
	}
	void delete() {
    if(length() == 1){
      Front = cur = Tail = null;
      index = -1;
      ListLength--;
    }
		else if ( index() == ListLength - 1 ) {
			cur.prev.next = null;
			Tail = cur.prev;
			cur = null;
      index = -1;
			ListLength--;
		}
		else if ( cur == null){
			cur = null;
      index = -1;
		}
		else if ( index() == 0){
			cur.next.prev = null;
			Front = cur.next;
			cur = null;
      index = -1;
			ListLength--;
		}
		else {
			Temp = cur.next;
			cur.prev.next = cur.next;
			cur.next.prev = cur.prev;
		  cur = null;
      index = -1;
			ListLength--;
		}
	}
	
	int index() {
		if(cur == null){
			return -1;
		}
		else {
			return index;
		}
	}
	
	Object get() {
		if (cur == null) {
			throw new RuntimeException("List Error: get() cur DNE "); 
    }
		else {
			return cur.data;
		}
		
	}
	
	Object front() {
		if (length()==0) {
			return -1;
		}
		else {
			return Front.data;
		}
	}
	Object back() {
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
    index = -1;
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
