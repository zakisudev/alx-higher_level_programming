#include "lists.h"

/**
 * palindrome - check if is palindrome with recursion
 * @l: l
 * @r: r
 *
 * Return: 1 palindrome, 0 not palindrome
 */
int palindrome(listint_t **l, listint_t *r)
{
	int result;

	if (r != NULL)
	{
		result = palindrome(l, r->next);
		if (result != 0)
		{
			result = (r->n == (*l)->n);
			*l = (*l)->next;
			return (result);
		}
		return (0);

	}
	return (1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of linked list
 *
 * Return: 1 palindrome, 0 not palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (0);
	}
	return (palindrome(head, *head));
}
