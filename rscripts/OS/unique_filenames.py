import os

# def check_file(filename):
#     """ http://stackoverflow.com/questions/82831/how-to-check-whether-a-file-exists-using-python
#     """
#     i_str = str(0)
#     i = 0
#     while os.path.isfile(filename) is True:
#         i_str = filename.split('.')[0][-1]
#         filename = filename.replace(i_str, str(i))
#         i = i + 1
#     print(filename)
#     return filename

# def title_fix(filename):
#     filename_numb = filename.split('.')[0] + '_' + str(0)
#     filename = filename_numb + '.png'
#     filename = check_file(filename)
#     return filename

def rename_out(output_path):
    oi = 1
    orig = output_path
    rep = orig[-4:]
    if os.path.exists(output_path) == True:
        while os.path.exists(output_path):
            output_path = orig.replace(rep, '_%.3d%s' % (oi, rep))
            oi += 1
    return output_path

def latest_v(output_path):
    just_path = os.path.split(output_path)[0]
    just_file = os.path.split(output_path)[1]
    files = os.listdir(just_path)
    gfiles = [f for f in files if just_file.replace('.txt', '') in f.replace('.txt', '')]
    if len(gfiles) > 1:
        latest = sorted(gfiles, key=lambda item: int(''.join([i if i.isdigit() else '0' for i in item.split('_')[-1]]))
                        )[-1]
        # print latest
        return os.path.join(just_path, latest)
    return output_path