class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_page = 0

    def visit(self, url: str) -> None:
        # clear forward history and add new url to history
        self.history = self.history[:self.current_page + 1] + [url]
        self.current_page += 1

    def back(self, steps: int) -> str:
        # move back in history by steps (or maximum possible) and return current url
        self.current_page = max(0, self.current_page - steps)
        return self.history[self.current_page]

    def forward(self, steps: int) -> str:
        # move forward in history by steps (or maximum possible) and return current url
        self.current_page = min(len(self.history) - 1,
                                self.current_page + steps)
        return self.history[self.current_page]
