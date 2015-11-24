from ml import *

def main():
    en = json.load(open(r'D:\Desktop\Source\Falcom\Decompiler\text_pos_en.json', 'r', encoding = 'utf-8-sig'))
    cn = json.load(open(r'D:\Desktop\Source\Falcom\Decompiler\text_pos_cn.json', 'r', encoding = 'utf-8-sig'))

    cn2 = {}

    for k, v in cn.items():
        if len(v) == len(en[k]):
            cn2[k] = v
        else:
            print(k.ljust(10), len(v) - len(en[k]))

    open('text_pos_final.json', 'wb').write(json.dumps(cn2, indent = 2, ensure_ascii = False).encode('utf-8-sig'))
    console.pause('done')

if __name__ == '__main__':
    Try(main)
