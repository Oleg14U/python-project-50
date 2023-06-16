from gendiff.formatters.json import render_json


def get_formatter(formater):
    if formater == 'json':
        return render_json
    raise ValueError(f"Unrecognized formater: {formater}")