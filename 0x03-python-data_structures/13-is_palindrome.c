#include "lists.h"

/**
 * reverse_list - a function to reverse a linked
 * list in place
 *
 * @head: pointer to the first element in the list
 *
 */

void reverse_list(listint_t **head)
{
	listint_t *current_head = *head;
	listint_t *next_node = NULL;
	listint_t *previous_node = NULL;

	while (current_head)
	{
		next_node = current_head->next;
		current_head->next = previous_node;

		previous_node = current_head;
		current_head = next_node;
	}
}

/**
 * is_palindrome - a function that checks if a
 * linked list is a palindrome
 *
 * @head: a pointer to the first element in the list
 *
 * Return: 1 if the list is a palindrome or 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *current_head = *head, *rev = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			rev = slow->next;
			break;
		}

		if (!fast->next)
		{
			rev = slow->next->next;
			break;
		}

		slow = slow->next;
	}
	reverse_list(&rev);
	while (rev && current_head)
	{
		if (rev->n == current_head->n)
		{
			rev = rev->next;
			current_head = current_head->next;
		}
		else
			return (0);
	}

	if (!rev)
		return (1);

	return (0);
}
