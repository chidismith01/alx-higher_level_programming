#include "lists.h"

/**
 * check_cycle - function that checks if a list has a cycle
 * @list: linked list
 * return: return 1 if there is cycle else 0
**/

int check_cycle(listint_t *list)
{
	listint_t *step2, *step1;
	if (!list || !list->next)
		return(0);
	step2 = list;
	step1 = list;

	while(step1 != NULL && step2 != NULL && step2->next != NULL)
	{
		step1 = step1->next;
		step2 = step2->next;
		if(step1 == step2)
		{
			return (1);
		}
	}
	return (0);
}
