# orig_grid = copy(grid)
seen_cheat = set()
seen_paths = {tuple(original_path)}
for cp in original_path:
    change_q = deque([(cp, [])])
    while True:
        (r, c), ch_path = change_q.popleft()
        if len(ch_path) == 3:
            break
        for dr, dc in DIRECTIONS:
            if not ch_path:
                if (pp := (r + dr, c + dc)) in grid and grid[pp] == "#":
                    change_q.append((pp, ch_path + [pp]))
            else:
                # end step must be on a "."
                if (pp := (r + dr, c + dc)) in grid and grid[pp] == ".":
                    change_q.append((pp, ch_path + [pp]))

    pairs = {tuple(ch_n[1][:2]) for ch_n in change_q}
    for pair in pairs:
        n1, n2 = pair
        if (cp, n2) in seen_cheat:
            continue
        grid[n1] = "."
        new_path_l, new_path = explore(grid, start_p, end_p, 0)
        new_path = type(new_path)
        if new_path_l < first_path_l and new_path not in seen_paths:
            print("saved", first_path_l - new_path_l, (cp, n2))
            seen_paths.add(new_path)
        grid[n1] = "#"
        seen_cheat.add((cp, n2))
