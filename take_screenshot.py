import os
import subprocess

def take_screenshot(*args, **kwargs):

    img_name = kwargs.get('img_name', None) or 'unknownimage'
    img_ext = kwargs.get('img_ext', None) or 'png'
    default_save_path = os.path.join('/tmp', img_name + '.' + img_ext)
    save_path = kwargs.get('save_path', None) or default_save_path

    width = kwargs.get('width', None) or 800
    height = kwargs.get('height', None) or 600

    default_user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'

    default_user_agent = 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7'

    user_agent = kwargs.get('user_agent', None) or default_user_agent

    url = kwargs.get('url')

    phantomscript = os.path.join(os.path.dirname(__file__), 'take_screenshot.js')

    size_str = '{w}px*{h}px'.format(w=width, h=height)

    cmd_args = [
        'phantomjs',
        '--ssl-protocol=any',
        phantomscript,
        url,
        save_path,
        size_str,
        user_agent
    ]

    output = subprocess.Popen(cmd_args,
                              stdout=subprocess.PIPE).communicate()[0]

    print output

    return save_path


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description='Save a screenshot.')
    parser.add_argument('url', help='url to screenshot')
    parser.add_argument('-width', help='width of the viewport', type=int)
    parser.add_argument('-height', help='width of the viewport', type=int)

    args = parser.parse_args()

    take_screenshot(**vars(args))