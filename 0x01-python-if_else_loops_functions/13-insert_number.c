#include "lists.h"
#include <stdlib.h>


/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to head of list
 * @number: integer number.
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current, *next_node;

    if (!head)
        return (NULL);

    new_node = malloc(sizeof(listint_t));
    if (!new_node)
        return (NULL);
    new_node->next = NULL;
    new_node->n = number;

    if (!*head)
        *head = new_node;
    else if(new_node->n < (*head)->n)
    {
        new_node->next = *head;
        *head = new_node;
    }
    else
    {
        current = *head;
        while(current->next)
        {
            next_node = current->next;
            if (new_node->n < next_node->n)
            {
                new_node->next = next_node;
                current->next = new_node;
                return new_node;
            }
            current = current->next;
        }
        current->next = new_node;
    }

    return new_node;

}
