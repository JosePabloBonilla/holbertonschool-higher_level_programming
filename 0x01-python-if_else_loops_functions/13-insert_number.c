#include "lists.h"
/**
 * insert_node - insert node
 * @head: head of list
 * @number: number to insert
 * Return: address of the new node, NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	tmp = *head;
	if (tmp == NULL || tmp->n >= number)
	{
		new->next = tmp;
		tmp = new;
		return (new);
	}

	while (tmp && tmp->next && tmp->next->n < number)
		tmp = tmp->next;

	new->next = tmp->next;
	tmp->next = new;
	return (new);
}
