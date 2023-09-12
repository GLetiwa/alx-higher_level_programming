#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of a linked list
 * Return: 0 if not a palindrome and 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr, *start, *prev, *temp;

	ptr = *head;
	start = *head;
	prev = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (ptr != NULL && ptr->next != NULL)
	{
		ptr = ptr->next->next;
		temp = start->next;
		start->next = prev;
		prev = start;
		start = temp;
	}
	if (ptr != NULL)
	{
		start = start->next;
	}
	while (start != NULL)
	{
		if (start->n != prev->n)
			return (0);
		start = start->next;
		prev = prev->next;
	}
	return (1);
}
