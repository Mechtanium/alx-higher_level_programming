#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks for cyclic list
 * @list: the list to be checked
 * 
 * Description: checks a singly liked list for cyclic linking
 * Return: 0 if linked list has no cyclic 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = list, *temp = NULL;

	if (ptr == NULL)
		return (0);

	if (ptr->next == NULL)
		return (0);
	else if (ptr->next != ptr)
	{
		while (!temp)
		{
			ptr = ptr->next;

			if (ptr == NULL)
				return (0);
			else
			{
				temp = ptr->next;

				while (temp != ptr && temp != NULL)
				{
					temp = temp->next;
					
				}
			}
		}
	}

	return (1);
}
