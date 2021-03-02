# SPDX-FileCopyrightText: 2020 Intel Corporation
#
# SPDX-License-Identifier: MIT

import argparse
import subprocess

args = None


def shell(cmd, check=True, capture_output=False, modify=False):
    if modify or args.verbose > 1:
        print(cmd)
    if modify and args.dry_run:
        return
    return subprocess.run(
        cmd, shell=True, check=check, capture_output=capture_output
    )


def output_to_list(output):
    return output.strip().decode('utf-8').split('\n')


def oneapi_packages():
    res = shell('spack list | grep intel-oneapi', capture_output=True)
    return output_to_list(res.stdout)


def installed_oneapi_packages():
    res = shell(
        'spack find | grep intel-oneapi', check=False, capture_output=True
    )
    return output_to_list(res.stdout)


def uninstall():
    shell(
        'spack uninstall --all --dependents -y '
        f'{" ".join(installed_oneapi_packages())}',
        modify=True,
    )


def install():
    shell(f'spack install {" ".join(oneapi_packages())}', modify=True)


def list():
    if args.line:
        print(' '.join(oneapi_packages()))
    else:
        shell('spack list | grep intel-oneapi')


def find():
    shell('spack find | grep intel-oneapi', check=False)


def compiler_add():
    shell('spack install intel-oneapi-compilers', modify=True)
    shell('spack compiler rm intel', check=False, modify=True)
    shell('spack compiler rm oneapi', check=False, modify=True)
    for dir in [
        'compiler/latest/linux/bin',
        'compiler/latest/linux/bin/intel64',
    ]:
        shell(
            f'spack compiler add '
            f'`spack location -i intel-oneapi-compilers`/{dir}',
            modify=True,
        )
    # below will error out if not installed
    shell('spack compilers | grep "oneapi@"', modify=True)
    shell('spack compilers | grep "intel@"', modify=True)


def main():
    global args

    parser = argparse.ArgumentParser(description='spack oneapi package tester')
    parser.add_argument(
        '--verbose', type=int, default=1, help='Informational messages'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        default=False,
        help='do not perform commands that modify the system',
    )
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    uninstall_parser = subparsers.add_parser(
        'uninstall', help='uninstall all oneapi packages'
    )
    uninstall_parser.set_defaults(func=uninstall)

    install_parser = subparsers.add_parser(
        'install', help='install all oneapi packages'
    )
    install_parser.set_defaults(func=install)

    find_parser = subparsers.add_parser(
        'find', help='list installed oneapi packages'
    )
    find_parser.set_defaults(func=find)

    list_parser = subparsers.add_parser(
        'list', help='list all oneapi packages'
    )
    list_parser.add_argument(
        '--line',
        action='store_true',
        default=False,
        help='display all components on a single line',
    )
    list_parser.set_defaults(func=list)

    list_parser = subparsers.add_parser(
        'compiler-add', help='add oneapi compilers to compilers.yaml'
    )
    list_parser.set_defaults(func=compiler_add)

    args = parser.parse_args()
    args.func()


main()
