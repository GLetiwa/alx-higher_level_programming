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
	listint_t *ptr, *start, *mid, *end;

	ptr = *head;
	start = (*head)->next;
	mid = end = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (ptr != NULL)
	{
		ptr = ptr->next;
	}
	ptr = start;
	while (ptr != mid)
	{
		ptr = ptr->next;
		start = ptr;
	}
	while (ptr != end)
	{
		ptr = mid->next;
		end = ptr;
	}
	if (start == end)
		return (1);
	return (0);
}
