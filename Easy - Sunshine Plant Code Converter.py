def plant_decision(plant_id):
    if bin(plant_id)[-1] == '0':
        return "skip"
    else:
        return "plant"
