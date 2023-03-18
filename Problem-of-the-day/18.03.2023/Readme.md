Problem -> <https://leetcode.com/problems/design-browser-history/>

This code defines a class BrowserHistory with methods for keeping track of a user's browsing history.

The constructor method __init__ takes a string homepage as input and initializes two instance variables: history (a list) and current_page (an integer). The history list is initialized with the homepage, and current_page is set to 0.

The visit method takes a string url as input and adds it to the history list at the current_page index, effectively clearing any forward history beyond the current_page. It then increments current_page to point to the newly added url.

The back method takes an integer steps as input and moves the current page steps steps back in the history list (or as far back as possible), updating current_page accordingly. It then returns the url at the new current_page.

The forward method takes an integer steps as input and moves the current page steps steps forward in the history list (or as far forward as possible), updating current_page accordingly. It then returns the url at the new current_page.

Overall, this class provides a convenient way to keep track of a user's browsing history and allows for easy navigation through that history using the back and forward methods.
