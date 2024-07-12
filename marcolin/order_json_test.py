import json
from bson import ObjectId

def generate_plottable_object(fasi):
    base_element = {
        "positionDx": {"$numberDouble": "0.0"},
        "positionDy": {"$numberDouble": "105.30044993252457"},
        "size.width": {"$numberDouble": "100.0"},
        "size.height": {"$numberDouble": "50.0"},
        "textColor": {"$numberLong": "4278190080"},
        "fontFamily": None,
        "textSize": {"$numberDouble": "12.0"},
        "textIsBold": False,
        "kind": {"$numberInt": "0"},
        "handlers": [
            {"$numberInt": "3"},
            {"$numberInt": "2"}
        ],
        "handlerSize": {"$numberDouble": "10.0"},
        "backgroundColor": {"$numberLong": "4294967295"},
        "borderColor": {"$numberLong": "4282589683"},
        "borderThickness": {"$numberDouble": "3.0"},
        "elevation": {"$numberDouble": "4.0"},
        "next": []
    }

    elements = []
    ids = []

    # Generate MongoDB ObjectIds
    for _ in range(len(fasi)):
        ids.append(str(ObjectId()))
        

    for i in range(len(fasi)):
        new_element = json.loads(json.dumps(base_element))  # deep copy of base_element
        new_element["positionDx"]["$numberDouble"] = str(i * 200.0)
        new_element["text"] = fasi[i]
        new_element["id"] = ids[i]

        if i < len(fasi) - 1:
            new_element["next"].append({
                "destElementId": ids[i + 1],
                "arrowParams": {
                    "thickness": {"$numberDouble": "1.7"},
                    "color": {"$numberLong": "4278190080"},
                    "startArrowPositionX": {"$numberDouble": "1.0"},
                    "startArrowPositionY": {"$numberDouble": "0.0"},
                    "endArrowPositionX": {"$numberDouble": "-1.0"},
                    "endArrowPositionY": {"$numberDouble": "0.0"}
                }
            })
        
        elements.append(new_element)

    plottable_object = {
        "_id": {"$oid": str(ObjectId())},
        "prodId": "redVent",
        "prodotto": "Ventilatori rossi",
        "descrizione": "Ventilatori grandi rossi",
        "famiglia": "Ventilatori",
        "dashboard": {"elements": elements},
        "fasi": {"$fasi" : fasi}
    }

    return plottable_object

def save_plottable_object_to_json(fasi, filename):
    plottable_object = generate_plottable_object(fasi)
    with open(filename, 'w') as json_file:
        json.dump(plottable_object, json_file, indent=4)

if __name__ == "__main__":
    fasi = ["Fase 1", "Fase 2", "Fase 3", "Mef","efua"]
    save_plottable_object_to_json(fasi, 'plottable_object.json')
