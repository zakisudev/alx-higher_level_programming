#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: Pointer to the head of the linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
    listint_t *sl = list;
    listint_t *fa = list;

    while (sl && fa && fa->next)
    {
        sl = sl->next;
        fa = fa->next->next;

        if (sl == fa)
            return 1;
    }

    return 0;
}
