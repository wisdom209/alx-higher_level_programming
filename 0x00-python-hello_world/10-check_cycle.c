#include lists.h

/**
 * check_cycle - check loop
 * @list: list
 *
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			slow = list;
			while (slow != fast)
			{
				slow = slow->next;
				fast = fast->next;
			}
			return (1);
		}
	}

	return (0);
}
