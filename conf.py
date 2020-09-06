IR_CMD = "/home/pi/bin/bto_ir_cmd"

ir_code = [
    {
        'order': '1',
        'name'  : 'LIGHT',
        'codes' : [
            {
                'name' : 'ON',
                'code' : '82826DA6590000'
            },
            {
                'name' : 'OFF',
                'code' : '82826DBE410000'
            },
            {
                'name' : 'UP',
                'code' : '82826DBA450000'
            },
            {
                'name' : 'DOWN',
                'code' : '82826DBB440000'
            },
            {
                'name' : 'NIGHT',
                'code' : '82826DBC430000'
            },
        ]
    },
    {
        'order':'2',
        'name': 'TV',
        'codes': [
            {
                'name' : 'SWITCH',
                'code' : 'C1022080003DBD'
            },
            {
                'name': 'UP',
                'code': 'C10220800020A0'
            },
            {
                'name': 'DOWN',
                'code': 'C10220800021A1'
            },
            {
                'name': 'NEXT',
                'code': 'C10220800034B4'
            },
            {
                'name': 'BEF',
                'code': 'C10220800035B5'
            },
            {
                'name': 'INPUT',
                'code': 'C1022080000585'
            }
        ]
    }
]
