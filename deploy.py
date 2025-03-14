import argparse, subprocess
import shutil
import os


def main():
    parser = argparse.ArgumentParser(description='commit and deploy script.')
    parser.add_argument("--days-ago", help="how many days ago the commit happens")
    parser.add_argument("--commit-message", help="commit message", required=True)
    parser.add_argument("--gh-page-repo", help="path to github pages repository", required=True)
    args = parser.parse_args()

    execute_command(["git", "add", "."])
    if args.days_ago:
        execute_command(["git", "commit", f'--date="{args.days_ago} day ago"', "-m", args.commit_message])
    else:
        execute_command(["git", "commit", "-m", args.commit_message])

    execute_command(["git", "push", "origin", "main"])

    execute_command(["gatsby", "build", "--prefix-paths"])

    shutil.copytree(get_gh_pages_artifacts_dir(), args.gh_page_repo, dirs_exist_ok=True)

    execute_command(["git", "add", "."],
                    cwd=args.gh_page_repo,
                    capture_output=True)

    execute_command(["git", "commit", "-m", args.commit_message],
                    cwd=args.gh_page_repo,
                    capture_output=True)

    execute_command(["git", "push", "origin", "main"],
                    cwd=args.gh_page_repo,
                    capture_output=True)


def execute_command(command_args, cwd: str = None, capture_output: bool = False):
    output = subprocess.run(command_args,
                            cwd=cwd,
                            capture_output=capture_output)
    print(output)


def get_gh_pages_artifacts_dir():
    gh_pages_artifacts_dir = os.path.join(os.getcwd(), "public")
    return gh_pages_artifacts_dir


if __name__ == "__main__":
    main()
