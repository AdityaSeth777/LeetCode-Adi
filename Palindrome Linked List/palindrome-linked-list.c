/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


bool isPalindrome(struct ListNode* head){
    if(head==NULL){
        return true;
    }
    struct ListNode* p1=head;
    struct ListNode* p2=head->next;
    while(p2 && p2->next){
        p1 = p1->next;
        p2 = p2->next->next;
    }
    
    struct ListNode *prev, *curr, *n, *h2;
    prev = NULL;
    curr = p1->next;
    h2 = curr;
    while(curr){
        n = curr->next;
        curr->next = prev;
        prev = curr;
        curr = n;
    }
    p2 = head;
    p1 = prev;
    while(p1){
        if(p1->val!=p2->val){
            return false;
        }
        p1 = p1->next;
        p2 = p2->next;
    }
    
    return true;

}