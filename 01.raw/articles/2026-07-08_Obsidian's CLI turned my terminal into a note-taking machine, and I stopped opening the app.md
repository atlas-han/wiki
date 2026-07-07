---
title: "Obsidian's CLI turned my terminal into a note-taking machine, and I stopped opening the app"
type: "article"
source: "https://www.xda-developers.com/obsidian-cli-terminal-workflow/"
site: "xda-developers.com"
author:
  - "[[Korbin Brown]]"
published: 2026-07-02
created: 2026-07-08
description: "Turns out I use the app more when I don't need to open it."
tags:
  - "clippings/article"
---
**Source URL**: https://www.xda-developers.com/obsidian-cli-terminal-workflow/

Note-taking apps have been trying to top one another for years [by releasing new features](https://www.xda-developers.com/stopped-using-obsidian-for-notes-turned-it-into-something-i-actually-open/). To me, a lot of it feels like unnecessary flash that I didn't ask for. My workflow wasn't suffering because of a lack of GUI features, so I didn't pay much attention to who was revamping their interface. The real bottleneck was switching to the GUI at all. Every time I needed to log a quick thought, it'd require alt+tabbing into the right window and clicking into a certain note before I could [jot down my thoughts](https://www.xda-developers.com/expected-bounce-off-obsidian-note-app-year-later-running-entire-life/) and get back to what I was doing.

I like Obsidian because it stores notes as plain Markdown files rather than locking them in a proprietary database. But until recently, using the app was a strictly GUI-only experience. With version 1.12 released a few months back, Obsidian rolled out an official command-line interface, and it's quickly become the way I interact with my vault most of the time now. I didn't expect a note-taking app to make my terminal more useful, but here we are.

## Vault access is now a command away

### And one toggle is all it takes to set up

Getting [Obsidian's CLI running](https://www.xda-developers.com/obsidian-cli-is-the-new-best-way-to-automate-your-notes/) only takes a second. Head to Settings, then General, scroll down to Advanced, and click the toggle for command-line interface. A window will pop up that asks you to register the obsidian command in your system's PATH. Just click on the Register button. Obsidian should now be ready to use from the command line, although you'll need to close any terminals that are currently open and launch a fresh one, which will have the new PATH settings.

In the terminal, just execute the `obsidian` command to get started. Then, there are over 100 subcommands that you can use to interact with Obsidian. Literally anything that you can do in the GUI, you can now do from the command line, as confirmed by Obsidian CLI docs. I was surprised at how user-friendly Obsidian made the CLI. All commands you start typing have autocompletion suggestions (press TAB to complete a command), so I got used to the syntax faster than I expected. The command I'd start with is `help` just to get a basic idea about what kind of commands you'll want to work with mainly.

Run `obsidian` files to list every note in your vault. The `read` command is used to dump a note's contents to stdout. You'd use it like this: `obsidian read file="Projects/Homelab"` (the quotes are only necessary if the names have spaces). Note that the `obsidian` prefix in my examples isn't necessary if you're already in the Obsidian TUI. I always leave one tab of my terminal permanently in Obsidian's TUI, just because it makes it easy to think of that as the Obsidian tab, and it saves me a few keystrokes every time.

To log a quick thought, you can use the `create` command and run something like this: `obsidian create name="Inbox/quick thought" content="..."`. Pretty nice to jot something down without needing to open the GUI, especially since there's a high chance [I'm already in the terminal](https://www.xda-developers.com/live-in-the-terminal-6-apps-are-why/) for some other reason. The CLI communicates with the app, so using the `move file` command to place a note in a different folder will automatically rewrite every link that points to the note's previous location.

## I stopped opening the app for small stuff

### Most of my daily notes come from the command line

![claude code inside obsidian](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/02/claude-code-obsidian.jpg?q=49&fit=crop&w=825&dpr=2)

The single command I use the most is `obsidian daily:append content="..."`. I used to keep my daily note pinned on a second monitor specifically so I could jot down quick notes while I was in the middle of other tasks. Now I can just fire off that command from whichever terminal I'm already in, and the thoughts coalesce into my daily note without ever needing to switch windows.

Searching my notes is also done from the command line now. I'm the type that already uses grep dozens of times per day, so Obsidian's CLI search fits into my workflow perfectly. A command like `obsidian search:context query="bottleneck" limit=10` behaves just like grep, except it's aware of my vault's current structure and will return matches along with their surrounding context.

I've also begun experimenting with AI integration. Tools like [Claude Code can read, search, and write to a vault](https://www.xda-developers.com/claude-code-inside-obsidian-and-it-was-eye-opening/) directly through the CLI. I keep all of my homelab documentation in Obsidian, so whenever I'm having Claude Code investigate an issue, I'll tell it to use my Obsidian vault to get clues about how things were set up. If Claude makes any changes to how things work, it can directly note those changes in my homelab notes.

## This doesn't make the GUI irrelevant

### The CLI still relies on the GUI app more than you'd expect

![Obsidian Community Plugins settings showing installed plugins and a check for updates button](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2025/09/plugin-obsidian-update.jpg?q=49&fit=crop&w=825&dpr=2)

There's one small limitation that I'm not a fan of. Obsidian needs to be running for the CLI to work at all. If you try to execute an Obsidian command without the app open, it'll bark at you to open the app before trying anything. That's only a minor inconvenience, and I wasn't aiming to eliminate the GUI app.

The other caveat is that the CLI can't touch anything that Obsidian itself doesn't have a hook for. If you're used to using third-party plugins, those plugins need to provide their own commands for interaction; otherwise, you're limited to using them from the GUI. A lot of my [plugins naturally lend themselves to GUI usage](https://www.xda-developers.com/obsidian-dataview-notion-replacement/) anyway, so this hasn't bothered me too much. Logging quick thoughts and searching past notes is mostly what I use Obsidian for, which I imagine is true for almost everyone else, too, and the CLI already covers that.

### Obsidian is now open less, but I use it more

It's a strange thing to say about a note-taking app, but the introduction of a CLI has made me use Obsidian even more. I was already living in the terminal for so many other tasks, so having my vault there made it that much easier to access. If you're thinking that it sounds tedious to learn about using Obsidian from the command line, just know that the user-friendly TUI makes it downright trivial.