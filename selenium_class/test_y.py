"""
@Author:Pegasus-Yang
@Time: 2020/5/22 上午10:59
"""
import yaml

with open('ydata.yml') as f:
    print(yaml.safe_load(f))