import subprocess
from pathlib import Path, PureWindowsPath


def set_cmd(
        path_holos_cli: Path,
        path_dir_farms: Path,
        path_dir_outputs: Path = None,
        name_farm_json: str = None,
        name_dir_farms_json: str = None,
        name_settings: str = None,
        id_slc_polygon: int = None,
) -> list[str]:
    cmd = [
        'cmd', '/c',
        str(PureWindowsPath(path_holos_cli)),
        str(PureWindowsPath(path_dir_farms)),
        '-u',
        'metric'
    ]

    if path_dir_outputs is not None:
        cmd += ['-o', path_dir_outputs]

    if name_farm_json is not None:
        cmd += ['-i', name_farm_json]

    if name_dir_farms_json is not None:
        cmd += ['-f', name_dir_farms_json]

    if name_settings is not None:
        if any([name_farm_json is not None, name_dir_farms_json is not None]):
            cmd += ['-s', name_settings]

    if id_slc_polygon is not None:
        cmd += ['-p', str(int(id_slc_polygon))]

    return cmd


def launch_holos(
        path_holos_cli: Path,
        path_dir_farms: Path,
        path_dir_outputs: Path = None,
        name_farm_json: str = None,
        name_dir_farms_json: str = None,
        name_settings: str = None,
        id_slc_polygon: int = None
) -> None:
    cmd = set_cmd(
        path_holos_cli=path_holos_cli,
        path_dir_farms=path_dir_farms,
        path_dir_outputs=path_dir_outputs,
        name_farm_json=name_farm_json,
        name_dir_farms_json=name_dir_farms_json,
        name_settings=name_settings,
        id_slc_polygon=id_slc_polygon
    )

    process = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True)
    process.communicate('\n')
    pass
