
def part1(file_name, days):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        ages = [int(entry) for entry in lines[0].strip().split(',')]
        fish_at_stage = [ages.count(i) for i in range(9)]
    print('Entrada: \n', ages)
    print('Fishes per day', fish_at_stage)

    for day in range(1, days + 1):
        expired_fish = fish_at_stage.pop(0)
        fish_at_stage[6] += expired_fish
        fish_at_stage.append(expired_fish)

    print(f"After {day} days: {sum(fish_at_stage)}")
part1('input6.txt', 256)