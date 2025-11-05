#pyinstaller --onefile --noconsole --add-data "img;img" 2048Game.py
import pygame
import random
import sys
import os
from time import sleep
from copy import deepcopy
from math import sqrt, log2
from time import time
import pyautogui

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('2048')
        self.screen = pygame.display.set_mode((400, 400))
        self.screen.fill((209, 212, 158))
        self.grid = [[0 for _ in range(4)] for _ in range(4)]
        self.run = True
        self.score = 0
        self.evaluation = True
        self.load_image()
        self.game_run()
        
    def get_resources_path(self, relative_path):
         base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
         return os.path.join(base_path, relative_path)
     
    def win(self):
        self.screen.fill((209, 212, 158))
        img_path = self.get_resources_path('./img/win.png')
        win = pygame.image.load(img_path)
        win = pygame.transform.scale(win, (400, 70))
        self.screen.blit(win, (0, 150))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            
    def lose(self):
            self.screen.fill((209, 212, 158))
            img_path = self.get_resources_path('./img/lose.png')
            lose = pygame.image.load(img_path)
            lose = pygame.transform.scale(lose, (400, 70))
            self.screen.blit(lose, (0, 150))
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.display.update()
                
    def is_win(self):
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 2048:
                    sleep(2)
                    return True
        return False
    def is_lose(self):
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 0:
                    return False
                if i > 0 and self.grid[i][j] == self.grid[i-1][j]:
                    return False
                if j > 0 and self.grid[i][j] == self.grid[i][j-1]:
                    return False
        sleep(2)
        return True
    def load_image(self):
        img_path = self.get_resources_path('./img/unit.png')
        unit = pygame.image.load(img_path)
        unit = pygame.transform.scale(unit, (70, 70))
        for i in range(4):
            for j in range(4):
                self.screen.blit(unit, (i*75+50, j*75+40))
                
    def load_square(self, num, x, y):
        img_path = self.get_resources_path('./img/2.png')
        square = pygame.image.load(img_path)
        if num == 2:
            img_path = self.get_resources_path('./img/2.png')
            square = pygame.image.load(img_path)
        elif num == 4:
            img_path = self.get_resources_path('./img/4.png')
            square = pygame.image.load(img_path)
        elif num == 8:
            img_path = self.get_resources_path('./img/8.png')
            square = pygame.image.load(img_path)
        elif num == 16:
            img_path = self.get_resources_path('./img/16.png')
            square = pygame.image.load(img_path)
        elif num == 32:
            img_path = self.get_resources_path('./img/32.png')
            square = pygame.image.load(img_path)
        elif num == 64:
            img_path = self.get_resources_path('./img/64.png')
            square = pygame.image.load(img_path)
        elif num == 128:
            img_path = self.get_resources_path('./img/128.png')
            square = pygame.image.load(img_path)
        elif num == 256:
            img_path = self.get_resources_path('./img/256.png')
            square = pygame.image.load(img_path)
        elif num == 512:
            img_path = self.get_resources_path('./img/512.png')
            square = pygame.image.load(img_path)
        elif num == 1024:
            img_path = self.get_resources_path('./img/1024.png')
            square = pygame.image.load(img_path)
        elif num == 2048:
            img_path = self.get_resources_path('./img/2048.png')
            square = pygame.image.load(img_path)
        square = pygame.transform.scale(square, (69, 69))
        self.screen.blit(square, (x*75+50, y*75+40))
        pygame.display.update()
        
    def left_event(self):
        is_move = False
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] != 0:
                    row, col = i, j
                    while col > 0:
                        
                        if self.grid[row][col-1] == 0:
                            self.grid[row][col-1] = self.grid[row][col]
                            self.grid[row][col] = 0
                            col -= 1
                            is_move = True
                        elif self.grid[row][col-1] == self.grid[row][col]: # 合并
                            self.grid[row][col-1] = 2*self.grid[row][col]
                            self.grid[row][col] = 0
                            col -= 1
                            is_move = True
                        else:
                            break
        return is_move
    
    def right_event(self):
        is_move = False
        for i in range(4):
            for j in range(3, -1, -1):
                if self.grid[i][j] != 0:
                    row, col = i, j
                    while col < 3:
                        if self.grid[row][col+1] == 0:
                            self.grid[row][col+1] = self.grid[row][col]
                            self.grid[row][col] = 0
                            col += 1
                            is_move = True
                        elif self.grid[row][col+1] == self.grid[row][col]: # 合并
                            self.grid[row][col+1] = 2*self.grid[row][col]
                            self.grid[row][col] = 0
                            col += 1
                            is_move = True
                        else:
                            break
        return is_move
    
    def up_event(self):
        is_move = False
        for i in range(4):
            for j in range(4):
                if self.grid[i][j]!= 0:
                    row, col = i, j
                    while row > 0:
                        if self.grid[row-1][col] == 0:
                            self.grid[row-1][col] = self.grid[row][col]
                            self.grid[row][col] = 0
                            row -= 1
                            is_move = True
                        elif self.grid[row-1][col] == self.grid[row][col]: # 合并
                            self.grid[row-1][col] = 2*self.grid[row][col]
                            self.grid[row][col] = 0
                            row -= 1
                            is_move = True
                        else:
                            break
        return is_move
    
    def down_event(self):
        is_move = False
        for i in range(3, -1, -1):
            for j in range(4):
                if self.grid[i][j] != 0:
                    row, col = i, j
                    while row < 3:
                        if self.grid[row+1][col] == 0:
                            self.grid[row+1][col] = self.grid[row][col]
                            self.grid[row][col] = 0
                            row += 1
                            is_move = True
                        elif self.grid[row+1][col] == self.grid[row][col]: # 合并
                            self.grid[row+1][col] = 2*self.grid[row][col]
                            self.grid[row][col] = 0
                            row += 1
                            is_move = True
                        else:
                            break
        return is_move
    
    def refresh_screen(self):
        self.screen.fill((209, 212, 158))
        self.load_image()
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] != 0:
                    self.load_square(self.grid[i][j], j, i)
        x, y = random.randint(0,3), random.randint(0,3)
        is_full = False
        turns = 0
        while self.grid[x][y] != 0:
            x, y = random.randint(0,3), random.randint(0,3) 
            turns+=1
            if turns > 100:
                is_full = True
                break
        if not is_full:
            number = 2 if random.randint(0,1) == 0 else 4 
            self.load_square(number , y, x)
            self.grid[x][y] = number
    
    def game_run(self):
        x, y = random.randint(0,3), random.randint(0,3)
        self.load_square(2, x, y)
        self.grid[y][x] = 2
        x, y = random.randint(0,3), random.randint(0,3)
        while self.grid[x][y] != 0:
            x, y = random.randint(0,3), random.randint(0,3)
        number = 2 if random.randint(0,1) == 0 else 4
        self.load_square(number , x, y)
        self.grid[y][x] = number
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.left_event():
                            self.refresh_screen()
                    if event.key == pygame.K_RIGHT:
                        if self.right_event():
                            self.refresh_screen()
                    if event.key == pygame.K_UP:
                        if self.up_event():
                            self.refresh_screen()
                    if event.key == pygame.K_DOWN:
                        if self.down_event():
                            self.refresh_screen()
                    if event.key == pygame.K_SPACE:
                        self.AI_play()
            if self.is_win():
                print("You Win!")
                self.win()
            if self.is_lose():
                print("You Lose!")
                self.lose()
            if self.evaluation:
                self.AI_play()
            pygame.time.Clock().tick(60)             
            pygame.display.flip()
        pygame.quit()
        
    def render(self):
        return self.grid

    def AI_play(self):
        ai = AI(self)
        grid = deepcopy(self.grid)
        move = None
        start = time()
        depth = 5
        while True:
            now = time()
            if now - start > 5:
                break
            move, _ = ai.minimax(depth, grid, start)
            depth+=1
            if depth>=8:
                break
        print((move, depth))
        if move == 0:
            self.left_event()
        elif move == 1:
            self.right_event()
        elif move == 2:
            self.up_event()
        elif move == 3:
            self.down_event()
            
        self.refresh_screen()
        
class AI:
    def __init__(self, game):
        self.game = game
        self.transposition_table = {}
        
    def hash_board(self, board):
        return str(board)
    
    def value_evaluate(self, grid):
        total_score = 0
        density_score = 0
        most_score = [0 for _ in range(12)]
        for k in range(12):
            for i in range(4):
                for j in range(4):
                    if grid[i][j] == 2**k:
                        most_score[k] += 1
        count = 11
        sorted_score = 0
        while most_score[count]==0:
            count -= 1
        number = 4           
        while count>=0 and number>0:
            sorted_score += most_score[count]**3
            count -= 1
            number -= 1
        
        for i in range(4):
            for j in range(4):
                if grid[i][j] != 0:
                    density_score += 1
                total_score += grid[i][j]
        if 15<=density_score<=16:
            density_score = (10*total_score) / density_score**2.1
        else:    
            density_score = (10*total_score) / density_score**2
        
        
        combine_score = 0
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if j+k<4 and grid[i][j] == grid[i][j+k]:
                        combine_score += 2*(grid[i][j]**2.5)
                        break
                    if i+k<4 and grid[i][j] == grid[i+k][j]:
                        combine_score += 2*(grid[i][j]**2.5)
                        break
        
       
        is_win = False
        is_lose = True
        for i in range(4):
            for j in range(4):
                if grid[i][j] == 2048:
                    is_win = True
        for i in range(4):
            for j in range(4):
                if grid[i][j] == 0:
                    is_lose = False
                if i > 0 and grid[i][j] == grid[i-1][j]:
                    is_lose = False
                if j > 0 and grid[i][j] == grid[i][j-1]:
                    is_lose = False
                
        if is_win:
            return float('inf')
        if is_lose:
            return float('-inf')
        
        return density_score +  sorted_score  + combine_score
    
    def left_event(self, grid):
        is_move = False
        for i in range(4):
            for j in range(4):
                if grid[i][j] != 0:
                    row, col = i, j
                    while col > 0:
                        if grid[row][col-1] == 0:
                            grid[row][col-1] = grid[row][col]
                            grid[row][col] = 0
                            col -= 1
                            is_move = True
                        elif grid[row][col-1] == grid[row][col]: # 合并
                            grid[row][col-1] = 2*grid[row][col]
                            grid[row][col] = 0
                            col -= 1
                            is_move = True
                        else:
                            break
        return is_move, grid
    
    def right_event(self, grid):
        is_move = False
        for i in range(4):
            for j in range(3, -1, -1):
                if grid[i][j] != 0:
                    row, col = i, j
                    while col < 3:
                        if grid[row][col+1] == 0:
                            grid[row][col+1] = grid[row][col]
                            grid[row][col] = 0
                            col += 1
                            is_move = True
                        elif grid[row][col+1] == grid[row][col]: # 合并
                            grid[row][col+1] = 2*grid[row][col]
                            grid[row][col] = 0
                            col += 1
                            is_move = True
                        else:
                            break
        return is_move, grid
    
    def up_event(self, grid):
        is_move = False
        for i in range(4):
            for j in range(4):
                if grid[i][j]!= 0:
                    row, col = i, j
                    while row > 0:
                        if grid[row-1][col] == 0:
                            grid[row-1][col] = grid[row][col]
                            grid[row][col] = 0
                            row -= 1
                            is_move = True
                        elif grid[row-1][col] == grid[row][col]: # 合并
                            grid[row-1][col] = 2*grid[row][col]
                            grid[row][col] = 0
                            row -= 1
                            is_move = True
                        else:
                            break
        return is_move, grid
    
    def down_event(self, grid):
        is_move = False
        for i in range(3, -1, -1):
            for j in range(4):
                if grid[i][j] != 0:
                    row, col = i, j
                    while row < 3:
                        if grid[row+1][col] == 0:
                            grid[row+1][col] = grid[row][col]
                            grid[row][col] = 0
                            row += 1
                            is_move = True
                        elif grid[row+1][col] == grid[row][col]: # 合并
                            grid[row+1][col] = 2*grid[row][col]
                            grid[row][col] = 0
                            row += 1
                            is_move = True
                        else:
                            break
        return is_move, grid
        
                    
    def minimax(self, depth, grid, start_time, is_player=True, alpha=float('-inf'), beta=float('inf')):
        move, score = None, None
        board_hash = self.hash_board(grid)
        if board_hash in self.transposition_table:
            return self.transposition_table[board_hash]
        if depth == 0 or self.game.is_win() or self.game.is_lose() or time() - start_time > 5:
            return move, self.value_evaluate(grid)
        if is_player:

            score = float('-inf')

            tempGame = [deepcopy(grid) for _ in range(4)]

            eval = float('-inf')
            move_ordered = []
            pro_grid = [0 for _ in range(4)]
            is_move = [False for _ in range(4)]
            is_move[0], pro_grid[0] = self.left_event(tempGame[0])
            is_move[1], pro_grid[1] = self.right_event(tempGame[1])
            is_move[2], pro_grid[2] = self.up_event(tempGame[2])
            is_move[3], pro_grid[3] = self.down_event(tempGame[3])
            for i in range(4):
                if is_move[i]:
                    move_ordered.append([i, self.value_evaluate(pro_grid[i])])
            move_ordered.sort(key=lambda x: x[1], reverse=True)

            for item in move_ordered:
                eval = self.minimax(depth-1, pro_grid[item[0]], start_time, False, alpha, beta)[1] 
                if eval > score:
                    score = eval
                    move = item[0]
                alpha = max(alpha, score)
                if alpha >= beta:
                    break
            if move == None:
                #print("it is None in max")
                tgrid = [deepcopy(grid) for _ in range(4)]
                is_move = [False for _ in range(4)]
                is_move[0], tgrid[0] = self.left_event(tgrid[0])
                is_move[1], tgrid[1] = self.right_event(tgrid[1])
                is_move[2], tgrid[2] = self.up_event(tgrid[2])
                is_move[3], tgrid[3] = self.down_event(tgrid[3])
                move_ordered = []
                for i in range(4):
                    if is_move[i]:
                        move_ordered.append([i, self.value_evaluate(tgrid[i])])
                move_ordered.sort(key=lambda x: x[1], reverse=True)
                if len(move_ordered) > 0:
                    move = move_ordered[0][0]
                    score = move_ordered[0][1] if score == float('-inf') else score
            self.transposition_table[board_hash] = (move, score)
            return move, score
        else:
            score = float('inf')
            for i in range(4):
                for j in range(4):
                    if grid[i][j] == 0:
                        grid[i][j] = 2
                        move, eval = self.minimax(depth-1, deepcopy(grid), start_time, True, alpha, beta)
                        if eval < score:
                            score = eval
                        grid[i][j] = 4
                        move, eval = self.minimax(depth-1, deepcopy(grid), start_time, True, alpha, beta)
                        if eval < score:
                            score = eval
                        grid[i][j] = 0
                    beta = min(beta, score)
                    if alpha >= beta:
                        #print('pruning')
                        if move == None:
                            #print("it is None")
                            tgrid = [deepcopy(grid) for _ in range(4)]
                            is_move = [False for _ in range(4)]
                            is_move[0], tgrid[0] = self.left_event(tgrid[0])
                            is_move[1], tgrid[1] = self.right_event(tgrid[1])
                            is_move[2], tgrid[2] = self.up_event(tgrid[2])
                            is_move[3], tgrid[3] = self.down_event(tgrid[3])
                            move_ordered = []
                            for i in range(4):
                                if is_move[i]:
                                    move_ordered.append((i, self.value_evaluate(tgrid[i])))
                            #print(move_ordered)
                            move_ordered.sort(key=lambda x: x[1], reverse=True)
                            move = move_ordered[0][0]
                            score = move_ordered[0][1] if score==float('inf') else score 
                        self.transposition_table[board_hash] = (move, score)
                        return move, score
            if move == None:
                #print("it is None")
                tgrid = [deepcopy(grid) for _ in range(4)]
                is_move = [False for _ in range(4)]
                is_move[0], tgrid[0] = self.left_event(grid[0])
                is_move[1], tgrid[1] = self.right_event(grid[1])
                is_move[2], tgrid[2] = self.up_event(grid[2])
                is_move[3], tgrid[3] = self.down_event(grid[3])
                move_ordered = []
                for i in range(4):
                    if is_move[i]:
                        move_ordered.append((i, self.value_evaluate(tgrid[i])))
                #print(move_ordered)
                move_ordered.sort(key=lambda x: x[1], reverse=True)
                move = move_ordered[0][0]
                score = move_ordered[0][1] if score==float('inf') else score
            self.transposition_table[board_hash] = (move, score)
            return move, score
        
if __name__ == '__main__':
    game = Game()