// 在独立js脚本中定义比较长的回调函数
window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        render_map: function (data) {

            // 根据id初始化绑定图表
            var myChart = echarts.init(document.getElementById('map-container'));

            echarts.registerMap('ls', data);

            const option = {
                backgroundColor: '#fff',
                tooltip: false,
                geo: {
                    map: 'ls',
                    show: true,
                    label: {
                        emphasis: {
                            show: false
                        }
                    },
                    itemStyle: {
                        normal: {
                            areaColor: '#6395fa',
                            borderColor: '#fff',
                            borderWidth: 2,
                            shadowColor: '#5AB2FE',
                            shadowBlur: 20
                        }
                    },
                    zoom: 1.2,
                },
                series: [
                    {
                        type: 'map',
                        map: 'ls',
                        geoIndex: 1,
                        aspectScale: 0.75, //长宽比
                        zoom: 1.2,
                        label: {
                            emphasis: {
                                show: false,
                                textStyle: {
                                    color: '#05C3F9'
                                }
                            }
                        },
                        roam: false,
                        itemStyle: {
                            normal: {
                                areaColor: '#6395fa',
                                borderColor: '#fff',
                                borderWidth: 2
                            },
                            emphasis: {
                                areaColor: '#C9E6FF50',
                                shadowColor: '#5AB2FE',
                                shadowBlur: 20
                            }
                        },
                        data: data.features, // 注意这里的data是数组，不是原始的geojson对象
                    }
                ]
            };

            // 监听点击事件
            myChart.on('click', (params) => {
                if (params.seriesType === 'map') {
                    console.log('=======================')
                    console.log(params.name)

                    window.dash_clientside.set_props(
                        'echarts-sync-event',
                        {
                            children: {
                                namespace: 'feffery_antd_components',
                                type: 'AntdMessage',
                                props: {
                                    type: 'info',
                                    content: '您点击了地区：' + params.name
                                }
                            }
                        }
                    )
                }
            })

            // 渲染
            myChart.setOption(option);
        }
    }
});