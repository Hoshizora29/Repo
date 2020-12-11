[
    {
        "id": "f479beee.d423a",
        "type": "tab",
        "label": "流程3",
        "disabled": false,
        "info": ""
    },
    {
        "id": "abaf374b.f3c348",
        "type": "inject",
        "z": "f479beee.d423a",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "onceDelay": 0.1,
        "x": 130,
        "y": 60,
        "wires": [
            [
                "caa4d104.16e9b"
            ]
        ]
    },
    {
        "id": "caa4d104.16e9b",
        "type": "function",
        "z": "f479beee.d423a",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey:\"ngPOcmH2wT9QYocm\"\n    };\n\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 240,
        "y": 220,
        "wires": [
            [
                "2b418759.994d58"
            ]
        ]
    },
    {
        "id": "2b418759.994d58",
        "type": "http request",
        "z": "f479beee.d423a",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "paytoqs": false,
        "url": "http://api.mediatek.com/mcs/v2/devices/D9xzoYqI/datachannels/Temperature/datapoints.csv",
        "tls": "",
        "persist": false,
        "proxy": "",
        "authType": "",
        "x": 460,
        "y": 240,
        "wires": [
            [
                "c8f36df7.eac8c",
                "adcc828d.bb065"
            ]
        ]
    },
    {
        "id": "c8f36df7.eac8c",
        "type": "http response",
        "z": "f479beee.d423a",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 670,
        "y": 140,
        "wires": []
    },
    {
        "id": "adcc828d.bb065",
        "type": "debug",
        "z": "f479beee.d423a",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 700,
        "y": 360,
        "wires": []
    }
]
