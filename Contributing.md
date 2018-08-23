# WTFpython contribution guide
Please read through it carefully, it helps both the contributors (you) and maintainers be more efficient.

# Step 1. Get an Invitation to the Organization
- To get assigned to an issue, you'll first have to invited by us to the organization!
- You'll then receive an email.
- Once the invite if accepted, only then we'd be able to assign you to the issue.
To get an invite check [this]( https://wtfpython-web-invite.herokuapp.com/) link.


Congratulations! Now that you are part of our organization, you can start working on issues. If you are familiar with git, you can skip to the next section and pick an issue.

## If you feel stuck at any moment during the entire contribution process
- If you have any questions, ask them in the channel in a precise and respectful way that maximizes your chances of getting the answer you’re looking for.
- Or you can create an issue with a Help label like [this](https://github.com/wtfpython-web/wtfpython-web/issues/16).

### Note:
 GSSoC participants are rewarded for helping others out! If you help some other person in a help labeled issue, you get extra point. And in general, that's how open source works! We help each-other to collectively improve our skills.

Coming back to the workflow, we use GitHub to manage our repository. If you’re not familiar with git/GitHub, we strongly recommend following a tutorial, such as this one:

#### For basic git knowledge required for this project, please check out [this](https://api.coala.io/en/latest/Developers/Git_Basics.html) link

# Step 2. Picking Up an Issue

Now pick an issue which isn’t assigned and which you would like to fix. Leave a comment that you would like to be assigned to the issue. This way we don’t have multiple people working on the same issue at the same time. Now you can start working on it!

### Caution

- As stated above, you should never work on an issue without being assigned.
And you can only be assigned to one issue at a time (max 2, if you have already created a PR for your first one or if both the issues are related).

- If you are inactive on an issue for long or don't have time to complete it, please get unassigned (by pinging on the channel), and let others do the job. Don't worry, it's not a bad thing to get unassigned from an issue, we want the project to move forward at a nice pace so that everyone is happy.

- If there is no activity on an issue for 5 or more days, and you want to take this up, just ping the assignee in the comments if (s)he is still working. And if there's no response from their end in 24 hrs, we'll assign you to the issue.

### Important
An important part of working on issues is documenting your work in such a way that it is easy for others to read and understand.

- Commit Guidelines: Before starting your first commit, check out this link: http://coala.io/commit.
- For more information about how to style Python code according to the PEP8 code style convention, please check the following link: PEP8 Style Guide for Python code: https://www.python.org/dev/peps/pep-0008/

If your commit message doesn't look good, and you wanna make changes to it, read[this](https://github.com/wtfpython-web/wtfpython-web/pull/15#issuecomment-399772374) comment.

# Step 3. Creating a Fork and Testing Your Changes

This tutorial assumes you are working on your own fork. To fork the repository, go to the official repository of wtfpython-web/wtfpython-web and click on the "Fork" button from the website interface.

To add your fork locally, simply run:

$ git remote add myfork fork_link

where myfork is the name of your fork, and fork_link is a link to your fork repository.

### Important
It is important that you <b>DO NOT</b> make your changes on the master branch of your forked repository to avoid the following cases:

- If you make a rebase to synchronize your repository to the original, every commit that is pushed to the remote master will be pulled in your master branch. Then if you make a pull request to commit your changes to the remote, the commits that got synced from the rebase will be recommitted along with your work in the pull request.

- You cannot have two pull requests using the same branch name. Therefore, if your fork’s master has been used in a pull request and you decide to work on a different issue you will have to branch eventually. Differently every new commit that you make on your master branch will get attached to the initial pull request and that will result in altering the purpose of that request.

- If your fork’s master has been used in a pull request, you have to keep the change in the branch until that get’s merged to the remote master. That will lead to the complications listed above, if you decide to work on a different issue.

In order to avoid the above mentioned cases you can create a new branch where you will work on the issue. To do that run:

$ git checkout -b branchname

# Step 4. Sending Your Changes

### Caution

Before committing your changes, please check that you are indeed in a development branch created in step 3. To check if you are in a branch, type:

$ git branch

Your current branch will have an asterisk (\*) next to it. Ensure that there is no asterisk next to the master branch.

Now that you’ve fixed the issue, you’ve tested it, and you think it is ready to be merged, create a commit and push it to your fork, using:

$ git push -u myfork branchname

where myfork is the name of your fork that you added at the previous step.

# Step 5. Creating a Pull Request
Now that your commit has been sent to your fork, it is time to create a Pull Request. You can do this by accessing your fork on GitHub and clicking New Pull Request.

<b>Congratulations! You have now created your first Pull Request!</b>

### Note

Do not delete your comments on Github, because that makes it hard for other developers to follow that issue. If there is a typo or a task list to be updated, you can edit your comment instead. If you need to add new information, make a new comment.

If you know you have more work to do on this Pull Request before it is ready to be accepted, you can indicate this to other developers by starting your Pull Request title with wip (case-insensitive, stands for “Work in Progress”).

# Step 6. Waiting for Review
After creating a Pull Request, your PR moves to the review process, and all you can do is wait. The best thing you can do at this step is review other people’s PRs. This will reduce maintainer's workload too! And yeah, Never close a Pull Request unless you are told to do so.

### Note

Reviewing code helps you to learn from other people’s mistakes so you can avoid making those same mistakes yourself in the future! Thus, you are improving yourself in the process.<b> And needless to mention, you'll be rewarded extra points in GSSoC for helping others by reviewing the code.</b>

We highly encourage you to do reviews. Don’t be afraid of doing something wrong - there will always be someone looking over it before merging it to master.

# Step 7. Review Process

### Important

Do not tag the reviewers more than once every time you push a change. They review PRs consistently whenever they have time! If you think it has been too long you haven't received a review (more than 5 days), a gentle reminder on slack would be great.

Now there are two possibilities:

- your Pull Request gets accepted, and your commits will get merged into the master branch
your Pull Request doesn’t get accepted, and therefore you will need to modify it as per the review comments

- It’s highly unlikely that your Pull Request will be accepted on the first attempt - but don’t worry, that’s just how it works. We are all here for learning, and getting better with time!

Now, if you need to modify your code, you can simply edit it again, add it, and commit it using

$ git commit -a --amend

This will edit your last commit message. If your commit message was considered acceptable by our reviewers, you can simply send it again (without any changes). If not, edit it and send it. You have successfully edited your last commit!

### Note

Don’t forget! After editing your commit, you will have to push it again. This can be done using:

$ git push --force myfork

The meaning of myfork is explained in step 3 of this guide. The Pull Request will automatically update with the newest changes.

Congratulations! Your PR just got accepted! You’re awesome.

### Attention

Do not delete the fork subsequent to Pull Request for review or after it is merged!

We highly encourage you to start reviewing other’s issues (if any) after you complete your issue, as reviewing helps you to learn more about the project and python.

### Note

If you need help picking up an issue, you can always ask us. The community is extremely helpful, so don’t ask to ask, just ask.