#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: head of linked list
 * Return: 0 for no cycle, 1 if it has a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	while (list)
	{
		tmp = list;
		list = list->next;
		if (tmp <= list)
			return (1);
	}
	return (0);
}
