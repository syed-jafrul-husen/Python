from tkinter import *
from tkinter import messagebox
import random
import copy
import time

_goal_state = '123456780'
_init_state = '724560831'
_algo = {1:"DFS"
         }

class EightPuzzle(object):
    def __init__(self, input_state=None):
        if input_state:
            self.state = copy.deepcopy(input_state)
        else:       
            self.state = copy.deepcopy(_goal_state)
            self.shuffle()            
            
    def shuffle(self):
        pos0 = self.state.index('0')
        for i in range(100):
            choices = _neighbors[pos0]
            pos = choices[random.randint(0, len(choices)-1)]
            self.swap(pos)
            pos0 = self.state.index('0')

    def swap(self, pos):
        pos0 = self.state.index('0')
        l = list(self.state)
        l[pos0], l[pos] = l[pos], l[pos0]
        self.state = ''.join(l)

    def get_next(self, current):
        pos0 = current.index('0')
        nextStates = []

        for pos in _neighbors[pos0]:
            l = list(current)
            l[pos0], l[pos] = l[pos], l[pos0]
            step = ''.join(l)
            nextStates.append(step)
        return nextStates  

    def DFS(self):

        def explore(current, depth):
            nonlocal goal, solved, limit
            if current == goal:
                solved = True
                return
            if depth >= limit:
                return
            next_depth = depth+1
            for next_node in self.get_next(current):
                if not next_node in visited:
                    visited[next_node] = True
                    previous[next_node] = current
                    if not next_depth in level:
                        level[next_depth] = []
                    level[next_depth].append(next_node)
                    explore(next_node, next_depth)
                if solved:
                    break

        root = self.state
        goal = '123456780'
        previous = {root: None}
        visited = {root: True}
        level = {0:[root]}
        solved = (root == goal)
        limit = 0
        while not solved and limit in level:
            depth = limit
            limit += 1
            for node in level[depth]:
                explore(node, depth)

        if solved:
            return self.retrieve_path(goal, previous), len(visited)
        return None, len(visited)

    def retrieve_path(self, goal, previous):
        path = [goal]
        current = goal
        while previous[current]:
            path.insert(0, previous[current])
            current = previous[current]
        return path
puzzle = EightPuzzle(_init_state)

def display():
    color = 'black' if puzzle.state != _goal_state else 'cyan'
    for i in range(9):
        if puzzle.state[i] != '0':
            var[i].set(str(puzzle.state[i]))
            label[i].config(bg=color)
        else:
            var[i].set('')
            label[i].config(bg='cyan')

def solve():
    for b in button:
        b.configure(state='disabled')
    option.configure(state='disabled')
    
    run = {1: puzzle.DFS}

    temp = select.get()
    index = 1
    for k,e in _algo.items():
        if e == temp:
            index = k
            break
    
    stime = time.time()
    path, n = run[index]()
    ttime = time.time()

    if not path:    
        print('This 8-puzzle is unsolvable!')
        for i in range(9):
            label[i].config(bg='red' if puzzle.state[i] != '0' else 'white')
        for b in button:
            b.configure(state='normal')
        option.configure(state='normal')
        return

    display_procedure(path)    

def display_procedure(path):
    if not path:
        for b in button:
            b.configure(state='normal')
        option.configure(state='normal')
        return
    puzzle.state = path.pop(0)
    display()
    win.after(520, lambda: display_procedure(path)) 

def shuffle():
    puzzle.shuffle()
    display()

def move(event):
    text = event.widget.cget('text')
    if not text:
        return
    
    pos = puzzle.state.index(text)
    pos0 = puzzle.state.index('0')
    if _distance[pos0][pos] > 1:
        return

    puzzle.swap(pos)
    display()

win = Tk()
win.geometry('+300+90')
win.title('8-PUZZLE using DFS')
algoFrame = Frame(win, width=0, relief=RAISED)
algoFrame.pack()
select = StringVar(algoFrame)
option = OptionMenu(algoFrame, select, _algo[1])
board = Frame(win, width=415, height=420, relief=RAISED,bg='light green')
board.pack()
var = [StringVar() for i in range(9)]
label = [Label(board, textvariable=var[i], bg='gray',fg='blue', font=('bold', 90)) for i in range(9)]
for i in range(3):
    for j in range(3):
        label[i*3+j].bind("<Button-1>", lambda event: move(event))
        label[i*3+j].place(x=135*j+5,y=140*i+5, width=130, height=130)
        
buttonFrame = Frame(win, relief=RAISED, borderwidth=1,bg='light blue')
buttonFrame.pack(fill=X, expand=True)
button = []
button.append(Button(buttonFrame, width='15',height='2',font='bold',bg='grey', relief=RAISED, text="Run", command=solve)) # to be initialized
for b in button:
    b.pack(side=TOP, padx=1, pady=1)

_neighbors = {0: [1,3],
              1: [0,2,4],
              2: [1,5],
              3: [0,4,6],
              4: [1,3,5,7],
              5: [2,4,8],
              6: [3,7],
              7: [4,6,8],
              8: [5,7]}

_distance = [[0,1,2,1,2,3,2,3,4],
             [1,0,1,2,1,2,3,2,3],
             [2,1,0,3,2,1,4,3,2],
             [1,2,3,0,1,2,1,2,3],
             [2,1,2,1,0,1,2,1,2],
             [3,2,1,2,1,0,3,2,1],
             [2,3,4,1,2,3,0,1,2],
             [3,2,3,2,1,2,1,0,1],
             [4,3,2,3,2,1,2,1,0]]

if __name__ == "__main__":
    display()
    win.mainloop()
