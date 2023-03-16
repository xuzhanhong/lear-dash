class Config:
    # 顶端进度条需要忽略的监听目标
    exclude_props = [
        'side-menu.style',
        'fold-side-menu-icon.icon'
    ]

    # 定义侧边菜单树状结构数据
    menuItems = [
        {
            'component': 'SubMenu',
            'props': {
                'key': 'dashboard',
                'title': '仪表盘',
                'icon': 'antd-dashboard'
            },
            'children': [
                {
                    'component': 'Item',
                    'props': {
                        'key': '/#概览面板',
                        'href': '/#概览面板',
                        'title': '概览面板'
                    }
                }
            ]
        },
        {
            'component': 'SubMenu',
            'props': {
                'key': 'other-pages',
                'title': '其他功能页面',
                'icon': 'antd-app-store'
            },
            'children': [
                {
                    'component': 'Item',
                    'props': {
                        'key': f'/#sub-page{i}',
                        'href': f'/#sub-page{i}',
                        'title': f'功能页面{i}'
                    }
                }
                for i in range(10)
            ]
        }
    ]
