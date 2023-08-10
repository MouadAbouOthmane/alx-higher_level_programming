#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *tmp;
    listint_t *head;

    if (!list)
        return (0);

    head = list;
    tmp = list;
    while (tmp->next != NULL)
    {
        if (tmp->next == head)
            return (1);
        tmp = tmp->next;
    }
    return (0);
}
