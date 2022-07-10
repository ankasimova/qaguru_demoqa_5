from pathlib import Path

import qaguru_demoqa_5


def resourse(path):
    import qaguru_demoqa_5
    qaguru_demoqa_5.__file__
    from pathlib import Path
    return str(Path(qaguru_demoqa_5.__file__).parent.parent.joinpath(f'picture/{path}'))