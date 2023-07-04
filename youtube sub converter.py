import os

# get file address from user
input_file = input(f'''enter the exact file loocation:
Ex:C:\Program Files\subtitle.ttml \n''')

# make SRT file name equal to the main file (ttml)
new_file_name = (input_file.split('\\'))[-1]

# set saving directory same as main file
output_directory = (' '.join((input_file.split('\\'))[:-1])).replace(' ', '\\')

# open and read main file
text_file = open (fr'''{input_file}''', 'r')

#make and open new file wich is in SRT format.
srt_file = open (fr'''{output_directory}\\{new_file_name[:-5]}.srt''', 'a')

# read all lines from main file and put them in old_lines variable
old_lines = text_file.readlines()

# from old_lines, line 14 till the last line, are put in new_lines to use
new_lines = old_lines[13:]

# consider first translation as 1
line_number = 1     

for line in new_lines:

    p1 = line[10:22] # starting time of a translation
    p2 = line[29:41] # ending time of the translation
    p3 = line[54:-5] # the translation

    # make a block of translation
    l = f'''{line_number}\n''' + p1 + ' --> ' + p2 + '\n' + p3 + '\n\n'
    
    # append the block of translation in the file we made before
    srt_file.write(l)            
    
    # add 1 to number line and make it ready for the next block to iterate
    line_number = line_number + 1


# closing the srt file.
srt_file.close

# open srt file for user
os.startfile(fr'''{output_directory}\\{new_file_name[:-5]}.srt''')

print('converted!!!')
