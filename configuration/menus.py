
menus = {'File': {'New:': 'lambda: print(\'File: New\')',
                  'Open': 'lambda: print(\'File: Open\')',
                  'Save': 'lambda: print(\'File: Save\')',
                  'Exit': 'self.quit'},
        'Edit': {'Undo': 'lambda: print(\'Edit: Undo\')',
                  'Redo': 'lambda: print(\'Edit: Redo\')',
                  'Copy': 'lambda: print(\'Edit: Copy\')',
                  'Cut': 'lambda: print(\'Edit: Cut\')',
                  'Paste': 'lambda: print(\'Edit: Paste\')'}
        }
