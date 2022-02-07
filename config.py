import constants

config = {

    "print_to_txt": True,

    "coins": {
        "btc": {
            "minor_timeframe": "1h",
            "major_timeframe": "12h",
            "timeframe_continuity": False,
            "minimum_reward_to_risk": 0.75, 
        },
        "eth": {
            "minor_timeframe": "30m",
            "major_timeframe": "6h",
            "timeframe_continuity": False,
            "minimum_reward_to_risk": 1, 
        },
        "bnb": {
            "minor_timeframe": "2h",
            "major_timeframe": "1d",
            "timeframe_continuity": False,
            "minimum_reward_to_risk": 0.8, 
        }
    },

    "scan_for": {
        "PMG_6": True,
        "PMG_5": True,
        "222_Reversal": True,
        "212_Reversal": True,
        "312_Reversal": True,
        "322_Reversal": True
    },

    # Unlikely that you will need to configure anything below here
    # Unless you want to add your own setups

    "setups_configuration": {
        "PMG_6": [
            {
                "desc": "Pivot MG 6-2d Reversal",
                "setup": [("2d", constants.RED,), ("2d", constants.RED,), ("2d", constants.RED,),
                          ("2d", constants.RED,), ("2d", constants.RED,), ("2d", constants.RED,)],
                "active_kline": "1",
                "sentiment": constants.BULLISH,
                "trigger": (5, "o",),
                "target": (0, "o",),
                "stop": (5, "c"),
                "major_triggered": "2u"
            },
            {
                "desc": "Pivot MG 6-2u Reversal",
                "setup": [("2u", constants.GREEN,), ("2u", constants.GREEN,), ("2u", constants.GREEN,),
                          ("2u", constants.GREEN,), ("2u", constants.GREEN,), ("2u", constants.GREEN,)],
                "active_kline": "1",
                "sentiment": constants.BEARISH,
                "trigger": (5, "o",),
                "target": (0, "o",),
                "stop": (5, "c"),
                "major_triggered": "2d"
            }
        ],
        "PMG_5": [
            {
                "desc": "Pivot MG 5-2d Reversal",
                "setup": [("2d", constants.RED,), ("2d", constants.RED,), ("2d", constants.RED,),
                          ("2d", constants.RED,), ("2d", constants.RED,)],
                "active_kline": "1",
                "sentiment": constants.BULLISH,
                "trigger": (4, "o",),
                "target": (0, "o",),
                "stop": (4, "c"),
                "major_triggered": "2u"
            },
            {
                "desc": "Pivot MG 5-2u Reversal",
                "setup": [("2u", constants.GREEN,), ("2u", constants.GREEN,), ("2u", constants.GREEN,),
                          ("2u", constants.GREEN,), ("2u", constants.GREEN,)],
                "active_kline": "1",
                "sentiment": constants.BEARISH,
                "trigger": (4, "o",),
                "target": (0, "o",),
                "stop": (4, "c"),
                "major_triggered": "2d"
            }
        ],
        "222_Reversal": [
            {
                "desc": "222 Reversal",
                "setup": [("2d", constants.RED,), ("2d", constants.RED,)],
                "active_kline": "1",
                "sentiment": constants.BULLISH,
                "trigger": (1, "o",),
                "target": (0, "o",),
                "stop": (1, "c"),
                "major_triggered": "2u"
            },
            {
                "desc": "222 Reversal",
                "setup": [("2u", constants.GREEN,), ("2u", constants.GREEN,)],
                "active_kline": "1",
                "sentiment": constants.BEARISH,
                "trigger": (1, "o",),
                "target": (0, "o",),
                "stop": (1, "c"),
                "major_triggered": "2d"
            },
        ],
        "212_Reversal": [
            {
                "desc": "212 Reversal",
                "setup": [("2d", constants.RED,), ("1", constants.RED,)],
                "active_kline": "1",
                "sentiment": constants.BULLISH,
                "trigger": (1, "o",),
                "target": (0, "o",),
                "stop": (1, "c"),
                "major_triggered": "2u"
            },
            {
                "desc": "212 Reversal",
                "setup": [("2u", constants.GREEN,), ("1", constants.GREEN,)],
                "active_kline": "1",
                "sentiment": constants.BEARISH,
                "trigger": (1, "o",),
                "target": (0, "o",),
                "stop": (1, "c"),
                "major_triggered": "2d"
            },
        ],
        "312_Reversal": [
            {
                "desc": "312 Reversal",
                "setup": [("3", constants.RED,), ("1", constants.RED,)],
                "active_kline": "1",
                "sentiment": constants.BULLISH,
                "trigger": (1, "o",),
                "target": (0, "o",),
                "stop": (1, "c"),
                "major_triggered": "2u"
            },
            {
                "desc": "312 Reversal",
                "setup": [("3", constants.GREEN,), ("1", constants.GREEN,)],
                "active_kline": "1",
                "sentiment": constants.BEARISH,
                "trigger": (1, "o",),
                "target": (0, "o",),
                "stop": (1, "c"),
                "major_triggered": "2d"
            },
        ],
        "322_Reversal": [
            {
                "desc": "322 Reversal",
                "setup": [("3", constants.RED,), ("2d", constants.RED,)],
                "active_kline": "1",
                "sentiment": constants.BULLISH,
                "trigger": (1, "o",),
                "target": (0, "o",),
                "stop": (1, "c"),
                "major_triggered": "2u"
            },
            {
                "desc": "322 Reversal",
                "setup": [("3", constants.GREEN,), ("2u", constants.GREEN,)],
                "active_kline": "1",
                "sentiment": constants.BEARISH,
                "trigger": (1, "o",),
                "target": (0, "o",),
                "stop": (1, "c"),
                "major_triggered": "2d"
            },
        ]
    }
}