#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return (*head);

    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;

    return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return (1);

    int size = 0, i;

    listint_t *tmp;
    for (tmp = *head; tmp != NULL; tmp = tmp->next)
        size++;

    int midIndex = size / 2;

    for (i = 0; i < midIndex; i++)
        head = &(*head)->next;

    if ((size % 2) != 0) // odd number of nodes
        head = &(*head)->next;

    reverse_listint(head);

    listint_t *tmp2 = *head;

    for (i = 0; i < midIndex; i++)
        tmp2 = tmp2->next;

    while (tmp2 != NULL)
    {
        if ((*head)->n != tmp2->n)
            return (0);

        *head = (*head)->next;
        tmp2 = tmp2->next;
    }

    return (1);
}
