#encoding:utf8
import re
from .chess_config import killing_rewards

'''
吃掉对方棋子所对应的奖励值
'''
def reward_scores(piece_name):
    if re.search('ju', piece_name):
        return killing_rewards['ju']
    if re.search('ma', piece_name):
        return killing_rewards['ma']
    if re.search('xiang', piece_name):
        return killing_rewards['xiang']
    if re.search('shi', piece_name):
        return killing_rewards['shi']
    if re.search('jiang',piece_name) or re.search('shuai', piece_name):
        return killing_rewards['jiang']
    if re.search('pao', piece_name):
        return killing_rewards['pao']
    if re.search('zu', piece_name) or re.search('bing', piece_name):
        return killing_rewards['zu']

def pieces_moves(current_map, piece_current_position):
    '''
    计算 每种棋子的[(下一步位置)，吃掉的棋子，奖励值],二维列表
    :param current_map: 当前的棋谱，即棋子摆放位置
    :param piece_current_position: 棋子的(当前位置)
    :return: [[(下一步位置)，吃掉的棋子，奖励值], ...]
    '''
    piece_name = current_map[piece_current_position[0]][piece_current_position[1]] # 棋子名
    next_position_info_list = []  # 要返回的二维列表

    def move_result(next_position, own_type):
        '''
        计算如果该棋子移动到下一步位置所产生的后果
        :param next_position: 下一步的(位置)
        :param own_type: 我方派别，红方或者黑方
        :return: [(下一步位置)，吃掉的棋子，奖励值], 移动类型
        '''
        next_position_piece_name = current_map[next_position[0]][next_position[1]]  #下一步位置上的棋子名
        if next_position_piece_name == '':
            next_position_info = [next_position]
            next_position_info.append('')
            next_position_info.append(0)
            return next_position_info, 1
        elif re.match(own_type, next_position_piece_name):
            return None, 2
        else:
            next_position_info = [next_position]
            next_position_info.append(next_position_piece_name)
            next_position_info.append(reward_scores(next_position_piece_name))
            return next_position_info, 3

    '''
    下面计算“车”的下一步合法位置
    '''
    if re.search('ju', piece_name):
        # 判断敌我方
        own_type = 'b'
        if re.match('r', piece_name):
            own_type = 'r'

        driections = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for driection in driections:
            for i in range(10):
                next_position = (piece_current_position[0]+(i+1)*driection[0], piece_current_position[1]+(i+1)*driection[1])
                if next_position[0] <= 9 and next_position[0] >= 0 and next_position[1] <= 8 and \
                                next_position[1] >= 0:
                    next_position_info, move_type = move_result(next_position, own_type)
                    if move_type == 1:
                        next_position_info_list.append(next_position_info)
                        continue
                    elif move_type == 2:
                        break
                    elif move_type == 3:
                        next_position_info_list.append(next_position_info)
                        break
        return next_position_info_list

    '''
    计算马的下一步合法位置
    '''
    if re.search('ma', piece_name):
        own_type = 'b'
        if re.match('r', piece_name):
            own_type = 'r'

        driections = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for driection in driections:
            next_position_1 = (piece_current_position[0]+driection[0], piece_current_position[1]+driection[1])
            if next_position_1[0] <= 9 and next_position_1[0] >= 0 and next_position_1[1] <= 8 and \
                                next_position_1[1] >= 0:
                next_position_info_1, move_type_1 = move_result(next_position_1, own_type)
                if move_type_1 == 1:
                    next_position_2 = (piece_current_position[0]+driection[0]*2, piece_current_position[1]+driection[1]*2)
                    if next_position_2[0] <= 9 and next_position_2[0] >= 0 and next_position_2[1] <= 8 and \
                                    next_position_2[1] >= 0:
                        sub_driections = [-1,1]
                        if driection[0] == 0:
                            for sub_driection in sub_driections:
                                next_position_3 = (next_position_2[0]+sub_driection, next_position_2[1])
                                if next_position_3[0] <= 9 and next_position_3[0] >= 0 and next_position_3[1] <= 8 and \
                                                next_position_3[1] >= 0:
                                    next_position_info_2, move_type_2 = move_result(next_position_3, own_type)
                                    if move_type_2 == 1:
                                        next_position_info_list.append(next_position_info_2)
                                    elif move_type_2 == 2:
                                        break
                                    elif move_type_2 == 3:
                                        next_position_info_list.append(next_position_info_2)
                        else:
                            for sub_driection in sub_driections:
                                next_position_3 = (next_position_2[0], next_position_2[1]+sub_driection)
                                if next_position_3[0] <= 9 and next_position_3[0] >= 0 and next_position_3[1] <= 8 and \
                                                next_position_3[1] >= 0:
                                    next_position_info_2, move_type_2 = move_result(next_position_3, own_type)
                                    if move_type_2 == 1:
                                        next_position_info_list.append(next_position_info_2)
                                    elif move_type_2 == 2:
                                        break
                                    elif move_type_2 == 3:
                                        next_position_info_list.append(next_position_info_2)
        return next_position_info_list
    '''
    计算相的下一步合法位置
    '''
    if re.search('xiang', piece_name):
        own_type = 'b'
        if re.match('r', piece_name):
            own_type = 'r'

        driections = [(1,1), (1,-1), (-1,1), (-1,-1)]

        for driection in driections:
            next_position_1 = (piece_current_position[0]+driection[0], piece_current_position[1]+driection[1])
            if next_position_1[0] <= 9 and next_position_1[0] >= 0 and next_position_1[1] <= 8 and \
                            next_position_1[1] >= 0:

                next_position_info_1, move_type_1 = move_result(next_position_1, own_type)
                if move_type_1 == 1:
                    next_position_2 = (piece_current_position[0]+driection[0]*2, piece_current_position[1]+driection[1]*2)
                    if next_position_2[0] <= 9 and next_position_2[0] >= 0 and next_position_2[1] <= 8 and \
                                    next_position_2[1] >= 0:
                        next_position_info_2, move_type_2 = move_result(next_position_2, own_type)
                        if move_type_2 == 1:
                            next_position_info_list.append(next_position_info_2)
                        elif move_type_2 == 2:
                            break
                        elif move_type_2 == 3:
                            next_position_info_list.append(next_position_info_2)
        return next_position_info_list

    '''
    计算士的下一步合法位置
    '''
    if re.search('shi', piece_name):
        own_type = 'b'
        if re.match('r', piece_name):
            own_type = 'r'

        driections = [(1,1), (1,-1), (-1,1), (-1,-1)]
        for driection in driections:
            next_position = (piece_current_position[0]+driection[0], piece_current_position[1]+driection[1])
            if ((next_position[0] <= 2 and next_position[0] >= 0)or(next_position[0] <= 9 and next_position[0] >= 7))\
                    and next_position[1] <= 5 and next_position[1] >= 3:
                next_position_info, move_type = move_result(next_position, own_type)
                if move_type == 1:
                    next_position_info_list.append(next_position_info)
                elif move_type == 2:
                    break
                elif move_type == 3:
                    next_position_info_list.append(next_position_info)
        return next_position_info_list

    '''
    计算将帅的下一步合法位置
    '''
    if re.search('jiang', piece_name) or re.search('shuai', piece_name):
        own_type = 'b'
        if re.match('r', piece_name):
            own_type = 'r'

        driections = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if piece_current_position[0]<=2 and piece_current_position[0]>=0:
            test_duijiang_driection = (1, 0)
        else:
            test_duijiang_driection = (-1, 0)
        test_duijiang_counter = 0
        for i in range(10)[1:]:
            test_duijiang_position = (piece_current_position[0]+i*test_duijiang_driection[0], piece_current_position[1])
            if test_duijiang_position[0] <= 9 and test_duijiang_position[0] >= 0:
                if test_duijiang_position != '':
                    test_duijiang_counter = 1
                    break
            else:
                continue

        for driection in driections:
            next_position = (piece_current_position[0]+driection[0], piece_current_position[1]+driection[1])
            if ((next_position[0] <= 2 and next_position[0] >= 0)or(next_position[0] <= 9 and next_position[0] >= 7))\
                    and next_position[1] <= 5 and next_position[1] >= 3 and test_duijiang_counter == 1:
                next_position_info, move_type = move_result(next_position, own_type)
                if move_type == 1:
                    next_position_info_list.append(next_position_info)
                elif move_type == 2:
                    break
                elif move_type == 3:
                    next_position_info_list.append(next_position_info)
        return next_position_info_list

    '''
    计算炮的下一步合法位置
    '''
    if re.search('pao', piece_name):
        own_type = 'b'
        if re.match('r', piece_name):
            own_type = 'r'

        driections = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for driection in driections:
            flag_piece_counter = 0
            for i in range(10):
                next_position = (piece_current_position[0]+(i+1)*driection[0], piece_current_position[1]+(i+1)*driection[1])
                if next_position[0] <= 9 and next_position[0] >= 0 and next_position[1] <= 8 and \
                                next_position[1] >= 0:
                    next_position_info, move_type = move_result(next_position, own_type)
                    if move_type == 1:
                        if flag_piece_counter < 1:
                            next_position_info_list.append(next_position_info)
                            continue
                        else:
                            continue
                    else:
                        flag_piece_counter += 1
                        if flag_piece_counter == 1:
                            continue
                        if move_type == 3:
                            next_position_info_list.append(next_position_info)
                            break
                        if move_type == 2:
                            break

        return next_position_info_list

    '''
    计算卒的下一步合法位置
    '''
    if re.search('zu', piece_name) or re.search('bing', piece_name):
        own_type = 'b'
        if re.match('r', piece_name):
            own_type = 'r'

        if re.search('zu', piece_name):
            driections = [(1, 0), (0, -1), (0, 1)]
            if piece_current_position[0] < 5:
                river_crossing = False
            else:
                river_crossing = True
        elif re.search('bing', piece_name):
            driections = [(-1, 0), (0, -1), (0, 1)]
            if piece_current_position[0] > 4:
                river_crossing = False
            else:
                river_crossing = True
        moves_counter = 0
        for driection in driections:
            if river_crossing == False:
                moves_counter = 1
            next_position = (piece_current_position[0]+driection[0], piece_current_position[1]+driection[1])
            if next_position[0] <= 9 and next_position[0] >= 0 and next_position[1] <= 8 and \
                            next_position[1] >= 0:
                next_position_info, move_type = move_result(next_position, own_type)
                if move_type == 2:
                    if moves_counter == 1:
                        break
                    else:
                        continue
                else:
                    next_position_info_list.append(next_position_info)
                    if moves_counter == 1:
                        break
                    else:
                        continue

        return next_position_info_list

'''
将棋子的走步转换成棋谱
'''
def moves_to_map(previous_map, previous_position, next_position):
    '''
    :param previous_map: 原先棋谱
    :param previous_position: 原先的(棋子位置)
    :param next_position: 下一步(位置)
    :return: next_map：输出的棋谱
    '''
    trans_map = []
    for map_row in previous_map:
        trans_map.append(list(map_row))
    t_piece = trans_map[previous_position[0]][previous_position[1]]
    trans_map[previous_position[0]][previous_position[1]] = ''
    trans_map[next_position[0]][next_position[1]] = t_piece
    next_map = []
    for map_row in trans_map:
        next_map.append(tuple(map_row))
    return tuple(next_map)
    pass

__all__ = [pieces_moves, moves_to_map]
