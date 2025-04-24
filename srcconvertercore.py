import subprocess
import logging
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

class MarkdownConverter:
    def __init__(self, config_path="config.ini"):
        self.logger = logging.getLogger(__name__)
        self.template_env = Environment(loader=FileSystemLoader("templates"))

    def convert(self, input_path, output_format="html", template="default.css"):
        """执行文档转换"""
        try:
            output_path = Path(input_path).with_suffix(f".{output_format}")
            cmd = [
                "pandoc", 
                input_path,
                "-o", str(output_path),
                "--css", f"templates/{template}",
                "--toc"
            ]
            self.logger.info(f"Converting {input_path} to {output_format}")
            subprocess.run(cmd, check=True)
            return True
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Conversion failed: {str(e)}")
            return False