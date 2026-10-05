class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class BrowserHistory:
    def __init__(self,homepage):
        self.current=Node(homepage)

    def visit(self,url):
        newNode=Node(url)
        self.current.next=newNode
        newNode.prev=self.current
        self.current=newNode

    def back(self,steps):
        while steps>0 and self.current.prev:
            self.current=self.current.prev
            steps-=1
        return self.current.data

    def forward(self,steps):
        while steps>0 and self.current.next:
            self.current=self.current.next
            steps-=1
        return self.current.data