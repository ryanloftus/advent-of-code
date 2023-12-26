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

def do_mapping(mapping, key_ranges):
    mapped_ranges = []
    for key_range in key_ranges:
        i = key_range[0]
        while i <= key_range[1]:
            max_unmatched = key_range[1]
            for m in mapping:
                dst_range_start = m[0]
                src_range_start = m[1]
                src_range_end = src_range_start + m[2] - 1
                if i >= src_range_start and i <= src_range_end:
                    mapped_range_start = dst_range_start + (i - src_range_start)
                    mapped_range_end = dst_range_start + min(key_range[1], src_range_end) - src_range_start
                    mapped_ranges.append((mapped_range_start, mapped_range_end))
                    i = min(key_range[1], src_range_end) + 1
                    max_unmatched = -1
                    break
                elif src_range_start > i and max_unmatched >= src_range_start:
                    max_unmatched = src_range_start-1
            if max_unmatched != -1:
                mapped_ranges.append((i, max_unmatched))
                i = max_unmatched + 1
    mapped_ranges.sort()
    i = 0
    while i < len(mapped_ranges) - 1:
        if mapped_ranges[i][1] >= mapped_ranges[i+1][1]:
            del mapped_ranges[i+1]
        elif mapped_ranges[i][1] >= mapped_ranges[i+1][0]:
            mapped_ranges[i] = (mapped_ranges[i][0], mapped_ranges[i+1][1])
            del mapped_ranges[i+1]
        else:
            i += 1
    return mapped_ranges

seed_nums = list(map(lambda x: int(x), lines[0][7:].split(" ")))
seed_ranges = []
for i in range(0, len(seed_nums), 2):
    range_start = seed_nums[i]
    range_end = seed_nums[i] + seed_nums[i+1] - 1
    seed_ranges.append((range_start, range_end))
seed_ranges.sort()
seed_to_soil = get_mapping("seed-to-soil map:")
soil_to_fertilizer = get_mapping("soil-to-fertilizer map:")
fertilizer_to_water = get_mapping("fertilizer-to-water map:")
water_to_light = get_mapping("water-to-light map:")
light_to_temperature = get_mapping("light-to-temperature map:")
temperature_to_humidity = get_mapping("temperature-to-humidity map:")
humidity_to_location = get_mapping("humidity-to-location map:")

soil_ranges = do_mapping(seed_to_soil, seed_ranges)
fertilizer_ranges = do_mapping(soil_to_fertilizer, soil_ranges)
water_ranges = do_mapping(fertilizer_to_water, fertilizer_ranges)
light_ranges = do_mapping(water_to_light, water_ranges)
temperature_ranges = do_mapping(light_to_temperature, light_ranges)
humidity_ranges = do_mapping(temperature_to_humidity, temperature_ranges)
location_ranges = do_mapping(humidity_to_location, humidity_ranges)

closest_location = min(map(lambda x: x[0], location_ranges))
print(closest_location)
