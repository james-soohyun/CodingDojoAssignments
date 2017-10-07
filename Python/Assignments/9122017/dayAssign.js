/* Creation of connected nodes/linked list in JavaScript */

/* Node constructor function: nodes in a linked list are objects that have a value and a next attribute. When the constructor function is called, a new node is created taking on the parameter as its value and can refer to another memory space that contains an object with its this.next attribute */
function Node(val)
{
	this.val = val;
	this.next = null;
}

/* Singlely linked list constructor function: Slls are objects that are not a node but have a head. In this case, the constructor function also has a function bound to the key add which adds a new node at the last node in a linked list. */
function Sll()
{
/* this.head places "head" into the object with the value null; head is a pointer that will be set to a memory space containing another object */
	this.head = null
/* this.add is a function that checks to see if there exists a node that branches from the current node; if there is, current will be set to the next node; if not, the function will create a node from the current node */
	this.add = function(val)
	{
		var tempNode = new Node(val);
		if (this.head == null)
		{
			this.head = tempNode;
		}
		else
		{
			var curNode = this.head;
			while (curNode.next != null)
			{
				curNode = curNode.next;
			}
		}
		curNode.next = tempNode;
	}
}