#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks for a cycle in a singly linked list
 * @list: pointer to the linked list
 * Return: 1 if it is a cycle and 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list;

	while (current != NULL)
	{
		current = current->next;
		if (current->next == list)
			return (1);
		else
			return (0);
	}
	return (0);

}
