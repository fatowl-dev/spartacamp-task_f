from pathlib import Path
import shutil


def main():
    src_path_str = './score_data'
    dest_path_str = './dest_data'
    dest_path = Path(dest_path_str)
    if dest_path.exists():
        print(f'すでに{dest_path_str}が存在しています')
        return

    shutil.copytree(src_path_str, dest_path_str)

    for csv_path in dest_path.rglob('*.csv'):
        str_csv = ""
        with open(csv_path, 'r') as f:
            str_csv = f.read()

        with open(csv_path, 'w') as f:
            f.write('氏名,メールアドレス,得点\n' + str_csv)


if __name__ == '__main__':
    main()
