#include "lists.h"

/**
 * insert_node - insert a node at sorted position
 * @head: head
 * @number: number
 *
 * Return: linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head, *temp2 = malloc(sizeof(listint_t));
	int position = 0, i = 0, j = 0;

	while (temp != NULL)
	{
		position++;
		if (number <= temp->n)
			break;
		temp = temp->next;
	}
	if (temp == NULL)
		position++;
	temp = *head;
	if (!temp2)
		return (NULL);
	while (temp != NULL)
	{
		temp = temp->next;
		i++;
	}
	if (position > i + 1 || position <= 0)
	{
		free(temp2);
		return (NULL);
	}
	if (*head == NULL || position == 1)
	{
		temp2->n = number;
		temp2->next = *head;
		*head = temp2;
		return (temp2);
	}
	temp = *head;
	for (j = 1; j <= position - 2; j++)
		temp = temp->next;
	temp2->n = number;
	temp2->next = temp->next;
	temp->next = temp2;
	return (temp2);
}
