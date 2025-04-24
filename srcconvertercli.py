import argparse
from .core import MarkdownConverter

def main():
    parser = argparse.ArgumentParser(description="Markdown文档转换工具")
    parser.add_argument("input", help="输入文件或目录")
    parser.add_argument("-f", "--format", choices=["html", "pdf", "docx"], default="html")
    parser.add_argument("-t", "--template", default="default.css")
    parser.add_argument("-v", "--verbose", action="store_true")
    
    args = parser.parse_args()
    converter = MarkdownConverter()
    
    if Path(args.input).is_dir():
        for md_file in Path(args.input).glob("*.md"):
            converter.convert(md_file, args.format, args.template)
    else:
        converter.convert(args.input, args.format, args.template)