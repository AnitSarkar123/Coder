from tools.builtin.read_file import ReadFileTool
from tools.builtin.edit_file import EditTool
from tools.builtin.write_file import WriteFileTool
from tools.builtin.shell import ShellTool
__all__ = [
    'ReadFileTool',
    'EditTool',
    'WriteFileTool',
    'ShellTool'
]
def get_all_builtin_tools() -> list[type]:
    return [
        ReadFileTool,
        EditTool,
        WriteFileTool,
        ShellTool
        
    ]