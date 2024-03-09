import pandas as pd
from datetime import datetime, timedelta


def media_index_value_chart_data(start_date='', end_date=''):
    """近七天图表数据"""
    data = pd.read_excel('./test.xlsx')
    if all([start_date, end_date]):
        start_date, end_date = datetime.strptime(start_date, '%Y-%m-%d').date(), datetime.strptime(end_date,
                                                                                                   '%Y-%m-%d').date()
        df = (
            data[
                (data.media_time.dt.date >= start_date) & (data.media_time.dt.date < end_date)].assign(
                created_at=lambda x: pd.to_datetime(x.media_time).dt.strftime('%Y-%m-%d')).rename(
                columns={'media_attitude_counts': '点赞数', 'media_comment_counts': '评论数', 'media_share_counts': '转发数',
                         'media_collect_counts': '收藏数', }))
    else:
        df = (data[data.media_time.dt.date >= data.media_time.max().date() - timedelta(days=7)].assign(
            created_at=lambda x: pd.to_datetime(x.media_time).dt.strftime('%Y-%m-%d')).rename(
            columns={'media_attitude_counts': '点赞数', 'media_comment_counts': '评论数', 'media_share_counts': '转发数',
                     'media_collect_counts': '收藏数', }))

    # 抖音互动量数据
    dy_interaction_data = df[df.platform == '抖音'].groupby(['created_at'], as_index=False).sum().melt(
        id_vars='created_at', value_vars=['点赞数', '评论数', '转发数'],
        var_name='series', value_name='count').to_dict(
        orient='records')
    # 微博互动量数据
    wb_interaction_data = df[df.platform == '微博'].groupby(['created_at'], as_index=False).sum().melt(
        id_vars='created_at', value_vars=['点赞数', '评论数', '转发数'],
        var_name='series', value_name='count').to_dict(
        orient='records')
    # 新媒体互动量趋势图数据
    sum_interaction_data = df.groupby(['created_at', 'platform'], as_index=False).sum().rename(
        columns={'platform': 'series', 'totals': 'count'})[
        ['created_at', 'count', 'series']].to_dict(
        orient='records')

    return dy_interaction_data, wb_interaction_data, sum_interaction_data


def media_index_value_content_data(start_date='', end_date='', date=''):
    """近七天品牌具体内容数据、根据时间范围及某个时间查询具体内容数据"""
    df = pd.read_excel('./test.xlsx')
    # 时间范围
    if all([start_date, end_date]):

        start_date, end_date = datetime.strptime(start_date, '%Y-%m-%d').date(), datetime.strptime(end_date,
                                                                                                   '%Y-%m-%d').date()
        results = df[(df.media_time.dt.date >= start_date) & (df.media_time.dt.date < end_date)].assign(
            media_create_time=lambda x: pd.to_datetime(x.media_time).dt.strftime('%Y-%m-%d'),
            web_link=lambda x: x.media_href.apply(lambda x: {'href': x})
        ).sort_values('totals', ascending=False)
        return results
    # 具体的时间
    elif date:
        results = df.assign(
            media_create_time=lambda x: pd.to_datetime(x.media_time).dt.strftime('%Y-%m-%d'),
            web_link=lambda x: x.media_href.apply(lambda x: {'href': x})
        ).query(f'media_create_time==@date').sort_values('totals', ascending=False)

        print('date---', date)
        return results
    # 默认近七天
    else:
        results = df[df.media_time.dt.date >= df.media_time.max().date() - timedelta(days=7)].assign(
            media_create_time=lambda x: pd.to_datetime(x.media_time).dt.strftime('%Y-%m-%d %H:%i'),
            web_link=lambda x: x.media_href.apply(lambda x: {'href': x})
        ).sort_values('totals', ascending=False)

        return results


def media_index_value_dataAnalysis(start_date='', end_date='', value='抖音', month=[]):
    """指标卡数据（近七天最大值、最大值占比，环比等）"""
    df = pd.read_excel('./test.xlsx')
    # 时间范围
    if all([start_date, end_date]):
        start_date, end_date = datetime.strptime(start_date, '%Y-%m-%d').date(), datetime.strptime(end_date,
                                                                                                   '%Y-%m-%d').date()
        data = df[(df.media_time.dt.date >= start_date) & (df.media_time.dt.date < end_date)].assign(
            media_time_day=lambda x: x.media_time.dt.strftime('%Y-%m-%d')).sort_values('media_time_day',
                                                                                       ascending=False)
    # 默认近七天
    else:
        data = df[df.media_time.dt.date >= df.media_time.max().date() - timedelta(days=7)].assign(
            media_time_day=lambda x: x.media_time.dt.strftime('%Y-%m-%d')).sort_values('media_time_day',
                                                                                       ascending=False)

    # 互动量(抖音、微博)数据
    interaction_data = (
        data.assign(media_time_day=lambda df: pd.to_datetime(df.media_time_day, format='%Y-%m-%d'),
                    totals=lambda df: df.media_attitude_counts + df.media_comment_counts +
                                      df.media_share_counts + df.media_collect_counts)
            .groupby(['media_time_day', 'platform'], as_index=False)['totals'].sum()).sort_values('media_time_day',
                                                                                                  ascending=False)
    # 最近七天互动量(总和)数据
    sevenDay_interactionData = pd.DataFrame({
        'media_time_day': [(interaction_data.media_time_day.max() - timedelta(days=item)).strftime('%Y-%m-%d') for item
                           in range(0, 7)],
    }).merge(interaction_data.groupby('media_time_day', as_index=False)['totals'].sum().
             assign(media_time_day=lambda x: x.media_time_day.astype('str')), on='media_time_day',
             how='left').fillna(0)
    # 计算最近七天(总和)最大值、最大值占比、环比
    sevenDay_interactionDescriptive = {
        'seven_max': (sevenDay_interactionData.totals.max()),
        'seven_max_proportion': int(
            (sevenDay_interactionData.totals.max() / sevenDay_interactionData.totals.sum()) * 100),
        'seven_qoq': [
            '{:.2%}'.format((sevenDay_interactionData.totals.iloc[0] - item) / item)
            if item else '环比值不存在' for item in sevenDay_interactionData.totals.to_list()]
    }

    # 最近七天微博、抖音等品牌互动量（曝光）数据以及描述性分析
    sevenDay_wb_dy_interactionData = [pd.DataFrame({
        'media_time_day': [(interaction_data.media_time_day.max() - timedelta(days=item)).strftime('%Y-%m-%d') for item
                           in range(0, 7)],
    }).merge(interaction_data[interaction_data.platform == platform].assign(
        media_time_day=lambda x: x.media_time_day.astype('str')), on='media_time_day', how='left').fillna(0) for
                                      platform in ['微博', '抖音']]
    # 计算最近七天(微博、抖音)、最大值、最大值占比、环比
    sevenDay_wb_dy_Descriptive = [
        {
            'seven_max': (sevenDay_Descriptive.totals.max()),
            'seven_max_proportion': int((sevenDay_Descriptive.totals.max() / sevenDay_Descriptive.totals.sum()) * 100),
            'seven_qoq': ['{:.2%}'.format((sevenDay_Descriptive.totals.iloc[0] - item) / item) if item else '环比值不存在' for
                          item
                          in sevenDay_Descriptive.totals.to_list()]
        }
        for sevenDay_Descriptive in sevenDay_wb_dy_interactionData]

    return sevenDay_interactionDescriptive, sevenDay_wb_dy_Descriptive[0], sevenDay_wb_dy_Descriptive[1]


def media_index_value_card_children(start_date='', end_date='', children=''):
    """将计算的最大值、昨日、三日环比赋值到指标卡前端children"""
    index_coreIndexDataAnalysis = media_index_value_dataAnalysis(start_date=start_date, end_date=end_date)

    for index, index_value_card in enumerate(children):
        for item in index_value_card:
            # 将近七天（最大值、昨日、三日环比）对前端children赋值
            if item['props'].get('className') != 'main-index-value-maxValueProportion':
                for item_child in item['props']['children']:
                    # 最大值区域
                    if item_child['props'].get('className') == 'main-index-value-maxValue':

                        # 最大值
                        item_child['props']['value'] = index_coreIndexDataAnalysis[index].get('seven_max')
                    # 昨日环比区域
                    elif item_child['props'].get('className') == 'main-index-value-oneDayPop':
                        for item_grandson in item_child['props'].get('children'):
                            # 昨日环比值
                            if item_grandson['props'].get('className') == 'pop-value':
                                item_grandson['props']['children'] = \
                                    index_coreIndexDataAnalysis[index].get('seven_qoq')[1]
                    # 三日环比区域
                    elif item_child['props'].get('className') == 'main-index-value-threeDayPop':
                        for item_grandson in item_child['props'].get('children'):
                            # 三日环比值
                            if item_grandson['props'].get('className') == 'pop-value':
                                item_grandson['props']['children'] = \
                                    index_coreIndexDataAnalysis[index].get('seven_qoq')[4]

            # 近七天最大值占比
            else:
                # 近七天最大值
                item['props']['children']['props']['percent'] = index_coreIndexDataAnalysis[index].get(
                    'seven_max_proportion')

    return children
