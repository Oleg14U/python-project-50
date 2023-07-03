from gendiff.formaters.stylish import render_stylish
from gendiff.formaters.plain import render_plain
from gendiff.formaters.json import render_json


def get_formatter(formatter):
    if formatter == 'stylish':
        return render_stylish
    if formatter == 'plain':
        return render_plain
    if formatter == 'json':
        return render_json
    raise ValueError(f"Unrecognized formatter: {formatter}")