"""
    Created by howie.hu at 2024-07-15.
    Description: 示例接口说明
    Changelog: all notable changes to this file will be documented
"""

from flask import request

from src.common import UniResponse, response_handle, token_required


@token_required()
def demo_get():
    """
    测试接口
    """
    return response_handle(request=request, dict_value=UniResponse.SUCCESS)
