file = open("input.txt", "r")
lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
file.close()

def get_mapping(name):
    i = lines.index(name) + 1
    mapping = []
    while i < len(lines) and lines[i] != "":
        mapping.append(list(map(lambda x: int(x), lines[i].split(" "))))
        i += 1
    return mapping

def do_mapping(mapping, key):
    for m in mapping:
        dst_range_start = m[0]
        src_range_start = m[1]
        range_len = m[2]
        if key >= src_range_start and key < src_range_start + range_len:
            return dst_range_start + (key - src_range_start)
    return key

seeds = list(map(lambda x: int(x), lines[0][7:].split(" ")))
seed_to_soil = get_mapping("seed-to-soil map:")
soil_to_fertilizer = get_mapping("soil-to-fertilizer map:")
fertilizer_to_water = get_mapping("fertilizer-to-water map:")
water_to_light = get_mapping("water-to-light map:")
light_to_temperature = get_mapping("light-to-temperature map:")
temperature_to_humidity = get_mapping("temperature-to-humidity map:")
humidity_to_location = get_mapping("humidity-to-location map:")

seed_locations = []
for seed in seeds:
    soil = do_mapping(seed_to_soil, seed)
    fertilizer = do_mapping(soil_to_fertilizer, soil)
    water = do_mapping(fertilizer_to_water, fertilizer)
    light = do_mapping(water_to_light, water)
    temperature = do_mapping(light_to_temperature, light)
    humidity = do_mapping(temperature_to_humidity, temperature)
    location = do_mapping(humidity_to_location, humidity)
    seed_locations.append(location)

closest_location = min(seed_locations)
print(closest_location)
