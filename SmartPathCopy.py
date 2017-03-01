import sublime, sublime_plugin
import re

class SmartPathCopyCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    current_filepath = self.view.file_name()

    rules = self.view.settings().get('smart_path_copy') or []

    subs = {
      'filepath': current_filepath,
      'line_number': self.view.rowcol(self.view.sel()[0].begin())[0] + 1
    }

    for rule in rules:
      result = re.search(rule[0], current_filepath)
      if result is not None:
        ret = rule[1]

        for key, val in subs.items():
          ret = re.sub(r'\${0}\b'.format(key), str(val), ret)

        for group_idx, group in enumerate(result.groups()):
          group_number = group_idx + 1
          ret = re.sub(r'\${0}'.format(group_number), str(group), ret)

        sublime.set_clipboard(ret)
        return

    sublime.set_clipboard(current_filepath)
