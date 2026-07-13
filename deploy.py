import argparse, subprocess
import shutil
import os
import sys


def main():
    parser = argparse.ArgumentParser(description='commit and deploy script.')
    parser.add_argument("--days-ago", help="how many days ago the commit happens")
    parser.add_argument("--commit-message", help="commit message", required=True)
    parser.add_argument("--gh-page-repo", help="path to github pages repository", required=True)
    args = parser.parse_args()

    # Clean up any orphaned gatsby worker processes left behind by a previously
    # interrupted build. They survive a Ctrl-C of this script (reparented to
    # init/systemd) and can wedge or slow the next build.
    kill_stray_gatsby_workers()

    execute_command(["git", "add", "."])
    if args.days_ago:
        execute_command(["git", "commit", f"--date={args.days_ago} days ago", "-m", args.commit_message], check=False)
    else:
        execute_command(["git", "commit", "-m", args.commit_message], check=False)

    execute_command(["git", "push", "origin", "main"])

    # gatsby build spends a long, silent stretch in image processing
    # (gatsby-plugin-sharp). Stream its output so progress is visible, and give
    # it a generous timeout so a genuine stall aborts loudly instead of hanging
    # forever like the un-guarded call used to.
    run_checked(["gatsby", "build", "--prefix-paths", "--verbose"], timeout=1800)

    execute_command(["git", "pull"],
                    cwd=args.gh_page_repo)

    # copytree only overwrites/adds; it never removes files that no longer exist
    # in the fresh build. Wipe the gh-pages working tree first (keeping .git) so
    # deleted/renamed pages and orphaned linked-file copies don't linger on the
    # live site.
    clean_gh_pages_repo(args.gh_page_repo)

    shutil.copytree(get_gh_pages_artifacts_dir(), args.gh_page_repo, dirs_exist_ok=True)

    execute_command(["git", "add", "."],
                    cwd=args.gh_page_repo)

    execute_command(["git", "commit", "-m", args.commit_message],
                    cwd=args.gh_page_repo, check=False)

    execute_command(["git", "push", "origin", "main"],
                    cwd=args.gh_page_repo)


def execute_command(command_args, cwd: str = None, check: bool = True):
    output = subprocess.run(command_args,
                            cwd=cwd,
                            capture_output=True,
                            text=True)
    print(output)
    if check and output.returncode != 0:
        sys.exit(f"command failed (exit {output.returncode}): {' '.join(command_args)}")
    return output


def run_checked(command_args, cwd: str = None, timeout: int = None):
    # Inherit stdio so long-running builds show live progress, and enforce a
    # timeout so a hung build is killed instead of blocking forever.
    try:
        result = subprocess.run(command_args, cwd=cwd, timeout=timeout)
    except subprocess.TimeoutExpired:
        kill_stray_gatsby_workers()
        sys.exit(f"command timed out after {timeout}s: {' '.join(command_args)}")
    if result.returncode != 0:
        sys.exit(f"command failed (exit {result.returncode}): {' '.join(command_args)}")
    return result


def kill_stray_gatsby_workers():
    subprocess.run(["pkill", "-f", "gatsby-worker"])


def clean_gh_pages_repo(repo_dir):
    # Remove every entry in the gh-pages repo except the .git directory, so the
    # subsequent copytree yields an exact mirror of the fresh build. `git add .`
    # later stages these deletions.
    for entry in os.listdir(repo_dir):
        if entry == ".git":
            continue
        path = os.path.join(repo_dir, entry)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


def get_gh_pages_artifacts_dir():
    gh_pages_artifacts_dir = os.path.join(os.getcwd(), "public")
    return gh_pages_artifacts_dir


if __name__ == "__main__":
    main()
