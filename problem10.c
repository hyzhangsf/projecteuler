#include <stdio.h>
#include <stdlib.h>
int TRUE = 1, FALSE = 0;

typedef struct Node_{
	int value;
	struct Node_ *next;
} Node;

typedef struct _List{
	Node* first_node;
	Node* last_node;
} List;

Node* new_node_ptr(int value){
	Node* new_node_ptr = (Node*) calloc(1, sizeof(Node));
	new_node_ptr->value = value;
	new_node_ptr->next = NULL;
	return new_node_ptr;
}

List* new_list_ptr(){
	return (List*) calloc(1, sizeof(List));
}

void append(List* list_ptr, int value){
	Node* new_node = new_node_ptr(value);
	if(list_ptr->first_node==NULL){
		list_ptr->first_node = new_node;
		list_ptr->last_node = new_node;
	}else{
		list_ptr->last_node->next = new_node;
		list_ptr->last_node = new_node;
	}
}
int is_prime(List* primes, int n){
	if (n==0 || n ==1)
		return FALSE;
	for(Node* node_ptr = primes->first_node; node_ptr != NULL; node_ptr = node_ptr->next ){		
		if(n % node_ptr->value == 0)
			return FALSE;		
	}
	append(primes, n);
	return TRUE;
}

int main(){
	List* primes = new_list_ptr();
	long long sum = 0;
	for(int n = 0; n < 2000000; n ++){
		if(is_prime(primes, n))
			sum += (long long)n;
	}
	printf("sum is %lld\n", sum);
	return 0;
}	