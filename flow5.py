[
    {
        "id": "7cecdba3.8a5dd4",
        "type": "tab",
        "label": "流程5",
        "disabled": false,
        "info": ""
    },
    {
        "id": "9d624d2a.06671",
        "type": "http in",
        "z": "7cecdba3.8a5dd4",
        "name": "Set GPIO5",
        "url": "/setgpio5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 130,
        "y": 200,
        "wires": [
            [
                "3ba6bbd9.f9e304",
                "475e2817.80ddc8"
            ]
        ]
    },
    {
        "id": "3ba6bbd9.f9e304",
        "type": "function",
        "z": "7cecdba3.8a5dd4",
        "name": "Set to 1",
        "func": "msg.payload = 1;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 340,
        "y": 260,
        "wires": [
            [
                "a3f815be.0f8f98"
            ]
        ]
    },
    {
        "id": "a3f815be.0f8f98",
        "type": "rpi-gpio out",
        "z": "7cecdba3.8a5dd4",
        "name": "",
        "pin": "29",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 700,
        "y": 300,
        "wires": []
    },
    {
        "id": "475e2817.80ddc8",
        "type": "function",
        "z": "7cecdba3.8a5dd4",
        "name": "Return status",
        "func": "msg.payload = \"GPIO set to HIGH\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 370,
        "y": 160,
        "wires": [
            [
                "48ae85aa.9aac7c",
                "866f50fb.02bf8"
            ]
        ]
    },
    {
        "id": "866f50fb.02bf8",
        "type": "debug",
        "z": "7cecdba3.8a5dd4",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 710,
        "y": 380,
        "wires": []
    },
    {
        "id": "48ae85aa.9aac7c",
        "type": "http response",
        "z": "7cecdba3.8a5dd4",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 630,
        "y": 160,
        "wires": []
    },
    {
        "id": "5b9024ef.39c58c",
        "type": "http in",
        "z": "7cecdba3.8a5dd4",
        "name": "Clear GPIO",
        "url": "/clear5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 140,
        "y": 440,
        "wires": [
            [
                "48d165d9.a77a4c",
                "1e4a72ae.13652d"
            ]
        ]
    },
    {
        "id": "48d165d9.a77a4c",
        "type": "function",
        "z": "7cecdba3.8a5dd4",
        "name": "Clear to 0",
        "func": "msg.payload = 0;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 380,
        "y": 440,
        "wires": [
            [
                "a3f815be.0f8f98"
            ]
        ]
    },
    {
        "id": "1e4a72ae.13652d",
        "type": "function",
        "z": "7cecdba3.8a5dd4",
        "name": "Return status",
        "func": "msg.payload = \"GPIO set to LOW\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 400,
        "y": 500,
        "wires": [
            [
                "48ae85aa.9aac7c",
                "866f50fb.02bf8"
            ]
        ]
    }
]
