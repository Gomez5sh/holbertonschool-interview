#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Insert node in linked list
 * @head: head node
 * @number: int to insert in list
 * Return: new_node node
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *point;

    if (!head)
    {
        return (NULL);
    }
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
    {
        return (NULL);
    }
    new_node->n = number;
    if (!*head)
    {
        *head = new_node;
        return (new_node);
    }
    point = *head;
    if (number < point->n)
    {
        new_node->next = point;
        *head = new_node;
        return (new_node);
    }
    while (point->next && number > point->next->n)
    {
        point = point->next;
    }
    new_node->next = point->next;
    point->next = new_node;
    return (new_node);
}