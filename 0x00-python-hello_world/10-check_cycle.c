#include "lists.h"

/**
 * check_cycle -  a function in C that checks if a
 * singly linked list has a cycle in it.
 * @list: A pointer to the first element in the list
 * we can call it a pointer to the first node.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *head, *nextnode;

	/*
	 * This condition checks if
	 * 1. the first element in the list is present
	 * 2. there is a next element in the list.
	 * If either of these are false, it means that there is no cycle
	 * hence we return 0
	 */
	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	head = list;
	nextnode = head->next;

	while (head != NULL && nextnode->next != NULL && nextnode->next->next != NULL)
	{
		if (head == nextnode)
		{
			return (1);
		}
		head = head->next;
		nextnode = nextnode->next->next;
	}
	return (0);
}

