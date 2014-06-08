import logging
import subprocess
import sys


def run_command(command, dry_run):
    logging.info('Running %s, output below' % command)
    if dry_run:
        return
    process = subprocess.Popen(command, shell=True,
        stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    try:
        stdout, stderr = process.communicate()
        if stdout:
            logging.info('stdout: %r', stdout)
        if process.returncode != 0:
            logging.error("non zero exit code (%d) when executing: %s ",
                process.returncode, command)
        if stderr:
            logging.error("stderr: %s", stderr)
    except:
        logging.critical('unknown error processing %s' % command)
        sys.exit(1)


def run_command_list(ordered_command_lists, dry_run):
    if dry_run:
        logging.warn('dry_run enabled')
    for command_list in ordered_command_lists:
        for command in command_list:
            run_command(command, dry_run)
