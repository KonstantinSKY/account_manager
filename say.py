from typing import Dict, Any, Optional

class Say(str):
    """Advanced terminal output utility with ANSI color support."""
    color: Dict[str, str] = {
        'Purple': '\033[95m', 'Cyan': '\033[96m', 'Blue': '\033[94m',
        'Green': '\033[92m', 'Yellow': '\033[93m', 'Red': '\033[91m'
    }
    style: Dict[str, str] = {'Bold': '\033[1m', 'Underline': '\033[4m'}
    styles_end: str = '\033[0m'

    def __init__(self, text: str):
        super().__init__()
        self.text = text
        self.default_color: str = ''
        self.default_style: str = ''

    def prn(self, color_key: Optional[str] = None, style_key: Optional[str] = None) -> None:
        color = self.color.get(color_key, self.default_color) if color_key else self.default_color
        style = self.style.get(style_key, self.default_style) if style_key else self.default_style
        
        start = f"{color}{style}"
        end = self.styles_end if start else ""
        print(f"{start}{self.text}{end}")

    def prn_ok(self) -> None:
        self.default_color = self.color["Green"]
        self.prn()

    def prn_err(self) -> None:
        self.default_color = self.color["Red"]
        self.prn()
