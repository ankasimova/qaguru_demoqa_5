def resource(path):
    import qaguru_demoqa_5
    from pathlib import Path
    return str(Path(qaguru_demoqa_5.__file__).parent.parent.joinpath(f'picture/{path}'))
