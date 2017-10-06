#encoding:utf8
#象棋系统测试
from Chinese_chess.chess_kernel.pieces_moves import pieces_moves

map_1 = (('b_ju1', 'b_ma1', 'b_xiang1', 'b_shi1', 'b_jiang', 'b_shi2', 'b_xiang2', 'b_ma2', 'b_ju2'),
        (     '',      '',         '',       '',        '',       '',         '',      '',      ''),
        (     '', 'b_pao1',        '',       '',        '',       '',         '', 'b_pao2',     ''),
        ('b_zu1','r_pao1', 'b_zu2',          '', 'b_zu3',         '', 'b_zu4',          '','b_zu5'),
        (     '',      '',         '',       '',        '',       '',         '',      '',      ''),
        (     '',      '',         '',       '',        '',       '',         '',      '',      ''),
        ('r_bing1',    '', 'r_bing2',        '', 'r_bing3',       '', 'r_bing4',      '','r_bing5'),
        (     '',      '',       '',        '',        '',       '',        '', 'r_pao2',      ''),
        (     '',      '',         '',       '',        '',       '',         '',      '',      ''),
        ('r_ju1', 'r_ma1', 'r_xiang1', 'r_shi1', 'r_shuai', 'r_shi2', 'r_xiang2', 'r_ma2', 'r_ju2'))
piece_current_position = (3, 1)
child = pieces_moves(map_1, piece_current_position)
print(child)
pos_list = [e[0] for e in child]
print(pos_list)
if piece_current_position not in pos_list:
    print('233')
else:
    print('55555')


# '''
# 下面将棋子全部输出
# '''
# print(type(map))
# for hang in range(10):
#     for i in range(9):
#         qizi_po = (hang, i)
#         qizi_na = map[hang][i]
#         if qizi_na != '':
#             e = pieces_moves(map, qizi_po)
#             print(qizi_na, end=':')
#             print(e)
