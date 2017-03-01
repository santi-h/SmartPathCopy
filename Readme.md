# SmartPathCopy (Sublime Text 2/3 plugin)
When you head over to the console right after making some changes to a file, chances are that the command you will run is related to the file you were just looking at, and the type of the command will depend on the type of the file.

For example, if you're making changes to `path/to/test.rb`, chances are you're going to run a command to run the tests in `path/to/test.rb`.

Similarly, if you're writing a migration on rails like `db/migrate/20150406132142_add_authentication_token_to_users.rb`, chances are that when you head over to the console, you just want to run either `rake db:migrate` or `rake db:migrate:up VERSION=20170213214913`

### Case in point
You're in the zone developing and writing tests like it's nobody's business.
You think your test is ready and want to quickly run it, but you don't have a [TDD](http://asquera.de/blog/2016-03-31/tdd-with-guard) mechanism in place or you haven't started it.
You head over to the console to run the test.
You start typing `rspec` and realized that you forgot the path to the spec file, so you go back to sublime to [`Copy Path`](https://github.com/SideBarEnhancements-org/SideBarEnhancements/blob/807b9232e644968194dd30fd4fa36a6d45ad436e/Side%20Bar.sublime-menu#L334).
While you're at it you look at the line number the test you want to run is on, so you can specify it as part of the `rspec` command.
You go back to the console and you're finally ready to run `rspec path/to/file:line_number`


All this process takes you out of the zone. So far away from it that the zone looks like a tiny dot from where you're at now.


With SmartPathCopy, all you need to do is hit `super`+`shift`+`c` and boom, `rspec path/to/file:line_number` copied to the clipboard and ready to run from the console.


You could use the [RSpec sublime package](https://packagecontrol.io/packages/RSpec), which works fine until you put a `binding.pry` somewhere, which you will.
So now you have to go back to the console and run it from there anyways. If you forget to `continue` or kill the spec in the console, every test you run in sublime with RSpec will hang. Hopefully some day [RSpec will support pry](https://github.com/maltize/sublime-text-2-ruby-tests/issues/227), until then I'll stick to the console.


### Instalation
Recommended way is using [PackageControl](http://wbond.net/sublime_packages/package_control/installation) package.

### Usage
Hit `super`+`shift`+`c` to send the relevant command to the clipboard. By default it will build the following commands:
- For files ending in `_spec.rb`: `rspec <file>:<line_number>`
- For files in `db/migrate`: `rake db:migrate:up VERSION=<migration_version>`
- For files in `lib/tasks`: `rake <task_name>`


### Configuration
The default configuration is:
```python
{
  "smart_path_copy": [
    ["_spec\\.rb$",                     "rspec $filepath:$line_number"  ],
    ["db/migrate/(\\d+)[^\\/]+\\.rb$",  "rake db:migrate:up VERSION=$1" ],
    ["lib/tasks/([^\\/]+)\\.rake$",     "rake $1"                       ]
  ]
}
```

Each element in the `"smart_path_copy"` list consists of a regex expression and a command.
The regex expression serves as a condition: If the file you're currently on satifies the condition (regex), then the command next to it will be copied to the clipboard when you hit `super`+`shift`+`c`.

If no condition is satisfied, the whole path of the current file is copied to the clipboard.

The default configuration is useful if you're developing in rails, but you can add your own configuration in `Sublime Text` > `Preferences` > `Settings`.

Notice that you can add groups in the regexes and use them (as `$<group_number>`) in the command.

You can also use in the command section:
- `$filepath`: absolute file path of the current file.
- `$line_number`: line number the cursor is on.

The default shortcut is `super`+`shift`+`c`, but you can modify it from `Sublime Text` > `Preferences` > `Key Bindings`.
For example, if you want the shortcut to be `super`+`shift`+`h`, you will add:
```python
[
  # ...
  { "keys": ["super+shift+h"], "command": "smart_path_copy"},
  # ...
]
```
