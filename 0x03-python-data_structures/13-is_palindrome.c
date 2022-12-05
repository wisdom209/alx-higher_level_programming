#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: double pointer to start of list
 *
 * Return: int
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *current, *prev, *next;

	prev = NULL;
	current = *head, next = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;

	return (*(head));
}

/**
 * is_palindrome - is palindrome
 * @head: head
 *
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head;
	listint_t *middle_start, *beginning_start;

	if (fast == NULL || fast->next == NULL || fast->next->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;

		if (fast == NULL)
		{
			beginning_start = slow->next;
			break;
		}

		if (fast->next == NULL)
		{
			beginning_start = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	slow->next = NULL;
	middle_start = reverse_list(&beginning_start);
	beginning_start = *head;

	while (middle_start != NULL && beginning_start != NULL)
	{
		if (middle_start->n == beginning_start->n)
		{
			middle_start = middle_start->next;
			beginning_start = beginning_start->next;
		}
		else
			return (0);
	}

	return (1);
}
