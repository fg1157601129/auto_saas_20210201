# -*- coding: utf-8 -*-
# @File    : query_from_db.py
# @Date    : 2019-09-03-16:57
# @Author  : FangGang
# @Version : 1
from public.DBTool import MysqlUtil


def query_code_from_db(mobile_num=None):
    """
    通过手机号查询验证码
    :param mobile_num:手机号%s格式
    :return: 查询到的验证码
    """
    sql_statement = 'SELECT code FROM kuxiu_supplement.t_supplement_sms WHERE ' \
                    'mobile_num = 86{} ORDER BY create_time DESC'.format(mobile_num)
    code = MysqlUtil().mysql_get_string(sql_statement)
    MysqlUtil().mysql_close()
    return code


def query_ticket_from_db(user_id=None):
    """
    查询黄金转盘的抽奖券
    :param user_id: 用户id，%s格式
    :return: 用户的抽奖券数量
    """
    sql_statement = 'SELECT ticket_num FROM kuxiu_supplement.t_supplement_game_ticket WHERE ' \
                    'user_id = %s AND game_id = 3' % user_id
    ticket = MysqlUtil().mysql_get_string(sql_statement)
    MysqlUtil().mysql_close()
    return ticket


def query_no_big_reward_num_from_db():
    """
    查询当前累计单抽未中大奖的次数，每次中奖后置为0
    :return: 当前累计单抽未中大奖的的次数
    """
    sql_statement = 'SELECT no_big_reward_num FROM kuxiu_supplement.t_supplement_game_one_turn_table_control'
    no_big_reward_num = MysqlUtil().mysql_get_string(sql_statement)
    MysqlUtil().mysql_close()
    return no_big_reward_num


def query_stock_from_db():
    """
    查询黄金转盘库存值
    :return:黄金转盘库存值
    """
    sql_statement = 'SELECT config_value FROM kuxiu_supplement.t_supplement_game_pool WHERE config_key = \'turn_table_gold_game_pool\''
    stock = MysqlUtil().mysql_get_string(sql_statement)
    MysqlUtil().mysql_close()
    return stock


def query_asset_from_db(user_id, *kwargs):
    """
    资产查询-查酷币/星光/小组星光/阳光/金币
    :param user_id:用户id
    :param args: kucoin/anchor_starlight/group_starlight/sun_light/gold_coin
    :return:对应查询值
    """
    sql_statement = 'SELECT %s FROM kuxiu_payment.T_PAYMENT_ASSET WHERE user_id = %s' % (*kwargs, user_id)
    print(sql_statement)
    value = MysqlUtil().mysql_get_string(sql_statement)
    MysqlUtil().mysql_close()
    return value


def query_asset_accumulated_from_db(user_id, type, activate):
    """
    资产累计查询
    :param user_id: uid
    :param type: KUCOIN/GROUP_STAR/INVITE_STAR/ANCHOR_STAR/RMB
    :param kwargs:Exchange/Reward/Barrage/Withdraw/WithdrawRollback/Invite
    :return:
    """
    sql_statement = 'SELECT accumulated_size FROM kuxiu_payment.T_PAYMENT_ASSET_ACCUMULATED WHERE user_id = %s ' \
                    'AND currency_type = \'%s\' AND activate = \'%s\'' % (user_id, type, activate)
    print(sql_statement)
    value = MysqlUtil().mysql_get_string(sql_statement)
    MysqlUtil().mysql_close()
    return value


def query_exchange_record_from_db(user_id, type, starlight_type=None):
    """
    查询最新一条兑换近路的星光值
    :param user_id:uid
    :param type:starlight_size/kucoin_size
    :param starlight_type:星光类型 GROUP_STAR/ANCHOR_STAR/INVITE_STAR
    :return:星光值
    """
    if starlight_type is None:
        sql_statement = 'SELECT %s FROM kuxiu_payment.T_PAYMENT_EXCHANGE WHERE user_id = %s ORDER BY ' \
                        'id DESC' % (type, user_id)
    else:
        sql_statement = 'SELECT %s FROM kuxiu_payment.T_PAYMENT_EXCHANGE WHERE user_id = %s AND ' \
                        'starlight_type = \'%s\' ORDER BY id DESC' % (type, user_id, starlight_type)
    print(sql_statement)
    value = MysqlUtil().mysql_get_string(sql_statement)
    MysqlUtil().mysql_close()
    return value


def query_exchange_record_count_from_db(date, user_id, type):
    """
    查询指定月份的兑换记录数
    :param date:年月'2019-09'
    :param user_id:uid
    :param type:星光类型 GROUP_STAR/ANCHOR_STAR/INVITE_STAR
    :return:星光值
    """
    sql_statement = 'SELECT COUNT(*) FROM kuxiu_payment.T_PAYMENT_EXCHANGE WHERE DATE_FORMAT(exchange_timestamp,' \
                    ' \'%%Y-%%m\')= \'%s\' AND user_id = %s AND starlight_type = \'%s\'' % (date, user_id, type)
    print(sql_statement)
    value = MysqlUtil().mysql_get_string(sql_statement)
    MysqlUtil().mysql_close()
    return value


def query_invite_starlight_size_from_db(date, user_id):
    """
    查询邀请记录的邀请星光
    :param date:日期 2019-09
    :param user_id:邀请用户uid
    :return:邀请星光值
    """
    v = []
    sql_statement = 'SELECT starlight_size FROM kuxiu_payment.T_PAYMENT_INVITE WHERE DATE_FORMAT(invite_timestamp,' \
                    '\'%%Y-%%m\')= \'%s\' AND invite_id = %s ORDER BY id DESC' % (date, user_id)
    print(sql_statement)
    rows = MysqlUtil().mysql_get_rows(sql_statement)
    MysqlUtil().mysql_close()
    if rows is not None:
        for row in rows:
            for i in row:
                v.append(i)
    return v


def query_anchor_reward_from_db(date, anchor_id, param=None, is_count=False):
    """
    查询主播收入记录
    :param param:查询的字段
    :param date:日期 '2019-09'
    :param anchor_id:主播uid
    :param is_count:是否查询数量
    :return:查询值
    """
    v = []
    if is_count:
        sql_statement = 'SELECT COUNT(*) FROM kuxiu_payment.T_PAYMENT_REWARD WHERE DATE_FORMAT(reward_timestamp,' \
                        '\'%%Y-%%m\') = \'%s\' AND anchor_id = %s' % (date, anchor_id)
    else:
        sql_statement = 'SELECT %s FROM kuxiu_payment.T_PAYMENT_REWARD WHERE DATE_FORMAT(reward_timestamp,' \
                        '\'%%Y-%%m\') = \'%s\' AND anchor_id = %s ORDER BY id DESC LIMIT 3' % (param, date, anchor_id)
    print(sql_statement)
    rows = MysqlUtil().mysql_get_rows(sql_statement)
    MysqlUtil().mysql_close()
    if rows is not None:
        for row in rows:
            for i in row:
                v.append(i)
        return v
    else:
        return None


def query_random_9_uid_from_db():
    """
    随机查询9个用户的id
    :return: list[user_id]
    """
    v = []
    sql_statement = 'select user_id from kuxiu_user.t_user_account order by rand() limit 9'
    print(sql_statement)
    rows = MysqlUtil().mysql_get_rows(sql_statement)
    MysqlUtil().mysql_close()
    if rows is not None:
        for row in rows:
            for i in row:
                v.append(str(i))
        return v
    else:
        return None


def query_signin_record_this_week_from_db(user_id):
    """
    查询用户本周的签到记录
    :param user_id: 用户id
    :return: list[sign_type]
    """
    v = []
    sql_statement = 'SELECT sign_type FROM kuxiu_supplement.t_supplement_user_sign_in WHERE user_id = %s AND' \
                    ' YEARWEEK(sign_date) = YEARWEEK(now()) ' % user_id
    print(sql_statement)
    rows = MysqlUtil().mysql_get_rows(sql_statement)
    MysqlUtil().mysql_close()
    if rows is not None:
        for row in rows:
            for i in row:
                v.append(str(i))
        return v
    else:
        return None


def query_system_config_param_value_from_db(code):
    """
    查询系统配置
    :param code: pk_top_padding_ratio/exchange_extra_give_switch/history_msg_switch/invalid_game_version
    :return:
    """
    sql_statement = 'SELECT param_value FROM kuxiu_supplement.t_supplement_system_config WHERE code = \'%s\'' % code
    print(sql_statement)
    v = MysqlUtil().mysql_get_string(sql_statement)
    MysqlUtil().mysql_close()
    return v


if __name__ == "__main__":
    # print(query_invite_starlight_size_from_db('2019-09', '77777010195'))
    print(query_system_config_param_value_from_db('pk_top_padding_ratio'))
