# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world')

def test(request):
    dic = {}

    # error : method error
    if request.method != 'GET':
        dic['error_code'] = 21
        dic['error_message'] = 'method error'
        dic['refrence'] = 'method : get'
        return HttpResponse(json.dumps(dic))

    # error : b does not exist
    if request.GET.get('b') is None:
        dic['error_code'] = 21
        dic['error_message'] = 'b dose not exist'
        dic['reference'] = 'b is required'
        return HttpResponse(json.dumps(dic))
    
    b = request.GET.get('b')

    """
    # error : the type of b is not str
    if type(b) != 'str':
        dic['error_code'] = 21
        dic['error_message'] = 'the type of b is not str'
        dic['reference'] = 'the type of b is str'
        return HttpResponse(json.dumps(dic))
    """

    if request.GET.get('a') is None:
        dic['error_code'] = 0
        dic['error_message'] = ''
        dic['reference'] = ''
        return HttpResponse(json.dumps(dic))

    try:
        a = int(request.GET.get('a'))
    except:
        # eooor : the type of a is not int
        dic['error_code'] = 21
        dic['error_message'] = 'the type of a is not int'
        dic['reference'] = 'the type of a is int'
        return HttpResponse(json.dumps(dic))
    else:
        dic['error_code'] = 0
        dic['error_message'] = ''
        dic['reference'] = ''
    
    return HttpResponse(json.dumps(dic))

