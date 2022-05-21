import pandas as pd

df_school_type = pd.read_csv(
    '../lab3-datasets/college-salaries/salaries-by-college-type.csv', index_col=None, encoding='utf-8'
)
df_school_region = pd.read_csv(
    '../lab3-datasets/college-salaries/salaries-by-region.csv', index_col=None, encoding='utf-8'
)


# 数据处理，把数据中的'$'与','符号去除
def data_handel(df: pd.DataFrame):
    for column in df.columns[2:]:
        df[column].fillna(method='ffill', inplace=True)
        df[column] = df[column].apply(
            lambda x: str(x)[1:].replace(',', '').strip() if str(x) != 'nan' else str(x)
        )
    df[get_salary_types()] = df[get_salary_types()].astype(float)


def data_init():
    global df_school_type, df_school_region
    data_handel(df_school_type)
    data_handel(df_school_region)


# 根据用户选择返回所需的数据
def get_data(school_type_or_region):
    return df_school_type if school_type_or_region == 'School Type' else df_school_region


# 获取工资类型
def get_salary_types():
    return df_school_type.columns.values[2:]


# 获取学校类型
def get_school_types():
    return df_school_type['School Type'].unique()


# 获取学校地区
def get_school_regions():
    return df_school_region['Region'].unique()


# 根据学校类型求工资
def get_salary_by_school_type(df: pd.DataFrame, column, method):
    df = df.drop(columns=['School Name'], inplace=False)
    if method == 'min':
        return df.groupby(df['School Type']).min().loc[:, column]
    elif method == 'max':
        return df.groupby(df['School Type']).max().loc[:, column]
    elif method == 'avg':
        return df.groupby(df['School Type']).mean().loc[:, column]
    else:
        return df.groupby(df['School Type']).median().loc[:, column]


# 根据学校地区求工资
def get_salary_by_school_region(df: pd.DataFrame, column, method):
    df = df.drop(columns=['School Name'], inplace=False)
    if method == 'min':
        return df.groupby(df['Region']).min().loc[:, column]
    elif method == 'max':
        return df.groupby(df['Region']).max().loc[:, column]
    elif method == 'avg':
        return df.groupby(df['Region']).mean().loc[:, column]
    else:
        return df.groupby(df['Region']).median().loc[:, column]


# 根据具体学校类型求各个阶段工资
def get_salary_by_certain_school_type(df: pd.DataFrame, school_type, method):
    df = df.drop(columns=['School Name'], inplace=False)
    if method == 'min':
        return df.groupby(df['School Type']).min().loc[school_type]
    elif method == 'max':
        return df.groupby(df['School Type']).max().loc[school_type]
    elif method == 'avg':
        return df.groupby(df['School Type']).mean().loc[school_type]
    else:
        return df.groupby(df['School Type']).median().loc[school_type]


# 根据具体学校地区求各个阶段工资中位数
def get_salary_by_certain_school_region(df: pd.DataFrame, school_region, method):
    df = df.drop(columns=['School Name'], inplace=False)
    if method == 'min':
        return df.groupby(df['Region']).min().loc[school_region]
    elif method == 'max':
        return df.groupby(df['Region']).max().loc[school_region]
    elif method == 'avg':
        return df.groupby(df['Region']).mean().loc[school_region]
    else:
        return df.groupby(df['Region']).median().loc[school_region]


# 图像start_mid_salary_compare_data的数据
def get_start_mid_salary_compare_data(school_type_or_region, method):
    if school_type_or_region == 'School Type':
        school_types = get_school_types()
        res = {'x': school_types}
        for salary_type in get_salary_types():
            res[salary_type] = [get_salary_by_school_type(df_school_type, salary_type, method)[x] for x in school_types]
        return res
    else:
        school_regions = get_school_regions()
        res = {'x': school_regions}
        for salary_type in get_salary_types():
            res[salary_type] = [get_salary_by_school_region(df_school_region, salary_type, method)[x] for x in
                                school_regions]
        return res


# 图像salary_box的数据
def get_salary_box_data(school_type_or_region, salary_type):
    if school_type_or_region == 'School Type':
        school_types = get_school_types()
        return {
            'x': school_types,
            'y': [df_school_type.loc[df_school_type['School Type'] == x, salary_type].values for x in school_types]
        }
    else:
        school_regions = get_school_regions()
        return {
            'x': school_regions,
            'y': [df_school_region.loc[df_school_region['Region'] == x, salary_type].values for x in school_regions]
        }
