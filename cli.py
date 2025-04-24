def check_dependencies():
    try:
        subprocess.run(["pandoc", "--version"], check=True, capture_output=True)
    except FileNotFoundError:
        print("错误：请先安装Pandoc（https://pandoc.org/installing.html）")
        sys.exit(1)