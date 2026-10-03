DSAI Mentorship — Git & GitHub Assignment

Introduction

This assignment is designed to give you hands-on practice with the basic Git and GitHub workflow, including:

Forking and cloning repositories

Creating and tracking files with Git

Using .gitignore

Creating and working with branches

Making commits and pushing changes

Creating and resolving merge conflicts

Understanding ours and theirs during conflict resolution

Rewriting Git history using git rebase

Removing an already-pushed commit

Understanding pull.rebase

Safely force-pushing rewritten history

Creating a Pull Request


You will work with the following repository:

Repository:
https://github.com/ShlokDivyam1109/DSAI-Mentorship-First-Repo

Throughout this assignment, replace <YOUR_NAME> with your actual name.


---

Task 1: Fork and Clone the Repository

First, fork the given repository to your own GitHub account.

After forking it, clone your fork, not the original repository, to your local machine.

Use

git clone <YOUR_FORK_URL>
cd DSAI-Mentorship-First-Repo

Verify that the repository was cloned correctly:

git remote -v

The origin remote should point to your fork.


---

Task 2: Create Your Personal Folder

Inside the repository, create a folder using your name.

The structure should look like:

DSAI-Mentorship-First-Repo/
└── <YOUR_NAME>/

All files belonging to your assignment must be placed inside this folder, except for the .gitignore file described later.


---

Task 3: Create the Python Program

Inside <YOUR_NAME>/, create:

<YOUR_NAME>/
└── main.py

The Python program must contain the following components.

1. A function to read secret.txt

Create a function that opens a file named:

secret.txt

The file must contain exactly:

Secret123

The function should read the password from the file and pass it to another function named:

check(password)

2. The check(password) function

Create the function:

def check(password):
    pass

Do not implement the password checking logic yet.

The function must initially contain exactly:

pass

You will modify this function later on the main and branch1 branches.

3. The main() function

Create:

def main():

main() must call the function responsible for reading the password from secret.txt.

4. Program entry point

At the very end of the Python file, include:

if __name__ == '__main__':
    main()

Do not omit this section.

At this point, the important part of your Python file should look approximately like:

def check(password):
    pass


---

Task 4: Create secret.txt

Inside your <YOUR_NAME> folder, create:

secret.txt

Its contents must be exactly:

Secret123

Your directory should now look approximately like:

DSAI-Mentorship-First-Repo/
└── <YOUR_NAME>/
    ├── main.py
    └── secret.txt


---

Task 5: Create the .gitignore

Create a .gitignore file outside your name folder, at the root of the repository.

The .gitignore must ignore:

secret.txt

This means that Git should not track the password file.

Your structure should now look like:

DSAI-Mentorship-First-Repo/
├── .gitignore
└── <YOUR_NAME>/
    ├── main.py
    └── secret.txt

Use

echo secret.txt >> .gitignore

Then check:

git status

secret.txt should not appear as a file to be committed.


---

Task 6: Commit and Push Your Initial Work

Add the required files to Git, commit them, and push them to your fork.

Use

git add .
git commit -m "Add initial password checker"
git push origin main

Check your GitHub repository and verify that:

Your <YOUR_NAME> folder exists.

Your Python file is present.

.gitignore is present.

secret.txt is not present on GitHub.



---

Task 7: Create branch1

Create a new branch named exactly:

branch1

Switch to it.

Use

git checkout -b branch1

Verify your current branch:

git branch

You should see something similar to:

* branch1
  main


---

Task 8: Modify the Password Checker on main

Now return to the main branch:

git checkout main

Modify the check(password) function.

It currently contains:

def check(password):
    pass

Change it to:

def check(password):
    return password == "Secret123"

Do not change the other required parts of the program.

The important change on main is therefore:

pass
↓
return password == "Secret123"

Commit this change:

git add .
git commit -m "Implement password checking"

Push it to GitHub:

git push origin main

At this point, main contains:

def check(password):
    return password == "Secret123"


---

Task 9: Make Different Changes in branch1

Now switch back to:

branch1

Use:

git checkout branch1

Remember that branch1 was created before the change made in Task 8.

Therefore, on branch1, check(password) should still contain:

def check(password):
    pass

Now make two changes on branch1.


---

Change 1: Change the Password Filename

Modify your Python program so that the filename being accessed changes from:

secret.txt

to:

password.txt

The filename must also be changed in .gitignore.

Therefore, .gitignore on branch1 must ignore:

password.txt

instead of:

secret.txt


---

Change 2: Change check(password)

Modify:

def check(password):
    pass

to:

def check(password):
    return True

Therefore, the two branches now contain different implementations.

main contains:

def check(password):
    return password == "Secret123"

branch1 contains:

def check(password):
    return True

This difference is intentional.

When branch1 is merged into main, Git will detect that both branches changed the same part of main.py differently, producing a merge conflict.

Commit the changes:

git add .
git commit -m "Change password file name and checker"

Push the branch:

git push origin branch1


---

Task 10: Merge branch1 into main

Now switch back to main:

git checkout main

Verify:

git branch

You should see:

* main
  branch1

Now merge:

git merge branch1

A merge conflict should occur because:

main changed check(password) to return password == "Secret123".

branch1 changed check(password) to return True.


You should see output similar to:

Auto-merging <YOUR_NAME>/main.py
CONFLICT (content): Merge conflict in <YOUR_NAME>/main.py
Automatic merge failed; fix conflicts and then commit the result.


---

Task 10.1: Check the Merge Conflict

Run:

git status

You should see something similar to:

both modified:   <YOUR_NAME>/main.py

This means Git could not automatically determine which version of the conflicting file should be retained.


---

Task 10.2: Open the Conflicted File

Open:

<YOUR_NAME>/main.py

You should see Git conflict markers similar to:

<<<<<<< HEAD
def check(password):
    return password == "Secret123"
=======
def check(password):
    return True
>>>>>>> branch1

The sections have the following meaning:

<<<<<<< HEAD

Everything between this marker and:

=======

is the version from the branch you currently have checked out.

In this case:

main

The section between:

=======

and:

>>>>>>> branch1

is the incoming version from:

branch1


---

Task 10.3: Accept the Incoming Changes

For this assignment, the branch1 version must prevail.

There are two ways to resolve the conflict.

Method 1: Resolve Manually

Replace the conflicting section with:

def check(password):
    return True

Make sure all Git conflict markers are removed:

<<<<<<<
=======
>>>>>>>

There must be no conflict markers left in the file.


---

Method 2: Accept branch1 Using Git

You can tell Git to use the incoming version directly.

Run:

git checkout --theirs <YOUR_NAME>/main.py

Here:

--theirs

means the version from the branch being merged into the current branch.

In this assignment:

theirs = branch1

So the conflicted main.py will be replaced with the version from branch1.

You can verify the result:

cat <YOUR_NAME>/main.py

The function should now contain:

def check(password):
    return True


---

Task 10.4: Stage the Resolved Conflict

After resolving the conflict:

git add .

Then check:

git status

Git should no longer report the file as an unresolved conflict.


---

Task 10.5: Complete the Merge

Complete the merge:

git commit

Git may open an editor containing a default merge commit message.

You can keep the default message and save/close the editor.

Alternatively:

git commit -m "Merge branch1 into main"

Then verify:

git status

The working tree should be clean.


---

Task 10.6: Verify the Merge

Check the history:

git log --oneline --graph --all

You should be able to see that the two branches were merged.

Also verify that main.py contains the branch1 version:

def check(password):
    return True

The filename should now be:

password.txt

and .gitignore should contain:

password.txt


---

Task 11: Add the Password Comment

After successfully resolving the merge, add the following comment to your Python file:

#Password is Secret123

For example:

#Password is Secret123

def check(password):
    return True

Commit the change:

git add .
git commit -m "Add password comment"

Push it to GitHub:

git push origin main

At this point, the commit:

Add password comment

has already been pushed to your GitHub repository.

This is intentional because the next task will demonstrate rewriting an already-pushed Git history.


---

Task 12: Rewrite Git History Using Interactive Rebase

Now remove the latest commit:

Add password comment

from your local Git history using an interactive rebase.


---

Step 12.1: Inspect the History

Run:

git log --oneline

You should see something similar to:

abc1234 Add password comment
def5678 Merge branch1 into main
...

The commit hashes will be different for everyone.

The important point is that:

Add password comment

is the latest commit.


---

Step 12.2: Start Interactive Rebase

Run:

git rebase -i HEAD~2

Git will open an editor containing the commits selected for the rebase.

You may see something similar to:

pick abc1234 Add password comment
pick def5678 Merge branch1 into main

The exact commit hashes will be different.


---

Step 12.3: Drop the Add password comment Commit

Change:

pick abc1234 Add password comment

to:

drop abc1234 Add password comment

So it becomes approximately:

drop abc1234 Add password comment
pick def5678 Merge branch1 into main

Save and close the editor.

Git will now attempt to rewrite the history without the Add password comment commit.


---

Important Note About Rebase and Merge Commits

The exact history may contain a merge commit because you merged branch1 into main.

Interactive rebase normally works with a linear sequence of commits. If your rebase encounters a merge-related situation or stops because of conflicts, use the commands below rather than trying to start another rebase.


---

Task 12.4: If the Rebase Stops

First check:

git status

If Git says that a rebase is in progress, follow the instructions Git gives you.

If there is a conflict:

1. Open the conflicted file.


2. Resolve the conflict.


3. Remove all conflict markers.


4. Stage the resolved file:



git add .

5. Continue the rebase:



git rebase --continue

Git may stop again. If it does, repeat:

Resolve conflict
↓
git add .
↓
git rebase --continue

until the rebase finishes.


---

Task 12.5: If Git Opens an Editor

During:

git rebase --continue

Git may open an editor asking for a commit message.

Keep the existing commit message unless Git specifically requires you to change it.

Save and close the editor.

The rebase will then continue.


---

Task 12.6: Abort the Rebase if Necessary

If something goes wrong and you want to completely cancel the rebase:

git rebase --abort

This returns your branch to the state it was in before the rebase started.

You can then inspect the history again:

git log --oneline --graph --all

Do not use git rebase --abort if the rebase has already completed successfully.


---

Task 12.7: Verify the Rebase

After the rebase finishes:

git status

You should no longer be told that a rebase is in progress.

Now inspect the history:

git log --oneline

The following commit should no longer appear:

Add password comment

Also check the file itself.

The following line should no longer be present:

#Password is Secret123


---

Task 13: Understand pull.rebase

Before pushing the rewritten history, understand how Git handles divergent local and remote branches when using:

git pull

Git can use either merge-based or rebase-based behavior.


---

Check the Current Setting

Run:

git config --get pull.rebase

It may return:

true

or:

false

or nothing if it has not been configured.


---

pull.rebase=false

When:

pull.rebase=false

Git uses merge-based behavior when a pull needs to reconcile divergent histories.

You can configure this with:

git config pull.rebase false


---

pull.rebase=true

When:

pull.rebase=true

Git uses rebase-based behavior when pulling.

Configure this with:

git config pull.rebase true

Check the setting:

git config --get pull.rebase


---

Why This Matters Here

Your local main history has now been rewritten.

However, the remote GitHub main still contains the old history, including:

Add password comment

Therefore, do not run a normal git pull to synchronize the two histories.

A normal pull could attempt to merge or rebase the old remote history back into your newly rewritten local history.

For this assignment, the objective is instead to replace the remote history with your rewritten local history.


---

Task 14: Force Push the Rewritten History

At this point:

Local main
    ↓
does NOT contain "Add password comment"

Remote main
    ↓
still contains "Add password comment"

The histories are therefore different.

A normal push:

git push origin main

will normally be rejected because the remote branch contains commits that are no longer present in your local history.

You must use:

git push --force-with-lease origin main


---

Why --force-with-lease?

A normal force push:

git push --force

unconditionally replaces the remote branch with your local history.

--force-with-lease is safer because Git checks that the remote branch is still at the expected state before replacing it.

Therefore, use:

git push --force-with-lease origin main

instead of:

git push --force origin main


---

Task 14.1: Verify the Final History

Run:

git log --oneline --graph --all

Then check your GitHub repository.

The commit:

Add password comment

should no longer appear in the main branch history.

Also verify that the following comment is no longer present in main.py:

#Password is Secret123

The final check(password) function should remain:

def check(password):
    return True

because that was the version selected from branch1 during the merge conflict.


---

Task 15: Create a Pull Request

Once you have completed all the previous tasks and pushed your final changes to your fork, create a Pull Request (PR) from your fork to the original repository.

Original repository:

ShlokDivyam1109/DSAI-Mentorship-First-Repo

Your Pull Request should target:

base repository: ShlokDivyam1109/DSAI-Mentorship-First-Repo
base branch: main

Your fork should be the source repository, with:

branch: main


---

Creating the Pull Request

1. Open your fork on GitHub.


2. Go to the Pull requests tab.


3. Click New pull request.


4. Select:



ShlokDivyam1109/DSAI-Mentorship-First-Repo

as the base repository. 5. Select:

main

as the base branch. 6. Select your fork as the head repository. 7. Select:

main

as the compare branch. 8. Review the changes. 9. Create the Pull Request.

Use a meaningful title such as:

Complete DSAI Mentorship Git Assignment - <YOUR_NAME>


---

IMPORTANT: Do NOT Merge the Pull Request

You are not required to have write access to the original repository.

Your fork is where you will make all your changes.

Your job is only:

Fork
  ↓
Clone
  ↓
Complete Assignment
  ↓
Push
  ↓
Create Pull Request
  ↓
STOP

After you create the Pull Request, do not merge it.

The mentor/repository owner will review your Pull Request and merge it into the original repository if the assignment has been completed correctly.

You should not request write access to the original repository.


---

Expected Final Repository Structure

Your repository should approximately contain:

DSAI-Mentorship-First-Repo/
├── .gitignore
└── <YOUR_NAME>/
    └── main.py

Remember:

secret.txt should be ignored.

password.txt should also be ignored on branch1.

The final main.py should use password.txt.

The final check(password) function should return True.

The merge between main and branch1 must have produced and resolved a conflict.

The branch1 version must have been selected during conflict resolution.

The Add password comment commit must have been removed using interactive rebase.

The rewritten history must have been pushed using --force-with-lease.

The Pull Request must be open and must not be merged by you.



---

Submission Checklist

Your submission is complete only when:

[ ] You forked the repository.

[ ] You cloned your fork.

[ ] origin points to your fork.

[ ] Your <YOUR_NAME> folder exists.

[ ] main.py is present.

[ ] secret.txt was created locally.

[ ] secret.txt is ignored by Git.

[ ] .gitignore is present at the repository root.

[ ] The initial check(password) function contains pass.

[ ] The initial work was committed and pushed.

[ ] branch1 was created.

[ ] main changed check(password) to return password == "Secret123".

[ ] The change to main was committed and pushed.

[ ] branch1 changed secret.txt to password.txt.

[ ] branch1 changed .gitignore to ignore password.txt.

[ ] branch1 changed check(password) to return True.

[ ] branch1 was committed and pushed.

[ ] Merging branch1 into main produced a merge conflict.

[ ] The merge conflict was inspected.

[ ] The conflict was resolved.

[ ] The branch1/incoming version was selected.

[ ] The merge was completed successfully.

[ ] The Add password comment commit was created and pushed.

[ ] Interactive rebase was used to remove the Add password comment commit.

[ ] pull.rebase was understood.

[ ] git rebase --continue was used if required.

[ ] git rebase --abort is understood as the method for cancelling an in-progress rebase.

[ ] The rewritten history was pushed using git push --force-with-lease origin main.

[ ] Add password comment no longer appears in the final main history.

[ ] #Password is Secret123 is no longer present in the final main.py.

[ ] The final check(password) function returns True.

[ ] A Pull Request was created from your fork's main branch.

[ ] The Pull Request targets the original repository's main branch.

[ ] The Pull Request is open.

[ ] You did not merge the Pull Request.



---

Git Commands You Should Practice

By completing this assignment, you should have used and understood the following Git and GitHub commands.

Repository Setup

git clone
git remote
git remote -v

Checking Repository State

git status
git log
git log --oneline
git log --oneline --graph --all
git branch

Adding and Committing Changes

git add
git commit

Pushing

git push
git push origin main
git push origin branch1
git push --force-with-lease origin main

Branching

git branch
git branch branch1
git checkout branch1
git checkout main
git checkout -b branch1

Merging

git merge branch1

Conflict Resolution

git checkout --ours <filename>
git checkout --theirs <filename>

You should understand that:

--ours

refers to the version from the branch you currently have checked out.

In this assignment:

ours = main

and:

theirs = branch1

Therefore:

git checkout --theirs <YOUR_NAME>/main.py

selects the incoming branch1 version.


---

Viewing History

Use:

git log
git log --oneline
git log --oneline --graph --all

These commands allow you to inspect how your branches, commits, and merge changed the repository history.


---

Rewriting History

Use:

git rebase -i HEAD~2

Interactive rebase allows you to:

Reorder commits

Edit commits

Squash commits

Drop/remove commits


In this assignment, you use it to remove:

Add password comment

from the history.


---

Continuing a Rebase

If Git stops during a rebase:

git status

Resolve any conflict, then:

git add .
git rebase --continue

Repeat as necessary until the rebase finishes.


---

Aborting a Rebase

If you need to cancel an in-progress rebase:

git rebase --abort

This restores the branch to its state before the rebase began.


---

Pull Rebase Configuration

Check:

git config --get pull.rebase

Set merge-based pull behavior:

git config pull.rebase false

Set rebase-based pull behavior:

git config pull.rebase true

You should understand that pull.rebase controls whether git pull uses merge or rebase behavior when local and remote histories have diverged.


---

Force Pushing After Rebase

After rewriting history, use:

git push --force-with-lease origin main

A normal:

git push origin main

may be rejected because the remote branch contains the old history.

--force-with-lease allows the rewritten local history to replace the remote history while first checking that the remote has not unexpectedly changed.


---

GitHub Pull Request

Finally, understand the workflow of submitting your work through a Pull Request:

Your Fork
   ↓
Your main branch
   ↓
Push to GitHub
   ↓
Create Pull Request
   ↓
Original Repository
   ↓
Mentor Reviews
   ↓
Mentor Merges

You do not need write access to the original repository to create a Pull Request.


---

Complete Command Checklist

By the end of the assignment, you should be comfortable with:

git clone
git remote
git remote -v
git status
git add
git commit
git push
git push origin main
git push origin branch1
git push --force-with-lease
git branch
git checkout
git checkout -b
git merge
git checkout --ours
git checkout --theirs
git log
git log --oneline
git log --oneline --graph --all
git rebase -i
git rebase --continue
git rebase --abort
git config --get pull.rebase
git config pull.rebase true
git config pull.rebase false

The objective is not merely to reach the final state.

You should understand what each command does, why it is being used, and how it affects:

Your working directory

The staging area

Branches

Commits

Merge conflicts

Git history

The remote repository


By the end of the assignment, you should be able to independently perform the complete:

Fork
  ↓
Clone
  ↓
Create files
  ↓
Commit
  ↓
Create branch
  ↓
Modify main
  ↓
Modify branch1
  ↓
Push
  ↓
Merge
  ↓
Resolve conflict
  ↓
Commit
  ↓
Rebase
  ↓
Remove a commit
  ↓
Force push
  ↓
Create Pull Request

workflow.