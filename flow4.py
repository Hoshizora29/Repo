[
    {
        "id": "a553acd2.796b4",
        "type": "tab",
        "label": "流程1",
        "disabled": false,
        "info": ""
    },
    {
        "id": "cf921f1.ea0fee",
        "type": "http in",
        "z": "a553acd2.796b4",
        "name": "",
        "url": "/pin4",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 110,
        "y": 180,
        "wires": [
            [
                "8ca8f57a.6f71b8"
            ]
        ]
    },
    {
        "id": "e41499dc.cc7c08",
        "type": "rpi-gpio in",
        "z": "a553acd2.796b4",
        "name": "GPIO4",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": false,
        "x": 120,
        "y": 280,
        "wires": [
            [
                "cb2445dc.a46118"
            ]
        ]
    },
    {
        "id": "cb2445dc.a46118",
        "type": "function",
        "z": "a553acd2.796b4",
        "name": "Set GPIO",
        "func": "global.set(\"GPIO\", msg.payload)\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 370,
        "y": 280,
        "wires": [
            [
                "44da7e82.16939"
            ]
        ]
    },
    {
        "id": "8ca8f57a.6f71b8",
        "type": "function",
        "z": "a553acd2.796b4",
        "name": "Get GPIO",
        "func": "msg.payload = global.get(\"GPIO\");\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 380,
        "y": 180,
        "wires": [
            [
                "f2e43a54.1ca728",
                "44da7e82.16939"
            ]
        ]
    },
    {
        "id": "f2e43a54.1ca728",
        "type": "http response",
        "z": "a553acd2.796b4",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 630,
        "y": 180,
        "wires": []
    },
    {
        "id": "44da7e82.16939",
        "type": "debug",
        "z": "a553acd2.796b4",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 630,
        "y": 280,
        "wires": []
    }
]
