#include <stdio.h>
#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into a linked list
 * @head: pointer to the linked list
 * @number: the number to be inserted
 * Return: address of the new node and NULL if it fails
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (current == NULL || new->n == number)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	else if (current != NULL || current->next->n < number)
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;

	return (new);

}
