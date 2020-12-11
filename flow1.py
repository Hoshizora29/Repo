[
    {
        "id": "870135c7.9c5458",
        "type": "tab",
        "label": "流程2",
        "disabled": false,
        "info": ""
    },
    {
        "id": "9435b96f.f8fd28",
        "type": "rpi-gpio in",
        "z": "870135c7.9c5458",
        "name": "Button",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 50,
        "y": 200,
        "wires": [
            [
                "513a0ede.0c38d",
                "211531d0.2974ce"
            ]
        ]
    },
    {
        "id": "513a0ede.0c38d",
        "type": "debug",
        "z": "870135c7.9c5458",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "x": 670,
        "y": 180,
        "wires": []
    },
    {
        "id": "407c4318.dae5dc",
        "type": "rpi-gpio out",
        "z": "870135c7.9c5458",
        "name": "LED",
        "pin": "7",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 690,
        "y": 320,
        "wires": []
    },
    {
        "id": "211531d0.2974ce",
        "type": "switch",
        "z": "870135c7.9c5458",
        "name": "if input is 1",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "repair": false,
        "outputs": 2,
        "x": 270,
        "y": 320,
        "wires": [
            [
                "a078096c.16ae88"
            ],
            [
                "29d38478.f0e48c"
            ]
        ]
    },
    {
        "id": "a078096c.16ae88",
        "type": "change",
        "z": "870135c7.9c5458",
        "name": "Change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 470,
        "y": 260,
        "wires": [
            [
                "407c4318.dae5dc"
            ]
        ]
    },
    {
        "id": "29d38478.f0e48c",
        "type": "change",
        "z": "870135c7.9c5458",
        "name": "Change to 1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 470,
        "y": 360,
        "wires": [
            [
                "407c4318.dae5dc"
            ]
        ]
    }
]
