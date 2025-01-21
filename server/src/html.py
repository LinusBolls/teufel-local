from src.speaker_controls import speaker_controls

def get_parent_dir(filepath):
    parts = filepath.split("/")
    return "/".join(parts[:-2]) if len(parts) > 1 else "/"

server_dir = get_parent_dir(__file__)

def get_index_html():
    with open(server_dir + '/static/index.html', 'r') as f:
        html_content = f.read()

        updated_html_content = html_content.replace(
            'const INITIAL_DATA = null;',
            f'const INITIAL_DATA = {speaker_controls};'
        )
        return updated_html_content