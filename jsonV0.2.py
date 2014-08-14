#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json

d = 'duanyulei'
data =  {
    "status": d, 
    "message": "",
    "data": {
        "total": 24,
        "list": [
            {
                "date": "07.01",
                "list": [
                    {
                        "text": d,
                        "icon": "template"
                    },
                    {
                        "text": "神庙2",
                        "icon": "template"
                    },
                     {
                        "text": "神庙2",
                        "icon": "template"
                    },
                     {
                        "text": "神庙2",
                        "icon": "template"
                    },
                     {
                        "text": "神庙2",
                        "icon": "template"
                    },
                    {
                        "text": "神庙3",
                        "icon": "template"
                    }
                ]
            },
            {
                "date": "07.01",
                "list": [
                    {
                        "text": "神庙",
                        "icon": "template"
                    },
                    {
                        "text": "神庙2",
                        "icon": "template"
                    },
                    {
                        "text": "神庙3",
                        "icon": "template"
                    }
                ]
            },
            {
                "date": "07.01",
                "list": [
                    {
                        "text": "神庙",
                        "icon": "template"
                    },
                    {
                        "text": "神庙2",
                        "icon": "template"
                    },
                    {
                        "text": "神庙3",
                        "icon": "template"
                    }
                ]
            },
            {
                "date": "07.01",
                "list": [
                    {
                        "text": "神庙",
                        "icon": "template"
                    },
                    {
                        "text": "神庙2",
                        "icon": "template"
                    },
                    {
                        "text": "神庙3",
                        "icon": "template"
                    }
                ]
            },
            {
                "date": "07.01",
                "list": [
                    {
                        "text": "神庙",
                        "icon": "template"
                    },
                    {
                        "text": "神庙2",
                        "icon": "template"
                    },
                    {
                        "text": "神庙3",
                        "icon": "template"
                    }
                ]
            },
            {
                "date": "07.01",
                "list": [
                    {
                        "text": "神庙",
                        "icon": "template"
                    },
                    {
                        "text": "神庙2",
                        "icon": "template"
                    },
                    {
                        "text": "神庙3",
                        "icon": "template"
                    }
                ]
            },
            {
                "date": "07.01",
                "list": [
                    {
                        "text": "神庙",
                        "icon": "template"
                    },
                    {
                        "text": "神庙2",
                        "icon": "template"
                    },
                    {
                        "text": "神庙3",
                        "icon": "template"
                    }
                ]
            }
        ]
    }
}
# print 'DATA:', repr(data)

# unsorted = json.dumps(data)
# print 'JSON:', json.dumps(data)
# print 'SORT:', json.dumps(data, sort_keys=True)
print 'INDENT:', json.dumps(data, sort_keys=True, indent=2)
