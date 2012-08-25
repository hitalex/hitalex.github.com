"""
This script is used to create post markdown files automatically
"""

#! /usr/bin/env python
import sys
import time

def display_usage():
    print "Usage: ./createpost post-title dest-folder"
    print "Example: ./createpost \"hello world\" ../_posts/"
    print "Note: If dest-folder is empty(not provided), it will be set as the current folder"
    return

def main(argv):
    if len(argv) <= 1 or argv[1] == "--help" or argv[1] == "-h":
        display_usage()
        return
    
    title = argv[1]
    #print title
    title = title.replace("\"", "")
    title = title.replace(" ", "-")  # replace all white spaces
    #title = title.lower()
    #print title
    if len(argv) >= 3: # which means dest-folder is not provided
        dest_folder = argv[2]
    else:
        dest_folder = "./"
        
    time_stamp = time.strftime('%Y-%m-%d',time.localtime(time.time())) # Get local time, the output will be like: 2012-08-24
    file_name = time_stamp + "-" + title + ".md"
    
    #print "Final file name:" + file_name
    if dest_folder[-1] != "/":
        dest_folder = dest_folder + "/"
    #print "Folder selected:" + dest_folder
    
    full_path = dest_folder + file_name
    print "Full path:" + full_path
    
    f = open(full_path, "w")
    f.write("---\nlayout: post\ntitle: \ncategories: \n- \ntags: \n- \n---\n")
    
    f.close()

if __name__ == "__main__":
    main(sys.argv)
