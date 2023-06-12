
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
    if (!*head || !(*head)->next)
        return (*head);
    listint_t *prev = NULL, *next = NULL, *current = *head;
    while (current)
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
    if (!*head || !(*head)->next)
        return (1);
    int size = 0, i;
    listint_t *slow_ptr = NULL, *fast_ptr = NULL, *tmp_head = NULL, *tmp_tail = NULL, 
                *left_half_ptr = NULL, *right_half_ptr = NULL;

    slow_ptr=fast_ptr=*head;

    while(fast_ptr && fast_ptr->next){
        size++;
        slow_ptr=slow_ptr->next;
        fast_ptr=fast_ptr->next->next;
    }

    if (fast_ptr == NULL) {
        right_half_ptr=slow_ptr;
        left_half_ptr=reverse_listint(head);
    }
    else {
        right_half_ptr=slow_ptr->next;
        left_half_ptr=reverse_listint(&slow_ptr);
    }

    tmp_head=tmp_tail=left_half_ptr;

    for (i = 0; i < size && right_half_ptr; i++) {
        if (tmp_head->n != right_half_ptr->n) {
            reverse_listint(&left_half_ptr);
            return (0);
        }
        tmp_tail=tmp_head;
        tmp_head=tmp_head->next;
        right_half_ptr=right_half_ptr->next;
    }

    reverse_listint(&left_half_ptr);

    if (i == size && !right_half_ptr) {
        return (1);
    } else {
        return (0);
    }
}
