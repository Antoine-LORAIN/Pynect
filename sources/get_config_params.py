from configparser import ConfigParser

def get_colors(path):
    parser = create_parser(path)
    sections = parser.sections()
    sections.remove("UTILS")
    sections.remove("CUSTOMIZATION")
    colors = []
    for bindings in sections:
        new_pos = len(colors)
        colors.append([])
        binds = bindings.split(',')
        min = binds[0]
        max = binds[1]
        color = parser.options(bindings)[0]
        rgb_str = parser.get(bindings, color)
        rgb = rgb_str.split(',')
        rgb_tuple = [rgb[0], rgb[1], rgb[2]]
        colors[new_pos].append((min, max))
        colors[new_pos].append(rgb_tuple)
    return colors

def get_scale(path):
    parser = create_parser(path)
    return parser.get('UTILS', 'scale')

def get_window_title(path):
    parser = create_parser(path)
    return parser.get("CUSTOMIZATION", "window_title")


def create_parser(file):
    parser = ConfigParser()
    parser.read(file)
    return parser