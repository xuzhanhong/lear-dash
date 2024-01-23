import dash
import time
import numpy as np
import pandas as pd
from dash import html
from faker import Faker
from datetime import datetime
import feffery_antd_charts as fact
import feffery_antd_components as fac
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

fake = Faker(locale='zh_CN')

# 生成随机示例数据
demo_df = pd.DataFrame(
    {
        '类型': np.random.choice(
            ['直接访问', '邮件营销', '联盟广告', '视频广告', '搜索引擎'],
            1000,
            p=[0.4, 0.2, 0.1, 0.1, 0.2]
        ),
        '访问时间': [
            fake
            .date_time_between_dates(
                datetime.strptime('2024-01-01', '%Y-%m-%d'),
                datetime.strptime('2024-01-31', '%Y-%m-%d')
            )
            for i in range(1000)
        ],
        '交易额': np.random.uniform(10, 1000, 1000).round(1)
    }
)
demo_df['key'] = [f'row-{i}' for i in range(demo_df.shape[0])]
demo_df['访问时间'] = demo_df['访问时间'].dt.strftime('%Y-%m-%d %H:%M:%S')

app.layout = html.Div(
    fac.AntdSpace(
        [
            fact.AntdColumn(
                id='demo-column-chart',
                data=(
                    demo_df
                    .groupby('类型', as_index=False)
                    .agg(获客量=pd.NamedAgg('访问时间', 'count'))
                    .to_dict('records')
                ),
                xField='类型',
                yField='获客量',
                height=250,
                columnWidthRatio=0.2
            ),
            fac.AntdSpin(
                fac.AntdTable(
                    id='demo-table',
                    columns=[
                        {
                            'title': '类型',
                            'dataIndex': '类型',
                            'width': 'calc(100% / 3)'
                        },
                        {
                            'title': '访问时间',
                            'dataIndex': '访问时间',
                            'width': 'calc(100% / 3)'
                        },
                        {
                            'title': '交易额',
                            'dataIndex': '交易额',
                            'width': 'calc(100% / 3)'
                        }
                    ],
                    data=demo_df.to_dict('records'),
                    bordered=True,
                    hiddenRowKeys=demo_df['key'].tolist(),
                    emptyContent=fac.AntdEmpty(
                        description='请点击上面的柱状图以筛选数据',
                        image='simple'
                    ),
                    size='small'
                ),
                text='分析中'
            )
        ],
        direction='vertical',
        style={
            'width': '100%'
        }
    ),
    style={
        'padding': '50px 200px'
    }
)


@app.callback(
    Output('demo-table', 'hiddenRowKeys'),
    Input('demo-column-chart', 'recentlyColumnClickRecord'),
    prevent_initial_call=True
)
def filter_table_data(recentlyColumnClickRecord):

    # 让加载动画更明显^_^
    time.sleep(0.3)

    return demo_df.query('类型 != "{}"'.format(recentlyColumnClickRecord['data']['类型']))['key'].tolist()


if __name__ == '__main__':
    app.run(debug=True)
