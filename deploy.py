import argparse, subprocess

def main():
    parser = argparse.ArgumentParser(description='commit and deploy script.')
    parser.add_argument("--days-ago", help="how many days ago the commit happens")
    parser.add_argument("--commit-message", help="commit message", required=True)
    parser.add_argument("--gh-page-repo", help="path to github pages repository", required=True)
    args = parser.parse_args()

    subprocess.run(["git", "add", "content"])
    if args.days_ago:
       subprocess.run(["git", "commit", f'--date="{args.days_ago} day ago"', "-m", args.commit_message])
    else:
       subprocess.run(["git", "commit", "-m", args.commit_message])

    subprocess.run(["git", "push", "origin", "main"])

    subprocess.run(["cp", "-r", "public/*", args.gh_page_repo])
    subprocess.run(["git", "commit", "-m", args.commit_message], cwd=args.gh_page_repo)
    subprocess.run(["git", "push", "origin", "main"], cwd=args.gh_page_repo)


if __name__== "__main__":
  main()
