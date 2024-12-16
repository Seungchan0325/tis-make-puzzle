
def create(path: str, name: str, description: list[str], streams: list[list], layout: list):
    with open("puzzles/" + path, "w") as f:
        f.write(f"@name\n{name}\n\n")

        f.write("@description\n")
        for line in description:
            f.write(line + "\n")
        f.write("\n")

        for stream in streams:
            f.write("@stream\n")
            f.write(stream[0] + "\n")
            f.write(stream[1] + "\n")
            f.write(f"{stream[2]}\n")
            for data in stream[3]:
                f.write(f"{data}\n")
            f.write("\n")
        
        f.write("@layout\n")
        for tile in layout:
            f.write(tile + "\n")
        f.write("\n")