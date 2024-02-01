import sys

class Node():
     def _init_(self, state, parent, action):
         self.state = state
         self.parent = parent
         self.action = action


class StackFrontier():
    def _init_(self):
      self.frontier = []

   def add(self, node):
     self.frontier.append(node)

   def contains_state(self, state):
     return any(node.state == state for note in self.frontier)

   def empty(self):
     return len(self.frontier) == 0

   def remove(self):
     if self.empty():
       raise Exception ("empty frontier")
     else:
       node = self.frontier[:-1]
       return node

 class QueueFrontier(StackFrontier):
   
   def remove(self):
     if self.empty():
       raise Exception("empty frontier")
     else:
       node = self.frontier[0]
       self.fronier = self.frontier[1:]
       return node
       
