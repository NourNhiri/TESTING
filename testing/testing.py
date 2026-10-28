list={
    "children": [
        {"children": [], "value": 74},
        {
            "children": [
                {
                    "children": [
                        {"children": [], "value": 44},
                        {"children": [], "value": 35},
                        {"children": [], "value": 67},
                        {"children": [], "value": 66},
                    ],
                    "value": 60,
                },
                {
                    "children": [
                        {"children": [], "value": 21},
                        {"children": [], "value": 47},
                        {"children": [], "value": 71},
                    ],
                    "value": 36,
                },
                {
                    "children": [
                        {"children": [], "value": 25},
                        {"children": [], "value": 18},
                    ],
                    "value": 24,
                },
            ],
            "value": 89,
        },
        {
            "children": [
                {
                    "children": [
                        {"children": [], "value": 75},
                        {"children": [], "value": 73},
                    ],
                    "value": 36,
                },
                {
                    "children": [
                        {"children": [], "value": 55},
                        {"children": [], "value": 9},
                    ],
                    "value": 78,
                },
            ],
            "value": 80,
        },
        {
            "children": [
                {
                    "children": [
                        {"children": [], "value": 35},
                        {"children": [], "value": 26},
                        {"children": [], "value": 100},
                        {"children": [], "value": 75},
                        {"children": [], "value": 45},
                    ],
                    "value": 78,
                },
                {
                    "children": [
                        {"children": [], "value": 41},
                        {"children": [], "value": 45},
                    ],
                    "value": 9,
                },
                {
                    "children": [
                        {"children": [], "value": 40},
                        {"children": [], "value": 28},
                    ],
                    "value": 12,
                },
            ],
            "value": 9,
        },
    ],
    "value": 55,
}
def zoek(list:dict,getal:int):
    for i,item in enumerate(list["children"]):
        if item["value"]==getal:
            return [i]
        answer=zoek(item,getal)
        if answer is not None:
            return [i]+answer


print(zoek(list,21))