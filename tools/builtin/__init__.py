from tools.builtin.read_file import ReadFileTool
from tools.builtin.edit_file import EditTool
from tools.builtin.write_file import WriteFileTool
from tools.builtin.shell import ShellTool
from tools.builtin.list_dir import ListDirTool 
from tools.builtin.grep import GrepTool
from tools.builtin.glob import GlobTool
from tools.builtin.web_search import WebSearchTool
__all__ = [
    'ReadFileTool',
    'EditTool',
    'WriteFileTool',
    'ShellTool',
    'ListDirTool',
    'GrepTool',
    'GlobTool',
    'WebSearchTool',
]
def get_all_builtin_tools() -> list[type]:
    return [
        ReadFileTool,
        EditTool,
        WriteFileTool,
        ShellTool,
        ListDirTool,
        GrepTool,
        GlobTool,
        WebSearchTool
    ]