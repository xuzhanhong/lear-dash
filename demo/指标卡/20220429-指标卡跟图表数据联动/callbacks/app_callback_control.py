import dash
from server import *
import pandas as pd
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State, MATCH, ALL
from models.new_media_data import media_index_value_chart_data, media_index_value_content_data, \
    media_index_value_card_children, media_index_value_dataAnalysis

media_indexValueDataAnalysis = media_index_value_dataAnalysis()
media_indexValueContentData = media_index_value_content_data().to_dict(
    orient='records')


@app.callback(
    [
        Output({'type': 'index-value-card', 'index': ALL}, 'className'),
        Output({'type': 'index-value-card-top-right-check', 'index': ALL}, 'className'),
        Output('media-index-value-chart', 'data')
    ],
    Input({'type': 'index-value-card', 'index': ALL}, 'n_clicks'),
    State('media-index-value-chart-data', 'data'),
    prevent_initial_call=True
)
def get_all_selected_card_index(clicks, chart_baseData):
    """指标卡回调"""
    print(clicks)
    className_list = ['index-value-card'] * len(clicks)
    className_trc_list = ['top-right-check-unselected'] * len(clicks)
    # 回调上下文
    ctx = dash.callback_context.triggered[0]['prop_id']
    if ctx.find('{"index":') != -1:
        # 指标卡渲染的数据
        current_ctx = eval(ctx[:-9])
        className_list[current_ctx.get('index')] = 'index-value-card index-value-card-selected'
        className_trc_list[current_ctx.get('index')] = 'top-right-check'

        if current_ctx.get('index') == 1:

            return className_list, className_trc_list, chart_baseData[1]
        elif current_ctx.get('index') == 2:

            return className_list, className_trc_list, chart_baseData[2]
        return className_list, className_trc_list, chart_baseData[0]
    className_list[0] = 'index-value-card index-value-card-selected'
    className_trc_list[0] = 'top-right-check'
    return className_list, className_trc_list, dash.no_update


@app.callback(
    [
        Output('media-index-value-chart-data', 'data'), Output('media-content-table-data', 'data'),
        Output({'type': 'index-value-card', 'index': ALL}, 'children'),
        Output({'type': 'index-value-card', 'index': ALL}, 'n_clicks')
    ],
    [
        Input('media-search', 'nClicks'),
        Input('media-index-value-chart', 'recentlyPointClickRecord')
    ],
    [
        State('media-dateRange', 'value'),
        State({'type': 'index-value-card', 'index': ALL}, 'className'),
        State({'type': 'index-value-card', 'index': ALL}, 'n_clicks'),
        State({'type': 'index-value-card', 'index': ALL}, 'children')
    ]
)
def condition_update(search_index, chart_evt, day, index_card_status, nClicksList, index_card_children):
    """根据条件更新首页数据"""
    # 初始化首页数据
    # 初始化核心指标数据
    chart_baseData = media_index_value_chart_data()
    # 初始化首页内容数据
    contentData = media_index_value_content_data().to_dict(orient='records')
    # 初始化指标卡children
    indexValueCardChildren = media_index_value_card_children(children=index_card_children)
    print('首页回调', dash.callback_context.triggered[0]['prop_id'])

    if any([search_index, chart_evt]):
        print('条件回调---', search_index, chart_evt)
        # 当前已选择指标卡索引
        index_card_click = index_card_status.index('index-value-card index-value-card-selected')
        nClicksList = [item + 1 if item else 0 if index == index_card_click else dash.no_update for index, item in
                       enumerate(nClicksList)]
        # 回调上下文
        ctx = dash.callback_context.triggered[0]['prop_id']
        # 查询按钮
        if ctx.find('media-search') != -1:

            start_date, end_date = (day[0], day[1]) if day else ('', '')
            print('day---', start_date, end_date)
            chart_baseData = media_index_value_chart_data(start_date=start_date, end_date=end_date)

            media_contentData = media_index_value_content_data(start_date=start_date, end_date=end_date).to_dict(
                orient='records')

            indexValueCardChildren = media_index_value_card_children(start_date=start_date, end_date=end_date,
                                                                     children=index_card_children)
            return chart_baseData, media_contentData, indexValueCardChildren, nClicksList
        elif ctx.find("PointClickRecord") != -1:

            contentData = media_index_value_content_data(date=chart_evt.get('data')['created_at']).to_dict(
                orient='records')

            return dash.no_update, contentData, index_card_children, nClicksList

    return chart_baseData, contentData, indexValueCardChildren, nClicksList
