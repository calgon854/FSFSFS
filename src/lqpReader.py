import re

def parseLQP(path: str) -> list[str]:
    with open(path, "r", encoding="latin-1") as file:
        file_content = file.read()
        segments = file_content.split("|=====================================================================================================|")
        
    return segments


def get_resections(segments: list[str]) -> list[str]:
    setups = []

    for segment in segments:
        if "Methode Freie Stationierung" in segment:
            setups.append(segment)
    return setups

# def process_resections(setups: list[str]):
#     entries = []

#     for setup in setups:
#         entry = setup.replace("\n", "").split("|-----------------------------------------------------------------------------------------------------|")
#         for point in entry:
#             setup_dict = dict()
#             if "St " in point:
#                 parts = point.split(" ")
#                 setup_dict.update({"name": parts[1]})

#             if "Pt " in point:
#                 pass
#         entries.append(setup_dict)


#     return entries

def process_resections(setups: list[str]) -> list[dict[str, any]]:
    entries = []

    for setup in setups:
        entry = setup.replace("\n", "").split("|-----------------------------------------------------------------------------------------------------|")
        anschluesse = []
        for point in entry:
            setup_dict = dict()
            if "St " in point:
                parts = re.split(r'\s+', point)  # Split after one ore more spaces " "
                pt_name = parts[1]
                IH = float(parts[4])
                easting = float(parts[6])
                northing = float(parts[8])
                height = float(parts[10].replace("|", ""))
                setup_dict.update({
                    "name": pt_name,
                    "IH": IH,
                    "O": easting,
                    "N": northing,
                    "H": height
                                  })

            if "Pt " in point:
                parts = re.split(r'\s+', point)
                pt_name = parts[1]
                easting = float(parts[6])
                northing = float(parts[8])
                height = float(parts[10].replace("|", ""))

                reflector_height = float(parts[12])
                diagonal_distance = float(parts[14])
                horizontal_distance = float(parts[22])
                horizontal_dir = float(parts[16])
                vertical_angle = float(parts[18].replace("|", ""))

                anschluesse.append(
                    {
                        "name": pt_name,
                        "O": easting,
                        "N": northing,
                        "H": height,
                        "RH": reflector_height,
                        "SD": diagonal_distance,
                        "HD": horizontal_distance,
                        "HZ": horizontal_dir,
                        "V": vertical_angle
                    }
                    )

            setup_dict.update({"anschluesse": anschluesse})
                
        entries.append(setup_dict)

    return entries
