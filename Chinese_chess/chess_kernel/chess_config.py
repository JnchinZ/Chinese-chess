#encoding:utf8
'''
tips：由于 在python中，strings, tuples, 和numbers是不可更改的对象，而list,dict等则是可以修改的对象。
所以这里我们的象棋系统的棋谱数据类型是数组类型的tuples
'''
#初始的棋谱
initial_map = (('b_ju1', 'b_ma1', 'b_xiang1', 'b_shi1', 'b_jiang', 'b_shi2', 'b_xiang2', 'b_ma2', 'b_ju2'),
                (      '',      '',         '',       '',        '',       '',         '',      '',      ''),
                (      '', 'b_pao1',        '',       '',        '',       '',         '', 'b_pao2',     ''),
                ('b_zu1',      '', 'b_zu2',          '', 'b_zu3',         '', 'b_zu4',          '','b_zu5'),
                (      '',      '',         '',       '',        '',       '',         '',      '',      ''),
                (      '',      '',         '',       '',        '',       '',         '',      '',      ''),
                ('r_bing1',    '', 'r_bing2',        '', 'r_bing3',       '', 'r_bing4',      '','r_bing5'),
                (      '', 'r_pao1',       '',        '',        '',       '',        '', 'r_pao2',      ''),
                (      '',      '',         '',       '',        '',       '',         '',      '',      ''),
                ('r_ju1', 'r_ma1', 'r_xiang1', 'r_shi1', 'r_shuai', 'r_shi2', 'r_xiang2', 'r_ma2', 'r_ju2'))

#配置思考深度think_depth
think_depth = 3

#配置吃棋子的奖励分数
killing_rewards = {
    'ju':7,
    'ma':6,
    'xiang':4,
    'shi':3,
    'jiang':100000,
    'pao':5,
    'zu':2
}
