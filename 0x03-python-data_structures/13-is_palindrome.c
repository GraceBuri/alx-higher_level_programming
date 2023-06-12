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
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	return (*head = prev);
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
	listint_t *tmp, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = mid = rev = (*head);
	for (i = 0; i < size / 2; i++)
    {
        if (size % 2 == 1 && i == size / 2 - 1)
            mid = mid->next;

        rev = rev->next;
    }

    mid->next = reverse_listint(&rev);

    while(mid && rev) {
        if(mid->n != rev->n) {
            mid->next = reverse_listint(&rev);
            return 0;
        }

        mid = mid->next;
        rev = rev->next;
    }

    mid->next = reverse_listint(&rev);

    return 1;
}
