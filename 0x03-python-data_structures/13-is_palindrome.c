#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * get_value_at_position - Get value at a position
 * @head: head of list
 * @position: position to get
 *
 * Return: int
 */
int get_value_at_position(listint_t *head, int position)
{
	listint_t *temp = head;
	int counter = -1;
	int value = 0;

	while (temp != NULL)
	{
		counter++;
		value = temp->n;
		temp = temp->next;
		if (counter == position)
			break;
	}
	return (value);
}

/**
 * is_palindrome - is palindrome
 * @head: head
 *
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	int length = 0, i = 0;
	listint_t *temp = *head;

	if (head == NULL)
		return (1);

	while (temp != NULL)
	{
		temp = temp->next;
		length++;
	}

	if (length == 1)
		return (1);

	for (i = 0; i < length / 2; i++)
	{
		int left_check = get_value_at_position(*head, i);
		int right_check = get_value_at_position(*head, length - i - 1);

		if (left_check != right_check)
			return (0);
	}

	return (1);
}
