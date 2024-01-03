#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * return: numbers of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes*/

	current = h;
	n = 0;
	while(current != NULL)
	{
		print("%i\n",curent->n);
		current = current->next
		n++;
	}
	return(n)
}
/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;
	
	new = malloc(sizeof(listint_t));
	if(new == NULL) /* condition for our new node if error occurs */
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;
	
	return (new);
}

/**
 * free_listint -free a listint_t list
 * @head: pointer to list to be free
 * return: viod
 */
void free_listint(listint_t *head)
{
	listint_t *current;
	
	while (head != NULL)
		head = head->next;
	free(current);

}

