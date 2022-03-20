import collections

 
 
def solution(dimensions, your_position, trainer_position, distance):
    w = dimensions[0]
    h = dimensions[1]
 
    sx, sy = your_position
    tx, ty = trainer_position
    td = get_distance(your_position, trainer_position)
 
    targets = set()

    self_directions, self_dict = get_directions(dimensions, your_position, your_position, distance)
    tl_directions, tl_dict = get_directions(dimensions, your_position, [0, h], distance)
    tr_directions, tr_dict = get_directions(dimensions, your_position, [w, h], distance)
    bl_directions, bl_dict = get_directions(dimensions, your_position, [0, 0], distance)
    br_directions, br_dict = get_directions(dimensions, your_position, [w, 0], distance)

    target_directions, target_dict = get_directions(
        dimensions, your_position, trainer_position, distance
    )
    deny_set = self_directions.union(tl_directions.union(tr_directions.union(bl_directions.union(br_directions))))
    deny_dict = collections.defaultdict(int)
    result = set()
    for dir in target_directions:
        if (dir not in deny_set):
            result.add(dir)
        else:
            add_target = True
            if (dir in self_dict and self_dict[dir] < target_dict[dir]):
                add_target = False
            if (dir in tl_dict and tl_dict[dir] < target_dict[dir]):
                add_target = False
            if (dir in tr_dict and tr_dict[dir] < target_dict[dir]):
                add_target = False
            if (dir in bl_dict and bl_dict[dir] < target_dict[dir]):
                add_target = False
            if (dir in br_dict and br_dict[dir] < target_dict[dir]):
                add_target = False
            if (add_target):
                result.add(dir)

                    

    return len(result)
 
 
# def get_all_viable_locations(dimensions, your_position, trainer_position, distance):
def get_directions(dimensions, your_position, trainer_position, distance):
    distance_dict = collections.defaultdict(int)
    res = set()
    tx, ty = trainer_position
    width, height = dimensions
    width_multiplier = 0
    while True:
        num_added_at_this_width = 0
        # print("====== width", width_multiplier)
        height_multiplier = 0
        while True:
            # print("       height", height_multiplier)
 
            num_added = 0
            new_locations = [
                [
                    2 * width_multiplier * width + tx,
                    2 * height_multiplier * height + ty,
                ],
                [
                    2 * width_multiplier * width - tx,
                    2 * height_multiplier * height + ty,
                ],
                [
                    -(2 * width_multiplier * width + tx),
                    2 * height_multiplier * height + ty,
                ],
                [
                    -(2 * width_multiplier * width - tx),
                    2 * height_multiplier * height + ty,
                ],
                [
                    2 * width_multiplier * width + tx,
                    -(2 * height_multiplier * height + ty),
                ],
                [
                    2 * width_multiplier * width - tx,
                    -(2 * height_multiplier * height + ty),
                ],
                [
                    -(2 * width_multiplier * width + tx),
                    -(2 * height_multiplier * height + ty),
                ],
                [
                    -(2 * width_multiplier * width - tx),
                    -(2 * height_multiplier * height + ty),
                ],
                [
                    2 * width_multiplier * width + tx,
                    2 * height_multiplier * height - ty,
                ],
                [
                    2 * width_multiplier * width - tx,
                    2 * height_multiplier * height - ty,
                ],
                [
                    -(2 * width_multiplier * width + tx),
                    2 * height_multiplier * height - ty,
                ],
                [
                    -(2 * width_multiplier * width - tx),
                    2 * height_multiplier * height - ty,
                ],
                [
                    2 * width_multiplier * width + tx,
                    -(2 * height_multiplier * height - ty),
                ],
                [
                    2 * width_multiplier * width - tx,
                    -(2 * height_multiplier * height - ty),
                ],
                [
                    -(2 * width_multiplier * width + tx),
                    -(2 * height_multiplier * height - ty),
                ],
                [
                    -(2 * width_multiplier * width - tx),
                    -(2 * height_multiplier * height - ty),
                ],
            ]
            for new_tx, new_ty in new_locations:
                # print(new_tx, new_ty)
                new_dist = get_distance(your_position, [new_tx, new_ty])
                candidate_loc = (new_tx, new_ty, new_dist)
                relative_vector = (new_tx - your_position[0], new_ty - your_position[1])
                
                if new_dist != 0:
                    relative_vector = (
                        round(relative_vector[0] / new_dist, 8),
                        round(relative_vector[1] / new_dist, 8),
                    )
                    
                if new_dist <= distance and relative_vector not in res:
                    # print(str(new_tx) + ", " + str(new_ty) + ", " + str(relative_vector))
                    if (distance_dict[relative_vector] != 0):
                        distance_dict[relative_vector] = min(distance_dict[relative_vector], new_dist)
                    else:
                        distance_dict[relative_vector] = new_dist
                    res.add(relative_vector)
                    num_added += 1
                    num_added_at_this_width += 1
            if num_added == 0:
                break
            height_multiplier += 1
 
        if num_added_at_this_width == 0:
            break
        width_multiplier += 1
    return res, distance_dict
 
 
def get_distance(a, b):
    return ((a[1] - b[1]) ** 2 + (a[0] - b[0]) ** 2) ** 0.5