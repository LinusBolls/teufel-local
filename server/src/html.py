from speaker_controls import speaker_controls

def get_index_html():
    with open('../static/index.html', 'r') as f:
        html_content = f.read()

        updated_html_content = html_content.replace(
            'const INITIAL_DATA = null;',
            f'const INITIAL_DATA = {speaker_controls};'
        )
        return updated_html_content