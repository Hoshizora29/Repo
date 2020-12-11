[
    {
        "id": "2e2d5c4a.23a6b4",
        "type": "tab",
        "label": "流程4",
        "disabled": false,
        "info": ""
    },
    {
        "id": "740e7b6a.3da394",
        "type": "inject",
        "z": "2e2d5c4a.23a6b4",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "onceDelay": 0.1,
        "x": 90,
        "y": 100,
        "wires": [
            [
                "f97e20dc.54cb7"
            ]
        ]
    },
    {
        "id": "f97e20dc.54cb7",
        "type": "function",
        "z": "2e2d5c4a.23a6b4",
        "name": "",
        "func": "msg.headers={\n    deviceKey: \"ngPOcmH2wT9QYocm\"\n    };\nmsg.payload= \"Temperature,,25.3\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 270,
        "y": 200,
        "wires": [
            [
                "9034447b.0a1a78"
            ]
        ]
    },
    {
        "id": "9034447b.0a1a78",
        "type": "http request",
        "z": "2e2d5c4a.23a6b4",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "paytoqs": false,
        "url": "https://api.mediatek.com/mcs/v2/devices/D9xzoYqI/datapoints.csv",
        "tls": "",
        "persist": false,
        "proxy": "",
        "authType": "",
        "x": 500,
        "y": 200,
        "wires": [
            [
                "dc252573.a7b2e8",
                "36593a11.a722e6"
            ]
        ]
    },
    {
        "id": "dc252573.a7b2e8",
        "type": "http response",
        "z": "2e2d5c4a.23a6b4",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 690,
        "y": 200,
        "wires": []
    },
    {
        "id": "36593a11.a722e6",
        "type": "debug",
        "z": "2e2d5c4a.23a6b4",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 700,
        "y": 280,
        "wires": []
    }
]
