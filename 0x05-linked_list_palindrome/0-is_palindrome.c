#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check for palindrome
 *
 * @head: head of list
 *
 * Return: 1 if True
 */

int is_palindrome(listint_t **head)
{
  listint_t **arr = NULL;
  listint_t *aba = NULL;
  int nexn = 0;

  if (!head)
    {
      return (0);
    }
  if (!*head)
    {
      return (1);
    }

  arr = head;
  aba = *head;
  nexn = traverse(arr, aba);

  return (nexn);
}

/**
 * traverse - Check for palindrome
 *
 * @arr: highest value
 * @aba: lowest value
 *
 * Return: 1 if True
 */

int traverse(listint_t **arr, listint_t *aba)
{
  int nexn, result = -1;

  if (aba == NULL)
    {
      return (1);
    }

  nexn = traverse(arr, aba->next);

  if (nexn == 0)
    {
      return (0);
    }
  if ((*arr)->n == aba->n)
    {
      result = 1;
    }
  else
    {
      result = 0;
    }

  *arr = (*arr)->next;

  return (result);
}
