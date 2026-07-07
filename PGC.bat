@echo off

set /p git_repo="Enter the repository name (without the .git): "
git remote set-url origin git@github.com:Kaua-da-Silva-Padin/%git_repo%.git
set /p current_branch="Enter the current branch: "
git push -u origin %current_branch%

echo "Your problem should be solved now, thanks for using P.G.C (Punch Git Cat)!"
pause
