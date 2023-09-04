#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks for a cycle in a singly linked list
 * @list: pointer to the linked list
 * Return: 1 if it is a cycle and 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	if (!list)
		return (0);

	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;

		if (first == second)
			return (1);
	}
	return (0);

}
