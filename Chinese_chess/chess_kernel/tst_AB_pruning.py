#encoding:utf8
#AlphaBeta剪枝算法，针对Minimax方法优化
import re
import random
from .chess_config import think_depth, killing_rewards
from .pieces_moves import pieces_moves, moves_to_map

class Choose_best_for_machine:
    def __init__(self, current_map, machine_camp = 'b'):
        self.think_depth = think_depth # 思考深度，即递归深度
        self.current_map = current_map  # 当前棋谱
        self.own_camp = machine_camp  # 机器方阵营
        self.alpha_beta = [[-float('inf'), float('inf')] for e in range(self.think_depth)] #alpha下界；beta上界。用来记录分数
        self.next_position = [[] for e in range(self.think_depth)]
        self.choose_best_moves(self.think_depth, self.current_map, self.own_camp)
        self.best_moves = self.next_position[0]

    def choose_best_moves(self, think_depth, current_map, own_camp):
        think_depth -= 1
        enemy_camp = 'r'
        if own_camp == 'r':
            enemy_camp = 'b'

        # 下面开始遍历机器阵营的走步
        for map_row_num, map_row in enumerate(current_map):
            for map_col_num, piece_name in enumerate(map_row):
                if re.match(own_camp, piece_name):
                    current_position = (map_row_num, map_col_num)  # 棋子原位置
                    next_position_info_list = pieces_moves(current_map, (map_row_num, map_col_num))  # 该棋子下一步的位置列表
                    for first_flag, next_position_info in enumerate(next_position_info_list):
                        # next_position_info = [(下一步位置)，吃掉的棋子，奖励值]
                        next_position = next_position_info[0]
                        killed_piece_name = next_position_info[1]
                        kill_rewards = next_position_info[2]

                        if think_depth > 0:
                            latest_map = moves_to_map(current_map, current_position, next_position)
                            self.choose_best_moves(think_depth, latest_map, enemy_camp)
                        if own_camp == self.machine_camp:
                            #如果是机器方阵营，那我们就选出分数最小值
                            if kill_rewards < self.alpha_beta[think_depth][1]:
                                # 选出最小值赋值给beta
                                self.alpha_beta[think_depth][1] = kill_rewards
                                self.next_position[think_depth] = [current_position, next_position]
                            else:
                                if first_flag == 0:
                                    continue
                                else:
                                    break
                        else:
                            #如果是人类方阵营，那我们就选出分数最大值
                            if kill_rewards >self.alpha_beta[think_depth][0]:
                                # 选出最小值赋值给alpha
                                self.alpha_beta[think_depth][0] = kill_rewards
                                self.next_position[think_depth] = [current_position, next_position]
                            else:
                                if first_flag == 0:
                                    continue
                                else:
                                    break
                        pass
                    pass
                else:
                    continue
