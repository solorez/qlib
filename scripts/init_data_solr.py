# https://www.wuzao.com/document/qlib/start/initialization.html#google_vignette

# import qlib
# # 区域取值 [REG_CN, REG_US]
# from qlib.constant import REG_CN
# # provider_uri = "~/.qlib/qlib_data/cn_data"  # 目标目录
# provider_uri = "~/.qlib/qlib_data/qlib_cn_1min"
# qlib.init(provider_uri=provider_uri, region=REG_CN)


import qlib
from qlib.contrib.data.handler import Alpha158

data_handler_config = {
    "start_time": "2008-01-01",
    "end_time": "2020-08-01",
    "fit_start_time": "2008-01-01",
    "fit_end_time": "2014-12-31",
    "instruments": "csi300",
}

if __name__ == "__main__":
    qlib.init()
    h = Alpha158(**data_handler_config)

    # 获取所有数据的列
    print(h.get_cols())

    # 获取所有标签
    print(h.fetch(col_set="label"))

    # 获取所有特征
    print(h.fetch(col_set="feature"))