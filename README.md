GitBackup
=========

I started using version control a few years ago, as part of a programming assignment in college. It did not take long for me to realize I could also use it for writing, for the exact same purpose: to track changes to my articles through time. This had the side beneift of giving me an off-site backup of everything I wrote for this site, in case something happened to my computer. I wrote this script to take advantage of that side benefit.

This script monitors a given directory for changes, then automatically pushes those changes to the associated source control repository with a generic commit message. I keep duplicate repositories at GitHub and Bitbucket, and push to both, so in practice this gives me real-time backup as I write, to two off-site locations. I can stop the script if I want to start making meaningful, progress-based commits again, but if I just want to ensure that everything stays backed up in real-time, I point this script at the directory.

## Usage

To use GitBackup, simply run the script with a target directory as a paramater. For example, to target "Dropbox/website", your command would look like this:

```
$: ./gbk.py ~/Dropbox/website
```

GitBackup would now start monitoring the "website" folder within Dropbox, and as files were changed, commit and push them with a generic commit message.

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/). a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). Read more about the license, and my other disclaimers, [at my website](https://zacs.site/disclaimers.html).