import dash
from dash import dcc
from dash import html
from plotly import graph_objs as go
from plotly import express as px
from dataProcess import *
import warnings

warnings.filterwarnings("ignore")

app = dash.Dash(
    __name__,
    external_stylesheets=[
        'https://codepen.io/chriddyp/pen/bWLwgP.css'
    ]
)

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='school_type_or_region',
                options=[{'label': i, 'value': i} for i in ['School Type', 'Region']],
                value='School Type'
            )
        ], style={'width': '33%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='salary_type',
                options=[{'label': i, 'value': i} for i in get_salary_types()],
                value='Mid-Career Median Salary'
            )
        ], style={'width': '33%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='method',
                options=[{'label': i, 'value': i} for i in ['min', 'max', 'avg', 'mid']],
                value='mid'
            )
        ], style={'width': '33%', 'display': 'inline-block'})
    ], style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
    }),

    html.Div([
        # 左边的柱状图
        dcc.Graph(
            id='start_mid_salary_compare',
        )
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        # 右边的箱型图
        dcc.Graph(id='salary_box')
    ], style={'width': '49%', 'display': 'inline-block'}),
    html.Div([
        # 下边的Sunburst图
        dcc.Graph(id='sunburst_salary_box'),

    ], style={'width': '49%', 'display': 'inline-block'}),
    html.Div([
        # 具体学校的图片
        dcc.Graph(id='certain_school'),
    ], style={'width': '49%', 'display': 'inline-block'}),
])


@app.callback(
    dash.dependencies.Output('start_mid_salary_compare', 'figure'),
    [dash.dependencies.Input('school_type_or_region', 'value'),
     dash.dependencies.Input('method', 'value')])
def update_start_mid_salary_compare_graph(school_type_or_region, method):
    graph_date = get_start_mid_salary_compare_data(school_type_or_region, method)
    trace = []
    for salary_type in get_salary_types():
        trace.append(
            go.Bar(
                x=graph_date['x'],
                y=graph_date[salary_type],
                name=salary_type
            )
        )
    layout = go.Layout(
        title=school_type_or_region + ' --- Salary Graph',
        # 横坐标设置
        xaxis={
            'title': school_type_or_region,
        },
        # 纵坐标设置
        yaxis={
            'title': 'Salary',
        },
        margin={'l': 50, 'b': 30, 't': 50, 'r': 0},
        height=450,
        hovermode='closest'
    )
    return {
        'data': trace,
        'layout': layout
    }


@app.callback(
    dash.dependencies.Output('salary_box', 'figure'),
    [dash.dependencies.Input('school_type_or_region', 'value'),
     dash.dependencies.Input('salary_type', 'value')])
def update_salary_box_graph(school_type_or_region, salary_type):
    graph_date = get_salary_box_data(school_type_or_region, salary_type)
    trace = []
    for i in range(len(graph_date['x'])):
        trace.append(go.Box(y=graph_date['y'][i], name=graph_date['x'][i]))
    layout = go.Layout(
        title=school_type_or_region + ' --- Salary Distribution',
        # 横坐标设置
        xaxis={
            'title': school_type_or_region,
        },
        # 纵坐标设置
        yaxis={
            'title': 'Salary Distribution',
        },
        margin={'l': 50, 'b': 30, 't': 50, 'r': 0},
        height=450,
        hovermode='closest'
    )
    return {
        'data': trace,
        'layout': layout
    }


@app.callback(
    dash.dependencies.Output('sunburst_salary_box', 'figure'),
    [dash.dependencies.Input('school_type_or_region', 'value'),
     dash.dependencies.Input('salary_type', 'value')])
def update_sunburst_salary_box_graph(school_type_or_region, salary_type):
    graph_date = get_data(school_type_or_region)
    fig = px.sunburst(
        graph_date,
        path=[school_type_or_region, 'School Name'],
        values=salary_type,
        branchvalues='total',
        color=salary_type,
        color_continuous_scale='RdBu',
        hover_data=['School Name']
    )

    fig.layout.height = 600
    fig.layout.margin = {'l': 50, 'b': 30, 't': 50, 'r': 0}
    fig.layout.hovermode = 'closest'

    return {
        'data': fig.data,
        'layout': fig.layout
    }


@app.callback(
    dash.dependencies.Output('certain_school', 'figure'),
    [dash.dependencies.Input('sunburst_salary_box', 'hoverData'),
     dash.dependencies.Input('school_type_or_region', 'value'),
     dash.dependencies.Input('method', 'value')])
def update_certain_school_graph(hoverData, school_type_or_region, method):
    try:
        school_name = hoverData['points'][0]['label'].strip()
    except TypeError:
        school_name = 'State'
    graph = get_data(school_type_or_region)
    array = []
    if school_name not in get_school_regions() and school_name not in get_school_types():
        dff = graph[graph['School Name'] == school_name].values
        array = dff[0][2:]
    elif school_name in get_school_types():
        array = get_salary_by_certain_school_type(graph, school_name, method)
    elif school_name in get_school_regions():
        array = get_salary_by_certain_school_region(graph, school_name, method)
    return {
        'data': [go.Scatter(
            x=['0', '10', '25', '50', '75', '90'],
            y=[array[0], array[2], array[3], array[4], array[5], array[1]],
            mode='lines+markers',
            line=dict(
                color='rgba(255, 182, 193)',
                width=1
            ),
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            title=f'Salary Of {school_name}',
            # 横坐标设置
            xaxis={
                'title': 'Mid-Career (x)th Percentile Salary',
                'tickmode': 'auto', 'nticks': 10, 'tickwidth': 0.1,
            },
            # 纵坐标设置
            yaxis={
                'title': 'Salary',
            },
            margin={'l': 60, 'b': 80, 't': 50, 'r': 0},
            height=550,
            width=700,
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    data_init()
    app.run_server()
