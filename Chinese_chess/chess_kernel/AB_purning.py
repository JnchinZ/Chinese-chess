#encoding:utf8
#AlphaBeta剪枝算法，针对Minimax方法优化
import re
import random
from .chess_config import think_deep, killing_rewards
from .pieces_moves import pieces_moves, moves_to_map

class Choose_best:
    def __init__(self, map, machine_camp = 'b'):
        self.think_deep = think_deep # 思考深度，即递归深度
        self.latest_map = map  # 当前棋谱
        self.machine_camp = machine_camp  # 机器方阵营
        self.best_p_position, self.best_n_position, self.best_score = self.choose_best_moves(self.think_deep, self.latest_map, self.machine_camp)
        pass

    '''
    遍历出一方的棋子信息：{(棋子原位置):[(下一步位置),吃掉的棋子,分数,array[棋谱]] ...}
    '''

    def traversal_moves(self, map, own_camp):
        '''
        :param map: 当前棋谱,是一个数组
        :param own_camp: 己方阵营('r' or 'b')
        :return: [[(棋子原位置), (下一步位置), 吃掉的棋子, 分数], ...]
        '''
        moves_info_list = [] #返回值:[[(棋子原位置), (下一步位置), 吃掉的棋子, 分数], ...]

        # 开始遍历，遍历出每个我方棋子的走法
        for map_row_num in range(10):
            for map_col_num in range(9):
                piece_name = map[map_row_num][map_col_num]
                if re.match(own_camp, piece_name):
                    moves_position = (map_row_num, map_col_num)   #棋子原位置
                    next_positions = pieces_moves(map, (map_row_num, map_col_num))    #该棋子下一步的位置列表
                    for next_position in next_positions:
                        moves_info = []
                        moves_info.append(moves_position)
                        moves_info.extend(next_position)
                        moves_info_list.append(moves_info)
                    pass
                else:
                    continue
        return moves_info_list          # 返回[[(棋子原位置), (下一步位置), 吃掉的棋子, 分数], ...]

    def choose_best_moves(self, think_deep, map, own_camp):
        think_deep -= 1
        # 下面开始选出对我方最有利的棋谱和分数
        moves_info_list = self.traversal_moves(map, own_camp)
        best_p_position_ = ()
        best_n_position_ = ()
        best_score_ = -killing_rewards['jiang']*2
        counts = 0
        for moves_info in moves_info_list:
            p_position_ = moves_info[0] #这一步的棋子原位置
            n_position_ = moves_info[1]  #这一步的下一步位置
            score_ = moves_info[3]  # 这一步的分数
            # print(p_position_,end=', ')
            # print(n_position_,end=':')
            # print(score_)
            latest_map_ = moves_to_map(map, p_position_, n_position_)  # 这一步的棋谱

            if score_ > 1000:
                think_deep = 0

            if think_deep > 0:
                if own_camp == 'r':
                    enemy_camp = 'b'
                else:
                    enemy_camp = 'r'
                #选出对敌方最有利的棋谱和分数
                best_p_position_e, best_n_position_e, best_score_e = self.choose_best_moves(think_deep, latest_map_, enemy_camp)
                score_ -= best_score_e

            if best_score_ < score_:
                best_p_position_ = p_position_
                best_n_position_ = n_position_
                best_score_ = score_
            else:
                counts += 1

            # if own_camp == 'b':
            #     print(best_score_, end='----own\n')
            # elif own_camp == 'r':
            #     print(best_score_, end='--enemy\n')
        if counts == len(moves_info_list):
            num = random.randint(0, len(moves_info_list)-1)
            best_p_position_ = moves_info_list[num][0]
            best_n_position_ = moves_info_list[num][1]
            best_score_ = 0
        return best_p_position_, best_n_position_, best_score_
